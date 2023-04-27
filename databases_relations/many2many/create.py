from models import Vaikas, Tevas
from session import session

tevas1 = Tevas(vardas="Tėvas", pavarde="Tėvaika")
motina = Tevas(vardas="Motina", pavarde="Tevienė")
vaikas1 = Vaikas(vardas="Vaikas", pavarde="Tėvaika")
vaikas2 = Vaikas(vardas="Vaikė", pavarde="Tėvaikytė")

tevas1.vaikai.append(vaikas1)

motina.vaikai.append(vaikas1)
motina.vaikai.append(vaikas2)

session.add(tevas1)
session.add(motina)
session.commit()
