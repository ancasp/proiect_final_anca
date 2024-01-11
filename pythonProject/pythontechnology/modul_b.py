# prima metoda de import
#from pythontechnology import modul_a
# importam un modul "cu totul"

#print(modul_a.test)
#courses = ["PE", "History", "Math"]
#index = modul_a.find_index(courses, "PE")
#print(index)

# a doua metoda de import

# import modul_a as ma
# importam un modul "cu totul" si ii punem si un alias

# print(ma.test)
# courses = ["PE", "History", "Math"]
# index = ma.find_index(courses, "PE")
# print(index)

# a treia varianta de import
# # import o functie sau o variabila, clasa etc
# from modul_a import find_index
# from modul_a import test
# print(test)
# courses = ["PE", "History", "Math"]
# index = find_index(courses, "History")
# print(index)

# a patra metoda de import
#
from modul_a import *  # * inseamna ca fac import la ALL(tot)
print(test)
courses = ["PE", "History", "Math"]
index = find_index(courses, "History")
print(index)

"""Good practices

1. Importam cate un modul pe linie
import pandas
import random
from pandas import *
from tkinter import *

 - le putem importa si pe acelasi rand, de ex:
import flask, math, openpyxl, pandas

2. Este un good practices sa nu importam doar o variabila, doar o functie, doar o clasa etc. Putem importa tot modulul
de forma
from random import *

3. Daca importam mai multe module pe aceeasi linie sau unele sub altele, ar fi de preferat sa fie scrise in ordine
alfabetica. Aceeasi recomandare este si in cazul in care impoprtam dintr-un modul functii in calse, variabile.
"""

# Modulele sunt de 3 tipuri:
#  - module standard - modulele care vin instalate by default cu Python: random, math, math, os, sys etc
#  - module externe - module create de catre alti developeri; ele se descarca si instaleaza separat; nu vin in acelasi
#  timp cu Python. ex: pandas, flask, django, openpyxl, tensorflow etc
#  - module locale "in proiect" in interiorul foderului unde avem codul. ex este modul_a

# Cum foloseste Python modulele

# import modul_a
# import pandas
# import random
 # Pentru a cauta un modul Python va incepe cautarea in felul urmator:
# 1. in folderul curent
# 2. in folderul unde se afla modulele standard(cele care vin odata cu Python)
# 3. In folderul unde se afla modulele externe(cele pe care le instalam ulterior din 3rd party)

#
# import sys
# print(sys.path)
""" ['C:\\Users\\ancas\\PycharmProjects\\pythonProject\\pythontechnology', 
'C:\\Users\\ancas\\PycharmProjects\\pythonProject', 
'C:\\Users\\ancas\\AppData\\Local\\Programs\\Python\\Python311\\python311.zip', 
'C:\\Users\\ancas\\AppData\\Local\\Programs\\Python\\Python311\\DLLs', 
'C:\\Users\\ancas\\AppData\\Local\\Programs\\Python\\Python311\\Lib', 
'C:\\Users\\ancas\\AppData\\Local\\Programs\\Python\\Python311',
 'C:\\Users\\ancas\\PycharmProjects\\pythonProject\\venv', 
 'C:\\Users\\ancas\\PycharmProjects\\pythonProject\\venv\\Lib\\site-packages']
"""

import random
random.__file__

"""
'C:\\Users\\ancas\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\random.py'
"""


# __init__.py - face ca un folder cu cod pe care vrea sa il facem modul, sa fie vazut ca un modul
# fisierul  __init__.py e musai
# de regula in acest fisier gasim importuri.
# in fisierul __init__.py putem gasi cod de exemplu o functie, sau nu putem gasi nimic