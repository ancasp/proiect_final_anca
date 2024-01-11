# Librariile din python
# librariile built-in

import os

path_folder = 'C:/Users/ancas/Desktop'
new_folder_name = "Iunie 29"
new_folder_path = f"{path_folder}/{new_folder_name}"
print(new_folder_path)
os.mkdir(new_folder_path)

fisiere = os.listdir(path_folder)
print(fisiere)

print(os.cpu_count()) # numarul de sub-procesoare/threads in CPU - procesorul calculatorului

help(os.listdir()) # help imi printeaza documentatia tehnica a unei librarii sau metode

import math
# factorial de 3 inseamna 1*2*3
print(math.sqrt(125))
print(math.factorial(5))

#SAU

from math import sqrt, factorial
print(math.sqrt(125))
print(math.factorial(5))

#alias la toata libraria
impport math as matematica
print(matematica.sqrt(125))

from math import sqrt as radical
from math import factorial as produsul_pana_la_n
print(radical(125))
print(produsul_pana_la_n(5))

import statistics
print(statistics.mean([2,3,4]))  # acesta este evrige

# in venv/lib/site-packages gasesc ce librarii am deja instalate

import time
#pentru a calcula performanta unui program/instructiuni folosesc perf_counter
start = time.perf_counter()
print("ana") # o instructiune banala, dar trebuie sa o punem in cod
time.sleep(1)
print(f"A durat {time.perf_counter() - start} secunde") # am scazut din time.perf_counter(adica timpul final),
# start, sa ne dea cat a durat de cand a inceput sa execute codul

import datetime
now  = datetime.datetime.now()
print(now)
print(now.year)

timp_formatat = now.strftime("%A %d-%B-%Y")
print(timp_formatat)



# w3schools.com - putem gasi modele de cum vrem sa arate formatul datei/timpului



# LIBRARII EXTERNE
# se instaleaza in terminal cu comanda pip install in Terminal(acolo unde e consola);
# pip este un sistem de instalare/management a librariilor in python


# instalam alte librarii, ex psutil pentru RAM - asta pt a afla RAM
import psutil
ram = psutil.virtual_memory()
print(ram)
ram_giga = ram[0]/2**30 #calculez in GB
print(ram_giga)

import pandas

data = {"nume_elevi": ["Ion", "Ana"],
        "materie_preferata": ["sport", "pictura"]}
tabel = pandas.DataFrame(data)
print(tabel)
path_folder = 'C:/Users/ancas/Desktop'
tabel.to_excel(f"{path_folder}/recap_excel_1.xlsx", index=False) # index = false inseamna ca nu imi afiseaza indexul in excelul creat


# pentru importuri, best practice
"""
 - se importa toate la inceputul programului
 - librariile built in si instalate se importa primele
 - apoi importam modulele, functiile, variabilele create de noi in alte fisiere
 - incercati sa importai doar ce aveti nevoie, de ex from math import factorial si nu import math
 - evitati sa importati asa: from math import *
 - etc: https://tealpython.com/python-import   -  aici gasesti info despre cum se importa
 - aliasuri:cat mai putine, de ex: from math import factorial as produs_de_la_1_la_n  
"""


"""
In python exista style guide, care face codul usor de citit, oarecum standardizat
official style guide https://peps.python.org/pep-0008/     PEP-8
google python style guide  https://google.github.io/styleguide/pyguide.html
"""


