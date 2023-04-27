from models import Vaikas, Tevas
from session import session


tevas = session.query(Tevas).get(1)
vaikas = Vaikas(vardas="Sekejas 3", pavarde="Vaikaitis")

vaikas.tevas = tevas
session.add(vaikas)
session.commit()
