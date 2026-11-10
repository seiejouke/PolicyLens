"""Toon twee offline Tkinter-wireframes met fictieve parlementaire data."""

import sqlite3
import tkinter as tk
from contextlib import closing
from pathlib import Path
from tkinter import ttk

DATABASE = Path(__file__).with_name("policylens.db")
DOCUMENTS = (
    ("FICTIEF — Bescherming van data bij publieke diensten", "Voorbeeld over gegevensgebruik", "12-03-2026", "Brief regering", "DEMO-001", "DEMO-2026-01"),
    ("FICTIEF — Datadeling en digitale overheid", "Voorbeeld over datadeling", "04-02-2026", "Motie", "DEMO-002", "DEMO-2026-02"),
    ("FICTIEF — Gebruik van data in beleid", "Voorbeeld over beleidsdata", "19-11-2025", "Schriftelijke vragen", "DEMO-003", "DEMO-2025-03"),
)


def load_documents(path=DATABASE):
    if not path.exists():
        return []
    with closing(sqlite3.connect(path)) as database, database:
        return database.execute(
            "SELECT title, subject, date, kind, document_id, number FROM documents ORDER BY id"
        ).fetchall()


def save_documents(documents, path=DATABASE):
    with closing(sqlite3.connect(path)) as database, database:
        database.execute(
            "CREATE TABLE IF NOT EXISTS documents ("
            "id INTEGER PRIMARY KEY, title TEXT, subject TEXT, date TEXT, "
            "kind TEXT, document_id TEXT, number TEXT)"
        )
        database.execute("DELETE FROM documents")
        database.executemany(
            "INSERT INTO documents (title, subject, date, kind, document_id, number) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            documents,
        )


class WireframeDemo:
    def __init__(self, window, database_path=DATABASE):
        self.window = window
        self.database_path = database_path
        self.database_error = ""
        try:
            self.documents = load_documents(database_path) or DOCUMENTS
        except sqlite3.Error as error:
            self.documents = DOCUMENTS
            self.database_error = f"Database kon niet worden gelezen: {error}"
        window.title("PolicyLens NL — wireframe-demo")
        window.geometry("900x650")

        header = ttk.Frame(window, padding=12)
        header.pack(fill="x")
        ttk.Label(header, text="POLICYLENS NL", font=("TkDefaultFont", 18, "bold")).pack(side="left")
        ttk.Button(header, text="Burger", command=lambda: self.show("burger")).pack(side="right", padx=4)
        ttk.Button(header, text="Onderzoeker", command=lambda: self.show("onderzoeker")).pack(side="right")

        self.status = tk.StringVar()
        self.term = tk.StringVar(value="data")
        self.pages = {
            "burger": self.make_burger(window),
            "onderzoeker": self.make_researcher(window),
        }
        ttk.Label(window, textvariable=self.status, padding=10).pack(fill="x", side="bottom")
        self.show("burger")

    def make_results(self, parent, columns):
        table = ttk.Treeview(parent, columns=columns, show="headings", height=5)
        headings = {"title": "Titel / onderwerp", "date": "Datum", "kind": "Documentsoort"}
        widths = {"title": 480, "date": 130, "kind": 210}
        for column in columns:
            table.heading(column, text=headings[column])
            table.column(column, width=widths[column], anchor="w")
        for document in self.documents:
            table.insert("", "end", values=(document[0], document[2], document[3]))
        table.pack(fill="x", pady=8)
        return table

    def make_burger(self, parent):
        page = ttk.Frame(parent, padding=16)
        ttk.Label(page, text="Vind documenten", font=("TkDefaultFont", 16, "bold")).pack(anchor="w")
        ttk.Label(page, text="Zoek in titels en onderwerpen van de Tweede Kamer.").pack(anchor="w", pady=4)
        search = ttk.LabelFrame(page, text="Zoekterm", padding=10)
        search.pack(fill="x", pady=8)
        self.burger_term = ttk.Entry(
            search, textvariable=self.term, state="readonly"
        )
        self.burger_term.pack(side="left", fill="x", expand=True)
        ttk.Button(search, text="Zoeken", state="disabled").pack(side="left", padx=8)
        ttk.Label(page, text="Resultaten voor “data” · 3 getoond (maximaal 10)").pack(anchor="w")
        self.burger_results = self.make_results(page, ("title", "date", "kind"))
        detail = ttk.LabelFrame(page, text="Geselecteerd fictief document", padding=10)
        detail.pack(fill="x", pady=5)
        ttk.Label(detail, text=self.documents[0][0] + "\n12-03-2026 · Brief regering", wraplength=800).pack(anchor="w")
        ttk.Button(detail, text="Open originele bron", state="disabled").pack(anchor="w", pady=6)
        terms = ttk.LabelFrame(page, text="Gerelateerde begrippen", padding=10)
        terms.pack(fill="x")
        ttk.Label(terms, text="data · datadeling · privacy").pack(anchor="w")
        ttk.Label(terms, text="Fictieve voorbeeldbegrippen; geen frequenties.").pack(anchor="w")
        return page

    def make_researcher(self, parent):
        page = ttk.Frame(parent, padding=16)
        ttk.Label(page, text="Onderzoek parlementaire metadata", font=("TkDefaultFont", 16, "bold")).pack(anchor="w")
        search = ttk.LabelFrame(page, text="Zoekterm en filters", padding=10)
        search.pack(fill="x", pady=8)
        row = ttk.Frame(search)
        row.pack(fill="x")
        self.research_term = ttk.Entry(
            row, textvariable=self.term, state="readonly"
        )
        self.research_term.pack(side="left", fill="x", expand=True)
        ttk.Button(row, text="Zoeken", state="disabled").pack(side="left", padx=6)
        filters = ttk.Frame(search)
        filters.pack(fill="x", pady=8)
        ttk.Label(filters, text="Vanaf (JJJJ-MM-DD)").pack(side="left")
        ttk.Entry(filters, width=14, state="disabled").pack(side="left", padx=4)
        ttk.Label(filters, text="Tot").pack(side="left")
        ttk.Entry(filters, width=14, state="disabled").pack(side="left", padx=4)
        ttk.Label(filters, text="Documentsoort").pack(side="left")
        ttk.Combobox(filters, width=18, state="disabled", values=("Alle soorten",)).pack(side="left", padx=4)
        ttk.Button(filters, text="Toepassen", state="disabled").pack(side="left")

        ttk.Label(page, text="3 fictieve records zichtbaar uit 3 opgehaald (maximaal 25)").pack(anchor="w")
        self.research_results = self.make_results(page, ("title", "date", "kind"))
        body = ttk.Frame(page)
        body.pack(fill="both", expand=True, pady=5)
        details = ttk.LabelFrame(body, text="Bronmetadata", padding=8)
        details.pack(side="left", fill="both", expand=True, padx=(0, 8))
        ttk.Label(
            details,
            text="Titel: Bescherming van data bij publieke diensten\n"
                 "Onderwerp: Fictief voorbeeld over gegevensgebruik\n"
                 "Datum: 12-03-2026    Soort: Brief regering\n"
                 "ID: VOORBEELD-001    Nummer: DEMO-2026-01\n"
                 "Bronlink: niet beschikbaar",
            justify="left", wraplength=430,
        ).pack(anchor="w")
        analysis = ttk.LabelFrame(body, text="App-analyse · voorbeeld", padding=8)
        analysis.pack(side="left", fill="both", expand=True)
        ttk.Label(analysis, text="Begrip                         Aantal\n"
                                 "data                                  3\n"
                                 "datadeling                      1\n"
                                 "privacy                             1",
                  justify="left", font=("TkFixedFont", 10)).pack(anchor="w")
        ttk.Label(analysis, text="Hele woorden in titel en onderwerp; hoofdletterongevoelig.",
                  wraplength=350).pack(anchor="w", pady=6)
        ttk.Button(analysis, text="Exporteer CSV", state="disabled").pack(anchor="w")
        ttk.Button(analysis, text="Bewaar voorbeelddata lokaal", command=self.save_samples).pack(anchor="w", pady=6)
        history = ttk.LabelFrame(page, text="Recente zoektermen · lokaal", padding=8)
        history.pack(fill="x")
        ttk.Combobox(history, state="disabled", values=("data",), width=20).pack(side="left")
        ttk.Button(history, text="Herhalen", state="disabled").pack(side="left", padx=4)
        ttk.Button(history, text="Wissen", state="disabled").pack(side="left")
        return page

    def save_samples(self):
        try:
            save_documents(DOCUMENTS, self.database_path)
            self.documents = load_documents(self.database_path)
            self.status.set(f"{len(self.documents)} fictieve records opgeslagen in {self.database_path.name}.")
        except sqlite3.Error as error:
            self.status.set(f"Opslaan mislukt: {error}")

    def show(self, name):
        for page in self.pages.values():
            page.pack_forget()
        self.pages[name].pack(fill="both", expand=True)
        self.status.set(self.database_error or
            f"{name.title()}-wireframe · vaste zoekterm “data” · "
            "fictieve voorbeeldgegevens; bediening is alleen ter illustratie."
        )


def main():
    window = tk.Tk()
    WireframeDemo(window)
    window.mainloop()


if __name__ == "__main__":
    main()
