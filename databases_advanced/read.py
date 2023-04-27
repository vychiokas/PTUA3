from main import Project
from session import session

project = session.query(Project).first()

print(project)


# project = session.query(Project).filter_by(name="New Project 2").first()

# print(project)
