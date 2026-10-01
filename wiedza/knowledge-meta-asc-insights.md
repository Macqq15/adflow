# Wiedza ekspercka — ASC Insights & Reporting (Advantage+ Shopping)

Co Meta Advantage+ Shopping Campaigns udostępnia w raportach — i czego NIE ma (w przeciwieństwie do Google).

---

## 1. Search Themes w ASC — NIE ISTNIEJĄ

**Meta nie udostępnia search terms ani search themes dla ASC.** W przeciwieństwie do Google Ads:

| Google Ads | Meta ASC |
|---|---|
| Pełny "Search terms" report (rzeczywiste zapytania) | **Brak search terms** |
| Intent signal = typed query | Intent-less surface (scroll feed) |
| Reporting: "kto wyszukał co?" | Reporting: "kto konwertował?" |
| Optimization unit: keyword match | Optimization unit: audience + creative |
| Transparency: full | Black-box ML |

Meta Marketing API dla ASC **nie eksponuje** query-level breakdown. Dostępne breakdowns to: age, gender, country, region, placement, device, impression_device. **Nie ma** `search_query` ani `search_term`.

### Konsekwencja dla analyst'ów

Pytanie "co ludzie wyszukują żeby znaleźć produkt?" jest **nieapplicable** w ASC. Zastąp je:

> **"Jaki segment demograficzny + placement + creative kombinacja daje najwyższy ROAS?"**

---

## 2. Co ASC FAKTYCZNIE reportuje

### Breakdowns dostępne

- **Product-level** — per-SKU ROAS, CTR, purchases (via catalog feed, breakdown `product_id`)
- **Placement** — Feed, Stories, Reels, Marketplace, Audience Network (`publisher_platform`, `platform_position`)
- **Age/gender** — demographic converters (`age`, `gender`)
- **Geographic** — `country`, `region`, `dma` (US-specific)
- **Ad creative** — per-ad ROAS, hook rate, thumb-stop rate
- **Device/OS** — `device_platform`, `impression_device`

### ASC-specific metrics (unique vs manual Sales)

- **`new_customer_acquisition`** — ratio new vs returning (wymaga Customer Lifetime Value setup w Events Manager)
- **`incremental_conversions`** — jeśli włączony Conversion Lift study
- **Existing customer budget cap** — splitting budget new vs returning
- **Per-product ROAS** — automatic via catalog (nie wymaga manual ad sets)

---

## 3. Alternatywne source'y intent data

Jeśli klient chce intent insights dla planning:

| Source | Co daje | Use case |
|---|---|---|
| **Google Keyword Planner** | Volume + commercial intent | Jeśli klient ma Google Ads account, cross-reference keywords |
| **Google Search Console** | Organic queries dla brand domain | Shared brand signal |
| **Pinterest Trends** | Visual search signals, top 50 kategorii | Trending themes dla Reels/Stories |
| **TikTok Creative Center** | Trending hashtags, top ads per region | Wizualny search intent dla Meta placements |
| **SEMrush / Ahrefs** | Competitor keyword analysis | Strategic positioning |
| **AnswerThePublic** | Question-based queries | Content angles |

**Best practice**: TikTok Creative Center + Pinterest Trends to najbliższy ekwiwalent "wizualnego search intent" dla Reels/Stories.

---

## 4. Audience-driven analysis (Meta's preferred approach)

Zamiast query analysis, Meta rekomenduje:

1. **Advantage+ Audience insights** — po 50+ konwersjach Ads Manager pokazuje top demographic clusters konwertujących
2. **Lookalike source analysis** — export top 1% customer LTV → analiza w Sheets/BI → stwórz bardziej precyzyjne seed audiences
3. **Custom Audience segmentation** — buyer personas via behavior:
   - Cart abandoners (30d)
   - 30d purchasers
   - ViewContent non-purchasers (warm but didn't convert)
   - 60-day customer churn



---

## 5. ASC insights per level

| Level | Available Insights |
|---|---|
| **Campaign** | ROAS, CPA, spend, reach, frequency, new customer % |
| **Ad Set** | **LIMITED w ASC** — Meta nie pozwala na manual audience splits. Jedyna opcja: existing vs new customer budget cap |
| **Ad** | Creative ranking (Quality, Engagement, Conversion rankings), placement breakdown, demographic |
| **Product** | Per-product ROAS, click potential (Commerce Manager only) |

---

## 6. "Click potential" — Meta-internal metric

- **Lokalizacja**: Commerce Manager → Catalog → per product
- **Co pokazuje**: Meta's estimate nieużytej expozycji per product
- **Użycie**: identyfikacja products które mogłyby sprzedawać więcej ale nie dostają ruchu (zazwyczaj problem feed quality albo pricing)

---

## 7. Rekomendacje dla agencji (TL;DR)

Gdy klient pyta **"co konwertuje w ASC?"**:

1. **Breakdown per product** (catalog) — top 10 SKUs driving 80% revenue
2. **Breakdown per placement** — Reels vs Feed vs Stories ROAS split
3. **Demographic breakdown** — age/gender/geo converters
4. **Creative ranking** — hook rate, thumb-stop, per-ad ROAS
5. **New vs returning** — ASC-specific, pokazuje acquisition efficiency

**Nie próbuj** replikować Google search terms report — to inne narzędzie, inna filozofia.

**Edukuj klienta**: Meta to **discovery engine**, nie **intent engine**.

---

## 8. Andromeda era — co zmieniło ASC

Meta Andromeda (nowy retrieval engine, rollout 2024-2026):

- **+8% relevance** (Meta internal)
- **+22% ROAS** w pilot testach
- Dla ASC oznacza że manual targeting jest mniej wartościowy (Meta AI lepiej targetuje)
- **Konsekwencja**: Advantage+ Audience > manual interests/lookalikes w większości przypadków (knowledge-meta-domain.md §16)

**Ale** — Andromeda to vision/kierunek, nie dyskretny release. Każde konto może mieć inną wersję (patrz knowledge-meta-domain.md §16 "Andromeda reality check").

---

## Źródła

- [Meta Marketing API — Advantage+ Shopping](https://developers.facebook.com/docs/marketing-api/advantage-shopping-campaigns)
- [Meta Business Help — About Advantage+ Shopping Campaigns](https://www.facebook.com/business/help/advantage-shopping-campaigns)
- [Jon Loomer — ASC Complete Guide](https://www.jonloomer.com/advantage-plus-shopping)
- [Foxwell Digital — ASC Framework](https://www.foxwelldigital.com/blog/advantage-shopping-campaigns)
- [Meta Andromeda Engineering](https://engineering.fb.com/2024/12/02/production-engineering/meta-andromeda-advantage-automation-next-gen-personalized-ads-retrieval-engine/)
- Hernan Vazquez YouTube (free content o ASC)
