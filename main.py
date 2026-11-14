"""Klikbaar LU3-prototype; fictieve data, zonder API."""
import re
import sqlite3
import tkinter as tk
from contextlib import closing
from datetime import date, datetime
from pathlib import Path
from tkinter import messagebox, ttk

DATABASE = Path(__file__).with_name("policylens.db")
FIELDS = ("Titel", "Onderwerp", "Datum", "Soort", "ID", "Nummer")
TERMS = ("data", "datadeling", "privacy", "overheid", "beleid")
DOCUMENTS = (
    ("FICTIEF — Bescherming van data bij publieke diensten", "Voorbeeld over gegevensgebruik", "12-03-2026", "Brief regering", "DEMO-001", "DEMO-2026-01"),
    ("FICTIEF — Datadeling en digitale overheid", "Voorbeeld over datadeling", "04-02-2026", "Motie", "DEMO-002", "DEMO-2026-02"),
    ("FICTIEF — Gebruik van data in beleid", "Voorbeeld over beleidsdata", "19-11-2025", "Schriftelijke vragen", "DEMO-003", "DEMO-2025-03"),
)


def save_documents(documents):
    try:
        with closing(sqlite3.connect(DATABASE)) as database, database:
            database.execute("CREATE TABLE IF NOT EXISTS documents (id INTEGER PRIMARY KEY, title TEXT, subject TEXT, date TEXT, kind TEXT, document_id TEXT, number TEXT)")
            database.execute("DELETE FROM documents")
            database.executemany("INSERT INTO documents (title, subject, date, kind, document_id, number) VALUES (?, ?, ?, ?, ?, ?)", documents)
        messagebox.showinfo("Opgeslagen", f"{len(documents)} fictieve records opgeslagen in {DATABASE.name}.")
    except sqlite3.Error as error:
        messagebox.showerror("Opslaan mislukt", str(error))


def make_page(notebook, name, documents, term, scenario):
    researcher = name == "Onderzoeker"
    page = ttk.Frame(notebook, padding=12)
    notebook.add(page, text=name)
    status, details, analysis = (tk.StringVar() for _ in range(3))
    filters = {label: tk.StringVar(value=value) for label, value in (("Vanaf", ""), ("Tot", ""), ("Soort", "Alle soorten"))}

    def selected(event=None):
        selection = table.selection()
        if not selection:
            return details.set("Selecteer een document.")
        document = table.item(selection[0], "values")
        fields = zip(FIELDS, document) if researcher else ((FIELDS[i], document[i]) for i in (0, 2, 3))
        details.set("\n".join(f"{field}: {value or 'Niet beschikbaar'}" for field, value in fields) + "\nBronlink: niet beschikbaar (fictief).")

    def search(remember=True):
        table.delete(*table.get_children())
        details.set("Selecteer een document.")
        analysis.set("")
        query = term.get().strip()
        if len("".join(query.split())) < 2:
            return status.set("Vul minstens twee zichtbare tekens in en klik op Zoeken.")
        if scenario.get() in ("Laden", "Netwerkfout"):
            return status.set("Even geduld: laden (demo)." if scenario.get() == "Laden" else f"Geen verbinding (demo). {'Klik op Opnieuw proberen.' if researcher else 'Probeer het opnieuw met de knop bovenaan.'}")
        found = sorted((doc for doc in documents if query.casefold() in f"{doc[0]} {doc[1]}".casefold()), key=lambda doc: datetime.strptime(doc[2], "%d-%m-%Y"), reverse=True)[:25]
        visible = found[:10]
        if researcher:
            try:
                start = date.fromisoformat(filters["Vanaf"].get()) if filters["Vanaf"].get() else date.min
                end = date.fromisoformat(filters["Tot"].get()) if filters["Tot"].get() else date.max
                if start > end:
                    raise ValueError
            except ValueError:
                return status.set("Gebruik JJJJ-MM-DD; Vanaf moet vóór of gelijk aan Tot liggen.")
            visible = [doc for doc in found if start <= datetime.strptime(doc[2], "%d-%m-%Y").date() <= end and filters["Soort"].get() in ("Alle soorten", doc[3])]
            if remember:
                history.configure(values=([query] + [value for value in history["values"] if value != query])[:5])
                history.set(query)
        if scenario.get() == "Geen resultaten":
            visible = []
        for document in visible:
            table.insert("", "end", values=document)
        filter_text = " | ".join(f"{label}: {value.get() or 'alle datums'}" for label, value in filters.items()) if researcher else "Geen onderzoeksfilters"
        empty = "Geen resultaten. " + ("Pas de zoekterm of filters aan." if researcher else "Probeer een andere zoekterm.")
        status.set(f"{len(visible)} zichtbaar uit {len(found)} voorbeeldrecords (max. {25 if researcher else 10}). {filter_text}" if visible else empty)
        words = re.findall(r"\w+", " ".join(f"{doc[0]} {doc[1]}" for doc in visible).casefold())
        counts = " · ".join(f"{word}: {words.count(word)}" for word in TERMS)
        analysis.set("App-analyse (fictieve metadata): " + counts + "\nHele woorden, hoofdletterongevoelig; titel + onderwerp van de zichtbare set." if researcher else "Verwante begrippen uit titel/onderwerp: " + (" · ".join(word for word in TERMS if word in words) or "geen"))
        if visible:
            table.selection_set(table.get_children()[0])
            selected()

    def action(label):
        if label == "Herhalen":
            term.set(history.get())
            search()
        elif label == "Wissen":
            history.configure(values=())
            history.set("")
        elif label == "Open originele bron":
            messagebox.showinfo("Bron niet beschikbaar", "Dit fictieve document heeft geen bronlink. Kies een ander document." if table.selection() else "Selecteer eerst een document.")
        else:
            messagebox.showinfo("CSV-export (demo)", f"Voorbeeld: {len(table.get_children())} zichtbare records met titel, onderwerp, datum, soort, ID en bronlink.\nEr wordt geen bestand geschreven.")

    search_row = ttk.Frame(page)
    search_row.pack(fill="x")
    ttk.Label(search_row, text="Zoekterm").pack(side="left")
    entry = ttk.Entry(search_row, textvariable=term)
    entry.pack(side="left", fill="x", expand=True, padx=6)
    entry.bind("<Return>", lambda event: search())
    ttk.Button(search_row, text="Zoeken", command=search).pack(side="left")
    if researcher:
        filter_row = ttk.Frame(page)
        filter_row.pack(fill="x", pady=6)
        for label, variable in filters.items():
            ttk.Label(filter_row, text=label + (" (JJJJ-MM-DD)" if label != "Soort" else "")).pack(side="left")
            ttk.Combobox(filter_row, textvariable=variable, values=("Alle soorten",) + tuple(dict.fromkeys(doc[3] for doc in documents)) if label == "Soort" else (), state="readonly" if label == "Soort" else "normal", width=19).pack(side="left", padx=4)
        ttk.Button(filter_row, text="Toepassen", command=search).pack(side="left")
    ttk.Label(page, textvariable=status, wraplength=920).pack(anchor="w", pady=6)
    table = ttk.Treeview(page, columns=FIELDS, displaycolumns=("Titel", "Datum", "Soort"), show="headings", height=5)
    for column, width in (("Titel", 530), ("Datum", 110), ("Soort", 200)):
        table.heading(column, text=column)
        table.column(column, width=width, anchor="w")
    table.pack(fill="both", expand=True)
    table.bind("<<TreeviewSelect>>", selected)
    ttk.Label(page, textvariable=details, justify="left", wraplength=920).pack(anchor="w", pady=6)
    ttk.Button(page, text="Open originele bron", command=lambda: action("Open originele bron")).pack(anchor="w")
    ttk.Label(page, textvariable=analysis, justify="left", wraplength=920).pack(anchor="w", pady=8)
    if researcher:
        history_row = ttk.Frame(page)
        history_row.pack(fill="x")
        ttk.Label(history_row, text="Recente zoektermen (demo)").pack(side="left")
        history = ttk.Combobox(history_row, state="readonly", width=20)
        history.pack(side="left", padx=6)
        for label in ("Herhalen", "Wissen", "Exporteer CSV"):
            ttk.Button(history_row, text=label, command=lambda label=label: action(label)).pack(side="left", padx=3)
        ttk.Button(page, text="Bewaar voorbeelddata lokaal (SQLite)", command=lambda: save_documents(documents)).pack(anchor="w", pady=6)
    search()
    return search


if __name__ == "__main__":
    window = tk.Tk()
    window.title("PolicyLens NL — LU3-prototype")
    window.geometry("980x780")
    documents = DOCUMENTS
    try:
        if DATABASE.exists():
            with closing(sqlite3.connect(DATABASE)) as database:
                documents = database.execute("SELECT title, subject, date, kind, document_id, number FROM documents ORDER BY id").fetchall() or DOCUMENTS
    except sqlite3.Error as error:
        messagebox.showerror("Laden mislukt", str(error))
    term, scenario = tk.StringVar(value="data"), tk.StringVar(value="Resultaten")
    ttk.Label(window, text="Prototype · fictieve data · bronopening, CSV-export en historieopslag gesimuleerd. Een voorstel is niet vanzelf geldende wet.", wraplength=940, padding=10).pack(fill="x")
    demo_row = ttk.Frame(window, padding=(10, 0))
    demo_row.pack(fill="x")
    ttk.Label(demo_row, text="Demo-toestand").pack(side="left")
    states = ttk.Combobox(demo_row, textvariable=scenario, values=("Resultaten", "Laden", "Geen resultaten", "Netwerkfout"), state="readonly")
    states.pack(side="left", padx=6)
    notebook = ttk.Notebook(window)
    notebook.pack(fill="both", expand=True, padx=10, pady=10)
    refreshers = [make_page(notebook, name, documents, term, scenario) for name in ("Burger", "Onderzoeker")]

    def retry():
        scenario.set("Resultaten")
        refreshers[notebook.index("current")]()

    ttk.Button(demo_row, text="Opnieuw proberen", command=retry).pack(side="left")
    states.bind("<<ComboboxSelected>>", lambda event: refreshers[notebook.index("current")]())
    notebook.bind("<<NotebookTabChanged>>", lambda event: refreshers[notebook.index("current")](False))
    window.mainloop()
