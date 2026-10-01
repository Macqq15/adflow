# Wiedza ekspercka — Pixel, CAPI, EMQ, AEM (Meta Tracking 2026)

Setup + diagnostyka + optymalizacja Meta trackingu. Stan: 2026.

---

## 1. Architektura: Pixel vs CAPI vs Dataset

| Layer | Status 2026 | Rola |
|---|---|---|
| **Pixel (browser)** | **AKTYWNY** (nie deprecated) | Client-side events, fbp/fbc capture, session context |
| **CAPI (server)** | **DE FACTO WYMAGANE** | Obchodzi ad-blockery, iOS ITP, cookie loss; główne źródło signal |
| **Dataset** (architektura od 2025) | Unifikacja web + app + offline + messaging | Pixel staje się jednym ze źródeł Datasetu |

**Rekomendacja 2026:** Pixel + CAPI razem (hybrid). **Nigdy CAPI sam** — Pixel daje fbp/fbc/browser context których CAPI-only nie ma. Meta oficjalnie promuje hybrid setup.

---

## 2. Event Match Quality (EMQ)

### Progi ogólne (skala 0-10)

| Score | Bucket | Interpretacja |
|---|---|---|
| 0-3 | Poor | Red flag, niekompletne customer info |
| 4-5 | Fair/OK | Room for improvement |
| 6-7.9 | Good | Minimalny akceptowalny baseline |
| 8-8.9 | Great | **Target produkcyjny** |
| 9-10 | Excellent | Diminishing returns powyżej 8 |

### Event-specific targety

| Event | Target EMQ |
|---|---|
| PageView / ViewContent | 4.5-7 (top-funnel, mało customer info) |
| AddToCart / InitiateCheckout | 6-8 |
| **Purchase** | **7.5-9** (0-5.9 at-risk, 6-7.9 good, 8-8.9 great, 9+ excellent) |
| Lead | 6+ |

### Parametry — priority ranking (Meta)

| Priority | Parametry |
|---|---|
| **High impact** | email (SHA-256 hashed), click ID (fbc/fbclid) |
| **Medium impact** | phone (SHA-256), external_id, FB Login ID, browser ID (fbp), birthdate, country |
| **Low impact** | first/last name, city, zip |
| **Technical** (nie hashować!) | fbp, fbc, IP, User-Agent |

**Rule of thumb:** email + phone + external_id + fbp + fbc **razem** = dramatyczny skok EMQ vs pojedyncze identyfikatory.

---

## 3. Server-Side GTM — comparison 2026

| Opcja | Cena/msc | Effort | Komu |
|---|---|---|---|
| **Stape.io Free** | $0 | Niski | 10K req — test/MVP |
| **Stape Pro** | $17 | Niski | 500K req — mała agencja |
| **Stape Business** | $83 | Niski | 5M req — **rekomendowany dla mid e-com** |
| **Stape Enterprise** | $167 | Niski | 20M req |
| **Stape Meta CAPI Gateway** | $10/pixel/msc (lub $100/100 pixeli) | Minimalny | No-code, managed |
| **Google Cloud Run** (self-hosted) | ~$40-120 | **Wysoki** (setup + maint) | Tylko zespół z DevOps |
| **Custom CAPI build** | $2K-5K+ initial | 40-80h dev | Enterprise z bespoke needs |

### Setup workflow (Stape + sGTM)

1. Utwórz sGTM container w Stape
2. Skonfiguruj **custom domain** (CNAME) — kluczowe dla 1st-party cookies
3. Meta CAPI tag template → pixel ID + access token
4. Przekaż event_id, em (hashed email), ph (hashed phone), fbp, fbc, external_id, IP, UA
5. Test w Events Manager → Test Events tab

### Pitfalls

- Brak custom domain = 3rd-party cookie (zanikają)
- `_fbc` nie trwały → trzeba refresh z fbclid
- Brak `event_id` = Pixel + CAPI double-count

---

## 4. AEM (Aggregated Event Measurement) — stan 2026

**Update czerwiec 2025**: Meta **usunęło 8-event cap**. AEM tab zniknął z Events Manager.

| Aspect | Status 2026 |
|---|---|
| Event prioritization | **Nie istnieje** — Meta automatycznie agreguje wszystkie eligible events |
| Domain verification | **Nadal wymagana** (dla Brand Safety, Ads Manager restrictions, ownership) |
| iOS 14.5+ impact | **20-35% reportowanych konwersji = modeled** (Meta twierdzi że underreporting spadł z 15% do 8%) |
| SKAdNetwork | Nadal dla app installs; AEM-like mechanizm dla web działa automatycznie |

**Co teraz matters** (zamiast prioritization): event schema consistency — `event_id`, `currency`, naming convention.

---

## 5. Deduplication (Pixel + CAPI)

### Wymaganie

Każdy event = **identyczne** `event_name` + `event_id` w Pixel i CAPI.

- `event_id` = UUID lub hash(order_id + timestamp). **Case-sensitive**.
- `external_id` ≠ `event_id`:
  - `external_id` = stabilny user ID (CRM, user.id)
  - `event_id` = unique per event (order.id, session.id)
- Window dedupu: Meta łączy w ciągu kilku minut
- Docelowy dedup rate: **~100%** dla eventów gdzie oba źródła firują

### Verify

Events Manager → Overview → kolumna **"Deduplication"**.

### Common issues

- Różne `event_id` (Pixel = UUID, CAPI = order_id — **mismatch!**)
- Różne casing (`"purchase"` vs `"Purchase"`)
- Brak `event_id` po jednej stronie
- Timing > 10 min między Pixel i CAPI

---

## 6. Standard events + required parameters

| Event | Required | Recommended |
|---|---|---|
| PageView | — | fbp, fbc |
| ViewContent | `content_ids`, `content_type` | value, currency |
| AddToCart | `content_ids`, `content_type=product` | value, currency |
| InitiateCheckout | `value`, `currency` | content_ids, num_items |
| **Purchase** | **`value`, `currency`** (bez = niekwalifikowany do optimization!) | content_ids, content_type=product, order_id |
| Lead | — | value, currency, content_name |

**Custom events** — tylko gdy standard events nie pokrywają (np. `TrialStarted`, `SubscriptionRenewed`). Wymagają custom conversion setup w Events Manager.

---

## 7. Diagnostyka

| Narzędzie | Co sprawdza | Status 2026 |
|---|---|---|
| **Meta Pixel Helper** (Chrome ext v4.0.1) | Pixel firing client-side | **AKTYWNY** (wymaga FB login od 02/2026). Nie widzi CAPI. |
| **Events Manager → Test Events** | Oba źródła (browser + server) | **Primary tool**, realtime |
| **Events Manager → Overview** | Dedup %, EMQ, event volume, diagnostics | Daily check |
| **Graph API Explorer** | CAPI payload validation | Dla devs |
| **Omnibug** (Chrome ext) | 25+ platform debugger | Alt dla Pixel Helper, multi-platform |

### ⚠️ Ograniczenia Marketing API

**EMQ (Event Match Quality), CAPI coverage ratio, Dedup rate** są **UI-only w Events Manager** — nie są dostępne przez Marketing API jako pola. Connector Mety ma narzędzie `ads_get_dataset_quality`, sprawdź najpierw, co zwraca. Przez samo API da się pobrać:

- ✅ `last_fired_time` (z `AdsPixel` endpoint)
- ✅ Event volume (z pixel `/events` edge, manual aggregation)
- ❌ EMQ per event — user musi sprawdzić w Events Manager UI
- ❌ CAPI coverage ratio — user musi sprawdzić w Events Manager UI
- ❌ Dedup rate — user musi sprawdzić w Events Manager UI

Dla automated EMQ tracking — trzeba by scrapować Events Manager UI (nie polecamy).

---

## 8. Common issues u e-commerce

| Issue | Fix |
|---|---|
| Pixel not firing | Sprawdź consent banner (CMP), ad-blocker, wrong pixel ID |
| EMQ < 5 | Dodaj hashed email + phone + external_id + fbp + fbc |
| Duplicate events | Brakujący/niezgodny event_id — zsynchronizuj po obu stronach |
| Cross-domain (sklep + checkout na różnych domenach) | Przekaż fbp/fbc via URL param lub server session; verify **obie** domeny |
| Purchase bez optimization | Dodaj **value + currency** (wymagane, inaczej event nie optymalizuje) |

---

## 9. Core Setup — weryfikacja (knowledge-meta-domain.md §10b cross-reference)

- **Status 2026:** AKTYWNY, dotyka verticals Health/Financial/wrażliwe
- **Detect:** Events Manager → Data Sources → [Pixel] → Settings → **"Data Restrictions"** (ikona: yellow = L1 Core, red = L2 Standard Event, near-zero events = L3 Full)
- **Impact:**
  - URL rules: redukcja URL do domain-only (tracisz path-based audiences)
  - Custom parameters: usunięte
  - Advanced matching: zablokowane
  - Custom audiences: delay/pause
- **Permanent** — po włączeniu nie można wyłączyć

---

## 10. Jan 6 2026 LPV bug — lesson learned

Patrz knowledge-meta-compliance.md §12. Platform bug mógł naruszyć tracking na wielu kontach. **Zawsze sprawdzaj** status platform (Facebook Business Status) przed debug własnego setupu.

---

## Źródła

- [Meta CAPI Deduplication](https://developers.facebook.com/docs/marketing-api/conversions-api/deduplicate-pixel-and-server-events/)
- [Meta fbp/fbc params](https://developers.facebook.com/docs/marketing-api/conversions-api/parameters/fbp-and-fbc)
- [Meta AEM official help](https://www.facebook.com/business/help/721422165168355)
- [Meta EMQ help](https://www.facebook.com/business/help/765081237991954)
- [Jon Loomer — Core Setup](https://www.jonloomer.com/qvt/what-is-core-setup/)
- [Stape pricing](https://stape.io/price)
- [Stape EMQ guide](https://stape.io/blog/how-to-improve-event-match-quality-facebook)
- [Attribuly — Purchase EMQ benchmarks](https://attribuly.com/blogs/meta-purchase-emq-benchmarks/)
- [Triple Whale — EMQ](https://www.triplewhale.com/blog/event-match-quality)
- [AdExchanger — iOS underreporting 15%→8%](https://www.adexchanger.com/platforms/meta-claims-underreporting-for-ios-web-conversions-is-now-down-from-15-to-8/)
