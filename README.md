# PolicyLens NL

Een lokale desktopapp in Python en Tkinter om fictieve parlementaire documenten
te zoeken. De gegevens komen uit `policylens_mock_tweede_kamer.csv`.

## Starten

Vereist Python 3.11+ met Tkinter. Voer vanuit de projectmap uit:

```powershell
python -m pip install -r requirements.txt
python policylens.py
```

## Werking en implementatie

- **Burger:** zoek in titel en onderwerp met minimaal twee tekens.
  Je ziet maximaal tien resultaten met titel, datum en documentsoort.
- **Onderzoek:** zoek met datumfilters (`dd-mm-jjjj`) en documentsoort.
  De app selecteert eerst de nieuwste 25 treffers en past daarop de filters toe.
- **Lokale opslag:** bewaar onderzoeksresultaten via TinyDB in `policy_data.json`.
  Bewaren vervangt de vorige set. Met **Laad opgeslagen data** haal je die terug,
  ook na herstart; zoekterm en filters worden bij laden niet toegepast.

De app werkt offline en realiseert een deel van het LU3-ontwerp. API-koppeling,
bronopening, gerelateerde begrippen, termtellingen, CSV-export en
zoekgeschiedenis ontbreken nog.

## Documentatie

- [LU3-ontwerp](docs/PolicyLens_NL_LU3_Ontwerp_v05_Gebruikersinterfaces.docx)
- [GenAI-logboek](docs/GENAI-LOG.md)
