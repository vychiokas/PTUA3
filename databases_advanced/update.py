from main import Project
from session import session


# project1 = session.query(Project).get(1)
# project1.price = 22000
# session.commit()

project1 = session.query(Project).filter_by(name="New Project 2").one()
project1.name = "Not so New Project 2"
session.commit()
