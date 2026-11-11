import sqlite3

conn = sqlite3.connect("gegevens.db")
cursor = conn.cursor()

cursor.execute("""

