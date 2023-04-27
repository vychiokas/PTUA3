from models import Vaikas, Tevas
from session import session

# vaikas = Vaikas(
#     vardas="Vaikas", pavarde="Tevaika", mokymo_istaiga="Čiurlionio gimnazija"
# )

senas_vaikas = session.query(Vaikas).get(1)

tevas = Tevas(vardas="Trecias Tevas", pavarde="Tevaika", vaikas=senas_vaikas)
session.add(tevas)
session.commit()
