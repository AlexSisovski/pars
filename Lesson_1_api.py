#!/usr/bin/env python
# coding: utf-8

# 1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя, сохранить JSON-вывод в файле *.json.

# In[30]:


import requests
import json
from pprint import pprint


# In[31]:


BASE_URL = 'https://api.github.com/'
user = 'AlexSisovski'
URL = BASE_URL + 'users/' + user + '/repos'
URL


# In[32]:


req = requests.get(URL)


# In[64]:


if req.status_code == 200:
    with open('repos.json','wb') as file:
        file.write(req.content)


# In[65]:


data = json.loads(req.text)


# In[76]:


print('Репозитории пользователя', user + ':')
for i in range(len(data)):
    print(data[i]['name'])

