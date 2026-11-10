# PolicyLens NL · Tkinter-wireframe-demo

Een offline GUI met twee schermen uit het LU3-ontwerp: **Burger** en
**Onderzoeker**. De schermen zijn wireframes met fictieve voorbeeldresultaten.
De zoekterm staat vast op `data`. Er wordt geen API aangeroepen.

## Starten

Vereist Python 3.11+ met Tkinter. Er zijn geen externe pakketten nodig.

```powershell
py main.py
```

Gebruik de knoppen bovenaan om tussen Burger en Onderzoeker te wisselen. De
knoppen en filters op de schermen zijn alleen ter illustratie en voeren geen
zoekopdracht, bronopening of CSV-export uit. In de Onderzoeker-wireframe kun je
wel op **Bewaar voorbeelddata lokaal** klikken om de fictieve records in SQLite
op te slaan. De app laadt opgeslagen voorbeelden bij de volgende start.

De database staat in `policylens.db` naast `main.py`. Het bestand wordt pas
aangemaakt wanneer je de opslagknop gebruikt en is uitgesloten van Git.
Het is een SQLite-databasebestand en geen leesbaar tekstbestand. Je kunt het
bekijken met bijvoorbeeld DB Browser for SQLite: open daarin `policylens.db`.
De app zelf heeft hiervoor geen extra pakket nodig.

## Wat de wireframes tonen

- **Burger:** vast zoekveld, maximaal tien resultaten, voorbeeldmetadata,
  bronactie en gerelateerde begrippen.
- **Onderzoeker:** vast zoekveld, voorbeeldfilters, metadata, analyse,
  exportbediening en recente zoektermen.
- **Gedeeld:** twee herkenbare routes en uitleg dat de gegevens fictief zijn.

De user-stories zijn hier visueel uitgewerkt, niet functioneel gebouwd. Zie
[de scope-notitie](docs/IMPLEMENTATIE.md). De Python GUI-code staat in
[main.py](main.py).
