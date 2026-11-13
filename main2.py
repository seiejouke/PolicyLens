"""Twee stakeholders met eigen wireframes met
dummy-data ter demonstratie van de applicatie"""

# Importeren van bibliotheken

import sqlite3 # database
import tkinter as tk # GUI 

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
            "SELECT title, subject, data, kind, document_id, number FROM documents ORDER BY id"
        ).fetchall()

def save_documents(documents, path=DATABASE):
    with closing(sqlite3.connect(path)) as database, database:
        database.execute(
            "CREATE TABLE IF NOT EXISTS documents ("
            "id INTEGER PRIMARY KEY, title TEXT, subject TEXT, data TEXT, "
            "kind TEXT, TEXT, document_id TEXT, number TEXT"
        )
        database.execute

