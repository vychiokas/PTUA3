from main import Project
from session import session

search2 = session.query(Project).filter(Project.price > 1000)

# Search2 =  [Project, Project]

price_sum = 0
for project in search2:
    price_sum += project.price

print(price_sum)
