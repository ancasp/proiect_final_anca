# Creati 200 fisiere json cu date random
# De exemplu date de genu {"dfsh":482395, "bfiwvfhwvi":397} etc.
# Opțional: faceți asta prin două modalități.

# Metoda 1: Utilizând modulul random:
import json
import random
import os

folder = "Rezultate exercitiul 1"
os.mkdir(folder)

for i in range(1, 201):
    data = {"un_nr": random.randint(1, 100), "alt_nr": random.randint(1, 100)}
    with open(f'{folder}/nume_fisier_{i}.json', 'w') as file:
        json.dump(data, file)

print("Au fost create 200 fișiere JSON cu date aleatoare.")

# Metoda 2: Utilizând modulul Faker pentru a genera date fictive realiste:
# instalarea modulului Faker  -  pip install Faker.

import json
from faker import Faker

# Creează un obiect Faker
fake = Faker()

# Creează 200 de fișiere JSON cu date fictive realiste
for i in range(1, 201):
    data_facker = {"name": fake.name(), "email": fake.email(), "address": fake.address()}
    with open(f'{folder}/nume_fisier_v2_{i}.json', 'w') as file:
        json.dump(data_facker, file, indent=4)

print("Au fost create 200 fișiere JSON cu date fictive realiste.")

# Ambele metode vor crea 200 de fișiere JSON în directorul curent, fiecare cu date aleatoare sau fictive,
# în funcție de metoda aleasă. Fișierele vor fi numite data_1.json, data_2.json, și așa mai departe.