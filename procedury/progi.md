# Progi, które rozstrzygają

Sprawdzaj je w tej kolejności. Pierwszy przekroczony próg to zwykle wąskie gardło.

To są punkty wyjścia, nie prawa. Liczba tuż za progiem przy zdrowej reszcie to nie problem. Powiedz, kiedy sprawa jest na granicy. Tam, gdzie się da, porównujemy konto z nim samym, a nie z cudzą średnią, bo polski rynek, branża i cena produktu zmieniają wszystko.

## Okno, nigdy jeden dzień

| Budżet dzienny na całym koncie | Patrz co |
| --- | --- |
| około 2000 zł i więcej | 4 dni |
| mniej | 7 dni |

Wyniki z jednego dnia to szum. Reklama potrafi mieć jeden dzień świetny, a następny fatalny, i średnio działać dobrze. Kto czyta dzień po dniu, wyłącza reklamy, które działają.

Jeśli wkleją liczby z jednego dnia, powiedz to i poproś o okno.

## Za mało danych

Mniej niż 3 dni albo mniej niż 1000 wyświetleń na reklamę to za wcześnie. Powiedz to i każ poczekać. „Za mało danych” oszczędza im pieniądze.

## Progi rentowności

Z `twoja-praca/<sklep>/sklep.md`:

- **Próg rentowności kosztu zakupu** = średnia wartość zamówienia × marża brutto
- **Próg rentowności ROAS** = 1 ÷ marża brutto

Każdą ocenę kosztu zakupu i ROAS robisz względem tych dwóch liczb. Bez nich mówisz tylko „drożej” albo „taniej niż w zeszłym tygodniu”, nigdy „zarabia” albo „traci”.

## Reguły wyłączania

| Sytuacja | Decyzja |
| --- | --- |
| reklama wydała 2 × próg rentowności kosztu zakupu i nie ma ani jednego zakupu | wyłącz reklamę |
| nowa kampania wydała 3 × próg rentowności kosztu zakupu i nie ma ani jednego zakupu | koniec tej rundy |

Wyłączenie robi użytkownik. Ty mówisz, co i dlaczego. Na poziomie dostępu 3 możesz wstrzymać reklamę sam, po jego potwierdzeniu, według kroków w `procedury/sklep.md`.

**Koniec rundy to nie koniec produktu.** Przed zamknięciem tematu zrób do trzech rund. Między rundami zmieniaj stronę produktu albo ofertę (zestaw, próg darmowej dostawy, cena, gwarancja), a reklamy zostaw. Druga albo trzecia runda często pokazuje zwycięzcę.

## Śledzenie

Porównaj zakupy według Mety z zamówieniami w sklepie w tym samym oknie. Najlepiej z zamówieniami z ruchu z Facebooka i Instagrama, jeśli sklep je rozróżnia.

Liczby nie będą identyczne, bo Meta liczy inaczej niż sklep (okna atrybucji, wyświetlenia bez kliknięcia). Problemem jest **różnica większa niż mniej więcej jedna piąta, w którąkolwiek stronę**. Wtedy śledzenie jest wąskim gardłem i nic poniżej nie ma sensu, dopóki go nie wyjaśnisz. Szczegóły w `wiedza/knowledge-pixel-capi.md`.

Częsta przyczyna w polskich sklepach to baner cookies, który blokuje piksel, zanim klient kliknie zgodę. Zapytaj o niego.

## Kreacja: unikalny CTR linku

Używaj **unikalnego CTR linku**, nie zwykłego CTR. Zwykły liczy też kliknięcia w nazwę strony, zdjęcie profilowe i komentarze.

| Sygnał | Werdykt |
| --- | --- |
| unikalny CTR linku o połowę niższy niż najlepsza reklama w tym samym zestawie | problem tej reklamy |
| unikalny CTR linku poniżej około 1% na zimnym ruchu | prawdopodobnie problem reklamy |

[DO KALIBRACJI] Próg 1% to punkt wyjścia. Po kilku polskich kontach sklepowych poprawimy go na podstawie danych.

Powyżej progu i bez sprzedaży reklama nie jest problemem. Powiedz to i idź dalej. To oszczędza tydzień przepisywania dobrych reklam.

## Zmęczenie kreacji

| Sygnał, zimny ruch, 7 dni | Werdykt |
| --- | --- |
| częstotliwość powyżej 3 i rosnący koszt unikalnego kliknięcia linku | reklama się męczy |
| częstotliwość powyżej 4 | wymień albo odśwież |

Szczegóły i progi dla retargetingu w `wiedza/knowledge-meta-creative.md` §5.

## CPM, oba końce

Porównuj z medianą CPM tego konta z ostatnich 30 dni.

| CPM | Co znaczy | Co zrobić |
| --- | --- | --- |
| co najmniej 1,5 × mediana | aukcja jest droga | poszerz kierowanie (cała Polska, szeroka grupa, mniej zawężeń) i zrób lepsze reklamy. oba, nie jedno |
| wyraźnie poniżej mediany i są zakupy | tanio i sprzedaje | zostaw. to cel, nie ostrzeżenie |
| wyraźnie poniżej mediany i brak zakupów | emisja odpłynęła tam, gdzie nikt nie kupi | sprawdź umiejscowienia, zwłaszcza Audience Network (`wiedza/knowledge-meta-domain.md` §15a), i cel optymalizacji (§1b) |

Jeśli sklep wysyła za granicę i poszerzacie kierowanie na inne kraje, pamiętaj o dopłatach lokalizacyjnych w części krajów, w UE i poza nią (`wiedza/knowledge-meta-domain.md` §15c).

## Strona i koszyk

Policz konwersję ruchu z Mety: zakupy ÷ unikalne kliknięcia linku. Porównaj ze średnią konwersją sklepu (zamówienia ÷ sesje) z panelu sklepu.

| Sygnał | Werdykt |
| --- | --- |
| ruch z Mety konwertuje mniej niż połowę średniej sklepu | strona nie domyka tego ruchu. sprawdź, czy reklama i strona obiecują to samo |
| dużo dodań do koszyka, mało rozpoczęć realizacji zakupu | koszt albo czas dostawy widoczny dopiero w koszyku, brak ulubionej metody płatności, wymuszone konto |
| dużo rozpoczęć realizacji zakupu, mało zakupów | problem w kasie. płatność, błędy formularza, niespodzianki w cenie |

Nie oceniaj strony bez ceny produktu. Droższy produkt ma prawo konwertować słabiej.

## Ekonomia zamówienia

| Sygnał | Werdykt |
| --- | --- |
| wszystko powyżej zdrowe, a koszt zakupu wyższy niż próg rentowności | reklamy działają, zamówienie jest za małe |

Powiedz to i powiedz, co zwykle podnosi wartość zamówienia: zestawy, próg darmowej dostawy trochę powyżej obecnej średniej, produkt dodawany w koszyku. Potem się zatrzymaj. Decyzja o ofercie należy do nich.

## Czytanie progów razem

Jeden przekroczony próg wskazuje jedno wąskie gardło. Dwa naraz zwykle znaczą, że wyższy spowodował niższy.

- **Niski CTR i słaba konwersja strony:** najpierw reklama. Słaba reklama przyprowadza przypadkowe kliknięcia, przez które każda strona wygląda na zepsutą.
- **Zdrowy CTR i słaba konwersja strony:** reklama robi swoje. Problem jest na stronie albo w ofercie.
- **Wysoki CPM i wszystko drogie:** kierowanie za wąskie. Najpierw poszerz, potem kreacja.
- **Niski CPM i brak zakupów:** emisja odpłynęła. Tanie wyświetlenia są przyczyną, nie pocieszeniem.
- **Wszystko zdrowe i brak zakupów:** najpierw śledzenie. Sprzedaż może się dziać i nie być widoczna w Mecie.

## Skalowanie

**Budżet w górę o 10% dziennie.** Nudne i celowo takie. Budżet rośnie tak mniej więcej dwukrotnie w tydzień.

Skaluj tylko to, co wygrało przez całe okno na koszcie zakupu albo ROAS **potwierdzonym w sklepie**, nie tylko w Mecie. Sprawdź też, czy jest towar na zwiększoną sprzedaż.

Podwojenie budżetu zwycięzcy to najczęstszy sposób, żeby go zabić. Duży skok wrzuca zestaw z powrotem w fazę nauki i to, co działało, przestaje działać.

Zmiana budżetu to zawsze kliknięcie użytkownika. Ty podajesz nową kwotę i mówisz, gdzie ją wpisać.
