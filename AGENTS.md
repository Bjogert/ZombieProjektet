# ZombieProjektet — gemensamma instruktioner för Codex och Claude Code

Den här filen är den kanoniska agent-ingången. Claude Code har även [CLAUDE.md](CLAUDE.md), som pekar hit; läs inte instruktionerna rekursivt.

## Uppdrag — beslutat
Bygg **en Project Zomboid-kartmod för Build 42 Stable**, inte ett fristående spel. Getaboda (cirka 4–5 byggnader) är första verkliga experimentet och framtida Smålandsvärldens utgångspunkt. Spelvärlden ska kännas svensk och tidsmässigt passa spelets 1990-tal; använd nutida geodata utan att återskapa en historiskt exakt karta. Använd Project Zomboids standardmekanik. Se [PROJECT_SPEC](docs/PROJECT_SPEC.md), [DECISIONS](docs/DECISIONS.md), [ROADMAP](docs/ROADMAP.md), [SCOPE](docs/SCOPE.md) och [ADR-0001](docs/decisions/0001-mod-or-game.md).

**Icke-mål:** fristående spelmotor, nya zombiesystem, nya överlevnadsmekaniker, fullt dynamisk terräng, multiplayer i första POC, komplett svensk assetkatalog eller automatisk geografisk komprimering i första testet.

## Principer
1. **Enklaste verifierbara skalbara lösning**: ingen spekulativ arkitektur. Behåll gränssnitt som tillåter större detaljrikedom senare.
2. **Bevara källan:** originalkoordinater, identifierare, källa/licens och verifierade egenskaper ändras aldrig av spelskalning/kvantisering. Skilj antaganden från fakta.
3. **Determinism och overrides:** samma indata/seed ger samma resultat. Använd separata identifierarbaserade korrigeringar; en omgenerering får inte tysta övertrampa dem.
4. **Svenska typer:** ett litet utbyggbart, datadrivet bibliotek av byggnadstyper, fasader, interiörregler och senare egna tiles. Antag rimliga standardvärden när data saknas; hitta inte på verifierade byggnadsplaceringar.
5. **Verifiera i spelet:** Python-test är aldrig bevis för att modden laddar, att kollision fungerar eller att ett hus går att gå in i.
6. **Kostnader och rättigheter:** öppna och fria verktyg först; inga inköp utan användarens godkännande. Följ [DATA_AND_RIGHTS](docs/DATA_AND_RIGHTS.md). Publicera inga detaljerade privata interiörer utan granskning.

## Första uppgift
Utför [BUILD42_SPIKE](docs/BUILD42_SPIKE.md) före storskalig geodatapipeline. Verifiera kompatibla kartverktyg, producera minsta möjliga separata karta och få den testad i aktuell Build 42 Stable. Dokumentera versionsnummer, reproduktionssteg, evidens och eventuella blockerare. Ingen falsk statusuppdatering om icke-speltestad kod.

## Agentarbete och mänsklig vy
- Följ [AGENT_WORKFLOW](docs/AGENT_WORKFLOW.md) och välj passande projekt-skills i `.agents/skills/` respektive `.claude/skills/`.
- Läs befintlig kod, tester och [GLOSSARY](GLOSSARY.md); arbeta i små, självständigt kontrollerbara vertikala steg. Ange ändrat beteende, körda kontroller, ej verifierat och risk.
- Specifikationer, tekniska beslut, granskningar och arbetshistorik skrivs i **Markdown**.
- Den förenklade mänskliga vyn kommer från [HUMAN_OVERVIEW](docs/HUMAN_OVERVIEW.md) och genereras till [PROJECT_OVERVIEW.html](docs/PROJECT_OVERVIEW.html) med `python tools/render_dashboard.py`. **Tekniskt facit är PROJECT_SPEC/DECISIONS/ROADMAP**; håll den mänskliga översikten konsekvent men duplicera inte tekniska detaljer.
- De klickbara HTML-knapparna skapar *förslag* (GitHub issue eller kopierad text), inte automatiska beslut eller commits.
- Kör `python tools/render_dashboard.py --check`, `python tools/check_agent_setup.py` och `python -m unittest discover -s tests -v` efter relevanta ändringar.

## Avgjorda vägval
Inga nya frågor om mod kontra fristående spel eller om Getaboda ska vara första testområdet: detta är redan beslutat. Om verkliga verktygsbegränsningar motsäger specifikationen, beskriv evidensen och föreslå minsta möjliga ändring i en Markdown-review.
