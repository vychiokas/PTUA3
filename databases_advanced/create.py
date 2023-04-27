from main import Project
from session import session


project1 = Project("New Project 1", 20000)
session.add(project1)
session.commit()

project2 = Project("New Project 2", 55000)
session.add(project2)
session.commit()
