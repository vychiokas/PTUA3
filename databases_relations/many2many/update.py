from models import Vaikas, Tevas
from session import session

tevas = session.query(Tevas).get(2)
tevas.vaikai[0].vardas = "Vaikas 1"
session.commit()
