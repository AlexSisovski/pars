# 1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя, сохранить JSON-вывод в файле *.json.
import requests
import json
from pprint import pprint

BASE_URL = 'https://api.github.com/'
user = 'AlexSisovski'
URL = BASE_URL + 'users/' + user + '/repos'

req = requests.get(URL)
if req.status_code == 200:
    with open('repos.json','wb') as file:
        file.write(req.content)

data = json.loads(req.text)

print('Репозитории пользователя', user + ':')
for i in range(len(data)):
    print(data[i]['name'])

