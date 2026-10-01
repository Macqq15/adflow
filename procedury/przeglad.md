# Przegląd: jedna skupiona godzina

Jedno zadanie: przejść pętlę. Pobrać liczby, zdiagnozować, przygotować jedną zmianę, dać ją do zatwierdzenia. Potem zamknąć laptopa.

Wyniki dzienne to szum. Codzienne poprawki robią z nich jeszcze większy szum.

## Najpierw okno

Okno zależy od budżetu, według `procedury/progi.md`: co 4 dni przy dużym budżecie, co 7 dni przy mniejszym.

**Nigdy nie czytaj jednego dnia.** Jeśli mówią, że reklamy „umarły”, i cytują wczoraj, to pierwsza rzecz do sprawdzenia. Poproś o okno, zanim cokolwiek zdiagnozujesz.

Raz, przy pierwszym przeglądzie, poradź wyłączenie powiadomień z Menedżera reklam na telefonie. To usuwa pokusę.

## Dane wejściowe

- Liczby z tego okna, zawsze te same kolumny i ta sama długość okna, co w `procedury/diagnoza.md`
- Ostatni plik z `twoja-praca/<sklep>/przeglady/`
- `twoja-praca/<sklep>/sklep.md`
- Sprzedaż ze sklepu za to samo okno

Nie wczytuj wszystkich dawnych przeglądów. Ostatni wystarczy.

## Godzina

1. **15 minut, pobranie.** Okno, te same miary co zawsze.
2. **15 minut, diagnoza.** Przejdź `procedury/diagnoza.md` i wróć z jednym wąskim gardłem.
3. **15 minut, zmiana.** Jedna zmiana wobec tego wąskiego gardła. Jeśli to nowa reklama i profil ma poziom dostępu 2, zbuduj ją przez connector jako wstrzymaną. Na poziomie 1 przygotuj ją w pliku, a użytkownik doda ją sam.
4. **15 minut, zatwierdzenie.** Pokaż, co przygotowałeś. Użytkownik ogląda i sam włącza.

## Cztery decyzje

Każde okno kończy się dokładnie jedną z nich dla każdej reklamy:

- **Zostaw.** Działa. Nie ruszaj.
- **Wyłącz.** Miała uczciwy test i przegrała, według reguł z `progi.md`.
- **Skaluj.** Wygrywa i ma miejsce, żeby rosnąć. Zasada skalowania w `progi.md`.
- **Odśwież.** Działała i słabnie. Ten sam kąt, nowe wykonanie: nowy początek tekstu, nowe pierwsze sekundy wideo, nowe zdjęcie.

## Zwycięzca bez kagańca

Kiedy jedna kreacja zjada większość budżetu, to Meta robi swoje, a nie problem do naprawy.

Nie ograniczaj wydatków na jedną kreację i nie wyłączaj tych, które dostają mało emisji. Dokładaj nowe kreacje do tego samego zestawu. Zwycięzca kiedyś się zmęczy, a wtedy następne już tam są i zbierają dane.

Pozwól zwycięzcy działać, dopóki jego koszt zakupu nie przekroczy progu rentowności przez całe okno. Wtedy go wyłącz i zapisz na liście byłych zwycięzców.

## Powrót starych zwycięzców

Stare zwycięskie reklamy nie są martwe, odpoczywają. Na rynek cały czas przychodzą nowi ludzie.

Mniej więcej co pół roku zaproponuj włączenie byłych zwycięzców. To najtańszy możliwy wzrost i zajmuje pięć minut. Przy powrocie użyj istniejącego posta, żeby zachować reakcje i komentarze (`wiedza/knowledge-meta-domain.md` §15b).

Listę byłych zwycięzców trzymaj w pliku przeglądu, żeby dało się ją znaleźć.

## Rutyny, gdy pętla już działa

Zaproponuj raz, gdy przeglądy idą regularnie:

- **Nowa wersja kreacji regularnie.** Weź najlepszą reklamę i przygotuj jedną wariację. Nawet spokojny tydzień to kilka nowych reklam.
- **Wyłączanie przegranych.** Może być automatyczną regułą w koncie reklamowym, ustawioną przez użytkownika według reguł z `progi.md`.
- **Podnoszenie budżetu.** Tylko po sprawdzeniu sprzedaży w sklepie, nie samego ROAS z Mety.

Wszystko, co zbudujesz, nadal powstaje wstrzymane do zatwierdzenia.

## Gdy sprzedaż spadła i nie wiadomo dlaczego

Przejdź do `procedury/gdy-przestalo-dzialac.md`.

## Zasady

- Nie ruszaj reklamy kontrolnej, dopóki testujesz coś przeciw niej. To ona płaci za test.
- Jedna zmiana na okno.
- Miara sukcesu wybrana na początku zostaje ta sama.
- Jeśli nic nie trzeba zmieniać, właściwa odpowiedź to niczego nie zmieniać. Okno bez zmian to pełnoprawne okno.

## Wynik

`twoja-praca/<sklep>/przeglady/RRRR-MM-DD--przeglad.md`: liczby, wąskie gardło, decyzja dla każdej reklamy, jedna zmiana, lista byłych zwycięzców.

## Kontrola człowieka

Użytkownik sam podejmuje decyzje zostaw, wyłącz, skaluj, odśwież i sam włącza zmiany w Menedżerze reklam. Potem przestaje patrzeć. Reszta tygodnia jest dla sklepu, nie dla konta reklamowego.
