# Meta Ads Placements — 2026 Knowledge File

Last verified: April 2026. Sources: Meta Business Help Center, Jon Loomer Digital, Foxwell Digital, Motion Creative Benchmarks 2026, Dataslayer changelog, AdAmigo, benly.ai. Benchmarks marked `[not publicly disclosed]` where Meta does not publish per-placement data — third-party estimates only.

## 1. Placements 2026 (19 surfaces)

**Facebook:** Feed, Video Feeds, Reels, Stories, Right Column (desktop), Marketplace, In-Stream Video, Search Results, Business Explore.
**Instagram:** Feed, Explore Feed, Explore Home (grid tile), Stories, Reels, Search Results (API rolled out March 2025).
**Messenger:** Stories, Sponsored Messages. *Messenger Inbox ad placement removed 11 Nov 2025.*
**Audience Network:** Native/Banner/Interstitial, Rewarded Video, In-Stream Video. *Default exclude for conversions.*
**Threads:** Feed (global rollout completed Jan–Apr 2026, mobile only, 4:5 + carousel + video).

## 2. Benchmarks per placement (third-party, 2026)

| Placement | CPM | CTR | Notes |
|---|---|---|---|
| Facebook Feed | ~$7.47 | 1.11% | Workhorse, highest volume |
| Instagram Feed | $6.25–$7.68 | ~1.2% | 4:5 gives ~1% CTR lift vs 1:1 |
| Instagram Stories | ~$6.25 | 1.34% | 61% higher CTR than FB Feed |
| Reels (IG+FB unified) | Lowest of primary placements | 2.0–2.5%+ | Meta subsidizing inventory |
| Right Column Desktop | Very low CPM | <0.3% | Legacy, minimal scale |
| Audience Network | Artificially low CPM | Inflated | ~67% bot traffic per 3rd-party audits |
| Messenger Stories | [not publicly disclosed] | [not publicly disclosed] | Thin inventory |
| Threads Feed | [not publicly disclosed] | [not publicly disclosed] | Delivery intentionally throttled in ramp |
| Search Results (IG/FB) | [not publicly disclosed] | Higher intent | New placement, limited data |

**Frequency thresholds (Andromeda era, 2026):** [DO WERYFIKACJI] algorithm may throttle at frequency around 2.5 over 7 days. Decyzje o wymianie kreacji podejmuj według `procedury/progi.md` (powyżej 3 z rosnącym kosztem kliknięcia, powyżej 4 wymiana). Reels fatigue faster than Feed (pattern recognition). Refresh creative every 2–3 weeks (was 4+ pre-Andromeda). Red flags: CTR down 20%+ from 7-day peak, CPA up 15%+ from baseline, frequency >3.0.

## 3. Advantage+ vs Manual — decision rules

**Default to Advantage+ Placements.** 2026 aggregate data: ~11.7% CPA improvement, 10–20% efficiency gain. GEM (Meta's generative ads model, live since Q2 2025) optimizes across sequences of placements, not individual ones — isolating placements breaks the optimization.

**Use Manual when:**
- Brand safety lockdown (regulated industries, Audience Network carve-out)
- Creative mismatch — no 9:16 asset → exclude Stories/Reels/Threads
- Niche B2B audience where Advantage+ drifts to cheap low-intent inventory
- Retargeting with specific placement strategy (Stories for warm, Feed for cold)
- Testing isolated placement hypothesis

**Jon Loomer's 2026 position:** don't manually exclude Audience Network when optimizing for conversions — the algorithm self-corrects. Only exclude if post-purchase data proves junk traffic.

## 4. Red flags — when to exclude

| Placement | Issue | Action |
|---|---|---|
| Audience Network Classic | ~67% bots per independent audits | **Default exclude** for lead gen / low-ticket e-com |
| Messenger Sponsored Messages | Intrusive, <1% CR | Exclude unless warm retargeting |
| Right Column Desktop | Ancient CTR (<0.3%) | Exclude unless pure reach play |
| Facebook Marketplace | Physical-product bias | Exclude for services/SaaS/info products |
| AN Rewarded Video | Incentivized clicks | Exclude for conversion campaigns |

## 5. Format × placement matrix

| Format | Feed | Stories | Reels | Right Col | Messenger | AN | Threads |
|---|---|---|---|---|---|---|---|
| Single 1:1 | Yes | — | — | Yes | Yes | Yes | Yes |
| Single 4:5 | **Optimal** | — | — | — | — | — | Yes |
| Video 9:16 | Yes (7% CTR lift) | **Yes** | **Yes** | — | Yes | — | Yes |
| Carousel 1:1 / 4:5 | Yes | Yes (card-by-card) | — | — | Yes | Yes | Yes (2026+) |
| Collection | Yes | Yes | — | — | — | — | — |
| Advantage+ Catalog | Yes | Yes | Yes | — | — | Yes | Yes |

**March 2026 update:** Meta unified Stories + Reels (FB and IG) into single 9:16 safe zone (top 14%, bottom 35%, sides 6%). One 9:16 asset covers 4 placements. Export 1440×2560 when possible.

## 6. Device breakdown

- **iOS vs Android:** CPA roughly at parity post-ATT. iOS CPMs compressed 24% vs Android since 2021 (attribution loss). Android higher volume globally, iOS higher LTV in Western developed markets — test, don't assume.
- **Mobile vs Desktop:** 90%+ traffic mobile. Desktop converts higher (3.8% vs 2.1%) but thin volume.
- **Bid adjustments:** Use **Value Rules** (launched June 2025, expanded 2026) — adjust bids by device, placement, age, gender, geo without breaking ML. Do NOT split into separate ad sets for device targeting — fragments learning.

## 7. Age / gender breakdown

- **Do not segment ad sets by age/gender** — Advantage+ Audience handles it, splitting fragments learning phase.
- **Special Ad Categories (housing, employment, credit)** lock age/gender breakdown — accept the constraint.
- **Use breakdowns for creative direction only:** if 80% of conversions come from 35–44, brief creative for that demo, but keep targeting broad.

## 8. Geo breakdown

- **Country:** primary lever for multi-market campaigns. Split only when CPA differs >30% and volume supports it.
- **Region / City / DMA:** for local services. Meta added DMA-level targeting in US.
- **Radius:** 1–80 km around pin, for brick-and-mortar and field services.

## 9. Placement-specific tactics (2026)

- **Reels-first prospecting:** lowest CPMs on primary inventory, Meta actively subsidizing adoption. Lead top-of-funnel creative with 9:16 Reels-native (hook <3s, captions baked in, vertical).
- **Stories + Link Stickers:** all clicks now via sticker (swipe-up deprecated 2021). Best for retargeting — warm audience closes in Stories cheapest.
- **Feed 4:5 vs 1:1:** 4:5 takes more screen real estate → ~1% CTR lift. Default to 4:5 for static Feed creative.
- **Threads (2026):** test 4:5 image/video early for cheap impressions while delivery ramps; expect 6–12 months of unstable benchmarks.
- **Search Results (IG/FB):** higher intent, treat like mid-funnel. Pair with product listings / branded terms.

## 10. Budget allocation (post-Andromeda)

- **Default: CBO / Advantage+ Campaign Budget** — Meta allocates across placements via GEM.
- **Manual per-placement budgets — deprecated** in most objectives; Meta removed granular controls through 2025.
- **Value Rules replace manual bid adjustments** for age/gender/geo/device/placement — this is the supported lever in 2026.

## 11. Recent changes (2025–2026)

- **Nov 2025:** GEM (generative ads model) launched — ~5% conversion lift, optimizes ad sequences, not individual placements.
- **July 2025:** Value Rules expanded to 25 placements.
- **March 2025:** Instagram Search Ads added to Marketing API.
- **Jan–Apr 2026:** Threads ads global rollout completed; carousel + Advantage+ Catalog added.
- **March 2026:** Stories/Reels unified 9:16 safe zone.
- **11 Nov 2025:** Messenger Inbox placement retired.
- **Meta Search Ads (FB/IG search):** rolled out 2025, not yet a Google Search competitor in scale — use as incremental placement inside Advantage+, don't build isolated campaigns.

## Decision rules — quick reference

1. **Default Advantage+ Placements** for any conversion campaign. Don't override without data.
2. **Audience Network** sprawdzaj, nie wyłączaj z automatu. Jeśli CPM jest tani, a sprzedaży brak, sprawdź, ile wydatków idzie do Audience Network, i wtedy rozważ wykluczenie (`procedury/progi.md`, CPM).
3. **Design 9:16 first** — one asset covers Stories+Reels+Threads.
4. **Feed creative = 4:5** static, 9:16 video.
5. **Odświeżanie kreacji** według `procedury/progi.md` (częstotliwość powyżej 3 z rosnącym kosztem kliknięcia, powyżej 4 wymiana).
6. **Use Value Rules** instead of splitting ad sets for age/gender/device.
7. **Don't trust placement-level CTR/CPA in isolation** — GEM optimizes sequences; evaluate at ad-set level.

---
Sources: [Jon Loomer — Meta Advertising Changes 2025](https://www.jonloomer.com/meta-advertising-changes-2025/) · [Foxwell Digital — GEM & creative 2026](https://www.foxwelldigital.com/blog/what-metas-gem-really-wants-from-your-creative-in-2026) · [AdAmigo — Meta Benchmarks 2026](https://www.adamigo.ai/blog/meta-ads-benchmarks-2026-by-objective-and-placement) · [benly.ai — Feed vs Stories vs Reels 2026](https://benly.ai/learn/meta-ads/meta-ads-feed-vs-stories-vs-reels) · [Power Digital — Audience Network bot audit](https://powerdigitalmarketing.com/blog/facebooks-audience-network-wasting-ad-dollars-bot-traffic/) · [Social Media Today — IG Search Ads](https://www.socialmediatoday.com/news/instagram-search-ads-placement-marketing-api/651195/) · [TechCrunch — Threads global ads](https://techcrunch.com/2026/01/21/threads-rolls-out-ads-to-all-users-worldwide/) · [Dataslayer — 83 Meta changes 2025](https://www.dataslayer.ai/blog/meta-ads-changes-2025-83-updates-that-changed-facebook-advertising-forever) · [Meta Business Help — Ads Manager breakdowns](https://www.facebook.com/business/help/1098535543548363)
