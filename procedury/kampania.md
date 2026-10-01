# Nowa kampania

Jedno zadanie: zbudować całą kampanię przez connector, wstrzymaną, i oddać ją użytkownikowi do sprawdzenia i włączenia.

**Ty budujesz. Użytkownik włącza.** Bez klikania w Menedżerze reklam i bez przepisywania ustawień ręcznie.

## Dane wejściowe

- `twoja-praca/<sklep>/sklep.md`: progi rentowności
- `twoja-praca/<sklep>/reklamy/<plik>.md`: 5 tekstów, 5 nagłówków, 5 opisów, tylko trzy pierwsze sekcje
- zdjęcia w `twoja-praca/<sklep>/kreacje/` albo od użytkownika
- adres karty produktu albo kolekcji

Nie wczytuj procedury diagnozy, przeglądu ani całej wiedzy.

## Wszystko powstaje wstrzymane

Connector tworzy kampanie, zestawy i reklamy wstrzymane. Nic nie wyda złotówki, dopóki użytkownik nie włączy tego w Menedżerze reklam.

Powiedz to na początku, bo „AI buduje mi kampanię” brzmi niepokojąco:

> Zbuduję całą kampanię. Wszystko będzie wyłączone. Nic nie wyda ani złotówki, dopóki sam tego nie obejrzysz i nie włączysz.

Każde narzędzie, które coś tworzy, wymaga zgody użytkownika. Najpierw pokaż plan budowy w całości, potem poproś o zgodę w osobnej wiadomości, potem buduj. Nigdy nie wywołuj `ads_activate_entity`.

## Lista przed budową

Sprawdź przez connector albo zapytaj. Jeśli czegoś brakuje, zatrzymaj się i pomóż to naprawić. Inaczej budowa się wysypie albo kampania będzie zepsuta.

- [ ] **Konto reklamowe ma metodę płatności** (`ads_get_ad_accounts`, pole `has_payment_method`).
- [ ] **Jest strona na Facebooku** podpięta do konta (`ads_get_ad_account_pages`).
- [ ] **Jest piksel, czyli zbiór danych, i widzi zakupy** (`ads_get_datasets`, `ads_get_dataset_stats`). Zdarzenie zakupu ma się wywoływać na stronie podziękowania, a nie w koszyku. Bez piksela Meta nie przyjmie zestawu nastawionego na sprzedaż. Szczegóły w `wiedza/knowledge-pixel-capi.md`.
- [ ] **Ile zakupów piksel już zapisał.** To wpływa na kierowanie niżej.
- [ ] **Strona produktu ładuje się na telefonie** i obiecuje to samo co reklamy.
- [ ] **Dane reklamodawcy i płatnika dla UE są uzupełnione.** Reklamy w UE wymagają podania, kto się reklamuje i kto płaci. Jeśli budowa zestawu zwraca błąd o reklamodawcy albo płatniku, sprawdź w ustawieniach konta sekcję przejrzystości reklam (Ad transparency) i to, czy nie jest zaznaczone, że reklamodawca i płatnik to różne podmioty bez uzupełnionego płatnika. Komunikat błędu potrafi wskazywać zupełnie inne miejsce niż przyczyna.

## Plan testu, ustalony przed budową

Skopiuj `szablony/plan-kampanii.md` do `twoja-praca/<sklep>/kampanie/RRRR-MM-DD--<nazwa>.md`, wypełnij i poproś o potwierdzenie.

| Decyzja | Domyślnie |
| --- | --- |
| Budżet rundy | **3 × próg rentowności kosztu zakupu** z `sklep.md`. Przykład: próg 80 zł, budżet 240 zł. Twardy limit |
| Wyłączenie wcześniej | wydane 2 × próg i zero zakupów |
| Koniec rundy | wydany cały budżet rundy i zero zakupów (`procedury/progi.md`) |
| Która runda | 1, 2 albo 3. Przed porzuceniem produktu robimy trzy |
| Reklama kontrolna | obecna najlepsza reklama albo „brak, pierwszy start” |
| Główna miara | koszt zakupu potwierdzony w sklepie, chyba że użytkownik wybierze inaczej |
| Okno testu | 5 do 7 dni |

Po zapisaniu te decyzje się nie zmieniają. Zmiana miary, gdy już widać liczby, to sposób na okłamanie siebie co do testu, który się przegrało.

Reguły wyłączania mów przy starcie, a nie przy pierwszych wydanych pieniądzach. Wtedy wyłączenie nie wygląda jak poddanie się.

Jeśli cel to zapis na listę zamiast zakupu, próg zapisu zastępuje próg rentowności kosztu zakupu (`procedury/sklep.md`).

## Co budujesz

**Jedna kampania.**

- Cel: Sprzedaż (`OUTCOME_SALES`).
- Budżet na poziomie kampanii, żeby Meta przesuwała pieniądze do lepszego zestawu.
- Budżet łączny równy budżetowi rundy i limit wydatków kampanii na tę samą kwotę, żeby nie dało się wydać więcej.
- Data startu i końca równa oknu testu.
- Kwoty connector przyjmuje w groszach waluty konta, 240 zł to 24000. Sprawdź walutę konta i pokaż kwotę w złotych.

**Dwa zestawy reklam** w tej kampanii.

| Ustawienie | Szeroki | Wąski |
| --- | --- | --- |
| Zainteresowania | brak | 2 lub 3 duże zainteresowania |
| Kraje | gdzie sklep wysyła, najczęściej tylko Polska | identycznie jak w Szerokim |
| Wiek | 18 do 65, chyba że produkt wymaga innego | identycznie |
| Optymalizacja | zakup, z pikselem jako obiektem promowanym | identycznie |
| Umiejscowienia | automatyczne (Advantage+) | identycznie |

- **Oba zestawy mają identyczne kraje, wiek i optymalizację.** Różnią się tylko zainteresowaniami. Inaczej porównanie nic nie mówi.
- **Nigdy nie wymyślaj identyfikatora zainteresowania.** Wyszukaj je po nazwie przez connector i użyj dokładnie tego, co wróci. Zmyślone identyfikatory są odrzucane albo, co gorsze, kierują do złych ludzi.
- **Duże zainteresowania.** Wąski zestaw może mieć kilka milionów osób zasięgu w Polsce i to jest w porządku. Wybieraj zainteresowania tego, kim klient jest, a nie tego, kim chciałby być.
- **Advantage+ Audience** jest domyślnie włączone. Wtedy wiek jest sugestią, a nie limitem. W Szerokim to zwykle dobrze. Jeśli produkt wymaga twardego limitu wieku, trzeba to wyłączyć.
- Przy wysyłce za granicę pamiętaj o dopłatach lokalizacyjnych w części krajów (`wiedza/knowledge-meta-domain.md` §15c).

**Kreacje.** Wgraj zdjęcia (narzędzia wgrywania obrazów connectora), potem zbuduj kreację dla każdej reklamy: strona na Facebooku, adres docelowy z parametrami UTM (niżej), tekst główny, nagłówek i opis. Teksty bierzesz z pliku reklam bez żadnych zmian i bez notatek.

**Reklamy.** Te same reklamy w obu zestawach, wskazujące na tę samą kreację. Wtedy polubienia, komentarze i udostępnienia zbierają się na jednym poście zamiast dzielić na dwa.

## Parametry UTM

Dzięki nim sklep pokaże, ile zamówień przyszło z której reklamy, niezależnie od tego, co widzi Meta. Dopisz do adresu docelowego:

```
?utm_source=facebook&utm_medium=paid&utm_campaign=<nazwa-kampanii>&utm_content=<nazwa-reklamy>
```

Małe litery, myślniki zamiast spacji, bez polskich znaków. Jeśli adres ma już znak `?`, kolejne parametry dołączasz znakiem `&`.

## Nazwy

Według `AGENTS.md`. Przykład:

```
SPRZEDAŻ - Kawa ziarnista
  Szeroki PL
    2026-10-05 Gorzka kawa
    2026-10-05 Data palenia
  Wąski | Kawa + Ekspresy do kawy
    2026-10-05 Gorzka kawa
    2026-10-05 Data palenia
```

## Kolejność budowy

1. Pokaż plan budowy: kampania, dwa zestawy, ile kreacji i reklam, kwoty w złotych. Poczekaj na zgodę.
2. Utwórz kampanię.
3. Utwórz oba zestawy. Zainteresowania wyszukaj wcześniej.
4. Wgraj zdjęcia, utwórz kreacje.
5. Utwórz reklamy w obu zestawach na tych samych kreacjach.
6. Odczytaj wszystko z powrotem (`ads_get_ad_entities`) i sprawdź, czy liczby, nazwy i linki się zgadzają.

Jeśli którekolwiek wywołanie zwróci błąd, przeczytaj treść błędu i napraw przyczynę. Nie ponawiaj na ślepo i nie zostawiaj kampanii zbudowanej do połowy bez słowa. Powiedz, co powstało, a czego brakuje.

## Przekazanie

Powiedz zwykłymi słowami, nie listą identyfikatorów:

1. Co powstało: nazwa kampanii, nazwy dwóch zestawów, ile reklam.
2. Że wszystko jest wyłączone.
3. Ile to kosztuje po włączeniu: budżet rundy i okno.
4. Co sprawdzić przed włączeniem: podgląd reklam, czy link prowadzi tam, gdzie trzeba, czy budżet się zgadza.
5. Jak włączyć: w Menedżerze reklam przełącznik przy kampanii, zestawach i reklamach. Meta wyświetla reklamę tylko wtedy, gdy włączone są wszystkie trzy poziomy.

To jedyna rzecz, którą użytkownik robi ręcznie, i tak ma zostać.

## Czego nie robisz

- Nie włączasz niczego. Nigdy.
- Nie budujesz osobnej kampanii testowej. Jedna kampania na produkt albo kategorię. Przeniesienie zwycięskiej reklamy do innej kampanii zeruje wszystko, czego się nauczyła.
- Nie zmieniasz kierowania w trakcie testu. To zeruje naukę i psuje porównanie.
- Nie ruszasz reklamy kontrolnej w trakcie testu.
- Przy pierwszym starcie bez grup podobnych odbiorców i bez retargetingu. Na to przyjdzie czas, gdy będzie ruch i zakupy.

## Gdy connector nie działa

Zapisz pełną specyfikację w pliku planu zwykłym językiem i powiedz, że to budowa ręczna. Najpierw spróbuj podłączyć connector według `polaczenie/connector.md`, bo to pięć minut, a oszczędza godzinę przepisywania ustawień.

## Wynik

`twoja-praca/<sklep>/kampanie/RRRR-MM-DD--<nazwa>.md`: decyzje testu, co zbudowano, identyfikatory i lista do sprawdzenia przed włączeniem.

## Kontrola człowieka

Użytkownik otwiera Menedżera reklam, ogląda podgląd reklam, sprawdza link i budżet i sam włącza kampanię. To moment, w którym zaczynają płynąć pieniądze, i należy do niego.
