# Zacznij tutaj

AdFlow to folder, który zamienia Claude albo ChatGPT w osobę od reklam na Mecie dla Twojego sklepu. Czyta Twoje konto reklamowe, znajduje to, co naprawdę hamuje sprzedaż, i mówi, co zmienić. Jedną rzecz naraz.

Nie ma tu programu do instalowania. Są pliki tekstowe, według których pracuje Twoje AI.

## Najpierw jedna rzecz, na której wszyscy się potykają

Przeglądarka nie otworzy folderu. Ani Claude w przeglądarce, ani ChatGPT w przeglądarce. Przyjmują pojedyncze pliki, więc przeciągnięcie tego folderu do karty w przeglądarce nie zadziała.

Dobrze działa aplikacja na komputer. Instalacja trwa dwie minuty. Jeśli pracujesz w Claude Code albo Codex (programy do pracy z AI w terminalu, dla bardziej zaawansowanych), aplikacja nie jest Ci potrzebna.

## Ile to kosztuje

- **AdFlow** jest za darmo.
- **Claude.** Otwarcie folderu w projekcie wymaga płatnego planu. Na darmowym planie zostaje zwykły czat (niżej).
- **ChatGPT.** Podłączenie konta reklamowego wymaga planu Plus albo wyższego.
- **Reklamy** opłacasz w Mecie jak zawsze. AdFlow niczego nie włącza i nie wydaje.
- **Zdjęcia z AI w Claude Code albo Codex** wymagają płatnego klucza Gemini. W ChatGPT albo Gemini robisz je w ramach swojego abonamentu.

## Co zrobić teraz

1. Jeśli pobrany folder jest w pliku ZIP, najpierw go rozpakuj (prawy przycisk, „Wyodrębnij wszystkie” na Windows, dwuklik na Macu). Folder w środku ZIP-a nie zadziała. Zapisz cały folder w miejscu, które łatwo znajdziesz. Pulpit jest w porządku.
2. Otwórz go w swoim AI według kroków poniżej.
3. Napisz **start**.

Tyle. Twoje AI przeczyta mapę i poprowadzi Cię dalej.

**Claude na komputerze.** Zainstaluj aplikację Claude. W lewym pasku kliknij plus przy Projects, wybierz opcję użycia istniejącego folderu z komputera i wskaż ten folder. Projekty z folderem wymagają płatnego planu Claude.

**ChatGPT na komputerze.** Zainstaluj aplikację ChatGPT, otwórz w niej ten folder, zezwól na dostęp i w polu wiadomości wybierz **Work locally**. Ten krok ludzie pomijają najczęściej. Zostaw go włączonego, gdy praca wymaga plików z Twojego komputera.

**Claude Code albo Codex.** Otwórz terminal w tym folderze i uruchom `claude` albo `codex`.

Jeśli nic się nie dzieje, napisz „Przeczytaj START-HERE.md i AGENTS.md, potem zacznij ze mną od początku”.

**Nie masz aplikacji?** Otwórz zwykły czat i dołącz pięć plików, czyli `AGENTS.md`, `procedury/sklep.md`, `procedury/diagnoza.md`, `procedury/progi.md` i `polaczenie/eksport.md`. Napisz „Postępuj według tych plików, zadawaj mi jedno pytanie naraz”. To działa, tylko wolniej. Czat nie zapisze niczego na Twoim dysku, więc wyniki skopiuj sobie sam, a w każdym nowym czacie zaczynasz od nowa.

## Połączenie z kontem reklamowym

Żeby AI widziało Twoje liczby, podłączasz oficjalny connector Mety, czyli dodatek, który pozwala Claude albo ChatGPT czytać Twoje konto reklamowe. To nie jest wtyczka ani nic, co zbudowaliśmy. Dodajesz go w ustawieniach Claude albo ChatGPT, logujesz się na Facebooku i gotowe. Instrukcja krok po kroku jest w pliku `polaczenie/connector.md`, a AI przeprowadzi Cię przez nią.

Bez connectora też da się pracować. Eksportujesz raport z Menedżera reklam i wklejasz go do czatu. Instrukcja jest w `polaczenie/eksport.md`.

## Co się dzieje po kolei

1. **Twój sklep.** Cztery pytania o średnią wartość zamówienia, marżę i o to, gdzie widzisz prawdziwą sprzedaż. Bez tego nie da się ocenić, czy reklama zarabia.
2. **Diagnoza.** AI czyta konto i nazywa jedno wąskie gardło, z liczbami, które na nie wskazują, i jedną zmianę do sprawdzenia.
3. **Przegląd.** Raz na tydzień albo raz na cztery dni, zależnie od budżetu. Każda reklama dostaje jedną decyzję, czyli zostaw, wyłącz, skaluj albo odśwież.
4. **Gdy przestało działać.** Osobna ścieżka dla reklamy albo sklepu, który sprzedawał i nagle przestał.
5. **Nowa kampania od zera.** Jeśli nie masz jeszcze reklam, AI zbierze zdania Twoich klientów z opinii i wiadomości, napisze z nich teksty reklam i zbuduje kampanię. Wszystko wyłączone, włączasz sam.
6. **Zdjęcia do reklam.** Z prawdziwego zdjęcia produktu AI robi zdjęcie w scenie, na przykład kubek na kuchennym blacie. W ChatGPT albo Gemini wystarczy prompt, który przygotuje AdFlow. W Claude Code i Codex działa to automatycznie, ale wymaga własnego klucza Gemini, który wklejasz sam do pliku `.env`, nigdy do czatu.

Wszystko, co AI przygotuje, ląduje w folderze `twoja-praca`. Następna rozmowa wie, na czym skończyliście.

## Podział ról

AI robi czarną robotę. Czyta, liczy, porównuje, pisze.

Ty podejmujesz każdą decyzję, która kosztuje pieniądze. AI nigdy niczego nie włącza, nie podnosi budżetu działającej reklamy i nie rusza reklamy, która na siebie zarabia. Podaje Ci liczbę i mówi, gdzie kliknąć.

Na start AI tylko czyta Twoje konto. Jeśli chcesz, żeby budowało kampanie, wpiszesz zgodę z nazwą swojego konta. Osobną zgodą możesz też pozwolić, żeby wstrzymywało reklamy, które przegrały test. Każde wstrzymanie i tak potwierdzasz. Zgodę możesz cofnąć w każdej chwili, pisząc „cofam zgodę”.

To, co AI zbuduje przez connector, powstaje wstrzymane. Nic nie wyda ani złotówki, dopóki sam tego nie włączysz w Menedżerze reklam.

## Najważniejsza zasada

Nie zaglądaj do konta reklamowego codziennie. Wyniki z jednego dnia to szum, a codzienne poprawki psują reklamy, które działają. AI powie Ci, kiedy patrzeć.

## Utknąłeś?

Napisz „utknąłem, co mam zrobić”. AI ma mapę, niech ją przeczyta.
