# GenAI-logboek

Dit logboek verzamelt de teruggevonden gebruikersprompts voor PolicyLens NL,
inclusief korte vervolgvragen, keuzes in vraagdialogen en hulp bij Git en de
ontwikkelomgeving. Het ondersteunt de reflectie voor LU3 en LU4. Neem geen
wachtwoorden, persoonsgegevens of andere gevoelige gegevens op.

## Controle op volledigheid — 2026-11-11

De eerdere versie bevatte 23 geciteerde prompts. Bij de controle zijn na
vergelijking met de lokale Codex- en Copilot-gespreksbestanden **47
gebruikersprompts uit zes sessies** opgenomen: **24 ontbrekende prompts
toegevoegd**. Ook zijn **vijf
antwoorden uit keuzedialogen** vastgelegd. De eerdere onbekende datums zijn
hersteld. Eén bestaand citaat is gecorrigeerd naar de oorspronkelijke tekst:
`naar an absolute` was in de bron `naar aan absolute` (S4-09).

Na die controle zijn leervragen S6-05 en S6-06 toegevoegd. Het actuele logboek bevat
**49 gebruikersprompts** en vijf antwoorden uit keuzedialogen.

De aanvullingen betreffen de projectomgeving en Git-uitleg op 30 oktober, de
MVP-inschatting en bouw op 6 november, drie expliciete scope-/Tkinter-prompts en
twee commit-/push-prompts op 10 november, en de sessies van 11 november.

- **Gecontroleerde bronnen:** de zes lokale gespreksbestanden hieronder, de
  VS Code-sessiecatalogus, de Git-geschiedenis inclusief agent-checkpoints,
  README, implementatienotitie en de LU3-/LU4-Worddocumenten. Twee aanvullende
  PolicyLens-sessies in de catalogus hadden geen gebruikersberichten.
- **Nauwkeurigheid:** de prompttekst is letterlijk uit de bron overgenomen;
  spelling en herhaalde berichten blijven behouden. Alleen IDE-context,
  witruimte rond een bericht en spaties aan regeleinden zijn weggelaten. Tijden zijn
  omgerekend naar **Europe/Amsterdam**. De ID's verwijzen naar de bron en de
  volgorde van het gebruikersbericht binnen die bron.
- **Afbakening:** dit dekt alle teruggevonden gebruikersprompts in deze zes
  lokale sessies tot en met S6-06. Gesprekken op andere apparaten, in andere
  accounts of verwijderde chats zijn hiermee niet bewezen volledig. Er is
  bijvoorbeeld geen teruggevonden prompt voor het oorspronkelijke opstellen
  van de LU3-/LU4-documenten; hun aanwezigheid bewijst die prompt niet.
- **Reflectiebewijs:** AI-bijdragen en controles hieronder beschrijven de
  historische sessieverslagen en beschikbare projectwijzigingen. Historische
  tests zijn bij deze documentcontrole niet opnieuw uitgevoerd. Eigen keuzes
  worden alleen aan expliciete verzoeken of vastgelegde antwoorden ontleend;
  de persoonlijke leerreflectie moet de auteur zelf aanvullen.

Systeem-/IDE-berichten, lege Companion Page-meldingen, interne toolaanroepen en
automatische beoordelingssessies zijn niet als gebruikersprompts meegeteld.
Bijlagen zijn niet gekopieerd; een verwijzing naar een screenshot blijft als
onderdeel van de oorspronkelijke prompt zichtbaar.

### Bronnenregister

| Bron | Periode | Lokale sessie-ID | Prompts |
| --- | --- | --- | ---: |
| S1 | 2026-10-30 | `fc67043e-5446-4740-8c8e-95d4cca3a3b9` (Copilot) | 3 |
| S2 | 2026-10-30 | `00075c4f-f0a8-4f5d-8ace-838efc786d5c` (Copilot) | 4 |
| S3 | 2026-11-06 | `01a1b03b-f952-7200-b76d-321ff36913c4` (Codex) | 7 |
| S4 | 2026-11-07 t/m 2026-11-10 | `a5cc83cf-edcd-492a-b10f-56335fa18c13` (Copilot) | 28 |
| S5 | 2026-11-11 | `c4979235-24b0-46ab-82f6-5a01bbf512b9` (Copilot) | 1 |
| S6 | 2026-11-11 | `01a1cb9a-8038-76b2-b3c9-71cda7b662e6` (Codex, huidig gesprek) | 6 |
| **Totaal** | | | **49** |

De lokale bronbestanden staan buiten de repository:

- S1, S2, S4 en S5: `%USERPROFILE%/.copilot/session-state/<sessie-ID>/events.jsonl`.
- S3: `%USERPROFILE%/.codex/sessions/2026/11/06/rollout-2026-11-06T10-41-23-01a1b03b-f952-7200-b76d-321ff36913c4.jsonl`.
- S6: `%USERPROFILE%/.codex/sessions/2026/11/11/rollout-2026-11-11T18-14-23-01a1cb9a-8038-76b2-b3c9-71cda7b662e6.jsonl`.

De VS Code-catalogus koppelt de oudere host-sessie
`1ed3aa20-4132-4af8-8c3b-6bba99415280` uit de Git-checkpoints aan S4. Dit zijn
twee verwijzingen naar hetzelfde gesprek, geen afzonderlijke promptbronnen.

## Nieuwe prompts bijhouden

Voeg bij iedere volgende projecttaak alle gebruikersprompts en korte
vervolgberichten toe. Bewaar de letterlijke formulering en noteer datum/tijd,
bron, AI-bijdrage, eigen keuze en controle. Leg antwoorden in keuzedialogen apart
vast. Als een bron ontbreekt, label de tekst als **reconstructie** of
**ontbrekende bron**; presenteer die niet als letterlijk citaat.

### [datum] — [doel van de taak]

- **Bron:** [sessie-ID/gespreksbestand of vermelding dat de bron ontbreekt]
- **Prompt(s):** [datum/tijd en letterlijke prompttekst per bericht]
- **Antwoord in keuzedialoog:** [alleen indien gegeven; letterlijk vastleggen]
- **AI-bijdrage:** [voorstel, uitleg of wijziging]
- **Eigen keuze:** [aantoonbaar overgenomen, aangepast of afgewezen; waarom]
- **Controle/uitkomst:** [hoe gecontroleerd en wat het resultaat was]

## Chronologisch promptoverzicht

### 2026-10-30 — .gitignore openen

**Prompt S1-01 — 2026-10-30 10:53:53**

> How do I open .gitignore, since code .ignore does not work interstingly

- **AI-bijdrage:** Uitgelegd dat `.gitignore` een andere bestandsnaam is dan
  `.ignore` en hoe het bestand in VS Code geopend kan worden.
- **Eigen keuze:** Hulp gevraagd bij het openen van het projectbestand.
- **Controle/uitkomst:** Uitleg gegeven; geen bevestiging vastgelegd dat de
  gebruiker het bestand daarna heeft geopend.

### 2026-10-30 — Codex-extensie start niet

**Prompt S1-02 — 2026-10-30 17:37:17**

> Codex is not starting?

**Prompt S1-03 — 2026-10-30 18:12:57**

> in vsc code, see screenshot

**Prompt S2-01 — 2026-10-30 18:15:39**

> Is codex down? It doesnt start in vsc extension

- **AI-bijdrage:** Op basis van de gemelde fout en een screenshot uitleg over
  herladen van VS Code, extensie-updates en het raadplegen van uitvoerlogs.
- **Eigen keuze:** De gebruiker verduidelijkte dat het om de VS Code-extensie
  ging en verwees naar een screenshot.
- **Controle/uitkomst:** De sessie bevat een toenmalige statuscontrole en
  probleemoplossingsadvies; een succesvolle oplossing is niet bevestigd.
  Het screenshot zelf is niet in dit log overgenomen.

### 2026-10-30 — Git-identiteit en branch publiceren

**Prompt S2-02 — 2026-10-30 18:32:24**

> How do I set global for git user.name ad user.email so I can commitin my repos without constantly setting it. also, I don't know what my user.name and user.email is

**Prompt S2-03 — 2026-10-30 18:34:39**

> isnt username and email supposed to be the same as my github, or are these different? im already logged into git through vsc, why doesnt it pick up that user data?

**Prompt S2-04 — 2026-10-30 18:49:52**

> why do I have the option to publish branch, what does it mean

- **AI-bijdrage:** Globale Git-auteursinstellingen gecontroleerd en uitgelegd
  hoe deze verschillen van GitHub-aanmelding; ook Publish Branch toegelicht.
- **Eigen keuze:** Gevraagd om eenmalige configuratie en uitleg voordat het
  project gepubliceerd werd; geen naam of e-mailadres in dit log opgenomen.
- **Controle/uitkomst:** De sessie meldde dat globale naam/e-mail nog niet
  ingesteld waren. De latere Git-geschiedenis bevat de eerste projectcommit
  `56ecfd1`; dit bewijst niet welke configuratiestappen de gebruiker uitvoerde.

### 2026-11-06 — MVP-complexiteit en budget van 80 uur

**Prompt S3-01 — 2026-11-06 10:42:00**

> Observe the documentation in the project;
>
> How complicated would a minimum viable product be if we follow the outline?

**Prompt S3-02 — 2026-11-06 10:45:21**

> I have perhaps 80 at best; what do you suggest then. It is a student casus.

- **AI-bijdrage:** LU3/LU4 gelezen en een inschatting gemaakt voor twee
  interfaces, API, analyse, SQLite, export en toetsingsbewijs. Daarna een
  planning van 60 werkuren met 20 uur reserve voorgesteld.
- **Eigen keuze:** De gebruiker gaf een maximum van ongeveer 80 uur aan en
  benadrukte dat het een studentcasus was.
- **Controle/uitkomst:** De inschatting was een planning, geen gemeten
  doorlooptijd. API-integratie werd als eerste technische onzekerheid benoemd.

### 2026-11-06 — eerste functionele MVP bouwen

**Prompt S3-03 — 2026-11-06 10:55:49**

> Build me a minimum viable product following the documentation.

- **AI-bijdrage:** Een modulaire Tkinter-app gebouwd met Burger- en
  Onderzoekweergave, echte Tweede Kamer-API, filters, tellingen, CSV-export en
  SQLite-zoekgeschiedenis. Launchers, tests en implementatienotities toegevoegd.
- **Eigen keuze:** Expliciet opdracht gegeven een MVP volgens de documentatie
  te bouwen. De verdere technische invulling kwam van de AI.
- **Controle/uitkomst:** De sessie rapporteerde 41 offline tests, 14
  desktopcontroles en een API-zoekopdracht met PDF-download. De historische
  checkpoint `8fd51d3` bevat de eerdere app, tests en bewijsbestanden. Echte
  gebruikersfeedback en persoonlijke reflectie waren nog niet uitgevoerd.
  Deze functionele versie is later door de wireframe-demo vervangen.

### 2026-11-06 — programma starten en Python-omgeving

**Prompt S3-04 — 2026-11-06 11:24:12**

> How to run the program (venv is not active)

**Prompt S3-05 — 2026-11-06 11:24:49**

> start bat not found

**Prompt S3-06 — 2026-11-06 11:25:33**

> $ python main.py
> Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings >Apps > Advanced app settings > App execution aliases.

- **AI-bijdrage:** De startprocedure uitgelegd, het launcherpad gecontroleerd
  en vastgesteld dat `python` de Windows Store-alias gebruikte. Daarna een
  lokale `.venv` aangemaakt en startinstructies gegeven.
- **Eigen keuze:** De gebruiker meldde de concrete startproblemen en de
  foutmelding uit de terminal.
- **Controle/uitkomst:** Volgens de sessie bestond `start.bat` in de projectmap
  en werd de virtuele omgeving gecontroleerd. Dat is historische informatie;
  de huidige wireframe-demo heeft deze launcher niet meer.

### 2026-11-06 — aansluiten bij Python Crash Course 3ED

**Prompt S3-07 — 2026-11-06 13:25:34**

> How far could I build this application if I only studied Python Crash Course 3ED?

- **AI-bijdrage:** De app vergeleken met de onderwerpen uit het boek;
  aanvullende leerstof benoemd voor Tkinter, SQLite en achtergrondverzoeken.
- **Eigen keuze:** Gevraagd hoeveel zelfstandig te bouwen is met alleen dit
  boek als basis; geen aparte implementatiekeuze in dit bericht.
- **Controle/uitkomst:** Een leerroute voorgesteld. Dit was een inhoudelijke
  vergelijking, geen bewijs dat de gebruiker deze onderdelen al beheerste.

### 2026-11-07 — AI-code verkorten met Ponytail

**Prompt S4-01 — 2026-11-07 12:39:19**

> Can we use the ponytail repo to shorten the AI generated code?

**Prompt S4-02 — 2026-11-07 12:42:45**

> Let's add and run it

**Keuzeantwoord K1 (S4) — 2026-11-07 12:43:28**

> install_scope: workspace_skill
> run_target: project

**Prompt S4-03 — 2026-11-07 12:46:40**

> How many lines of code does the program have

**Prompt S4-04 — 2026-11-07 12:47:28**

> How much did ponytail improve

**Prompt S4-05 — 2026-11-07 12:48:01**

> How come it did nothing despite the point being of doing exactly that

**Prompt S4-06 — 2026-11-07 12:48:43**

> Yes, you have to actually use, run, build or whatever to apply ponytail on the application

- **AI-bijdrage:** Eerst de CSV-export aangepast en Ponytail als projectskill
  toegevoegd. Na de correctie door de gebruiker ook dubbele zoektermstatus,
  een overbodige timeoutcontrole en invoervalidatie vereenvoudigd.
- **Eigen keuze:** Via K1 gekozen voor een projectskill en toepassing op het
  hele project. De gebruiker wees erop dat toevoegen zonder daadwerkelijke
  codeverkorting niet aan het doel voldeed.
- **Controle/uitkomst:** De sessie meldde aanvankelijk geen verkorting; na de
  herziening ging de app van 1.049 naar 1.045 regels. Historisch gemeld:
  41 unittests en 14 desktopcontroles geslaagd. De Ponytail-bestanden zijn op
  10 november tijdens het opruimen weer verwijderd.

### 2026-11-07 — versie van ongeveer 200 regels onderzoeken

**Prompt S4-07 — 2026-11-07 15:14:33**

> Could a minimul version of this be done with 200 lines of code?

- **AI-bijdrage:** Uitgelegd dat ongeveer 200 regels een beperktere
  zoek-/resultatenapp mogelijk maken, met verlies van onderzoeksfuncties.
- **Eigen keuze:** De gebruiker onderzocht een veel kleinere versie; in dit
  bericht is nog geen opdracht tot bouwen gegeven.
- **Controle/uitkomst:** Alleen een scope-inschatting; geen codewijziging.

### 2026-11-08 — API benaderen zonder GUI

**Prompt S4-08 — 2026-11-08 15:09:44**

> What is an easy way to access and pull data from the API, using the script without using GUI right away?

- **AI-bijdrage:** Een terminalaanroep voor de toenmalige `ApiClient` en een
  verwijzing naar het API-controlescript gegeven.
- **Eigen keuze:** Gevraagd om een eenvoudige manier om gegevens op te halen
  zonder eerst de GUI te gebruiken.
- **Controle/uitkomst:** Uitleg voor de toenmalige modulaire versie; de huidige
  demo bevat geen API-client en deze opdrachten horen bij die eerdere versie.

### 2026-11-10 — terug naar één eenvoudig applicatiescript

**Prompt S4-09 — 2026-11-10 12:41:31**

> We moeten het project aanzienlijk versimpelen dat een beginnde pythron programmeer het kan bouwen adhv het boek Python Crash Course 3ED. Het project moet naar aan absolute barebones versie van de user-stories. Zo weinig mogelijk code. Hoe minder hoe beter.

**Keuzeantwoord K2 (S4) — 2026-11-10 12:59:27**

> scope: citizen_core

**Keuzeantwoord K3 (S4) — 2026-11-10 13:03:48**

> interface: desktop

**Prompt S4-10 — 2026-11-10 13:35:26**

> main.py is dus de gehele applicatie?

**Prompt S4-11 — 2026-11-10 13:39:33**

> Voldoet het aan het LU3 documentatie?

- **AI-bijdrage:** De modulaire app teruggebracht tot een burgerzoeker in één
  `main.py` van 122 regels. Daarna uitgelegd welke LU3-stories ontbraken.
- **Eigen keuze:** Via K2 eerst alleen de burger-kern gekozen en via K3 het
  Tkinter-desktopvenster behouden. Vervolgens expliciet nagevraagd of dit de
  volledige applicatie was en aan LU3 voldeed.
- **Controle/uitkomst:** De sessie meldde drie tests, een GUI-startcontrole en
  tien echte API-resultaten. De vergelijking met LU3 liet ontbrekende
  onderzoekerstories zien; deze versie voldeed niet aan de volledige baseline.

### 2026-11-10 — alle user-stories in één script terugbrengen

**Prompt S4-12 — 2026-11-10 13:48:15**

> We hebben alle user-stories nodig, zolang we het simpel houden en minimale code gebruiken binnen hetzelfde script. Wat stel je voor

**Prompt S4-13 — 2026-11-10 13:49:11**

> Okee, doe dat

- **AI-bijdrage:** Burger- en Onderzoekweergave, filters, tellingen, CSV,
  zoekgeschiedenis en foutmeldingen weer samengebracht in één script.
- **Eigen keuze:** De gebruiker wilde alle stories behouden en gaf vervolgens
  opdracht het voorgestelde eenvoudige script te bouwen.
- **Controle/uitkomst:** De sessie meldde 434 regels, 13 geslaagde tests,
  GUI-controles met testdata en een echte API-zoekopdracht. Deze versie is
  daarna opnieuw beperkt; dit beschrijft niet de huidige werking.

### 2026-11-10 — vaste zoekterm, dummydata en twee Tkinter-wireframes

**Prompt S4-14 — 2026-11-10 13:59:21**

> Dit is onnodig complex, we moeten de scope nog verder limiteren. Laten we de zoektermen limiteren tot het woord 'data'.
>
> Dus twee wireframes, 1 voor burger, 1 voor onderzoeker, beide kunnen enkel de zoekterm 'data' gebruiken. Zodat we de wireframes kunnen demonstreren en dit lokaal opslaan. Dit hoort het project aanzienlijk te simplificeren en toch binen de userstories valt.

**Prompt S4-15 — 2026-11-10 14:03:12**

> Dit is onnodig complex, we moeten de scope nog verder limiteren. Laten we de zoektermen limiteren tot het woord 'data'.
>
> Dus twee wireframes, 1 voor burger, 1 voor onderzoeker, beide kunnen enkel de zoekterm 'data' gebruiken. Zodat we de wireframes kunnen demonstreren en dit lokaal opslaan. Dit hoort het project aanzienlijk te simplificeren en toch binen de userstories valt.
>
> De data is dus fictief ter voorbeeld. Dus geen echte API maar dummy data. Dus we richten ons op de userstories en wireframes and fictieve zoekresulten ter illustratie terwijl we wel aan de userstories voldoen.
>
> Dit hoort relatief simpel te zijn.

**Prompt S4-16 — 2026-11-10 14:08:58**

> Ja, enkel het moet wel in tkinter GUI voor de 2 wireframes volgens de documentatie in LU3.

- **AI-bijdrage:** De demo eerst als twee lokale HTML-wireframes gemaakt en
  na de expliciete correctie vervangen door twee schermen in één Tkinter-app.
- **Eigen keuze:** De gebruiker beperkte de zoekterm tot `data`, koos expliciet
  fictieve resultaten zonder API en verduidelijkte dat beide wireframes in
  Tkinter moesten worden gebouwd. De twee deels herhaalde scopeberichten zijn
  afzonderlijk bewaard omdat het tweede bericht aanvullende eisen bevat.
- **Controle/uitkomst:** De sessie meldde twee geslaagde Tkinter-tests,
  waaronder schermwisseling. De huidige beperking is beschreven in
  [IMPLEMENTATIE.md](IMPLEMENTATIE.md): de stories worden visueel getoond,
  maar zoek-, filter-, analyse- en exportacties zijn niet functioneel gebouwd.
  De wens in de prompt om aan alle stories te voldoen is dus geen bewijs van
  daadwerkelijke functionele conformiteit.

### 2026-11-10 — eenvoudige lokale SQLite-opslag

**Prompt S4-17 — 2026-11-10 14:14:44**

> Hoe kunnen we hier een simpele database toepassen voor het opslaan van de csv of vergelijkbaar? Suggesties?

**Prompt S4-18 — 2026-11-10 14:15:24**

> Okee, bouw dit en hou het simpel en overzichtelijk

- **AI-bijdrage:** SQLite voorgesteld en een opslagknop voor fictieve records
  toegevoegd, inclusief laden bij een volgende start en uitsluiting van het
  databasebestand via `.gitignore`.
- **Eigen keuze:** Na het voorstel expliciet opdracht gegeven dit eenvoudig
  en overzichtelijk te bouwen.
- **Controle/uitkomst:** De sessie meldde vier geslaagde tests, syntaxcontrole
  en handmatige opslag-/herlaadcontrole. Tijdens die controles zijn niet
  gesloten databaseverbindingen en een verouderde testverwachting hersteld.
  De testbestanden zijn later op verzoek verwijderd.

### 2026-11-10 — project en tests opruimen

**Prompt S4-19 — 2026-11-10 14:21:27**

> Schoon het project op, scripts en files die niet essentieel zijn dus

**Prompt S4-20 — 2026-11-10 15:05:08**

> Volgens mij hebben we de test scripts ook niet nodig?

- **AI-bijdrage:** Ponytail-hulpmiddelen, caches en lege restmappen verwijderd.
  Daarna ook de testscripts en hun README-instructie verwijderd.
- **Eigen keuze:** De gebruiker vroeg om alleen essentiële bestanden te
  behouden en gaf vervolgens aan de testscripts niet nodig te vinden.
- **Controle/uitkomst:** Vóór het verwijderen van de tests meldde de sessie
  vier geslaagde tests; daarna alleen een syntaxcontrole. De app,
  SQLite-demo en LU3-/LU4-documenten zijn behouden.

### 2026-11-10 — artifacts en het databasebestand uitleggen

**Prompt S4-21 — 2026-11-10 15:07:22**

> Wat zijn artifacts?

**Prompt S4-22 — 2026-11-10 15:09:40**

> database staat erin als een .db die we niet kunnen openen. Leg uit hoe de db werkt, en welke db

- **AI-bijdrage:** Het begrip artifact uitgelegd en de SQLite-werking
  beschreven: één `documents`-tabel, zes velden, opslaan/overschrijven en laden
  bij starten. README en implementatienotitie verduidelijkt.
- **Eigen keuze:** Gevraagd om uitleg van de gebruikte bestanden en database,
  omdat het `.db`-bestand niet als gewone tekst leesbaar was.
- **Controle/uitkomst:** Uitleg vergeleken met de opslagcode. Er is geen
  bevestiging vastgelegd dat de gebruiker een externe SQLite-viewer gebruikte.

### 2026-11-10 — huidige demo toetsen aan LU3

**Prompt S4-23 — 2026-11-10 15:11:51**

> Voldoen wij aan de specificaties van LU3? Wat moet er nog gebeuren? Maak een samenvatting

- **AI-bijdrage:** De wireframe-demo met de LU3-baseline vergeleken en
  ontbrekende functionaliteit, gebruikersfeedback en reflectie benoemd.
- **Eigen keuze:** Expliciet gevraagd wat nog nodig was in plaats van alleen
  af te gaan op de visuele aanwezigheid van beide schermen.
- **Controle/uitkomst:** De documentvergelijking onderscheidde ontwerp van
  realisatie: de huidige demo is geen volledige functionele implementatie.
  Voor LU3 blijven uitgevoerde feedback en eigen reflectie nodig; voor LU4
  zijn onder meer de ontbrekende werking en toetsingsbewijzen relevant.

### 2026-11-10 — Git-conflict oplossen en publiceren

**Prompt S4-24 — 2026-11-10 15:20:33**

> Git doesnt allow to update

**Keuzeantwoord K4 (S4) — 2026-11-10 15:21:25**

> main_py: keep_local
> incoming_files: scripts_only

**Keuzeantwoord K5 (S4) — 2026-11-10 15:26:19**

> push_now: true

- **AI-bijdrage:** Een branch met zowel een lokale als inkomende commit en
  een conflict op `main.py` onderzocht, het conflict opgelost en gepusht.
- **Eigen keuze:** Via K4 de lokale PolicyLens-app behouden, de Python-
  oefenscripts toegevoegd en Word-lockbestanden uitgesloten. Via K5 expliciet
  toestemming gegeven de opgeloste wijzigingen naar GitHub te pushen.
- **Controle/uitkomst:** Merge `44d299f` is zichtbaar in Git. De sessie meldde
  daarna een branch die gelijkliep met `origin/master`.

### 2026-11-10 — GenAI-logboek toevoegen

**Prompt S4-25 — 2026-11-10 15:31:01**

> Laten we alle AI-prompts gedurende deze repo bijhouden in een apart document in repo zodat we gebruik gen-AI kunnen inzien bij reflectie. Wat stel je voor?

**Prompt S4-26 — 2026-11-10 15:31:52**

> Okee, voeg het document toe;

- **AI-bijdrage:** Dit document, een invulformat en een README-link toegevoegd.
  De eerste versie bevatte 23 prompts en onvolledige dateringen.
- **Eigen keuze:** De gebruiker wilde GenAI-gebruik kunnen terugzien bij de
  reflectie en gaf opdracht het afzonderlijke document toe te voegen.
- **Controle/uitkomst:** De eerste versie is terug te vinden in commit
  `19fe2a1`. De huidige controle vult de toen ontbrekende bronnen en prompts
  aan, zonder eerdere samenvattingen als nieuw bewijs te behandelen.

### 2026-11-10 — logboek committen en ontbrekende push

**Prompt S4-27 — 2026-11-10 15:33:46**

> Commit changes met beschrijving

**Prompt S4-28 — 2026-11-10 15:42:40**

> De github repo lijkt niet geupdate te zijn ondanks de commit?

- **AI-bijdrage:** README en logboek gecommit als `19fe2a1` met beschrijving
  `Document GenAI prompts and reflection choices`. Na de vervolgvraag de
  lokale commit ook naar GitHub gepusht.
- **Eigen keuze:** Eerst expliciet om een commit gevraagd en daarna gemeld
  dat de GitHub-repository nog niet bijgewerkt leek.
- **Controle/uitkomst:** De sessie onderscheidde een lokale commit van een
  push; na het pushen liep `master` gelijk met `origin/master` op `19fe2a1`.

### 2026-11-11 — project controleren bij starten

**Prompt S5-01 — 2026-11-11 18:12:03**

> start codex

- **AI-bijdrage:** De bestaande demo met de implementatienotitie vergeleken,
  database-opslag/laden gecontroleerd en tijdelijke Word-lockbestanden opgeruimd.
- **Eigen keuze:** De enige gebruikersprompt in deze sessie was `start codex`;
  de overige controle- en opruimacties kwamen van de AI.
- **Controle/uitkomst:** De sessie meldde geslaagde opslag-/laadcontroles.
  Git-checkpoint `d8f17ed` toont de verwijdering van twee Word-lockbestanden.
  Dit is een historisch verslag van die sessie, geen nieuwe opdracht.

### 2026-11-11 — begrijpen of de lokale branch actueel is

**Prompt S6-01 — 2026-11-11 18:14:35**

> How to see if my current project is up to date with the associated repo?

**Prompt S6-02 — 2026-11-11 18:16:04**

> do I automatically pull the repo or is it done manually

**Prompt S6-03 — 2026-11-11 18:16:39**

> right so how do I know im up to date with the master or w/e its called

- **AI-bijdrage:** De remote en trackingbranch gecontroleerd,
  `git fetch origin` uitgevoerd en het verschil tussen fetch, pull en status uitgelegd.
- **Eigen keuze:** De gebruiker vroeg hoe updates gecontroleerd worden en of
  pull automatisch gebeurt; er is geen opdracht gegeven een pull uit te voeren.
- **Controle/uitkomst:** Na fetch waren er nul commits vóór of achter
  `origin/master`, op `19fe2a1`, en was de werkmap schoon. Voor handmatig
  bijwerken is `git pull --ff-only` uitgelegd. Dit is de status ten tijde van
  die controle, vóór de huidige wijziging aan dit logboek.

### 2026-11-11 — volledigheid van dit promptlog controleren

**Prompt S6-04 — 2026-11-11 18:18:03**

> Can we put all AI related prompts int GENAI-LOG.md? I believe we're missing prompts during this project. Verify and update me

- **AI-bijdrage:** Projectbestanden, Worddocumenten, Git-geschiedenis en lokale
  sessiebronnen onderzocht; de 47 teruggevonden prompts en vijf vastgelegde
  keuzeantwoorden centraal opgenomen met datum/tijd en bronverwijzing.
- **Eigen keuze:** De gebruiker vroeg expliciet alle AI-gerelateerde prompts
  in dit bestand te verzamelen en de vermoedelijke omissies te controleren.
- **Controle/uitkomst:** De 47 promptteksten en vijf keuzeantwoorden zijn per
  ID met de lokale bronnen vergeleken op inhoud, aantal en unieke opname.
  De wijzigingen betreffen alleen dit logboek; er zijn geen applicatietests
  opnieuw uitgevoerd. De grenzen van de beschikbare geschiedenis staan in
  de volledigheidscontrole bovenaan.

### 2026-11-11 — main.py regel voor regel begrijpen en zelf herschrijven

**Prompt S6-05 — 2026-11-11 19:27:34**

> explain the main.py code line by line so I can re-write and understand the code myself.

- **AI-bijdrage:** De 184 regels van de huidige hoofdapplicatie gelezen en
  uitgelegd hoe de imports, voorbeeldgegevens, SQLite-functies, Tkinter-klasse,
  widgets, callbacks en programmastart samenwerken.
- **Eigen keuze:** De gebruiker wil de code zelf kunnen herschrijven en
  begrijpen, en vraagt daarom om uitleg per regel.
- **Controle/uitkomst:** De uitleg is gebaseerd op de huidige `main.py` in de
  projecthoofdmap. Applicatiecode is niet gewijzigd en er zijn geen
  applicatietests uitgevoerd; deze taak betreft uitleg en registratie.
### 2026-11-11 — hoofdstukken uit twee leerboeken koppelen aan main.py

**Prompt S6-06 — 2026-11-11 19:40:31**

> Which chapters in Python Crash Course 3th edition and \
> **Python GUI Programming with Tkinter - Second Edition**   explain how to build the code in main.py

- **AI-bijdrage:** De inhoudsopgaven van Python Crash Course (3e editie) en
  Python GUI Programming with Tkinter (2e editie) gecontroleerd en relevante
  hoofdstukken gekoppeld aan de Python-basis, widgets, callbacks, klassen,
  Treeview-tabellen en databasefuncties in `main.py`.
- **Eigen keuze:** De gebruiker wil de applicatie zelf leren bouwen met deze
  twee boeken en vraagt welke hoofdstukken daarvoor nodig zijn.
- **Controle/uitkomst:** De Python-basis past bij PCC-hoofdstukken 2–6 en
  8–10; de GUI vooral bij Tkinter-hoofdstukken 1, 3, 4 en 8. Appendix B behandelt
  SQL-basiskennis. Hoofdstuk 12 gebruikt PostgreSQL/psycopg2; voor de gebruikte
  SQLite-aanroepen en `contextlib.closing` is aanvullende Python-documentatie
  nodig. Bronnen: [PCC-inhoudsopgave](https://nostarch.com/download/PCC3e_detailedTOC.pdf),
  [Tkinter-inhoudsopgave van de uitgever](https://leanpub.com/pythonguiprogrammingwithtkinter-secondedition),
  [databasehoofdstuk](https://subscription.packtpub.com/book/programming/9781801815925/12/ch12lvl1sec63/connecting-to-postgresql-with-psycopg2),
  [sqlite3](https://docs.python.org/3/library/sqlite3.html) en
  [contextlib.closing](https://docs.python.org/3/library/contextlib.html#contextlib.closing).
  Alleen het logboek is bijgewerkt; de applicatiecode is ongewijzigd.
