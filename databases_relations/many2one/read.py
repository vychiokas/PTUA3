from models import Tevas, Vaikas
from session import session

vaikas = session.query(Vaikas).get(1)

print(vaikas.__table__.columns.keys())
# for tevas in vaikas.tevai:
#     print(tevas.vardas)


# tevas1 = session.query(Tevas).get(1)

# print(tevas1.vaikas.vardas)
