from main import Project
from session import session


project1 = session.query(Project).filter_by(name="New Project 1").one()

session.delete(project1)
session.commit()
