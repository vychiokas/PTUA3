import json

with open('example2.json', 'r') as file:
    data = json.load(file)

print(type(data))