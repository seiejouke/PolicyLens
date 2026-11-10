# LU3 wireframes als Tkinter-demo

De demo toont twee schermroutes in één lokaal Tkinter-venster, gebouwd in
[main.py](../main.py):

- **Burger:** gebaseerd op WF-B01/B02; vast zoekveld `data`, fictieve
  resultaten, beknopte metadata, voorbeeldbronactie en gerelateerde begrippen.
- **Onderzoeker:** gebaseerd op WF-O01/O02; hetzelfde vaste zoekveld,
  voorbeeldfilters, uitgebreide metadata, analyse, CSV- en historiebediening.
- De navigatieknoppen wisselen van scherm, zoals de twee gebruiksroutes in
  WF-G01 en US-G02.

Alle getoonde records, tellingen en filters zijn illustratief en fictief.
Alleen het wisselen van wireframe en het opslaan/laden van de fictieve records
werkt. De zoekopdracht, filters, bronactie, analyse, CSV-export en
zoekgeschiedenis zijn alleen afgebeeld; er is geen API. De SQLite-database
`policylens.db` staat naast `main.py` en wordt gemaakt via **Bewaar
voorbeelddata lokaal** in de onderzoekerwireframe. Dit is dus een **GUI-
wireframe voor demonstratie**, niet een functionele realisatie of
acceptatietest van alle stories.

De expliciete scopewijziging is: vaste zoekterm `data`, lokale dummydata en
twee Tkinter-schermen in plaats van werkende API-, filter-, analyse-,
CSV-export- en zoekgeschiedenisfuncties. Alleen dummyresultaten worden lokaal
in SQLite bewaard. De originele LU3- en LU4-documenten blijven ongewijzigd.

## Lokale database

De demo gebruikt **SQLite**, een eenvoudige database die in één lokaal bestand
staat. Python bevat hiervoor al de `sqlite3`-module; er draait dus geen aparte
database-server en er is geen internetverbinding nodig. Het bestand
`policylens.db` staat in dezelfde map als `main.py` en wordt aangemaakt zodra
je in het onderzoekerscherm op **Bewaar voorbeelddata lokaal** klikt.

De tabel `documents` bevat de fictieve resultaten met de velden `title`
(titel), `subject` (onderwerp), `date` (datum), `kind` (soort document),
`document_id` (demo-ID) en `number` (demonstratienummer). Bij opslaan vervangt
de app de bestaande voorbeeldrecords door de huidige ingebouwde dummydata.
Bij het starten laadt de app de opgeslagen records; als er nog geen records
zijn, toont hij de ingebouwde voorbeelden. Er worden geen echte gegevens of
API-resultaten opgeslagen.

Een `.db`-bestand is geen tekstbestand, dus een gewone teksteditor toont
onleesbare tekens. Je kunt de database bekijken met een SQLite-programma,
bijvoorbeeld **DB Browser for SQLite**: open daarin `policylens.db` en kies
de tabel `documents`. Dit programma is alleen nodig om de database te
bekijken; de demo zelf heeft geen extra Python-pakketten nodig.
