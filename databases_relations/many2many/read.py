from models import Vaikas, Tevas
from session import session

tevas = session.query(Tevas).get(2)
for vaikas in tevas.vaikai:
    print(vaikas.vardas, vaikas.pavarde)
