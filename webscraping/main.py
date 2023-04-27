import requests

# response = requests.get("http://google.com")
# print(response.text)

# r = requests.get('https://www.python.org/static/img/python-logo.png')
# print(r.content)
# b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x01"\x00\x00\x00R\x08\x06\x00\x00\x00\xf0\xeb\xd9\xc3\x00\x00\x00\tpHYs\x00\x00\x0b\x13......


# with open('logo.png', 'wb') as f:
#     f.write(r.content)

# response = requests.get("http://google.com/neegzistuojantis_kelias")
# print(response.status_code)
# print(response.text)


# r = requests.get('http://python.org/')
# if r.status_code not in range(400, 600):
#     print('Pavyko prisijungti! Dirbame toliau...')
# else:
#     print(f'Kažkas ne taip.. Kodas {r.status_code}')
# Kažkas ne taip.. Kodas 404



# r = requests.get('http://python.org/blabla')
# if r.ok:
#     print('važiuojam toliau!')
# else:
#     print(f'Klaida! kodas {r.status_code}')
# Klaida! kodas 404


# r = requests.get('http://python.org/')
# print(r.headers)
# {'Connection': 'keep-alive', 'Content-Length': '48981', 'Server': 'nginx', 'Content-Type': 'text/html; charset=utf-8',
# 'X-Frame-Options': 'DENY', 'Via': '1.1 vegur, 1.1 varnish, 1.1 varnish', 'Accept-Ranges': 'bytes', 
# 'Date': 'Sun, 29 Dec 2019 10:30:44 GMT', 'Age': '1447', 'X-Served-By': 'cache-iad2131-IAD, cache-bma1647-BMA', 
# 'X-Cache': 'HIT, HIT', 'X-Cache-Hits': '1, 8', 'X-Timer': 'S1577615444.011509,VS0,VE0', 'Vary': 'Cookie', 
# 'Strict-Transport-Security': 'max-age=63072000; includeSubDomains'}

# import json
# data = {'name': 'Jonas', 'lastname': 'Jonaitis'}

# r = requests.post('http://httpbin.org/post', data=data)


# response = json.loads(r.text)
# print(type(response))
# print(response["form"]["lastname"])


import json


data = '''{
  "student": [ 

     { 
        "id":"01", 
        "name": "Tom", 
        "lastname": "Price" 
     }, 

     { 
        "id":"02", 
        "name": "Nick", 
        "lastname": "Thameson",
        "status": null,
        "married": true
     } 
  ]   
}'''
data_dict = json.loads(data)


data_dict['student'][1]['name'] = 'Kyle'
for student in data_dict['student']:
    student.update({'gender':'male'})
print(data_dict)

# {'student': [{'id': '01', 'name': 'Tom', 'lastname': 'Price', 'gender': 'male'}, 
# {'id': '02', 'name': 'Kyle', 'lastname': 'Thameson', 'gender': 'male'}]}

new_json = json.dumps(data_dict, indent=2)
print(new_json)


with open('example2.json', 'w') as file:
    json.dump(data, file, indent=2, sort_keys=True)