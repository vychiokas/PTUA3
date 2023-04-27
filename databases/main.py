import sqlite3

conn = sqlite3.connect("my_app.db")
c = conn.cursor()

with conn:
    c.execute(
        """CREATE TABLE IF NOT EXISTS
    darbuotojai (
    vardas text,
    pavarde text,
    atlyginimas integer
    )"""
    )

while True:
    print("Įveskite darbuotoją")
    vardas = input("Vardas: ")
    pavarde = input("Pavarde:")
    atlyginimas = int(input("atlyginimas :"))

    with conn:
        c.execute(
            f"INSERT INTO darbuotojai VALUES ('{vardas}', '{pavarde}', {atlyginimas})"
        )
        print(c.execute("SELECT * FROM darbuotojai").fetchall())
