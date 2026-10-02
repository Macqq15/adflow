# Connector Meta Ads

Podawaj kroki po jednym. Poczekaj, aż użytkownik wróci, zanim wyślesz następny. Siedem kroków naraz czyta się jak zadanie domowe.

Podłączamy to:

```
https://mcp.facebook.com/ads
```

To oficjalny connector Mety. Nie jest wtyczką, niczego się nie pobiera i nie zbudowaliśmy go my. Pozwala AI czytać konto reklamowe i budować w nim rzeczy wstrzymane.

## Nie wysyłaj ich do terminala

Connector podłącza się w ustawieniach aplikacji. Nikt nie instaluje programów, nie edytuje plików konfiguracyjnych i nie otwiera terminala.

## Claude

1. Otwórz claude.ai w przeglądarce albo aplikację Claude.
2. Wejdź w **Settings**, potem **Connectors**.
3. Wybierz dodanie własnego connectora (**Add custom connector**).
4. Nazwij go dokładnie **Meta Ads** i wklej `https://mcp.facebook.com/ads`. Od tej nazwy zależy blokada niebezpiecznych narzędzi w Claude Code.
5. Pojawi się okno z opcjami logowania (Authentication, OAuth client, Request headers). Niczego nie zmieniaj. Zostaw to, co oznaczone **Detected**, i kliknij **Add**.
6. Kliknij **Connect**. Otworzy się okno logowania do Facebooka.
7. Zaloguj się kontem, które ma dostęp do konta reklamowego, i zaznacz tylko te konta reklamowe, którymi chcesz zarządzać.
8. W nowej rozmowie włącz connector Meta Ads.

Na darmowym planie Claude można mieć ograniczoną liczbę własnych connectorów. Jeśli dodanie się nie udaje, zapytaj, czy nie mają już innego.

## Claude Code

Dwie drogi, wybierz jedną.

1. **Przez konto claude.ai.** Dodaj connector jak wyżej. Pojawi się w Claude Code zalogowanym tym samym kontem, ale dopiero w nowej sesji. Jeśli go nie widać, zamknij Claude Code i otwórz ponownie. Sprawdź komendą `/mcp`.
2. **Bezpośrednio w Claude Code**, na przykład gdy logujesz się kluczem API, a nie kontem claude.ai. W terminalu wpisz `claude mcp add --transport http -s user meta-ads https://mcp.facebook.com/ads`. Potem uruchom Claude Code, wpisz `/mcp`, wybierz `meta-ads` i zaloguj się w przeglądarce kontem Facebooka.

`.claude/settings.json` w tym folderze wymaga zgody na narzędzia zapisu i blokuje `ads_activate_entity` i narzędzia usuwające w obu wariantach nazw (`mcp__claude_ai_Meta_Ads__…` i `mcp__meta-ads__…`). Działa tylko przy nazwie connectora dokładnie „Meta Ads” w claude.ai albo `meta-ads` w terminalu. Przy innej nazwie blokada go nie obejmie, a zostaje tylko zakaz zapisany w `AGENTS.md`. To zabezpieczenie dodatkowe, nie jedyne.

## ChatGPT

1. Otwórz chatgpt.com albo aplikację ChatGPT.
2. Wejdź w **Settings**, potem **Apps** i **Advanced settings**, i włącz **Developer mode**. Wymaga planu Plus, Business albo Enterprise.
3. Wróć do **Apps** i kliknij **Create app**. Nazwij ją **Meta Ads**, wklej `https://mcp.facebook.com/ads`, jako sposób logowania wybierz **OAuth**.
4. ChatGPT przekieruje do Mety. Zaloguj się i zatwierdź uprawnienia.
5. W nowej rozmowie wybierz aplikację Meta Ads.

## Codex

1. W terminalu wpisz `codex mcp add meta-ads --url https://mcp.facebook.com/ads`.
2. Potem `codex mcp login meta-ads` i zaloguj się w przeglądarce kontem Facebooka.

[DO SPRAWDZENIA] Komendy są z pomocy Codexa, logowania do Mety w Codexie nikt jeszcze nie przeszedł. Jeśli nie zadziała, użyj `polaczenie/eksport.md`.

## Jeśli menu wygląda inaczej

Meta, Claude i ChatGPT regularnie przestawiają ustawienia. Jeśli to, co opisuje użytkownik, nie zgadza się z krokami, nie kłóć się z jego ekranem. Zapytaj, co widzi, i znajdźcie razem miejsce, w którym AI dodaje zewnętrzne narzędzia. Zawsze jest w ustawieniach i zawsze przyjmuje adres URL.

## Sprawdź połączenie naprawdę

Zielona lampka to nie test. Zapytaj connector o coś, co zna tylko prawdziwe konto:

> Jak nazywa się moje konto reklamowe i ile wydałem w ostatnich 7 dniach?

Przeczytaj odpowiedź użytkownikowi i zapytaj, czy się zgadza. Jeśli nazwa konta jest obca albo liczby są dziwne, pewnie zalogował się nie tym profilem Facebooka.

## Gdy nie działa

Sprawdzaj po kolei. Nie zgaduj.

| Co widzą | Co to zwykle jest |
| --- | --- |
| Okno logowania się nie otwiera | Blokada wyskakujących okien. Zezwól i spróbuj ponownie |
| Zalogowany, ale nie widać konta reklamowego | Nie ten profil Facebooka. Wyloguj się i użyj tego, który ma dostęp do reklam |
| „Brak uprawnień” albo pusta lista kont | Użytkownik nie ma dostępu w ustawieniach firmy. Ktoś z uprawnieniami administratora musi go nadać |
| Łączy się, ale liczby są puste | Często nowe konto bez wydatków. Zapytaj, kiedy ostatnio działała reklama |
| Czyta, ale budowanie nie działa | Zwykle brak uprawnień. Potrzebny jest dostęp administratora do konta reklamowego, nie tylko do strony |

Jeśli po tej liście nadal nie działa, zatrzymaj się. Zapisz problem w `twoja-praca/<sklep>/sklep.md`, przejdź na `polaczenie/eksport.md` i zrób diagnozę na eksporcie. Problem z połączeniem nie może zjeść pierwszej sesji.

## Jak pobierać dane

Zanim pobierzesz metryki, sprawdź nazwy pól przez `ads_get_field_context`. Nazwy z procedur to opisy, a connector ma własne, na przykład unikalne kliknięcia linku to `unique_link_click`, unikalny CTR linku to `unique_link_clicks_ctr`, wydatki to `amount_spent`, leady to `lead`. Nie każde pole istnieje. Kosztu unikalnego kliknięcia linku connector nie podaje, więc policz go sam, wydatki ÷ unikalne kliknięcia linku.

Procedury opisują dane słowami, na przykład „dla każdej aktywnej reklamy z ostatnich 7 dni: wydatki, CPM, częstotliwość, unikalny CTR linku, zakupy, wartość zakupów”. Poproś connector dokładnie o to. Jeśli jakiegoś pola nie ma, powiedz, którego brakuje, i nie zastępuj go innym bez uprzedzenia. Zwykły CTR to nie to samo co unikalny CTR linku.

## Narzędzia connectora

Connector ma ponad sto narzędzi. Nazwy zaczynają się od `ads_`.

**Czytają konto, używasz ich swobodnie:**
- `ads_get_ad_accounts`: lista kont, waluta, czy jest metoda płatności
- `ads_get_ad_entities`: kampanie, zestawy, reklamy i ich wyniki. Jeśli wynik ma pole `next_actions`, dokończ wskazane odczyty, zanim odpowiesz
- `ads_insights_performance_trend`, `ads_insights_anomaly_signal`, `ads_insights_auction_ranking_benchmarks`, `ads_insights_industry_benchmark`, `ads_insights_advertiser_context`: trendy, anomalie, rankingi aukcji
- `ads_account_get_activity_logs`: historia zmian na koncie
- `ads_get_datasets`, `ads_get_dataset_quality`, `ads_get_dataset_stats`, `ads_get_dataset_details`, `ads_pixel_event_read`: piksel i jakość danych
- `ads_get_creatives`, `ads_get_ad_preview`, `ads_get_ad_preview_screenshot`, `ads_get_ad_images`, `ads_get_ad_videos`: kreacje
- `ads_catalog_list_*`, `ads_catalog_get_*`: katalog produktów
- `ads_library_search`: biblioteka reklam
- `ads_get_errors`, `ads_get_opportunity_score`, `ads_get_help_article`, `ads_get_field_context`: błędy, rekomendacje Mety, pomoc

**Zmieniają konto, tylko po zgodzie użytkownika w osobnej wiadomości:**
- tworzenie: `ads_create_campaign`, `ads_create_ad_set`, `ads_create_ad`, `ads_create_creative`, `ads_create_custom_audience`, `ads_boost_ig_post` (domyślnie kieruje do USA, zawsze ustaw kraj), wgrywanie grafik i wideo
- zmiana: `ads_update_entity`. Używasz go tylko do wstrzymania reklamy na poziomie dostępu 3, z samym polem `status` ustawionym na `PAUSED`. Nigdy do budżetu, kierowania ani innych pól działających obiektów. Nigdy ze statusem `DELETED` ani `ARCHIVED`, `ads_creative_update`, `ads_update_custom_audience`
- katalog, piksel i testy A/B: wszystko z `create`, `update`, `delete`, `connect`, `disconnect` w nazwie

**Nigdy:** `ads_activate_entity` i wszystkie narzędzia usuwające (`ads_creative_delete`, `ads_delete_custom_audience`, `ads_delete_local_ad_image`, `ads_catalog_*_delete`, `ads_catalog_delete_product`, `ads_pixel_*_delete`). Usuwanie jest nieodwracalne, robi je użytkownik sam w Menedżerze reklam. O `ads_activate_entity`: To narzędzie włącza kampanię, zestaw albo reklamę i od tej chwili płyną pieniądze. Włączenie należy do użytkownika i robi je sam w Menedżerze reklam. W Claude Code to narzędzie jest zablokowane w `.claude/settings.json`.

Dwie rzeczy, które warto wiedzieć:
- `ads_update_entity` na aktywnej kampanii, zestawie albo reklamie wstrzymuje ją przy każdej zmianie poza nazwą. Zmiana budżetu działającej reklamy przez connector ją wyłącza. Dlatego budżety zmienia użytkownik w Menedżerze reklam.
- Kwoty budżetu connector przyjmuje w najmniejszej jednostce waluty konta, czyli 50 zł to 5000. Zawsze sprawdź walutę konta i podaj kwotę użytkownikowi w złotych.

## Uprawnienia, powiedz o nich raz

- **Po stronie Mety.** W ustawieniach firmy, w sekcji connectorów AI, można zostawić samo czytanie albo wyłączyć pojedyncze akcje, na przykład zmiany budżetu. Tam też odłącza się asystenta.
- **Po stronie Claude.** Przy connectorze ustawia się zgodę osobno dla każdego narzędzia. Narzędziom, które zmieniają konto, daj wymóg zgody, a `ads_activate_entity` zablokuj całkiem.
- **Po stronie ChatGPT.** Przed każdą zmianą pokazuje, co chce zrobić, i czeka na zgodę.

## Co to odblokowuje

Powiedz to raz, na końcu. Ludzie po cichu się tego boją, a uczciwa odpowiedź uspokaja.

**AI czyta konto.** Kampanie, wydatki, wyniki, liczby z ostatnich dni, na których działa diagnoza i przegląd.

**AI może też budować.** Kampanie, zestawy reklam, kreacje, reklamy. Oszczędza to wieczór klikania w Menedżerze reklam.

**Wszystko, co zbuduje, powstaje wstrzymane.** Connector ma wprawdzie narzędzie do włączania, ale AdFlow go nie używa, a w ustawieniach możesz je zablokować. Nic nie wyda złotówki, dopóki sam tego nie włączysz w Menedżerze reklam.

| AI | Ty |
| --- | --- |
| czyta liczby | zatwierdzasz reklamy |
| buduje kampanię, wstrzymaną | włączasz ją |
| mówi, co zbudowało | kontrolujesz wydatki |

Connector widzi to, co widzi Meta. Jeśli część zakupów do Mety nie dociera, na przykład przez baner cookies, wnioski AI są tak samo zaniżone jak panel. Dlatego diagnoza zawsze porównuje Metę ze sprzedażą w sklepie.
