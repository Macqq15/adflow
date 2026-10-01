"""Zdjęcie produktu w scenie przez Gemini, na podstawie prawdziwego zdjęcia produktu.

Użycie:
    python narzedzia/zdjecie.py --produkt zdjecie.jpg --prompt-plik prompt.txt --wynik twoja-praca/sklep/kreacje/2026-10-01--kubek--kuchnia.png

Klucz Gemini API bierze z pliku .env w folderze AdFlow (zalecane). Jeśli ustawiona jest zmienna środowiskowa
GEMINI_API_KEY, ma ona pierwszeństwo. Ostatnia możliwość to plik ~/.config/gemini/api-key.
Bez dodatkowych bibliotek, wystarczy Python 3.8+.
"""
import argparse
import base64
import json
import os
import sys
import time
import urllib.error
import urllib.request

MODEL = "gemini-3.1-flash-image-preview"
FORMATY = ["4:5", "9:16", "1:1"]


def klucz():
    if os.environ.get("GEMINI_API_KEY"):
        return os.environ["GEMINI_API_KEY"].strip()
    env = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env")
    if os.path.exists(env):
        with open(env, encoding="utf-8-sig") as f:
            for linia in f:
                nazwa, _, wartosc = linia.strip().partition("=")
                if nazwa.strip() == "GEMINI_API_KEY" and wartosc.strip():
                    return wartosc.strip().strip('"').strip("'")
    sciezka = os.path.join(os.path.expanduser("~"), ".config", "gemini", "api-key")
    if os.path.exists(sciezka):
        with open(sciezka, encoding="utf-8") as f:
            k = f.read().strip()
            if k:
                return k
    return None


TYPY = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png", ".webp": "image/webp"}


def czesc_obrazu(sciezka):
    with open(sciezka, "rb") as f:
        dane = base64.b64encode(f.read()).decode("ascii")
    mime = TYPY[os.path.splitext(sciezka)[1].lower()]
    return {"inlineData": {"mimeType": mime, "data": dane}}


def generuj(produkty, prompt, wynik, format_, model):
    k = klucz()
    if not k:
        return {"blad": "Brak klucza. Skopiuj .env.example jako .env i wklej klucz po GEMINI_API_KEY=."}

    czesci = [czesc_obrazu(p) for p in produkty] + [{"text": prompt}]
    zapytanie = json.dumps({
        "contents": [{"parts": czesci}],
        "generationConfig": {
            "responseModalities": ["TEXT", "IMAGE"],
            "imageConfig": {"aspectRatio": format_},
        },
    }).encode("utf-8")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    naglowki = {"Content-Type": "application/json", "x-goog-api-key": k}

    for proba in range(2):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, data=zapytanie, headers=naglowki), timeout=180) as r:
                odpowiedz = json.loads(r.read().decode("utf-8"))
            break
        except urllib.error.HTTPError as e:
            tresc = e.read().decode("utf-8", "replace")
            if e.code == 404:
                return {"blad": f"Model {model} jest niedostępny. Sprawdź aktualną nazwę modelu do obrazów w Google AI Studio i podaj ją przez --model."}
            if e.code == 400 and "API_KEY_INVALID" in tresc:
                return {"blad": "Klucz w .env jest nieprawidłowy. Sprawdź, czy klucz jest wklejony w całości bez spacji, albo wygeneruj nowy w Google AI Studio."}
            if e.code == 429 and "free_tier" in tresc and "limit: 0" in tresc:
                return {"blad": "Darmowy plan Gemini nie generuje obrazów. Włącz płatności dla klucza w Google AI Studio (Billing) i spróbuj ponownie."}
            if e.code == 429 and proba == 0:
                print(json.dumps({"status": "limit zapytań, czekam 65 s"}, ensure_ascii=False), flush=True)
                time.sleep(65)
                continue
            return {"blad": f"HTTP {e.code}", "szczegoly": tresc[:500]}
        except urllib.error.URLError as e:
            return {"blad": f"Sieć: {e.reason}"}
    else:
        return {"blad": "Limit zapytań, spróbuj za kilka minut."}

    obraz, tekst = None, ""
    for kandydat in odpowiedz.get("candidates", [])[:1]:
        for czesc in kandydat.get("content", {}).get("parts", []):
            if "inlineData" in czesc:
                obraz = czesc["inlineData"]
            if "text" in czesc:
                tekst = czesc["text"]
    if not obraz:
        return {"blad": "Model nie zwrócił obrazu.", "tekst": tekst, "surowe": json.dumps(odpowiedz)[:500]}

    rozszerzenie = "png" if "png" in obraz.get("mimeType", "image/png") else "jpg"
    wynik = os.path.splitext(wynik)[0] + "." + rozszerzenie
    os.makedirs(os.path.dirname(wynik) or ".", exist_ok=True)
    with open(wynik, "wb") as f:
        f.write(base64.b64decode(obraz["data"]))
    with open(os.path.splitext(wynik)[0] + ".prompt.txt", "w", encoding="utf-8") as f:
        f.write(prompt)
    return {"status": "ok", "plik": wynik, "model": model, "format": format_, "tekst_modelu": tekst}


def main():
    for strumien in (sys.stdout, sys.stderr):
        strumien.reconfigure(encoding="utf-8")
    p = argparse.ArgumentParser(description="Zdjęcie produktu w scenie przez Gemini")
    p.add_argument("--produkt", action="append", required=True, help="Zdjęcie produktu (można podać kilka razy)")
    p.add_argument("--prompt", help="Prompt sceny")
    p.add_argument("--prompt-plik", help="Plik z promptem sceny")
    p.add_argument("--wynik", required=True, help="Ścieżka pliku wynikowego")
    p.add_argument("--format", default="4:5", choices=FORMATY, help="Proporcje, domyślnie 4:5 (feed)")
    p.add_argument("--model", default=MODEL)
    a = p.parse_args()

    if bool(a.prompt) == bool(a.prompt_plik):
        p.error("Podaj dokładnie jedno: --prompt albo --prompt-plik")
    for sciezka in a.produkt:
        if not os.path.exists(sciezka):
            p.error(f"Nie ma pliku: {sciezka}")
        if os.path.splitext(sciezka)[1].lower() not in TYPY:
            p.error(f"Nieobsługiwany format: {sciezka}. Zapisz zdjęcie jako JPG, PNG albo WEBP (zdjęcia HEIC z iPhone'a trzeba najpierw przekonwertować).")
    if a.prompt_plik and not os.path.exists(a.prompt_plik):
        p.error(f"Nie ma pliku z promptem: {a.prompt_plik}")
    if os.path.exists(a.wynik):
        p.error(f"Plik {a.wynik} już istnieje. Podaj inną nazwę, żeby nie nadpisać poprzedniego zdjęcia.")
    prompt = a.prompt or open(a.prompt_plik, encoding="utf-8").read()

    wynik = generuj(a.produkt, prompt, a.wynik, a.format, a.model)
    print(json.dumps(wynik, ensure_ascii=False, indent=2))
    sys.exit(0 if wynik.get("status") == "ok" else 1)


if __name__ == "__main__":
    main()
