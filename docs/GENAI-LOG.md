# GenAI-logboek

Dit logboek houdt het gebruik van generatieve AI voor PolicyLens NL bij als
input voor de LU3-reflectie. Het is geen volledige chat-export: leg relevante
prompts en beslissingen vast, maar neem geen wachtwoorden, persoonsgegevens of
andere gevoelige gegevens op.

## Nieuwe sessie of taak vastleggen

Kopieer dit format voor iedere betekenisvolle taak. Noteer prompts zo letterlijk
mogelijk; vat ze niet stilzwijgend samen.

### [datum] — [doel van de taak]

- **Prompt(s):** [letterlijke prompt(s)]
- **AI-bijdrage:** [voorstel, uitleg of wijziging]
- **Eigen keuze:** [overgenomen, aangepast of afgewezen; waarom]
- **Controle/uitkomst:** [hoe gecontroleerd en wat het resultaat was]

## Beschikbare eerdere prompts

De onderstaande items zijn overgenomen uit de beschikbare gespreksgeschiedenis.
Waar alleen een samenvatting beschikbaar was, is de prompt als reconstructie
aangeduid. Dit overzicht is daarom geen complete export van alle eerdere
prompts uit de repo.

### Datum niet beschikbaar — AI-code inkorten

- **Prompt(s):** “Can we use the ponytail repo to shorten the AI generated code?”;
  “Let's add and run it”; “How many lines of code does the program have”;
  “How much did ponytail improve”; “How come it did nothing despite the point
  being of doing exactly that”; “Yes, you have to actually use, run, build or
  whatever to apply ponytail on the application”.
- **AI-bijdrage:** Ponytail aan het project toevoegen en code verkorten.
- **Eigen keuze:** De eerste wijziging voldeed niet aan het doel; gevraagd om
  Ponytail daadwerkelijk op de applicatie toe te passen.
- **Controle/uitkomst:** De beschikbare geschiedenis vermeldt latere
  redundantieverwijderingen en geslaagde unit- en GUI-tests.

### Datum niet beschikbaar — applicatie versimpelen

- **Prompt(s):** “Could a minimul version of this be done with 200 lines of
  code?”; “What is an easy way to access and pull data from the API, using the
  script without using GUI right away?”.
- **AI-bijdrage:** Onderzocht hoe de applicatie en API-toegang eenvoudiger
  konden worden gemaakt.
- **Eigen keuze:** De scope is daarna verder beperkt tot eenvoudige
  wireframes.

### Datum niet beschikbaar — scope terugbrengen naar twee wireframes

- **Prompt(s):** “We moeten het project aanzienlijk versimpelen dat een
  beginnde pythron programmeer het kan bouwen adhv het boek Python Crash
  Course 3ED. Het project moet naar an absolute barebones versie van de
  user-stories. Zo weinig mogelijk code. Hoe minder hoe beter.”;
  “main.py is dus de gehele applicatie?”; “Voldoet het aan het LU3
  documentatie?”; “We hebben alle user-stories nodig, zolang we het simpel
  houden en minimale code gebruiken binnen hetzelfde script. Wat stel je
  voor”; “Okee, doe dat”.
- **AI-bijdrage:** De implementatie is vereenvoudigd en opnieuw ingedeeld.
- **Eigen keuze:** De gewenste scope is aangescherpt tot twee Tkinter-wireframes,
  een vaste zoekterm `data` en fictieve lokale voorbeelden; geen echte API.
- **Controle/uitkomst:** De wireframe-demo is samengevat in
  [IMPLEMENTATIE.md](IMPLEMENTATIE.md).

### Datum niet beschikbaar — lokale opslag

- **Prompt(s):** “Hoe kunnen we hier een simpele database toepassen voor het
  opslaan van de csv of vergelijkbaar? Suggesties?”; “Okee, bouw dit en hou
  het simpel en overzichtelijk”.
- **AI-bijdrage:** SQLite-opslag voor de fictieve records toegevoegd.
- **Eigen keuze:** SQLite gekozen als eenvoudige lokale database zonder extra
  Python-pakketten; de demo-gegevens blijven fictief.
- **Controle/uitkomst:** De beschikbare sessiegeschiedenis meldt dat de
  opslag-, herlaad- en GUI-controles slaagden. Testbestanden zijn later op
  verzoek verwijderd.

### 2026-11-10 — project opruimen en documentatie verduidelijken

- **Prompt(s):** “Schoon het project op, scripts en files die niet essentieel
  zijn dus”; “Volgens mij hebben we de test scripts ook niet nodig?”;
  “Wat zijn artifacts?”; “database staat erin als een .db die we niet kunnen
  openen. Leg uit hoe de db werkt, en welke db”; “Voldoen wij aan de
  specificaties van LU3? Wat moet er nog gebeuren? Maak een samenvatting”.
- **AI-bijdrage:** Overbodige bestanden en tests verwijderd, SQLite uitgelegd
  en de demo vergeleken met het LU3-ontwerp.
- **Eigen keuze:** De gebruiker koos ervoor testbestanden weg te laten en vroeg
  om uitleg en een eerlijk overzicht van de afwijkingen van LU3.
- **Controle/uitkomst:** De app is syntactisch gecontroleerd; de LU3-vergelijking
  benoemde ontbrekende functionele onderdelen, feedback en reflectie.

### 2026-11-10 — Git-update

- **Prompt(s):** “Git doesnt allow to update”.
- **AI-bijdrage:** De lokale branch bleek één commit voor en één commit achter
  op `origin/master`, met een conflict op `main.py`.
- **Eigen keuze:** Behoud de lokale PolicyLens-app, voeg de inkomende Python-
  oefenscripts toe, maar neem de tijdelijke Word-lockbestanden niet op.
- **Controle/uitkomst:** Merge voltooid en naar `origin/master` gepusht; de
  branch liep daarna gelijk met de remote.

### 2026-11-10 — GenAI-gebruik documenteren

- **Prompt(s):** “Laten we alle AI-prompts gedurende deze repo bijhouden in een
  apart document in repo zodat we gebruik gen-AI kunnen inzien bij reflectie.
  Wat stel je voor?”; “Okee, voeg het document toe;”.
- **AI-bijdrage:** Dit logboek en het invulformat zijn toegevoegd.
- **Eigen keuze:** Eerdere prompts worden opgenomen voor zover ze beschikbaar
  zijn; reconstructies worden expliciet aangeduid in plaats van als exacte
  chattranscripten gepresenteerd.
- **Controle/uitkomst:** Controleer het logboek bij iedere volgende betekenisvolle
  GenAI-taak en vul de eigen afweging en controle aan.
