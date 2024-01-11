# Creati 200 fisiere Excel cu date random, cu o singură filă fiecare (sheet), folosind librăria pandas.
# ** vă incurajez să citiți documentația pandas, este și ăsta #skill de programator

# Pentru a crea 200 de fișiere Excel cu date aleatoare folosind biblioteca pandas în Python,
# utilizam modulul openpyxl pentru a scrie datele în fișierele Excel.

# trebuie instalate modulele pandas și openpyxl -  pip install pandas openpyxl.

import pandas as pd
import random
from openpyxl import Workbook
import os

folder = "Rezultate exercitiul 2"
os.mkdir(folder)

# Creează o funcție pentru a genera date aleatoare
def generate_random_data():
    data = {"un_nr": random.randint(1, 100), "alt_nr": random.randint(1, 100)}
    return data

# Creează 200 de fișiere Excel cu date aleatoare
for i in range(1, 200):
    data = generate_random_data()
    df = pd.DataFrame([data])

# Creează un workbook Excel și salvează DataFrame-ul în el
    workbook = Workbook()
    sheet = workbook.active
    for index, row in df.iterrows():
        sheet.append(row.tolist())

# Salvează fișierul Excel cu numele corespunzător
    excel_filename = f'{folder}/excel_{i}.xlsx'
    workbook.save(excel_filename)

print("Au fost create 200 fisiere Excel cu date aleatoare.")

# Acest cod va crea 200 de fișiere Excel în directorul curent, fiecare conținând o singură
# foaie de calcul cu date aleatoare. Fișierele vor fi numite data_1.xlsx, data_2.xlsx, și așa mai departe.