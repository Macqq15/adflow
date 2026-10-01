# knowledge-meta-catalog.md

Zweryfikowany stan wiedzy: Meta Commerce Manager + Product Catalogs + Product Sets + Advantage+ Catalog Ads. Data: kwiecien 2026. Zrodla cytowane w sekcji koncowej.

## 1. Catalog architecture 2026

Od 2023 **Catalog Manager zostal wchloniety przez Commerce Manager** (business.facebook.com/commerce). Jedno UI obsluguje: katalog, Shop na FB/IG, checkout, zamowienia. "Catalog Manager" jako osobny produkt nie istnieje - link przekierowuje.

| Catalog type | Zastosowanie |
|---|---|
| E-commerce | Standard SKU, 90% przypadkow |
| Travel | Hotele, loty, destynacje |
| Real Estate | Listings nieruchomosci |
| Auto | VIN-level, dealerships |
| Home Services | Uslugi lokalne |

**Hierarchia:** `item_group_id` (model) > `id` (SKU/wariant) > `content_id` (tracking Pixel/CAPI, musi == `id`).

## 2. Feed sources

| Metoda | Pros | Cons | Best use |
|---|---|---|---|
| Shopify/Woo/Magento native | Realtime sync, zero config | Przesyla wszystko (brak filtrow) | <5K SKU, jedna platforma |
| Scheduled feed (URL) | Hourly/daily/weekly refresh, kontrola | Opoznienia stock | Sredni katalog, CSV/XML host |
| Uploaded (CSV/XML) | Pelna kontrola | Manual, brak synchr | <100 SKU, test |
| API (Catalog Batch) | Realtime, programatic | Dev required | >50K SKU, enterprise |
| **BaseLinker** (PL) | XML export z 300+ platform (Shoper/IdoSell/Allegro), multi-warehouse sync | Dodatkowy koszt, XML scheduled (nie realtime) | PL multi-channel |
| **Sembot** (PL) | Feed optimization PL, rules | Mniejszy niz DFW | PL SMB |
| **DataFeedWatch** | 2000+ kanalow, PL UI, AI mapping | Premium pricing | Multi-channel, multi-market |

## 3. Atrybuty

**Required (9):** `id`, `title` (<=150), `description` (<=5000), `availability` (in stock/out of stock/preorder), `condition` (new/refurbished/used), `price` (z walutą: "99.00 PLN"), `link`, `image_link` (min 500x500, **realnie 1200x1200**), `brand`.

**High-impact optional:**
- `google_product_category` (pelna sciezka taksonomii Google)
- `product_type` (wlasna taksonomia sklepu)
- `sale_price` + `sale_price_effective_date`
- `gtin` / `mpn` (zwiekszaja match rate)
- **`custom_label_0-4`** - 5 kolumn dla segmentacji Product Sets (margin, bestseller tier, sezon, launch date, stock level)

**Uwaga:** Edycja `custom_label` wywoluje re-review produktu (temporary unavailable). Alternatywa: **Internal Labels** (nowsze, nie triggeruja review).

## 4. Disapproval reasons - taksonomia 2026

| Kategoria | % disapproval | Typowy trigger |
|---|---|---|
| Personal Attributes (Policy 4.3) | **24%** | "You" language, before/after (implied transformation), targetowanie wagi/zdrowia |
| Landing Page Mismatch | **11%** | "Free shipping" w ad, min. order na LP; MARS scan realtime |
| AI-generated content brak disclosure | **14%** | Nieoznaczone AI creative |
| Health/medical claims | wysokie | "Helps improve in 7 days" = unverified, nawet przy FDA |
| Image issues | srednie | Text >20% (miekki), watermark, low-res <500px |
| Feed vs LP price/stock drift | srednie | Auto-disapprove po 3 wykryciach |
| Restricted verticals | kategoryczne | Alcohol, weapons, adult, supplements (per-country) |

Diagnostyka: Commerce Manager > Catalog > Issues > filter by "Rejected" - Meta podaje konkretny policy code.

## 5. Product Sets strategy

Rule: **1-4% produktow generuje 80-90% sprzedazy** (Pareto w e-com).

| Set | Definicja (custom_label lub rule) | Cel |
|---|---|---|
| Top bestsellers | `custom_label_0 = bestseller` (top 4% revenue 30d) | Prospecting, najwyzszy ROAS |
| Zombie | >100 klikniec, 0 zakupow / 60d | Wyklucz z budzetu |
| Seasonal | `custom_label_1 = Q4` / holiday | Ramp-up sezonowy |
| Margin-based | `custom_label_2 = high_margin` (>40%) | Value-based bidding |
| New arrivals | `custom_label_3 = launch_30d` | Awareness + cold |
| Low stock | `availability=in stock AND quantity<10` | Exclude (unikaj wyprzedania w ads) |
| Brand-based | `brand = X` | Multi-brand segmentation |

Foxwell best practice: osobny Product Set per CLV tier (new customer acquisition vs existing - Meta Customer Lifecycle Strategy, Q2 2026).

## 6. DPA vs Advantage+ Catalog Ads

**"Dynamic Product Ads" = stara nazwa, formalnie rebranded na "Advantage+ Catalog Ads" w 2023.** Nie ma juz dwoch produktow - jest jeden z dwoma trybami konfiguracji:

| Wybor 2026 | Kiedy |
|---|---|
| Manual targeting + wlasny Product Set | Niszowa oferta, duzy catalog, testy, wlasna segmentacja buyer tiers |
| **Advantage+ Catalog Ads (default)** + Andromeda retrieval | Default dla 95% przypadkow. +22% ROAS on avg, Meta AI wybiera produkty. Broad audience. |

Od 2025 Advantage+ = default dla Sales/Leads/App Promotion. Andromeda (2024-2026) = nowy retrieval engine, +8% relevance score.

## 7. Catalog performance metrics

- **Product-level ROAS** (Commerce Manager > Performance) - benchmark DPA: 2-3x avg, top quartile 5x+
- **Click potential** - Meta-specific score (0-100) szacujacy predicted CTR dla produktu
- **Impression share per product** - % wygranych aukcji (via Value Rules)
- **Conversion rate uplift** - DPA dostarcza +30% vs static retargeting
- **Personalized click rate** - +50% vs non-personalized

## 8. Common issues

| Problem | Diagnostyka |
|---|---|
| "Disapproved, nie wiem czemu" | Commerce Manager > Diagnostics > wybierz produkt > Policy code |
| Feed freshness | Daily minimum; realtime przez API jesli stock zmienia sie szybko |
| Out-of-stock | Ustaw `availability=out of stock` - Meta auto-exclude z ads w <24h |
| Multi-currency | Osobny katalog per waluta LUB `override` per country feed |
| Content ID mismatch Pixel vs feed | Case-sensitive: "ITEM101" != "item101" = brak matchu |

## 9. Catalog health checklist

- [ ] >=99% produktow "Active" (Commerce Manager dashboard)
- [ ] Feed refresh <24h (scheduled) lub <1h (API)
- [ ] 0 missing required attributes
- [ ] Price feed == price LP (check sample 20 SKU)
- [ ] Images >=1200x1200 (nie tylko 500 minimum)
- [ ] Title 50-150 chars, keyword upfront
- [ ] Description wypelnione (nie tylko SKU)
- [ ] `google_product_category` set (pelna sciezka)
- [ ] `custom_label_0-4` uzywane strategicznie
- [ ] 0 duplikatow `id`

## 10. Pitfalls

1. **Duplicate products** - ten sam SKU, rozne `id` (np. Shopify variant vs parent) - rozbija learning
2. **Shopify native + custom feed conflict** - dwa zrodla = ghost disapprovals. Wybierz jedno.
3. **Advantage+ Creative auto-edycja opisow** - Meta zmienia copy; wylacz dla brandow regulowanych (Ad Set > Advantage+ creative > off)
4. **Product set overlap** - ten sam produkt w 5 setach = audience overlap, wojna aukcyjna wewnetrzna
5. **500x500 minimum trap** - technicznie pass, performance fail na mobile
6. **Zbyt czeste edycje `custom_label`** - triggeruje re-review, produkt znika z ads na 4-24h; uzyj Internal Labels

## 11. Polish-specific

| Platforma PL | Meta catalog path |
|---|---|
| **BaseLinker** | XML Facebook Feed app, 82+ sklepow pod jednym kontem |
| **Shoper** | Natywny Facebook Product Ads, auto-feed |
| **IdoSell** | Dedykowana integracja "Katalogi Produktow na Facebooku" |
| **Allegro** | Przez BaseLinker (brak natywnego) |
| **Sembot** | Feed optimization PL-first |

**Taksonomia:** Uzywaj angielskich kategorii Google (Meta = Google taxonomy). PL titles OK, category zawsze EN path.

**VAT w `price`:** Zawsze ceny **brutto** (z VAT). Format: `"129.99 PLN"`. Niespojnosc brutto/netto feed vs LP = disapproval.

---

## Sources

- [Meta: Product Data Specifications for Catalogs](https://www.facebook.com/business/help/120325381656392)
- [Meta: About catalogs for products and services](https://www.facebook.com/business/help/890714097648074)
- [Meta: Product image specifications](https://www.facebook.com/business/help/686259348512056)
- [Meta: Troubleshoot Products With Policy Violations](https://www.facebook.com/business/help/2741254916111768)
- [Meta: About Advantage+ Catalog Ads](https://www.facebook.com/business/help/397103717129942)
- [Meta Engineering: Andromeda retrieval engine](https://engineering.fb.com/2024/12/02/production-engineering/meta-andromeda-advantage-automation-next-gen-personalized-ads-retrieval-engine/)
- [Jon Loomer: 83 Changes to Meta Advertising in 2025](https://www.jonloomer.com/meta-advertising-changes-2025/)
- [Jon Loomer: Advantage+ Catalog Ads glossary](https://www.jonloomer.com/glossary/advantage-catalog-ads/)
- [Foxwell Digital: Customer Lifecycle Strategy 2026](https://www.foxwelldigital.com/blog/customer-lifecycle-strategy-coming-to-meta-ads-in-2026)
- [AdAmigo: Meta Ad Policy Compliance 2026](https://www.adamigo.ai/blog/meta-ad-policy-compliance-strategies-2026)
- [AdNabu: Facebook Product Feed Specifications 2026](https://blog.adnabu.com/facebook/facebook-product-feed-specifications/)
- [Flexify: Internal vs Custom Labels](https://www.flexify.net/help/using-internal-labels-to-create-product-sets-on-meta)
- [Cropink: Custom Labels vs Internal Labels](https://cropink.com/internal-labels-vs-custom-labels)
- [DataFeedWatch: Facebook Dynamic Product Ads integration](https://www.datafeedwatch.com/integrations/facebook-dynamic-product-ads)
- [BaseLinker API docs](https://api.baselinker.com/)
- [IdoSell: Facebook Product Ads i Catalog Facebook](https://pomoc.idosell.com/marketing-i-promocje/integracja-z-facebookiem/facebook-product-ads-i-catalog-facebook)
- [LighterImage: Facebook Catalog Image Optimization](https://lighterimage.com/guides/facebook-catalog-image-optimization.html)
- [Marpipe: Complete Guide to Meta Catalog Ads Setup](https://www.marpipe.com/blog/facebook-product-feed-complete-guide-to-meta-catalog-ads-setup)
- [Cropink: Meta DPA Guide 2026](https://cropink.com/meta-dpa)
- [1ClickReport: Meta Andromeda 2026](https://www.1clickreport.com/blog/meta-andromeda-update-2025-guide)
