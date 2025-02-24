# math
import math

x = math.sqrt(64)
print(x)

x = math.ceil(1.2)  # 2
print(x)

x = math.floor(1.2)  # 1
print(x)

import random

r = random.randint(1, 6)
print(r)

r = random.random()  # decimale tra 0 e 1
print(r)

lista = ["MO", "BO", "RM", "PA", "PM"]
r = random.choice(lista)

# alternativa al choice (ma anche no)
r = lista[random.randint(0, len(lista) - 1)]

lista = [1, 2, 3, 4, 5, 6, 7, 8]
print(lista)

random.shuffle(lista)
print(lista)

# json
import json

# da json (str) a python (list o dict)
x = '{ "name": "John", "age":30, "city": "New York"}'
print(type(x))

y = json.loads(x)
print(type(y))
print(y["name"])

x = '[{ "name": "John", "age":30, "city": "New York"}, { "name": "Rob", "age":33, "city": "New York"}]'
y = json.loads(x)
print(type(y))

# da python (list o dict) a json (str)
x = {"marca": "Ford", "modello": "Fiesta", "anno": 1985}
y = json.dumps(x)
print(type(y))

# requests
import requests

resp = requests.get("https://jsonplaceholder.typicode.com/posts")

if resp.status_code == 200:
    body = resp.text

    with open("articoli.json", "wt") as f:
        f.write(body)

    posts = resp.json()

    print(posts[1]["title"])

# altra request per scaricare un'immagine
resp = requests.get(
    "https://cdn-imgix.headout.com/media/images/c90f7eb7a5825e6f5e57a5a62d05399c-25058-BestofParis-EiffelTower-Cruise-Louvre-002.jpg?auto=format&w=1051.2&h=540&q=90&fit=fit"
)

if resp.status_code == 200:
    with open("eiffel.jpg", "wb") as f:
        f.write(resp.content)

# d&D charisma
resp = requests.get("https://www.dnd5eapi.co/api/2014/ability-scores/cha")

for s in resp.json()["skills"]:
    print(s["name"])
