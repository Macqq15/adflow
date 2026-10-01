# Wiedza domenowa — Analiza kampanii Meta Ads

Reguły operacyjne do diagnostyki i rekomendacji. Procedury z `procedury/` odsyłają tu do konkretnych sekcji. Stan: kwiecień 2026.

---

## 1. Zasady analizy kampanii

### Filtrowanie danych — dwa tryby

**Diagnostyka bieżąca** (sprawdź konto, zdiagnozuj, optymalizuj):

- **ZAWSZE filtruj po `spend > 0`** w analizowanym okresie — to jedyny potrzebny warunek
- Sortuj od największych wydatków — najważniejsze na górze
- Paused kampanie → pomiń w performance, ale raportuj oddzielnie jeśli miały spend w okresie

**Analiza historyczna** (trendy, porównania okresów, sezonowość):

- NIE filtruj po statusie — bierz wszystkie kampanie z `spend > 0` w danym okresie
- Kampania która wtedy działała, a dziś jest paused — nadal generowała dane, nie fałszuj wykresów

### Definicja "aktywna kampania" (Meta)

**Aktywna = `effective_status == "ACTIVE"`.**

Sam `configured_status = "ACTIVE"` (ustawiony na ACTIVE) **NIE oznacza że się wyświetla**. `effective_status` bierze pod uwagę:
- End date w przeszłości → `effective_status = CAMPAIGN_PAUSED`
- Spend cap osiągnięty → delivery się zatrzymuje mimo ACTIVE
- Ad set / ad w tej kampanii PAUSED lub DELETED → kampania nie wyświetla nic
- Review (pending review) → nie wyświetla
- Disapproved creative → nie wyświetla

Gdy user pyta "ile mam aktywnych kampanii" — zawsze sprawdzaj `effective_status`, nie `configured_status`.

### Zakres dat (Meta pułapki)

- **Data freshness**: ostatnie 2-3 godziny są niekompletne. Zawsze filtruj `until=yesterday`.
- **Pełne dane konwersji**: Meta attribution potrzebuje do 28 dni żeby się ustabilizować (`7d click + 1d view` to default — patrz §4).
- **Attribution windows removed Jan 2026**: `7d_view` i `28d_view` nie zwracają już danych. Available: `1d_click`, `7d_click`, `28d_click`, `1d_view`.

### Pułapki `actions` i `action_values`

- **To listy obiektów**, nie pola: `[{"action_type": "purchase", "value": "5"}, ...]`
- **Action naming — 3 źródła atrybucji które się nakładają**:
  - `purchase` (Pixel)
  - `offsite_conversion.fb_pixel_purchase` (Pixel, stara nazwa)
  - `omni_purchase` (unified: Pixel + CAPI + Modeled)
- **Używaj `max(...)` a nie `sum(...)`** gdy parsujesz — sum policzy dwukrotnie
- Dla ASC zawsze `omni_purchase` — to najdokładniejszy
- Dla manual Sales campaigns `purchase` zwykle wystarcza

---

## 1b. Optimizing event — najważniejsza decyzja w kampanii


Optimizing event = co mówisz Meta że chcesz dostać (Purchase, Lead, Video View, AddToCart, Reach, Engagement, Traffic). To nie jest tylko "co liczyć" — to fundamentalna decyzja algorytmiczna.

### Dwa rodzaje optymalizacji

**Reactive Optimization** (o czym wszyscy wiedzą):
- Meta analizuje activity na reklamach + stronie
- Daje więcej tego o co poprosiłeś
- Optymalizuj pod Purchase → algorytm uczy się z każdego zakupu → wysyła ruch podobny do tych co kupili

**Proactive Optimization** (o czym mało kto wie):
- Meta zaczyna optymalizować ZANIM dostanie jakikolwiek sygnał z Twojej kampanii
- **Zanim pojawi się pierwszy Purchase…**
- **Zanim pojawi się pierwszy AddToCart…**
- **Zanim pojawi się pierwszy click**…
- …Meta już pokazuje reklamę **tylko małej puli ludzi** których algorytm uważa za likely to take the chosen action

### Konsekwencje operacyjne

- **Meta nie blastuje reklamy na całą audience** — nawet jeśli audience size 10M, reklama trafia tylko do tych co Meta uważa za likely konwertujących
- Proactive optimization = **Twój optimizing event determinuje kto w ogóle zobaczy reklamę**, nie tylko kto konwertuje
- Zły optimizing event → reklama trafia do niewłaściwej puli → kampania martwa od pierwszego dnia, niezależnie od kreacji / audience / budżetu

### Decision matrix

| Cel biznesowy | Optimizing event | Kiedy używać |
|---|---|---|
| E-commerce purchase | `PURCHASE` | Masz 15-50+ purchases/tydz. Gold standard. |
| E-commerce purchase, mało danych | `ADD_TO_CART` albo `INITIATE_CHECKOUT` | < 15 purchases/tydz. Tymczasowo niżej w lejku żeby zbudować signal |
| Lead gen — Instant Form | `LEAD` | Form-based. Meta optymalizuje pod completed form |
| Lead gen — external form | `COMPLETE_REGISTRATION` | Form na Twojej stronie, Pixel custom event |
| Lead gen — mało danych | `LANDING_PAGE_VIEW` | Dopóki nie zbierzesz 50 leads/tydz |
| Traffic (top of funnel) | `LINK_CLICKS` | Rzadko używane teraz — Meta preferuje LPV |
| Engagement / content | `POST_ENGAGEMENT` | Brand awareness, viral content push |
| Video views | `THRUPLAY` (15s+) | Brand / awareness z video content |
| Reach / awareness | `REACH` | Brand awareness z frequency cap |

### Pułapka "schodzenia w dół lejka"

Gdy nie masz dość signals na top event (Purchase):
- Opcja A: optymalizuj pod lower-funnel event (AddToCart), buduj signal, **potem przełącz na Purchase**
- Opcja B: zostań na Purchase mimo słabego signal → Meta konserwatywnie gasi delivery → kampania umiera
- **Opcja A lepsza w 90% przypadków**, ale każde przełączenie = reset learning phase

### Pułapka "złego event'u dla cold audience"

Klasyczny błąd: nowa kampania prospecting z `PURCHASE` optimization, ale brand nie ma jeszcze trustu / brand awareness → nikt z cold nie kupuje w 24h → Meta nie znajduje "likely purchasers" → kampania gaśnie.

Fix dla sklepu: zostań przy optymalizacji pod zakup (patrz niżej, „50 events to heurystyka”), daj kampanii pełne okno i sprawdź, czy piksel naprawdę widzi zakupy. Optymalizacja pod wyświetlenie strony albo lead dla zimnego ruchu w sklepie zwykle przyprowadza ludzi, którzy klikają, a nie kupują.
- Alternatywa: Advantage+ Shopping Campaign (ASC) z Purchase, Meta sama dzieli ruch zimny i ciepły

---

## 2. Learning Phase — szczegóły

### Status enum (`learning_stage_info.status`)

| Status | Znaczenie | Akcja |
|---|---|---|
| `LEARNING` | Aktywnie zbiera dane, jeszcze nie ustabilizowane | Czekaj, nie ruszaj |
| `SUCCESS` | 50+ events w rolling 7d. Wyszło z learning | Możesz optymalizować, skalować ostrożnie |
| `LEARNING_LIMITED` | Meta przewiduje że NIE osiągnie 50 events/7d | Delivery staje się konserwatywne. Budżet / audience za słabe |
| `FAIL` | Historyczne — w aktualnych docs zastąpione przez LEARNING_LIMITED | (Obsługuj na wszelki wypadek jako LEARNING_LIMITED) |

### Próg wyjścia: **50 optimization events / 7 dni** per ad set.

### Uwaga: "50 events" to heurystyka, nie prawo


**To co naprawdę oznacza "wyjście z learning":**
- Wyższa **stabilność** wyników (Meta czuje że może dać Ci stable results)
- NIE oznacza że kampania jest "lepsza" lub że Meta działa inaczej
- **Pułapka**: stable results na niskiej jakości event = stabilne złe wyniki. Np. optimize pod `LINK_CLICKS`, zebrasz 200/tydz = SUCCESS, ale ROAS katastrofalny bo klikacze nie kupują.

**Quality > Volume nawet przy niskim volume:**

Test w praktyce (zweryfikowany w dziesiątkach kont):
- Optimizing pod `PURCHASE` z niskim volume (5-20 events/tydz) **często wygrywa** z optimizing pod `ADD_TO_CART` albo `VIEW_CONTENT` mimo że ma 5-10× mniej events
- Dlaczego: proactive optimization. Meta przy `PURCHASE` szuka **likely buyers** w całej puli — przy `VIEW_CONTENT` szuka **likely viewers** (kluczowo gorsi ludzie jako leads)

**Sweet spot — kiedy schodzić niżej w lejku:**

- Jeśli wysoka-quality event daje **chwilową stabilność potem nagle pusty tydzień** → zbyt volatile → rozważ 1 krok niżej w lejku
- Typowy sweet spot e-com: `INITIATE_CHECKOUT` (gdy Purchase volatile) albo `ADD_TO_CART` (gdy Purchase martwy)
- Typowy sweet spot lead gen: `LEAD` (form complete) > `COMPLETE_REGISTRATION` > `LANDING_PAGE_VIEW`
- **Zawsze testuj**: nie zakładaj że "więcej events = lepiej"

### Pułapka testowania kreacji na traffic optimization


**Anti-pattern**: popularna taktyka "testuj kreacje taniej używając Traffic optimization, potem przenieś winners do Purchase campaign".

**Dlaczego to nie działa:**
- Traffic optimization pokazuje reklamę ludziom którzy **kliknią najtaniej** (niezależnie czy konwertują)
- To **zupełnie inni ludzie** niż ci których Meta pokazałby przy Purchase optimization
- Winner creative w traffic test **nie gwarantuje że wygra** w purchase campaign
- Zdarzają się nawet sytuacje gdzie **loser z traffic testu wygrywa w purchase** (bo to różne segmenty audience)

**Test w praktyce**:
- Ten sam ad + ten sam funnel + dwa optimizations: Purchase vs Traffic
- Traffic miał 3× tańszy CPC
- Traffic campaign nie dał **ani jednego webinar registrant**
- Purchase campaign dał stabilne conversions

**Konkluzja**: traffic testing to **false economy**. Tańsze kliknięcia nie znaczą lepsze dane. Testuj w realnej kampanii (purchase-optimized) z niższym budżetem.

**Wyjątek**: testy scroll-stopping obrazu (hook rate, 3s view rate) mogą korelować z purchase performance, bo hook to głównie visual disruption niezależna od optimization event.

### Minimum daily budget heurystyka:

```
daily_budget >= (target_CPA × 50) / 7
```

Przykład: target CPA = 20 PLN → min daily budget = ~143 PLN żeby learning phase miał szansę.

### Typowy czas: 3–7 dni (do 14 dni przy słabym sygnale)

### Co RESETUJE learning phase (significant edits — konkretna lista)

1. Zmiana budżetu > 20% (pojedynczy edit)
2. Zmiana targetingu / audience (dodanie/usunięcie interests, lookalike, custom audience)
3. Zmiana optimization goal (Purchase → AddToCart albo odwrotnie)
4. Zmiana bid strategy (Lowest Cost → Cost Cap itd.)
5. Zmiana bid amount przy Cost Cap / Bid Cap (w ramach tej samej strategii)
6. Zmiana kreacji (nowy ad albo znacząca edycja istniejącego)
7. Dodanie/usunięcie placementów
8. Zmiana attribution setting
9. Pause > 7 dni i reaktywacja

### Co NIE resetuje

- Zmiana budżetu ≤ 20%
- Zmiana nazwy ad set / ad
- Dodanie nowego ada bez pauzowania istniejących
- Zmiana bid amount w tej samej strategii jeśli jest < 20% zmiany (Jon Loomer 2025)

### Nowe podejście Jon Loomer 2026

Historycznie learning phase był świętością ("nie ruszaj!"). Loomer zmienił stanowisko w 2025: **reset learning phase nie jest inherentnie zły** — liczy się volume sygnałów, nie "ochrona fazy". Jeśli kampania nie działa w learning → śmiało zmieniaj, bo teraz jest gorzej.

**Dla AdFlow rekomendacja**: ostrzeż usera o resecie learning phase przy mutacjach, ale nie blokuj — wyjaśnij że 7 dni obserwacji po resecie jest normalne.

---

## 3. Bid Strategies — matryca decyzyjna

| Strategy (API enum) | Min events do sensu | Kiedy stosować |
|---|---|---|
| `LOWEST_COST_WITHOUT_CAP` | 0 (zawsze OK) | Default. Nowe konta/kampanie, < 50 conv/tydz, testy |
| `LOWEST_COST_WITH_BID_CAP` | 50+/tydz | Expert-level, rzadko używane |
| `COST_CAP` | 50+/tydz stabilnie | Znany stabilny CPA, chcesz volume w ceiling |
| `LOWEST_COST_WITH_MIN_ROAS` | 50+ purchases/tydz + wartość | E-commerce z wartością konwersji, rentowność > volume |

**Ścieżka migracji e-commerce:**
1. Start: `LOWEST_COST_WITHOUT_CAP` (default)
2. Po 50+ purchases/tydz stabilnie: test `LOWEST_COST_WITH_MIN_ROAS` z target 80% faktycznego ROAS
3. Podnoś ROAS target o 5-10% co 50 nowych purchases

**Ścieżka migracji lead gen:**
1. Start: `LOWEST_COST_WITHOUT_CAP`
2. Po 50+ leadów/tydz stabilnie: test `COST_CAP` na ~20% powyżej faktycznego CPA
3. Obniżaj Cost Cap o 5-10% co 50 leadów

**Pułapki:**
- Cost Cap / Min ROAS **z agresywnym targetem** → kampania przestaje wydawać
- Bez 50+ events/tydz te strategie under-delivery — przyspieszony learning fail
- Każda zmiana strategii = reset learning 7-14 dni

---

## 4. Attribution (stan 2026)

### Unified attribution (default od ~2021)

- Domyślne okno: `7d_click + 1d_view`
- `use_unified_attribution_setting: true` → Insights matchuje Ads Manager UI

### Attribution windows dostępne (kwiecień 2026)

| Window | Status |
|---|---|
| `1d_click` | ✅ |
| `7d_click` | ✅ (default część) |
| `28d_click` | ✅ |
| `1d_view` | ✅ (default część) |
| `7d_view` | ❌ Removed Jan 12, 2026 |
| `28d_view` | ❌ Removed Jan 12, 2026 |

### iOS 14.5+ i modelowane konwersje

- **15-30% konwersji iOS to estymaty** (modeled), nie direct attribution
- AEM (Aggregated Event Measurement) od mid-2025 **automatyczny** — Meta usunęła limit 8 eventów per domena. Wszystkie eligible events agregują się same.
- **NIE mów userowi żeby "prioritytyzował 8 eventów"** — to już nieaktualne. Jedyne co user robi: weryfikuje domenę w Business Manager.

### CAPI (Conversions API) — must-have w 2026

- Pixel sam = tracy ~30% iOS + adblockers + privacy signals
- CAPI server-side = backup dla Pixela
- **Event Match Quality (EMQ)**: skala 1-10. Target: `> 7.0` na Purchase
- **CAPI / Pixel ratio**: target `> 80%` CAPI coverage
- Dedup przez `event_id` — ten sam w Pixel i CAPI

---

## 5. Audience strategy (2026)

### Advantage+ Audience — 2026 default

- Meta rekomenduje dla 9 głównych performance objectives
- Lookalikes traktowane jako "suggestions" a nie hard restriction
- Jon Loomer / Foxwell 2025-2026: Advantage+ Audience wygrywa z manual targeting w większości testów A/B

### Custom Audience retention

| Source | Max retention |
|---|---|
| Website | 180 dni |
| Engagement | 365 dni |
| Video views | 365 dni |
| Customer list | - (static) |

### Lookalike

- Ratio 1% do 10% (większe = szersze = mniej precyzyjne)
- **Rekomendacja**: start 1%, testuj 3-5% równolegle
- **UWAGA**: lookalike z Purchasers zawsze > lookalike z PageView — source quality decyduje

### Audience overlap — progi

| Overlap % | Status | Akcja |
|---|---|---|
| < 15% | Safe | Bez akcji |
| 15-25% | Monitor | Obserwuj CPA — może zacząć rosnąć |
| > 25-30% | **Self-cannibalization** | Konsoliduj ad sety albo wyklucz jeden z drugiego |

### Worldwide targeting

**Tier 1 "Big Six"** (US/Canada/UK/Ireland/Australia/NZ) to często tylko ~50% potencjału. Dla info products, e-commerce z auto-fulfillment, bez sales calls wymagających time zones — **warto testować worldwide**.

Case study: po rollout worldwide doubled revenue. Reports z ROAS:
- Romania 3.54x
- Trinidad/Tobago 4.40x
- Argentina 3.06x
- Ecuador 5.06x
- India 4.64x (CPA niższe niż US, AOV wyższe)

**Pułapki worldwide**:
- Exclude Indonesia + Taiwan na początku (junk traffic w większości przypadków)
- ASC nie daje wyboru języka — A/B test pokazał że ASC i tak wygrywa z manual Sales + English setting na 7398 conversions ($11.95 vs $13.04 CPA)
- Sprawdzaj breakdown per country po pierwszym tygodniu — ewentualnie wyklucz kraje z junk

**Kiedy NIE iść worldwide**:
- Sales calls z time zones
- Local fulfillment / shipping
- Regulowane produkty (compliance per country)
- Licensing restrictions (software, health)

---

## 5b. Audience Immersion Strategy (retargeting)


### Problem z retargetingiem przy PURCHASE optimization

Gdy retargetujesz quality audience (np. webinar viewers) i optymalizujesz pod `PURCHASE`:
- Meta pokazuje reklamę **tylko małemu ułamkowi** tej audience — tych którzy algorytm uważa za najbardziej likely to buy
- Reszta audience (która jest już high-quality, ale może nie jest "top likely") — **nie zobaczy Twojej reklamy**
- Tracisz expozycję tam gdzie masz już quality — kontrintuicyjnie przy cold Meta filtruje, przy warm nie chcesz tej filtracji

### Rozwiązanie — duplicate z różnymi optimization events

Setup:
- **Campaign A**: retargeting audience, optimization = `PURCHASE`
- **Campaign B**: te same ads, ta sama audience, optimization = `LINK_CLICKS`
- **Campaign C**: te same ads, ta sama audience, optimization = `REACH`
- **Campaign D**: te same ads, ta sama audience, optimization = `POST_ENGAGEMENT`
- **Campaign E**: te same ads, ta sama audience, optimization = `LANDING_PAGE_VIEW`

Każda kampania biegnie symultanicznie. **Każda serwuje do innego wycinka audience** (Meta proactively filtruje per event), więc w agregacie **przepuszczasz reklamę przez znacznie większą część audience** niż z jednym objective.

### Kluczowe insighty

- Retargeting **REACH campaign często wygrywa** z retargeting PURCHASE campaign (counter-intuitive ale zweryfikowane)
- Wyjaśnienie: reach/engagement optimization blanketuje audience, purchase ją zawęża. Quality audience nie potrzebuje filtracji.
- **Cost caps z wysokim bidem + niski budżet** = jeszcze silniejsze immersion dla małych high-ticket audiences

### Kiedy używać

- Webinar viewers (ready to buy, pokazuj przed cart close)
- Email list custom audience (warm, high-intent)
- Product Launch Formula cohort (ostatni dzień przed cart close = blanket)
- Sale announcement dla customer list
- Cart abandonment retargeting

### Kiedy NIE używać

- **Website viewers (non-buyers)** — jeszcze nie ma quality, każdy optimization event to będzie podobna pula (wystarczy 1)
- **Page engagers** — tylko Facebook engagement, słabe jako source quality
- **Broad interest audience** — to nie retargeting, użyj 1 dobrego event

---

## 6. Advantage+ Shopping Campaigns (ASC) — stan 2026

### API versioning

| Version | Data | Status |
|---|---|---|
| v22.0 | 2025 | Legacy ASC endpoints w pełni supported |
| v23.0 | Apr 2025 | Dodane `advantage_state` + `advantage_state_info` (read-only) |
| v24.0 | Sep/Oct 2025 | Create/update legacy ASC/AAC BLOCKED na v24; działa na v23 fallback |
| **v25.0** | **Q1 2026** | **BREAKING: Create/update legacy ASC/AAC blocked na WSZYSTKICH wersjach. Musi być Advantage+ unified structure** |

### ASC targeting constraints

- **Nie można** wykluczać interests / demografii
- **Można** ustalić country-level geo
- **Można** ustalić język (od late 2025)
- **Można** ustalić existing-customer budget cap (split new vs returning)
- Minimum do sensu: Pixel z Purchase events + catalog (dla e-com)

### ASC vs manual Sales — decision matrix

| Użyj ASC gdy... | Użyj manual Sales gdy... |
|---|---|
| ≥ 50 purchases/tydz account-wide | < 50 purchases/tydz |
| Masz catalog (e-com) | Brak katalogu (usługi, B2B) |
| Broad creative pool (5+ kreacji) | Wąska nisza wymagająca exclusions |
| Testujesz scaling | Testujesz nowe angles / audiencje |

### Health/Wellness/Finance restrictions (od 2025)

> [DO WERYFIKACJI] Te ograniczenia Meta wprowadzała najpierw głównie w USA. Zanim powiesz sklepowi z Polski, że nie może optymalizować pod zakup, sprawdź komunikat w Menedżerze reklam i aktualne zasady przez `ads_get_help_article`.

**Health (Jan 2025+)**:
- Nie można optymalizować pod Purchase / AddToCart / Checkout / Appointment
- Musi używać: LPV, Engagement, Video Views, Lead
- Custom audiences z nazwami wskazującymi na health conditions (np. "Diabetes Book Buyers") **BLOCKED od Sep 2025**
- Lookalike z tych audiences też BLOCKED

**Finance (early 2025+)**:
- Musi zadeklarować Financial Products category albo rejection
- Customer-list custom audiences **restricted od March 2025**
- Advertiser verification mandatory w 38 krajach
- Custom audiences z nazwami typu "High Income Leads", "Low Credit Score Leads" **BLOCKED** (Aug 2025)

Nie obchodź tych ograniczeń, na przykład zmianą nazwy listy. Jeśli kampania podlega ograniczeniom, pracuj w ich ramach albo zapytaj wsparcie Mety.

**Special Ad Categories (Housing/Employment/Credit)**:
- Age locked 18-65+
- All genders
- No ZIP targeting < 15mi
- No lookalikes z Meta data
- No detailed interests

---

## 7. CBO — Campaign Budget Optimization

### Kiedy włączać

- 3-5 ad sets per CBO campaign (nie 1-2, nie 10+)
- Weekly budget ≥ 50 × target CPA (żeby każdy ad set miał szansę learning)
- Dobre gdy kilka ad setów z podobnym celem, chcesz żeby Meta alokował

### Min spend per ad set

- Ustaw 10-20% budżetu kampanii na start
- Aggregate min-spends ≤ 50-70% budżetu (zostaw miejsce algorytmowi)
- Po ~1 tygodniu **usuń min-spends** żeby Meta mogło optymalizować free

### Kiedy NIE używać CBO

- 1 ad set w kampanii (bez sensu)
- Testy z bardzo różnymi audiences (Meta alokuje do najtaniej konwertującej, resztę głodzi)
- Kampanie brand vs performance w jednej — rozdziel

---

## 8. Budget scaling

> Zasada skalowania dla użytkownika jest w `procedury/progi.md` (+10% dziennie, zmianę robi użytkownik). Ta sekcja to tło.

### Zasady (2026 update)

- **Tempo bezpieczne**: ≤ 20% wzrostu na pojedyncze zmiany, co 3-4 dni
- **Jon Loomer 2025 update**: nie pilnuje już ściśle 20% — "learning reset to nie koniec świata". Co się liczy: sygnały, nie ochrona fazy.
- CBO skaluje płynniej niż per-ad-set increases
- Budget decrease > 20% również resetuje learning — takie same zasady

### Progi skalowania (decision table)

| Sygnał | Akcja |
|---|---|
| ROAS > target + 30%, `delivery_status.days_remaining_at_budget = 0` | Skaluj według `procedury/progi.md` (+10% dziennie) |
| CPA < target, frequency < 2, IS audience OK | Podnieś +10-15% |
| ROAS/CPA w celu, frequency 2-3 | Budżet OK, szukaj nowych kreacji |
| ROAS pogarsza się po podwyżce | Cofnij do poprzedniego, poczekaj tydzień |

### Skalowanie przez duplikację (manual Sales)

1. Tylko dla zaawansowanych i nigdy jako pierwszy krok, bo duży skok budżetu często zabija zwycięzcę (`procedury/progi.md`). Duplikuj ad set z wyższym budżetem
2. Zostaw oryginał
3. Po 7 dniach sprawdź który wygrywa
4. Pause przegranego

**Uwaga**: duplikacja = nowy learning phase dla duplikatu. Nie duplikuj za często.

---

## 9. Account-level limits

| Limit | Wartość |
|---|---|
| Max kampanii per ad account | 5 000 (rozszerzalne do 10 000) |
| Max ad sety per ad account | 5 000 (rozszerzalne do 10 000) |
| Max ads per ad set | 50 |
| `spend_cap` | USD cents, hard cap. NIE wpływa na pacing, IO & R&F nie supported |
| Daily budget minimum | ~$1/day dla impressions, ~$5/day dla conversion objectives |

### Spend cap pułapka

- Klient ustawia spend_cap blisko miesięcznego budżetu → kampanie gasną pod koniec miesiąca

---

## 10. Prezentacja danych

- **ZAWSZE tabelki** z wartością konwersji (purchase_value)
- **Nad każdą tabelką** napisz: *"Dane za [X] dni, atrybucja 7d click + 1d view (unified)."*
- **ROAS** — format procentowy (450% nie 4.5x). Jeśli user preferuje `x` format — respektuj preference
- **Currency** — sprawdzaj `account_currency` z insights. NIE zgaduj po nazwie konta
- **Frequency** zawsze z kontekstem: "1.8 (ok)", "3.2 (warning)", "4.1 (wypalenie)"
- NIE pokazuj aliasów kont user'owi — pokazuj nazwę konta

---

## 10b. Core Setup — ukryty setting który może zepsuć retargeting

Mało znana funkcja Events Manager która może zrujnować custom audiences + custom conversions bez żadnego ostrzeżenia.

### Co to jest

**Core Setup** to restriction mode w Events Manager. Meta czasem **włącza to automatycznie** dla kont z risky niches (health, finance). Gdy włączone — **nie możesz tego wyłączyć**.

### Jak sprawdzić

1. Events Manager → Data Sources → wybierz Pixel
2. Settings → szukaj **"Core Setup"**
3. Jeśli widoczne i ON = tryb restrictive aktywny

### Co się psuje gdy Core Setup ON

**1. URL rules w custom conversions i audiences są ignorowane.**

Meta bierze pod uwagę TYLKO top-level domain. Wszystko po `/` jest ignorowane.

Przykład: chcesz audience "Visited `/thankyou`":
- **Intencja**: użytkownicy którzy zobaczyli `/thankyou` po zakupie
- **Rzeczywistość przy Core Setup ON**: audience = wszyscy którzy weszli na domain, niezależnie od ścieżki

**Konsekwencje dla retargetingu:**
- "Visited product page" audience = de facto "visited site at all"
- "Visited thank-you page" (purchasers proxy) = de facto "visited site"
- Exclusion audiences nie działają precyzyjnie → retargetujesz tych którzy już kupili → przepala budżet

**Konsekwencje dla custom conversions:**
- Custom conversion "Purchase = URL contains /thank-you" = de facto "Purchase = URL is your domain" = każda wizyta liczy się jako purchase
- Totalny chaos danych

**2. Custom parameters są ignorowane.**

Standard parameters (value, currency, content_ids) działają. Custom parameters (content-name, content-tag, itp.) są odrzucane przez Pixel.

### Fix (adaptacja gdy Core Setup ON)

- **NIE używaj URL rules** dla żadnych custom conversions ani audiences
- **Używaj events** zamiast URL rules:
  - `ViewContent`, `AddToCart`, `InitiateCheckout`, `Purchase` (standard events)
  - Custom events (np. `ProductViewed`, `ConfigurationComplete`)
  - Standard parameters (value, currency, content_ids) — te działają
- **Przekonstruuj audiences** na bazie events zamiast URL paths

### Dlaczego Meta to zrobił

Zabezpieczenie przed transmisją personal information (health conditions, finances, itd.) przez URL parameters. Account z Core Setup ON = Meta klasyfikuje Cię jako "risky for data leakage" i ogranicza precyzję targetowania.

---

## 11. Diagnostyka "kampania nie wyświetla"

Gdy user zgłasza "kampania nic nie wydaje" — sprawdź w tej kolejności:

1. **`effective_status`** — czy faktycznie ACTIVE, czy paused / ended / in_review
2. **`spend_cap`** — czy nie osiągnięty (account, campaign albo ad set level)
3. **Learning phase FAIL / LIMITED** — bez eventów Meta konserwatywnie gasi delivery
4. **Budget utilization** — czy `daily_budget > daily_spend` (mogło być budget-limited)
5. **Creative status** — czy ad jest approved, nie disapproved
6. **Pixel health** — czy Pixel odpala, jeśli nie → konwersje nie wracają → algorytm gasi
7. **Audience saturation** — `reach / audience_size > 0.7` = publiczność wyczerpana
8. **Targeting restrictions** — Special Ad Category może ograniczać delivery
9. **Ad account status** — czy nie jest restricted / disabled
10. **Currency mismatch / billing issue** — sprawdź `business_manager.billing_status`

**Każda z tych przyczyn wymaga innego fix'a.** Sprawdź wszystkie 10 punktów i wskaż 1 do 3 najbardziej prawdopodobnych.

---

## 12. Sezonowość Meta (e-commerce, PL)

| Okres | Charakterystyka | Akcja |
|---|---|---|
| Styczeń | Wyprzedaże posezonowe, powrót po świętach | Standardowy budżet |
| Luty | Walentynki (2-tygodniowa kampania) | +20-30% na kreacje walentynkowe |
| Marzec-Kwiecień | Wiosna, Wielkanoc, Dzień Kobiet | Sezonowe kreacje |
| Maj-Czerwiec | Dzień Matki, Dzień Ojca, Dzień Dziecka | Po 2 tyg kampanie per okazja |
| Lipiec-Sierpień | Lato, wakacje — **dołek** dla wielu branż | Nie skaluj agresywnie, skup się na LTV |
| Wrzesień | Back to school | Sezonowy boost edu / dzieci |
| Październik-Listopad | **BFCM (Black Friday / Cyber Monday)** = największy peak | Przygotuj kreacje 4-6 tyg wcześniej, podnoś budżet 15%/tydz |
| Grudzień | Święta (do 20.12 dostawa na czas) | Po 20.12 wycofaj ofertę "dostawa na święta" |

### Przed szczytem sezonu (4-6 tyg wcześniej)

1. Zwiększ budżet 10-15% co tydzień → daj Meta algorytmowi czas na adaptację
2. Przygotuj sezonowe kreacje (Halloween, BFCM, Christmas)
3. Sprawdź Pixel, CAPI, spend_cap — nie chcesz że coś pada w szczycie
4. Rozszerz catalog product sets jeśli masz sezonowe SKU

### W szczycie

- **NIE zmieniaj** optimization goal ani bid strategy — pozwól algorytmom pracować
- Skaluj tylko budżet jeśli `days_remaining_at_budget = 0`

### Po szczycie

- Stopniowo obniżaj budżet (10-15%/tydz)
- Nie tniej nagle — learning phase reset w dołku sezonowym = katastrofa

---

## 13. Kanibalizacja kampanii (retargeting vs prospecting)

- Lookalike z Customers 180d + retargeting Customers 30d → overlap może być 40%+
- **Zawsze wykluczaj** customer audience z prospecting ad sets
- **Retargeting ad set** powinien mieć frequency cap — ad set-level frequency control

Przykład excluded setup:
- Ad set A (prospecting): Lookalike 1-3% Buyers 180d. **Exclude**: Customers 30d, Customers all-time
- Ad set B (retargeting): Website visitors 30d (no purchase). **Exclude**: Customers 30d

---

## 14. Checklist przed startem kampanii (PMax equivalent)

### Account setup
- [ ] Pixel + CAPI skonfigurowane
- [ ] EMQ > 7 na Purchase event
- [ ] Domain verified (dla AEM)
- [ ] Business Manager verification (dla Financial Services / Health)
- [ ] Catalog skonfigurowany (dla ASC e-com)
- [ ] Custom Audiences: Buyers 180d, Customers all-time, Website 30d

### Campaign
- [ ] Correct objective (OUTCOME_SALES vs OUTCOME_LEADS vs OUTCOME_TRAFFIC)
- [ ] Geo ustawione (nie zostawiaj "all")
- [ ] Attribution `7d_click + 1d_view` (unified)
- [ ] `special_ad_categories: []` albo właściwa kategoria (Housing/Employment/Credit/Finance)

### Ad Set
- [ ] Optimization goal pasuje do objective (Purchase dla Sales, Lead dla Leads)
- [ ] Budget daily vs lifetime — default daily
- [ ] Targeting: Advantage+ Audience jeśli klient nie ma preference "no broad"
- [ ] Placementy: Advantage+ Placements (Meta optymalizuje)
- [ ] Age + gender: domyślnie 18-65+, all (unless brand requires)

### Ad
- [ ] Creative format odpowiedni do placementu (9:16 dla Reels/Stories, 1:1 lub 4:5 dla Feed)
- [ ] Character count OK (125 primary text, 40 headline, 30 description)
- [ ] CTA button dopasowany (Shop Now, Learn More, Sign Up)
- [ ] Landing URL z UTM tags
- [ ] Pixel PageView odpala na landing page (weryfikuj w Test Events)

---

## 15. Rutyna miesięczna

| Tydzień | Zadanie |
|---|---|
| 1 | Pełna diagnoza (`procedury/diagnoza.md`) |
| 1 | Status fazy nauki każdego aktywnego zestawu (§2) |
| 2 | Przegląd kreacji, rotacja zmęczonych (`knowledge-meta-creative.md` §5) |
| 2 | Nakładanie się grup odbiorców (§5) |
| 3 | Piksel i CAPI, EMQ (`knowledge-pixel-capi.md`) |
| 3 | Historia zmian na koncie |
| 4 | Czy strategia stawek pasuje, czy skalować (§3, §8) |
| 4 | Review catalog / disapproved products (dla e-com) |

## 15a. Audience Network: sprawdzaj, wykluczaj, gdy szkodzi

> Dla sklepu: nie wykluczaj z automatu. Wyklucz, gdy tani CPM idzie w parze z brakiem sprzedaży albo podejrzanymi leadami (`procedury/progi.md`, CPM). Poniżej tło, dlaczego bywa groźny przy leadach.


### Problem — Bot Traffic

Audience Network (AN) pozwala reklamom wyświetlać się na **3rd-party apps + websites** spoza FB/IG. Meta dzieli revenue z ownerem tej app/website.

**Exploit**: ludzie budują **bot networks**:
1. Boty wchodzą na konto reklamodawcy, klikają, opt-in'ują (jako "leads")
2. Algo widzi activity → zaczyna serwować reklamy **other similar bots** żeby "optymalizować"
3. Boty "odwiedzają" website z Audience Network ads
4. **Creator botów dostaje revenue od Facebooka** za "impressions" na swojej website
5. Scale → decent passive income

**Case study**: B2B lead gen client z CPL ~$200. Jednej nocy CPL **spadł do ~$2**. To nie success — to bot invasion. Algo "nauczyło się" jak dostarczać $2 "leads". Nie dało się tego odwrócić.

**Fix**: wyklucz Audience Network, wyczyść listę leadów z botów i zgłoś sprawę do wsparcia Mety. Nie zakładaj nowych kont, żeby ominąć problem.

### Drugi problem — "Junk impressions"

Nawet gdy nie jest to bot traffic, w praktyce Audience Network **często dostaje slammed** z low-quality impressions. Nie zawsze, ale **gdy idzie źle, idzie **BARDZO** źle, **BARDZO** szybko**.

### Risk-reward analysis

- **Reward** (gdy AN działa): slight incremental reach, **minimal dodatkowe conversions**
- **Risk** (gdy AN idzie źle): totalnie compromised algo, konieczność rebudowy wszystkiego

**Conclusion**: risk vastly outweighs reward. **Exclude od dnia 1.**

### Jak wyłączyć

**W Business Manager (global dla konta):**

1. Business Manager → **Advertising Settings**
2. **Account Controls**
3. **Placement Controls**
4. Slide toggle: **"My business can only advertise on specific placements"**
5. Uncheck **"Audience Network"**

**Ważny detal**: to NIE resetuje learning phase w istniejących kampaniach (w przeciwieństwie do manualnych zmian placements per ad set).

### Wyjątki

- **Brand awareness kampanie** z bardzo dużym budżetem (nad $50k/mies) — AN może działać dla reach
- **Video content na dedicated placements** — rzadko, ale bywa
- **Typowo**: exclude zawsze, chyba że masz konkretny powód

---

## 15b. Post IDs — aggregate social proof + learning

### Problem: duplikat ad = nowy Post ID

Gdy tworzysz "ten sam" ad w różnych ad setach lub kampaniach, Meta **tworzy osobne Post IDs**. Każdy ma:
- Własne likes, shares, comments (social proof)
- Własną algorithmic learning
- Osobny "feed life"

**Konsekwencja**: social proof **spread'uje się cienko** zamiast koncentrować. Gdy scale'ujesz winner przez duplikację, zostawiasz całe algo learning w starym adie.

### Case study

Working with client in sceptical niche. Client miał **control ad z ogromną social proof** (lots of likes/comments/shares).

Powstało **kilka lepszych ads** (lepsze copy). **Żaden nie pobił control'a.** Dlaczego?

Gdy client zechciał zmienić landing page → ad został **odtworzony** z tą samą copy, headline, video — ale **nowym Post ID** (erased social proof).

**Przy nowym Post ID z tą samą kreacją → nowa copy pobiła original CONSIDERABLY.**

**Lesson**: nie underestimate social proof. Nie underestimate Post ID persistence.

### Rozwiązanie: Use Existing Post ID

Zamiast tworzyć duplikat ad, **pointuj do istniejącego posta**. Wszystkie ad sety / kampanie używają tego samego Post ID → aggregate:
- **Social proof** (all likes/comments/shares in one place)
- **Algorithmic learning** (cross-campaign)

### Jak znaleźć Post ID

1. Ads Manager → select ad
2. Click **"Preview"**
3. Click arrow upper right
4. Under "See Post" → select **"Facebook Post with Comments"**
5. Skopiuj part URL po `posts/` — string of numbers
6. **Pro tip**: paste Post ID w ad name → łatwe tracking (np. `[PID:1234567890] Summer_Sale_V2`)

### Jak użyć Post ID w nowym adzie

1. Przy tworzeniu new ad, szukaj dropdown: **"Create Ad"**
2. W dropdown → **"Use Existing Post"**
3. Scroll down, tiny link: **"Enter Post ID"** (łatwo przeoczyć)
4. Paste numbers
5. Configure rest, publish

### Debata: Post ID vs raw duplicate

Domyślnie lepsze są Post IDs. Kontrargument: przy scaling, **duplicate without changes** może być better bo zachowuje attribution windows specific to ad set.

**AdFlow approach**: Post IDs by default dla aggregating social proof. Duplicates tylko przy świadomym scaling testing (duplicate ad set z nowym budżetem).

---

## 15c. European Digital Services Taxes (DST) — Location Fees

### Co się dzieje

Od **1 lipca 2026**, Meta zaczyna **przekazywać DST** (Digital Services Tax) na reklamodawców zamiast absorbować go sam.

Historia: kraje EU wprowadzały DSTs od 2019 (France first). Meta płaciła sama **miliardy tax** przez lata. Teraz **changes model** — passesuje na advertisers.

### Lista krajów + stawki (stan 2026)

| Kraj | Location fee |
|---|---|
| **Austria** | 5% |
| **France** | 3% |
| **Italy** | 3% |
| **Spain** | 3% |
| **Turkey** | 5% |
| **United Kingdom** | 2% |

(Polska **nie na liście** jeszcze. Ale może się zmienić — monitor.)

### Jak to działa

- Billing: spend + location fee = total charge
- Fee per ad spend w danym kraju (nie per impression, conversion, revenue)
- **NIE pokazuje się w Ads Manager dashboards**
- **NIE uwzględnione w daily budget**
- **NIE uwzględnione w CPA/ROAS/bids/spend limits**
- Widoczne **tylko na invoice** końcowym

### Pułapka algorytmiczna

**Algo jest unaware of location fees.** Dla algo:
- CPA US = $101 → "worse"
- CPA Austria = $100 → "better"
- Algo faworytuje Austria → serwuje więcej tam
- Ty **actually** płacisz $100 + 5% = $105 za Austria
- Algo myśli że dostaje $100 CPA, Ty faktycznie płacisz $105
- **Real CPA w Austria wyższe niż US**, ale algo tego nie widzi

### Fix — Value Rules

Meta's nowy feature pozwala **modify bid per user type**:

1. Ads Manager → Campaign → **Value Rules**
2. Create rule: **"Users in Austria"**
3. **Bid adjustment: -5%** (albo -10% dla bezpieczeństwa)
4. Save

Algo widzi że oferujesz 95% normal bid w Austria → bid'uje tylko na really good opportunities → balances real cost.

**Per kraj**: setup separate value rules, rate matching DST rate (-5% dla Austria, -3% dla France, itd.).

### Kiedy to jest big deal

- **Razor thin margins** — 2-5% może wreck economics
- **Large spend** — 5% z $100k/msc = $5k/msc extra
- **Heavy European traffic** — jeśli < 10% spend na EU, ignoruj

### Kiedy NIE jest big deal

- **Healthy margins** — to koszt doing business
- **Small spend na EU** — fee absorbable

### Alternative: exclude countries

Nuclear option: wyklucz te kraje z targetowania. Ale:
- **Tracisz konwersje** które byłyby profitable
- **Heavy-handed** — lepiej użyć Value Rules

### Monitoring

- **UK**: DST 2% — tax może spaść po trade deal z US
- **Canada**: briefly had DST, eliminowany przez trade deal
- **US opposed** do DSTs na corporations jak Meta/Google → **USA nigdy nie będą miały DST** (najpewniej)
- **Polska**: nie ma DST yet, ale możliwe w 2027+

**AdFlow powinien update listę krajów + stawek kwartalnie** (co 3 miesiące sprawdzać oficjalne Meta announcements).

---

## 16. Andromeda — reality check

### Co to jest Andromeda

Meta's nowa architektura targetingu (rollout rozpoczęty 2025, deployed na wszystkie konta do lipca 2025). Generalnie: AI-powered creative optimization + expanded audience exploration.

### Dlaczego większość people misunderstanding


**Co trzeba zrozumieć:**

1. **Zuckerberg przyznał**: Facebook ma w tym samym czasie **tysiące wersji platformy** (user side). Logicznie: to samo na ad side.
2. **Meta ToS explicitly pozwala** im na split-testing bez informowania i to może wpływać na performance.
3. **Obserwacyjnie**: każdy kto zarządzał wieloma kontami wie, **że konta działają różnie** — różne features, różne UI, różna performance przy tych samych ustawieniach.

### Konsekwencje

- **"Andromeda update"** to **vision / kierunek**, nie jeden dyskretny release
- Różne konta mogą mieć **różne wersje Andromedy** w tym samym czasie
- Rollout to prawie zawsze **v1 → v1.1 → v1.2 → v1.3 → v2.0**, nie binary change
- Meta stale tweakuje — nie oczekuj że "understand Andromeda" = ustabilizowana wiedza

### Operacyjne zasady

1. **Nie traktuj żadnego insightu o Meta jako absolute** — to co działa dla jednego konta może nie działać dla innego (inne algo version)
2. **Testuj na własnym koncie** — jeśli knowledge mówi "X działa", a Tobie nie — to nie znaczy że knowledge jest zły, może masz inną algo version
3. **Twoje notatki z `twoja-praca/` > pliki `wiedza/`**, bo odzwierciedlają aktualną rzeczywistość Twojego konta
4. **Przy Advantage+ features** (Advantage+ Audience, Advantage+ Creative, Advantage+ Placements) nie zakładaj że user ma tę samą wersję co inna agencja — **testuj per konto**

### "Adaptation mindset"


Najzdrowsza perspektywa dla AdFlow: traktuj knowledge files jako **current best understanding**, nie **bible**. Kiedy user zgłasza "to nie działa u mnie" — prawdopodobnie ma inną algo version. Fix: test, iterate, zapisz w `twoja-praca/<sklep>/` to, co działa naprawdę.

---

## Źródła

- [Meta Business Help — Learning Phase](https://www.facebook.com/business/help/112167992830700)
- [Meta Marketing API — Advantage+ Shopping](https://developers.facebook.com/docs/marketing-api/advantage-shopping-campaigns/)
- [Jon Loomer — Bid Strategies](https://www.jonloomer.com/facebook-ads-bid-strategies/)
- [Jon Loomer — Meta Ads Targeting 2026](https://www.jonloomer.com/meta-ads-targeting-2026/)
- [Jon Loomer — Learning Phase Edits](https://www.jonloomer.com/facebook-ads-edits-learning-phase/)
- [Foxwell Digital — Audience Overlap Advantage+](https://www.foxwelldigital.com/blog/how-to-lower-audience-overlap-advantage-shopping-campaigns)
- [Tracklution — Sensitive Ad Categories 2025](https://www.tracklution.com/learn/navigating-meta-sensitive-ad-categories-2025/)
- [Dataslayer — Attribution Window Jan 2026](https://www.dataslayer.ai/blog/meta-ads-attribution-window-removed-january-2026)
