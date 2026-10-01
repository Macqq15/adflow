# AdFlow

Folder, który zamienia Claude albo ChatGPT w osobę od reklam na Mecie dla sklepu internetowego. Czyta konto reklamowe, znajduje jedno wąskie gardło i mówi, co zmienić. Wszystko po polsku.

Działa w aplikacji Claude albo ChatGPT na komputerze, w Claude Code i w Codex. Z kontem reklamowym łączy się przez oficjalny connector Mety, bez kodu i bez kluczy API. Bez connectora pracuje na eksporcie z Menedżera reklam.

## Jak zacząć

1. Pobierz folder (zielony przycisk Code, potem Download ZIP) i rozpakuj go.
2. Otwórz `START-HERE.md` i zrób trzy kroki, które tam są.
3. Napisz do swojego AI **start**.

## Co jest w środku

- `START-HERE.md` dla Ciebie
- `AGENTS.md` i `CLAUDE.md` dla AI, czyli mapa, zasady i podział ról
- `procedury/` z profilem sklepu, diagnozą, przeglądem, ścieżką na spadek sprzedaży, słowami klientów, tekstami reklam, nową kampanią i zdjęciami produktów
- `wzory/` z polskimi wzorami otwarć i reklam dla sklepów
- `narzedzia/zdjecie.py`, jedyny skrypt w paczce. Z prawdziwego zdjęcia produktu robi zdjęcie w scenie przez Gemini. Potrzebuje własnego klucza Gemini API z włączonymi płatnościami, który wklejasz sam do pliku `.env` (wzór w `.env.example`, nigdy do czatu), i działa w Claude Code albo Codex. W aplikacji Claude albo ChatGPT AdFlow da Ci prompt do wklejenia w ChatGPT albo Gemini
- `polaczenie/` z connectorem Mety i eksportem z Menedżera reklam
- `wiedza/` z wiedzą o reklamach na Mecie, od fazy nauki po piksel i odrzucone reklamy
- `twoja-praca/`, gdzie lądują Twoje diagnozy i przeglądy

## Bezpieczeństwo

AI niczego nie włącza, nie podnosi budżetu działającej reklamy i nie rusza reklamy, która zarabia. To, co zbuduje przez connector, powstaje wstrzymane i włączasz to sam w Menedżerze reklam. W ustawieniach firmy w Mecie możesz dodatkowo zostawić connectorowi samo czytanie.

## Status

Wersja robocza. Diagnoza, przegląd i ścieżka na spadek sprzedaży są gotowe. Słowa klientów, teksty reklam i nowa kampania są nowe i w testach. Kampanię AI buduje zawsze wyłączoną, włączasz ją sam. Zdjęcia produktów są w testach, skrypt jeszcze nie przeszedł pełnej próby z płatnym kluczem.
