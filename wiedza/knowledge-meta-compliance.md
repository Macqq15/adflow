# Wiedza ekspercka — Compliance Meta Ads

Zgodność z zasadami Mety: odrzucone reklamy, ograniczone konta, kategorie wrażliwe, weryfikacja. Stan: 2026.

**Dla kont w risky niches**: health, supplements, biz opp, finance, crypto, weight loss. Ale techniki działają dla każdego konta.

---

## 1. Odrzucona reklama i ograniczone konto

Zasada: nie obchodzimy systemu weryfikacji Mety. Żadnych podmian treści po akceptacji, „rozgrzewania” konta seriami publikowanych i wyłączanych reklam ani zakładania nowych kont po blokadzie. To łamie zasady Mety i może skończyć się trwałą blokadą firmy. Każda taka akcja wymagałaby też publikowania reklam, czego AI w AdFlow nie robi.

### Gdy reklama została odrzucona

1. Przeczytaj powód odrzucenia w Menedżerze reklam (status reklamy, szczegóły). Connector pokazuje błędy przez `ads_get_errors`.
2. Sprawdź, której zasady dotyczy, w Zasadach reklamowych Mety (`ads_get_help_article`).
3. Popraw reklamę: tekst, grafikę albo stronę docelową. Najczęstsze przyczyny w sklepach to obietnice efektu, „przed i po”, zwracanie się do cech osobistych odbiorcy („Masz cukrzycę?”) i niezgodność reklamy ze stroną. Szczegóły w `knowledge-meta-creative.md` §9.
4. Jeśli uważasz, że odrzucenie jest błędne, użytkownik klika **Poproś o weryfikację** (Request review) przy reklamie.
5. Nie publikuj w kółko tej samej treści. Powtarzane odrzucenia obciążają konto.

### Gdy konto albo strona ma ograniczenia

1. Użytkownik otwiera **Jakość konta** (Account Quality) w ustawieniach firmy. Tam jest powód i przycisk odwołania.
2. Odwołanie składa użytkownik, z prawdziwymi danymi firmy. AI może pomóc napisać uzasadnienie.
3. Do czasu decyzji nie zakładaj nowego konta reklamowego ani nowej firmy, żeby ominąć ograniczenie.
4. Dla bezpieczeństwa: weryfikacja firmy (§8) i domeny (§9), dwuetapowe logowanie dla wszystkich administratorów.

---

## 6. Health / Finance specyfika

> [DO WERYFIKACJI] Te ograniczenia Meta wprowadzała najpierw głównie w USA. Zanim powiesz sklepowi z Polski, że nie może optymalizować pod zakup, sprawdź komunikat w Menedżerze reklam i aktualne zasady przez `ads_get_help_article`.

### Health (Jan 2025+)

Nie można:
- Optymalizować pod `PURCHASE`, `ADD_TO_CART`, `CHECKOUT`, `APPOINTMENT`
- Custom audiences z health-indicating names (np. "Diabetes Book Purchasers") — **BLOCKED Sep 2025+**
- Lookalike z tych audiences — **BLOCKED**
- Targeting < 18 dla weight loss

Musisz używać:
- `LANDING_PAGE_VIEW`, `ENGAGEMENT`, `VIDEO_VIEWS`, `LEAD` (basic)

### Finance (early 2025+)

- Musi zadeklarować **Financial Products category** przy setup kampanii
- Bez tego = rejection
- Customer-list custom audiences — **restricted od March 2025**
- Advertiser verification wymagany w 38 krajach (2026)
- Custom audiences z financial-indicating names ("High Income", "Low Credit Score") — **BLOCKED Aug 2025+**

## 7. Special Ad Categories

Gdy Twoje konto jest w Special Ad Category (Housing / Employment / Credit), Meta wymusza:

- **Age**: locked 18-65+ (nie możesz segmentować wiekowo)
- **All genders** (nie możesz target per gender)
- **No ZIP targeting < 15 miles** (geo restrictions)
- **No lookalikes from Meta data** (Meta-generated lookalikes zabronione)
- **No detailed interests** (interest targeting severely limited)
- **Ogłoszenie w UI**: musisz oznaczyć kampanię jako Special Ad Category przy tworzeniu (campaign level, nie ad set level)

### Diagnostyka

Gdy diagnoza wykryje kampanię w Special Ad Category:
- Flag as CONTEXT (not problem) w outputcie
- Wszystkie rekomendacje targetowania muszą respektować te restrictions
- NIE proponuj Advantage+ Audience (Meta-generated) dla tych kampanii

---

## 8. Business Manager verification

### Kiedy wymagana

- **Financial Services** kampanie (38 krajów, w tym PL od Q1 2026)
- **Pharmaceutical / health** (niektóre kraje, w tym UK, US, Germany)
- **Political / social issues** ads
- **Accounts flagged by Meta** — mogą wymagać ad-hoc

### Proces

1. Business Manager → Business Settings → Security Center
2. **Business Verification** button
3. Upload dokumentów (business registration, proof of address)
4. **1-3 dni** na review
5. Po verification → dostęp do wrażliwych kategorii

### Pułapka

- Bez verification, ads w tych kategoriach **dostają rejection automatycznie**
- Wielu klientów nie wie że problem to brak verification (myślą że copy jest zły)
- **AdFlow should check**: status verification Business Managera przed rekomendowaniem kampanii w risky niches

---

## 9. Domain verification (dla AEM)

### Po co

iOS 14.5+ AEM (Aggregated Event Measurement) wymaga zweryfikowanej domeny żeby:
- Meta mógł priorytetyzować events (8 per domain, teraz automatic)
- Track conversions na iOS prawidłowo
- Unikać "Action Blocked — URL Restricted" rejections

### Jak zweryfikować

1. Business Manager → Business Settings → **Brand Safety** → **Domains**
2. Add domain
3. **3 metody weryfikacji**:
   - **DNS TXT record** (najszybsze, profesjonalne) — dodaj TXT z Meta do DNS
   - **HTML file upload** — upload file z Meta na root domeny
   - **Meta tag** — paste w `<head>` section
4. Czekaj na propagację (DNS: 15 min do 48h)

---

## 10. Ad Library compliance research

### Co to jest

Meta Ad Library (facebook.com/ads/library) — **public search wszystkich aktualnych ads**. Możesz sprawdzić:
- Jakie ads konkurencji biegają teraz
- Ile ads total per strona
- Czy konkurent ma "Page Transparency" issues

### Zastosowanie w compliance strategy

1. **Przed uruchomieniem kampanii w risky niche** — sprawdź Ad Library czy konkurenci mają ads approved
2. **Jeśli Twoje ads są rejected, a konkurent biega z podobnymi** → review policy (feedback loop w Business Manager)
3. **Adaptacja copy** — zobacz jak konkurenci formułują claims (w granicach policy)

### Pułapka

- Ad Library pokazuje **tylko currently running ads**
- Rejected ads NIE pojawiają się tam
- Więc widzisz tylko "compliance winners" — nie wiesz ile ich ads zostało rejected

---

## 12. Crisis management — Meta platform bugs

### Dlaczego to jest w compliance

Platform bugs Meta **to nie Twoja wina**, ale mogą zniszczyć Twoje wyniki w ciągu godzin. Umiejętność rozpoznania "to Meta bug, nie moja kampania" = kluczowa dla sanity agencji.

### Case study: Jan 6 2026 — Landing Page Views bug

**Co się stało:**
- 6 stycznia 2026, ~9AM PST
- **Massive** drop w metryce `landing_page_view` we wszystkich kontach
- Konta które normalnie miały 90% link clicks → LPV teraz widziały 40-50%
- Np. konto 1000 LPV/dzień → 500/dzień overnight
- **Performance kampanii spadł** bo Meta używa LPV jako signal dla optymalizacji (szczególnie dla high-ticket / low-volume kont)

**Teorie co to było:**

Theory 1 (iOS26 aggressive blocking):
- iOS26 (wrzesień 2025) strip'uje `fbclid` parameter z URL przed page load
- To MASSIVE problem — `fbclid` to kluczowy element jak Meta łączy user profile z akcją na stronie
- ALE: iOS26.3 rollout w beta Jan 6 to small numbers, iOS changes adopted slowly — nie explanation dla massive overnight change

Theory 2 (Meta's proactive response to Apple):
- Meta widzi że Apple idzie w strone blokowania fbclid i innych tracking
- Meta **proactively** próbuje rebuild algorytm który przetrwa te zmiany
- Modeluje landing page views zamiast polegać na direct tracking
- **Platform-level change** niezależne od site, Pixel code, browser, device
- (Wsparcie theory: Meta no longer wymaga Pixela dla campaigns optimizing for LPV — direct evidence że Meta modeluje LPV)

**Resolution**: Po ~tygodniu Meta **informally przyznał że to bug**, naprawił, LPV wróciły do normalnych poziomów.

### Framework kryzysowy — 5 action items

Gdy zauważasz **massive degradation** performance na wielu kontach jednocześnie:

**Action 1: Button up signal transmission**
- Sprawdź czy wszystkie core events **firing**: ViewContent, AddToCart, InitiateCheckout, Lead, Purchase
- **CAPI z airtight transmission** (ratio CAPI:Pixel > 80%)
- Event Match Quality > 7.0 na wszystkich eventach
- Dla two-step checkout: fire Lead albo AddToCart przy opt-in

**Action 2: Rethink audience strategy**
- Retargeting audience przez website może zawierać **znaczną część** poprzedniej populacji
- Consider: **on-platform engagement audiences** (Facebook page engagers, Instagram engagers) — te nie zależą od website tracking
- Exclusion audiences mogą być "leaky" — accept imperfect exclusions

**Action 3: Adjust budget/scaling**
- Kryzys może być **tymczasowy** (jak w Jan 6 — naprawione w tydzień)
- Rozważ **obniżenie budżetu** albo **wolniejsze scaling** dopóki shockwaves nie ustąpią
- Przygotuj systems do **scale back up** gdy resolved

**Action 4: Device segmentation (ostrożnie)**
- Duplikuj kampanie segmentowane przez device type (iOS vs Android)
- Pozwala izolować **co się dzieje** per device
- **Ostrzeżenie**: często tworzy więcej problemów niż rozwiązuje — small volumes, learning phase reset, itd.
- Analizuj **actual CPA delta** iOS vs Android przed decyzją — jeśli parity → nie warto segmentować

**Action 5: Relax**
- To jest paid traffic game. Change is inevitable.
- Kontynuuj pracę na kreacjach i funnelu
- Test nowe approaches (manual bids mogą być wonky)
- **Paniczne decyzje w momencie kryzysu = gorsze decyzje**

### Jak rozpoznać "to Meta bug" vs "moja kampania się zepsuła"

**Sygnały że to platform issue:**
- **Wiele kont** pokazuje ten sam wzorzec w tym samym czasie
- **Konkretna metryka** zmienia się drastycznie bez zmian konfiguracji
- **Ads Manager UI** pokazuje nietypowe zachowanie (opóźnienia, brakujące dane, errors)
- **Community (Jon Loomer Group, Foxwell Network)** raportują ten sam problem
- **Timing correlates** z public iOS update albo Meta platform update

**Sygnały że to Twoja kampania:**
- Degradation tylko w **niektórych** kontach
- Koinciduje z **edytami** które robiłeś
- Metryki są spójne z historyczną volatility
- Inne agencje nie raportują

### Gdzie szukać info

- **Facebook Business Status**: [status.facebook.com](https://status.facebook.com) — oficjalny status
- **Jon Loomer blog & Facebook Group**
- **Foxwell Network Slack**
- **Twitter/X: search "Meta Ads bug" + filter by latest**
- **Andrew Foxwell newsletter** — często pierwszy raportuje platform-wide issues

---

## 13. Ludzie i treści wygenerowane przez AI

- Najprościej i najbezpieczniej: bez realistycznych ludzi wygenerowanych przez AI. Produkt w scenie, dłonie, prawdziwi klienci za ich zgodą.
- Meta oznacza część treści stworzonych lub zmienionych przez AI etykietą informacyjną i wymaga ujawnienia w niektórych kategoriach reklam. Sprawdź aktualne zasady przez `ads_get_help_article`, zanim użyjesz syntetycznej osoby.
- W UE obowiązki przejrzystości dla treści generowanych przez AI wynikają też z AI Act. [DO WERYFIKACJI] Zakres i daty stosowania dla reklam sprawdź w aktualnym źródle, zanim cokolwiek obiecasz użytkownikowi.
- Nie ukrywaj oznaczeń i nie próbuj sprawić, żeby odbiorca ich nie zauważył.

---

## 14. Comment Management — signal for algo

### Czemu komentarze matter


3 powody:

**1. People read comments**
- Szczególnie **older demographics** i **skeptical audiences**
- Check comments jako "scam verification"
- Lots of positive comments = reassurance

**2. Engagement opportunity**
- Honest questions w komentarzach — respond = conversion opportunity
- Ignore = lost sale

**3. Algorytmiczny signal** (⭐ najbardziej niedoceniany)
- Meta evaluates **who comments + what they comment**
- Content komentarzy **wpływa na targeting**

### Kluczowy insight: komentarze wpływają na targeting

Real example:

> Ad for **cooking brand**. Someone randomly comments o **bass fishing**. Next: more comments o bass fishing. Next: **ad serwowany do bass fishing enthusiasts**.

Meta widzi content komentarzy → traktuje jako signal "tym ludziom ten content jest relevant" → serwuje do similar people. Flood cycle.

**Implikacja**: **zły pierwszy komentarz może skręcić całą targeting** w złą stronę. Comment section to **audience steering tool** którego większość ignoruje.

### 4 zasady comment management

**Zasada 1: Ban negative commenters + hide/delete komentarz**

- **Ban**, nie tylko hide — jeśli tylko hide, Meta nadal serwuje reklamy tej osobie
- Negative commenter zostawia więcej negative comments w przyszłości = **vicious cycle**
- Ban breaks the cycle

**Jak ban:**
- W Ads Manager comment: **... menu** → **Ban from Page**

**Zasada 2: Legit customer service complaints → DM**

- Move conversation to private message
- **Hide original comment** (nadal viewable dla commenter'a i friends'ów)
- Public-facing ad section stays clean

**Zasada 3: Meta's comment moderation tool + keyword filters**

W Meta Business Suite → Comment Moderation:
- Auto-hide komentarze zawierające keywords
- Sample filters:
  - **Spam indicators**: "scam", "BS", "fake"
  - **Brand-specific**: konkurent nazwy
  - **Language**: profanity filter

Regularne unhide false flags (co tydzień-dwa).

**Zasada 4: Engage positive comments**

Na ads bez wielu komentarzy:
- Positive comment → **odpowiedz**
- Jeśli brand-related (np. music), pytaj "what's your favorite?"
- Tag inne positive commenters → group conversation
- Więcej engagement = thread elevated w default comment sort = first impression viewer'ów lepsza

### Bonus tips

**1. Text expander dla standard responses**
- QuickKey / TextExpander / macOS text replacement
- Standardowe "thanks for your comment!" / "DM sent" etc.
- Wariować subtly żeby nie wyglądało canned

**2. Arguments między komentującymi = algo juice**
- If ludzie kłócą się w komentarzach **bez negative brand impact** → let them go
- More engagement = more algo distribution
- Zakaz: gdy kłótnia dotyczy Twojego brand / product quality → intervene

---

---

## Źródła

- [Meta Business Help — Business Verification](https://www.facebook.com/business/help/2058515294227817)
- [Meta Business Help — Domain Verification](https://www.facebook.com/business/help/286768115176155)
- [Meta Ad Library](https://www.facebook.com/ads/library/)
- [Tracklution — Sensitive Ad Categories 2025](https://www.tracklution.com/learn/navigating-meta-sensitive-ad-categories-2025/)
