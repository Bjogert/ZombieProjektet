# ZombieProjektet — Småland i Project Zomboid

**Status (2026-10-11): design beslutad; teknisk kartintegration ännu inte verifierad i spelet.**

Ett öppet hobbyprojekt för att bygga en igenkännbar svensk spelvärld som en **kartmod till Project Zomboid Build 42 Stable**. Första testområdet är **Getaboda mellan Agunnaryd och Södra Ljunga**, cirka 4–5 hus. Sedan kan världen växa mot Ljungbytrakten.

**Princip:** enklaste fungerande och skalbara lösningen. Verkliga huslägen, vägar och marktyper från tillåtna geodata; vanliga byggnader och detaljer genereras med svenska standardregler. Enskilda hus kan senare förbättras via separata datafiler utan att deras ändringar skrivs över.

## Börja här
- **För dig:** [Projektöversikt (HTML)](docs/PROJECT_OVERVIEW.html) — ladda ner filen och öppna den i en webbläsare för klickbara vägval och kommentarer. Den skickar inte ändringar direkt till GitHub.
- **För agenter:** [Specifikation](docs/PROJECT_SPEC.md), [beslut](docs/DECISIONS.md), [roadmap](docs/ROADMAP.md) och [agentinstruktioner](AGENTS.md).
- **Första tekniska testet:** [Build 42-spike](docs/BUILD42_SPIKE.md).

## Nuläge och ärliga begränsningar
Det finns ett Python-experiment som tilldelar reproducerbara stilar till GeoJSON-byggnader. Det skapar **inte** fungerande Project Zomboid-kartor, tiles, inredningar eller modpaket. Getabodas verkliga geometri är ännu **inte** inläst eller verifierad. Ingen speltestad Build 42-karta finns ännu i detta repo.

## Lokala kontroller (Python 3.10+, inga tredjepartsberoenden)
```sh
python -m unittest discover -s tests -v
python tools/check_agent_setup.py
python tools/render_dashboard.py --check
python tools/building_styles.py --input data/sample/buildings.geojson --output build/building-styles.json
```

Ändra statusöversikten i `docs/HUMAN_OVERVIEW.md`; kör `python tools/render_dashboard.py` för att uppdatera HTML-vyn.

## Juridiskt
Endast eget material och tillåtna data får distribueras. Egna kodfiler licensieras enligt [MIT](LICENSE); varje extern datakälla, importerad resurs och eventuell grafik har sina respektive villkor. Se [DATA_AND_RIGHTS.md](docs/DATA_AND_RIGHTS.md). Projektet är inte knutet till The Indie Stone.
