# Scope — Getaboda proof of concept

## POC-resultat (beslutat)
En **separat svensk spelkarta** i Project Zomboid Build 42 Stable med:
1. Getabodas cirka 4–5 verkligt placerade byggnader, närliggande vägar och grundläggande skog/åker/vatten från tillåtna geodata, kontrollerade mot källorna.
2. Enkla, spelbara svenska hus utifrån ett litet datafilsbaserat bibliotek. Minst ett hus ska ha fungerande entré och enkel inredning.
3. Korrekt klassificering där data finns; annars dokumenterat antagen typ, som kan korrigeras i t.ex. QGIS.
4. Reproducerbar generering och stabil byggnadsidentitet. Manuella ändringar för enskilda byggnader ska överleva omgenerering.
5. Dokumenterad installation och *verifiering i det riktiga spelet*.

## Vägen dit
Det första tekniska deltestet (M0) är betydligt mindre: en minimal karta med ett spelbart hus i Build 42. Manuella export/import-steg är tillåtna tills kartformatet är verifierat.

## Senare — inte blockerande för POC
- Fler svenska hustyper, grafiska tiles, detaljerade verkliga hus, offentlig community och kanske en visuell huseditor.
- Geografisk komprimering mellan bebyggda platser med bevarat vägnät.
- Testad multiplayer med vänner, GitHub Releases och senare Steam Workshop.
- Bevarade gamla sparfiler när möjligt; under utvecklingen är nystart acceptabel.
- Höjdvisualisering, större städer, nya svenska spelobjekt.

## Utanför scope
Egen motor/Godot, nya zombiesystem, egen nätkod, AI-NPC:er, total 1993-rekonstruktion, tillräckligt exakta interiörer för alla hus, hela Småland i första versionen och dyr GIS-infrastruktur.
