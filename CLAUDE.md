@AGENTS.md

## Tylko dla Claude Code

- Skille `/adflow-start`, `/adflow-diagnoza`, `/adflow-przeglad`, `/adflow-zdjecia`, `/adflow-reklamy` i `/adflow-kampania` to skróty. Każdy odsyła do procedury w `procedury/`. Źródłem prawdy są procedury, nie skille.
- Connector Meta Ads dodany na koncie claude.ai jest widoczny także tutaj, jeśli Claude Code jest zalogowany tym samym kontem, ale dopiero w nowej sesji. Nie instaluj go osobno z terminala, chyba że użytkownik wyraźnie tego chce.
- Każde narzędzie, które zmienia konto reklamowe, wymaga zgody użytkownika. Nie obchodź tego i nie proś o wyłączenie.
- `.claude/settings.json` wymaga zgody na każde narzędzie connectora, które zmienia konto, i blokuje `ads_activate_entity`. Lista narzędzi jest w `polaczenie/connector.md`.
