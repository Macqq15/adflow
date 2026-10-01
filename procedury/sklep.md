# Profil sklepu

Jedno zadanie: zebrać liczby, bez których nie da się ocenić, czy reklama zarabia. Cztery pytania, jedno naraz. Potem połączenie i pierwsza diagnoza.

## Pytania

Zadawaj po jednym. Jeśli ktoś nie zna odpowiedzi, podpowiedz, gdzie ją znajdzie, a jeśli nie da się jej zdobyć teraz, wpisz `[BRAK]` i idź dalej.

1. **Jak nazywa się sklep i na czym stoi?** Shopify, WooCommerce, Shoper, IdoSell albo inna platforma. Adres strony.
2. **Jaka jest średnia wartość zamówienia?** Z panelu sklepu, z ostatnich 30 albo 90 dni. Cała wartość koszyka, nie cena jednego produktu.
3. **Jaka jest marża brutto?** Ile z każdej złotówki sprzedaży zostaje po koszcie towaru. Jeśli nie wiedzą dokładnie, wystarczy przybliżenie w procentach. Zapytaj też, czy wliczają dostawę i prowizje płatności.
4. **Gdzie widzisz prawdziwą sprzedaż?** Panel sklepu, bramka płatności, system księgowy. To jest liczba, której ufamy bardziej niż Mecie.

Dopytaj raz, bez naciskania: czy prowadzili już reklamy na Mecie i jaki jest mniej więcej budżet dzienny.

## Jeśli reklamy zbierają zapisy, nie zakupy

Newsletter, lista oczekujących, darmowy poradnik. Wtedy zamiast pytań 2 i 3 zapytaj:

- **Ile najwyżej chcesz zapłacić za jeden zapis?** To jest próg. Reklama powyżej niego przez całe okno idzie do pauzy.
- **Gdzie lądują zapisy?** Narzędzie do newslettera, baza, arkusz. To źródło prawdy, bo Meta widzi tylko osoby, które zgodziły się na pomiar w banerze cookies, i zwykle pokazuje mniej zapisów niż naprawdę jest.

W pozostałych procedurach ten próg zastępuje „próg rentowności kosztu zakupu”, a zapisy z bazy zastępują „zamówienia w sklepie”.

## Policz i zapisz

Skopiuj `szablony/sklep.md` do `twoja-praca/<nazwa-sklepu>/sklep.md` i wypełnij.

Policz dwa progi i pokaż, jak je policzyłeś:

- **Próg rentowności kosztu zakupu** = średnia wartość zamówienia × marża brutto. Przykład: 200 zł × 40% = 80 zł. Zakup droższy niż 80 zł w pierwszym zamówieniu to strata na tym zamówieniu.
- **Próg rentowności ROAS** = 1 ÷ marża brutto. Przykład: 1 ÷ 0,40 = 2,5. ROAS poniżej 2,5 to strata na pierwszym zamówieniu.

Powiedz jednym zdaniem, co to znaczy dla nich. Jeśli wspomną, że klienci często wracają, zapisz to. Wtedy pierwszy zakup może być na zero albo lekko pod kreską, ale to ich świadoma decyzja, nie Twoja.

## Poziom dostępu

Zapytaj o to dopiero po podłączeniu connectora, jednym prostym pytaniem: czy AI ma tylko czytać konto, czy także budować wyłączone kampanie. Domyślnie jest tylko odczyt.

**Poziom 1, odczyt.** Diagnoza, przegląd, teksty, zdjęcia. Na koncie nic nie powstaje.

**Poziom 2, budowanie wyłączone.** Możesz tworzyć kampanie, zestawy, kreacje i reklamy oraz wgrywać zdjęcia. Wszystko powstaje wyłączone.

**Nigdy, na żadnym poziomie:** włączanie czegokolwiek, zmiana budżetu albo ustawień działającej kampanii, zestawu czy reklamy, usuwanie. To użytkownik robi zawsze sam w Menedżerze reklam. Powiedz to wprost, zanim zapytasz o poziom.

Żeby przejść na poziom 2, użytkownik przepisuje zdanie z dokładną nazwą konta reklamowego, którą pokazał connector:

> Zgadzam się, żeby AdFlow tworzył wyłączone kampanie na koncie <nazwa konta>.

Samo „tak” albo „ok” nie wystarcza. Jeśli nazwa konta w zdaniu nie zgadza się z kontem, które widzisz, zatrzymaj się i zapytaj, o które konto chodzi.

Zapisz w `twoja-praca/<sklep>/sklep.md` poziom, nazwę i identyfikator konta, datę i dokładne zdanie zgody.

Potem pomóż ustawić blokady po stronie narzędzi, bo zdanie w czacie nie jest blokadą techniczną:

- w Claude przy connectorze Meta Ads ustaw `ads_activate_entity` i narzędzia usuwające na „nigdy”, a narzędzia tworzące na „pytaj”
- w ustawieniach firmy w Mecie, w sekcji connectorów AI, zostaw samo czytanie przy poziomie 1 albo dopuść tworzenie przy poziomie 2. [DO SPRAWDZENIA] dokładne nazwy opcji w tej sekcji
- w Claude Code robi to już `.claude/settings.json`

Zgodę można cofnąć słowami „cofam zgodę”. Wtedy wracasz na poziom 1 i zapisujesz to w profilu z datą.

Nawet na poziomie 2 każda budowa wymaga osobnego potwierdzenia: pokazujesz plan z kwotami, użytkownik odpisuje „buduj” w osobnej wiadomości.

## Dalej

1. Jeśli nie ma jeszcze połączenia, przejdź do `polaczenie/connector.md`. Jeśli nie da się go zrobić, do `polaczenie/eksport.md`.
2. Po podłączeniu ustal poziom dostępu (wyżej).
3. Potem od razu `procedury/diagnoza.md`. Pierwsza sesja kończy się diagnozą, nie samą konfiguracją.
