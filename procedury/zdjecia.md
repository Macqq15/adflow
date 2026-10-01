# Zdjęcia produktów do reklam

Jedno zadanie: z prawdziwego zdjęcia produktu zrobić 2 do 3 zdjęć w scenie, gotowych do reklamy. Produkt na zdjęciu musi zostać dokładnie taki, jaki jest w sklepie.

AI nie wymyśla produktu. Edytuje prawdziwe zdjęcie i zmienia tylko otoczenie.

## Dane wejściowe

- Zdjęcie produktu ze sklepu, najlepiej na jednolitym tle, w dobrej rozdzielczości. Plik od użytkownika albo zdjęcie z karty produktu w sklepie.
- Nazwa produktu i to, do czego służy. Jeśli istnieje, `twoja-praca/<sklep>/sklep.md`.
- Jeśli była diagnoza, jej wnioski o kreacji. Zwycięski kąt reklamy podpowiada scenę.

## Wybierz drogę

**Droga A, Claude Code albo Codex.** Masz terminal i możesz uruchomić `python narzedzia/zdjecie.py` (na macOS `python3`). Sprawdź najpierw `python --version` albo `python3 --version`. Jeśli Pythona nie ma albo na Windows otwiera się Microsoft Store, poproś o instalację z python.org. Potrzebny jest klucz Gemini API.

**Droga B, aplikacja Claude albo ChatGPT, także zwykły czat w przeglądarce.** Bez terminala i bez klucza. Przygotowujesz prompt, a użytkownik wkleja go razem ze zdjęciem produktu do ChatGPT albo aplikacji Gemini, które same generują obrazy w ramach swojego abonamentu. Claude obrazów nie generuje. W tej drodze nie zakładaj `.env` i nie wspominaj o kluczu, nie jest potrzebny.

## Klucz Gemini (tylko droga A)

Klucz to hasło, które pozwala wydawać pieniądze z karty użytkownika. Trafia do osobnego pliku `.env` w folderze AdFlow i nigdy nie przechodzi przez czat. Podawaj kroki po jednym.

1. Załóż plik: skopiuj `.env.example` jako `.env` (w Claude Code albo Codex komendą `cp .env.example .env`, na Windows w PowerShell `Copy-Item .env.example .env`). Plik jest pusty, klucza jeszcze nie ma.
2. Użytkownik wchodzi na aistudio.google.com, loguje się kontem Google i klika **Get API key**, potem **Create API key**. Najlepiej w nowym, osobnym projekcie „adflow”, żeby klucz nie miał dostępu do niczego innego.
3. Włącza płatności (Billing) dla tego projektu. Darmowy plan nie generuje obrazów, skrypt zwróci wtedy błąd z limitem 0.
4. Ustawia alert budżetowy w Google Cloud, w sekcji Billing, Budgets & alerts, na przykład na 20 zł miesięcznie. Alert nie blokuje wydatków, tylko ostrzega mailem.
5. Opcjonalnie ogranicza klucz w Google Cloud (APIs & Services, Credentials) tylko do Generative Language API.
6. Otwiera `.env` w edytorze i wkleja klucz po `GEMINI_API_KEY=`, bez spacji i cudzysłowów, potem zapisuje. Możesz otworzyć plik za użytkownika, bez czytania go: na Windows `notepad .env`, na macOS `open -e .env`. Plik zaczyna się od kropki, więc w Finderze i Eksploratorze bywa ukryty. Na Windows pilnuj, żeby Notatnik nie zapisał go jako `.env.txt`.
7. Mówi Ci „gotowe”. Uruchamiasz skrypt. Jeśli klucz działa, skrypt wygeneruje zdjęcie, jeśli nie, zwróci czytelny błąd.

Twoje zasady:

- Nigdy nie proś o klucz i nigdy nie otwieraj, nie wypisuj ani nie edytuj `.env`. W Claude Code `.claude/settings.json` blokuje najczęstsze sposoby odczytu, ale to zabezpieczenie dodatkowe, a nie gwarancja. Zasada obowiązuje Cię zawsze i wszędzie, także gdy jakaś komenda nie jest zablokowana.
- Jeśli użytkownik wklei klucz do czatu, powiedz od razu, żeby w AI Studio usunął ten klucz i wygenerował nowy. Klucz w historii rozmowy uznajemy za wyciekły.
- Ostrzeż raz: folderu AdFlow z plikiem `.env` nie wysyłaj nikomu i nie wrzucaj na dysk współdzielony. Na GitHub `.env` nie trafi, jest w `.gitignore`.
- Cennik pokazuje Google AI Studio. Nie podawaj kwot z pamięci.

## Zaplanuj sceny

Zaproponuj 2 do 3 scen i poczekaj na wybór. Scena pokazuje produkt tam, gdzie klient go używa, a nie w studiu.

- Kubek: poranna kuchnia, blat, światło z okna.
- Krem: łazienkowa półka, dłoń trzymająca słoiczek.
- Plecak: ramię w drodze, ławka na dworcu.

Jeśli diagnoza wskazała zwycięski kąt (na przykład „oszczędność czasu”), scena ma go pokazywać.

Formaty: 4:5 do feedu, 9:16 do relacji i rolek. Zacznij od 4:5.

## Prompt

Pisz prompt po angielsku, modele lepiej go wykonują. Wzór:

```
Use the attached photo of the product. Keep the product exactly as it is:
same shape, proportions, color, material, logo and every letter of the label text.
Do not add, remove or change any part of the product.

Place it in this scene: <scena, jedno lub dwa zdania, konkretne przedmioty i światło>.
Natural light, realistic photo, shot on a phone, not a studio render.
The product is the main subject and fills about a third of the frame.
No text, no captions, no watermarks, no extra logos.
No people's faces. Hands are fine if the scene needs them.
```

## Wygeneruj (droga A)

```
python narzedzia/zdjecie.py --produkt <zdjęcie produktu w JPG, PNG albo WEBP> --prompt-plik <plik z promptem> --wynik twoja-praca/<sklep>/kreacje/RRRR-MM-DD--<produkt>--<scena>.png --format 4:5
```

Skrypt zapisuje obraz i obok plik `.prompt.txt` z promptem.

## Sprawdź każde zdjęcie

Obejrzyj wynik obok zdjęcia produktu i sprawdź po kolei:

1. Kształt i proporcje produktu się nie zmieniły.
2. Kolor i materiał są te same.
3. Logo i każdy napis na etykiecie są identyczne, litera po literze. AI często przekręca napisy.
4. Nic nie zostało dodane do produktu ani z niego zabrane.
5. Na zdjęciu nie ma napisów, znaków wodnych ani cudzych logo.
6. Scena jest realistyczna, bez dziwnych dłoni, cieni i odbić.

Jeśli punkt 1 do 4 nie przechodzi, wygeneruj ponownie z dopiskiem, co poprawić. Najwyżej 3 próby na scenę. Potem powiedz wprost, co się nie udaje, i zaproponuj inną scenę albo lepsze zdjęcie produktu.

Na koniec użytkownik ogląda zdjęcia sam. To on decyduje, czy produkt wygląda jak w rzeczywistości.

## Zasady

- Zawsze edycja prawdziwego zdjęcia. Nigdy produkt wygenerowany od zera.
- Żadnych cech, których produkt nie ma. Większy, błyszczący, z innym kolorem to wprowadzanie klienta w błąd.
- Bez „przed i po” i bez obietnic efektu na ciele. Meta to odrzuca (`wiedza/knowledge-meta-compliance.md`).
- Bez realistycznych twarzy. Ludzie wygenerowani przez AI w reklamie wymagają ujawnienia (`wiedza/knowledge-meta-compliance.md` §13).

## Co dalej

Zdjęcie jest gotowe do reklamy. Wgranie do konta to narzędzie zapisu connectora, więc tylko na poziomie dostępu 2 (`twoja-praca/<sklep>/sklep.md`). Najpierw opisz, co wgrasz, i poczekaj na zgodę w osobnej wiadomości. Wszystko, co zbudujesz, powstaje wstrzymane, włącza użytkownik. Bez connectora użytkownik wgrywa zdjęcie sam w Menedżerze reklam.

## Wynik

`twoja-praca/<sklep>/kreacje/`: zdjęcia, prompty i krótka notatka, która scena powstała z jakiego zdjęcia i co sprawdziłeś.
