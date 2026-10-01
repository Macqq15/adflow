# Diagnoza: co naprawdę hamuje sprzedaż

Jedno zadanie: wziąć liczby, znaleźć jedno wąskie gardło, pokazać dowód i dać jedną następną zmianę.

Jedno. Nie czternaście.

Diagnoza tylko czyta. Niczego nie zmieniasz w koncie.

## Dane wejściowe

- `twoja-praca/<sklep>/sklep.md`: progi rentowności i źródło prawdziwej sprzedaży. Bez tego pliku wróć do `procedury/sklep.md`.
- `procedury/progi.md`: liczby, które rozstrzygają. Czytaj je stamtąd, nie z pamięci.
- Dane z Mety, według Twojego trybu połączenia. Dla każdej aktywnej reklamy za okno (7 albo 4 dni): wydatki, wyświetlenia, częstotliwość, CPM, unikalne kliknięcia linku, unikalny CTR linku, koszt unikalnego kliknięcia linku, zakupy, wartość zakupów, koszt zakupu, dodania do koszyka, rozpoczęcia realizacji zakupu. Do tego status fazy nauki każdego zestawu i mediana CPM konta z 30 dni.
- Dane ze sklepu za to samo okno: zamówienia, przychód, sesje. Zapytaj o nie, jeśli ich nie masz.

Nie wczytuj całej `wiedza/`. Sięgasz do konkretnej sekcji dopiero wtedy, gdy trafisz na problem, którego dotyczy.

## Najpierw: czy jest z czym pracować

1. **Okno.** Jeśli dane są z jednego dnia, powiedz to i poproś o okno z `progi.md`.
2. **Ilość danych.** Poniżej progu „za mało danych” powiedz, że trzeba poczekać, i zakończ. Nie wymyślaj diagnozy.
3. **Reguły wyłączania.** Jeśli reklama albo kampania przekroczyła próg z `progi.md`, powiedz to wprost na początku. Ta runda jest skończona, wyłącz, a diagnoza dotyczy tego, co zmienić przed następną.

## Ścieżka

Idź w tej kolejności. Problem wyżej unieważnia wszystko poniżej.

1. **Śledzenie.** Czy zakupy w Mecie zgadzają się z zamówieniami w sklepie? Problem ze śledzeniem wygląda dokładnie jak każdy inny problem, dlatego jest pierwszy. Jeśli różnica przekracza próg, to jest wąskie gardło i na tym kończysz.
2. **Kreacja.** Unikalny CTR linku i zmęczenie według `progi.md`. Potem porównaj obietnicę: przeczytaj nagłówek reklamy obok nagłówka strony, na którą prowadzi. Jeśli reklama obiecuje jedno, a strona otwiera się czymś innym, to problem reklamy niezależnie od CTR.
3. **Aukcja i kierowanie.** CPM na obu końcach według `progi.md`. Sprawdź też status fazy nauki. Zestaw w nauce albo z ograniczoną nauką ma prawo być droższy, zanim go ocenisz, zajrzyj do `wiedza/knowledge-meta-domain.md` §2.
4. **Strona i koszyk.** Konwersja ruchu z Mety względem średniej sklepu i miejsce, w którym ludzie odpadają: koszyk, kasa, płatność.
5. **Ekonomia zamówienia.** Koszt zakupu względem progu rentowności. Jeśli tu jest problem, powiedz to i zatrzymaj się. To nie jest kurs budowania oferty.

## Darmowa poprawka, sprawdzaj za każdym razem

Zanim zalecisz cokolwiek innego, ułóż reklamy według unikalnego CTR linku i przeczytaj nagłówki i teksty tych z góry listy.

**Nagłówek, w który ludzie klikają najczęściej, mówi, po co naprawdę przyszli.** Ten sam nagłówek na stronie produktu albo kolekcji, na którą prowadzi reklama, to często najtańsza poprawa konwersji.

Działa nawet przy zerowej sprzedaży, więc to jedyna naprawdę użyteczna rzecz przy teście bez zakupów. Podaj konkretny nagłówek do wstawienia, nie zasadę.

## Gdy działało i przestało

To inne pytanie. Przejdź do `procedury/gdy-przestalo-dzialac.md`.

## Wynik

Skopiuj `szablony/diagnoza.md` do `twoja-praca/<sklep>/diagnozy/RRRR-MM-DD--diagnoza.md` i wypełnij:

1. **Wąskie gardło.** Jedno, nazwane wprost, z liczbami, które na nie wskazują.
2. **Co wykluczyłeś i dlaczego.** Użytkownik musi móc się z Tobą nie zgodzić, więc pokaż tok rozumowania.
3. **Jedna następna zmiana.** Najmniejsza zmiana, która sprawdzi diagnozę. Kto ją robi (zwykle użytkownik, bo dotyczy działających reklam), gdzie kliknąć i po jakim czasie sprawdzić wynik.
4. **Darmowa poprawka nagłówka**, jeśli jest.

W rozmowie powiedz to samo krótko. Najpierw dowód, potem zalecenie.

## Zasady

- Dowód przed zaleceniem, zawsze.
- Nigdy nie zalecaj więcej niż jednej zmiany naraz.
- Chroń reklamę, która zarabia. Nigdy nie proponuj jej ruszania.
- Progi to sygnały ostrzegawcze, nie prawa. Powiedz, gdy sprawa jest na granicy.
- Jeśli uczciwa odpowiedź brzmi „za mało danych”, powiedz to.

## Kontrola człowieka

Użytkownik czyta dowody przed zaleceniem i decyduje, czy się zgadza. Jeśli rozumowanie się nie trzyma, zalecenie też nie. Poproś, żeby się z nim spierał.
