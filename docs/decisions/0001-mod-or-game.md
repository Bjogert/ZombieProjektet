# ADR-0001: Välj Project Zomboid-kartmod

**Status: GODKÄND (2026-10-11). Ersätter tidigare UNDECIDED.**

## Beslut
Bygg ZombieProjektet som en **kartmod för Project Zomboid Build 42 Stable**. Första POC är Getaboda, därefter utökningar mot Ljungbytrakten. Behåll spelets befintliga mekanik. Skapa inte ett fristående spel parallellt.

## Varför
Projektet är ett roligt hobbyprojekt för att spela i igenkännbar svensk geografi, på sikt med vänner. Att skapa en hel överlevnadsmotor skulle fördröja det målet och skapa onödiga beroenden.

## Konsekvenser
- Prioritera verifiering av Build 42:s faktiska kartverktyg och modformat innan större generatorarbete.
- Framtida dataformat ska vara **enkla och läsbara för människor och agenter**, inte designade för hypotetisk motorportning.
- Ett fristående spel är en avlägsen möjlighet, inte en planerad gren eller aktiv milstolpe.
- Uppdatera projektplan och agentinstruktioner så att motstridiga äldre alternativ inte styr utveckling.
