# MODULE
# radacina patrata a unui nr
print(25**0.5)

import math # ne folosim de libraria math
print(math.sqrt(25))

# sinus

print(math.sin(2))

# Ce fisiere am intr-un folder
import os # os adica Operation System

path = "C:\Users\ancas\Desktop"
# https://pathcopycopy.github.io/

print(r"ceva\aici\nu\e\bine")
print(os.listdir(path))

# In python sunt module built-in, adica care nu trebuie instalate
# de exemplu math, os, statistics

# import statistics

from statistics import mean
print(mean([1,2,3,4]))

import math # importa toata libraria, astfel putem folosi toate metodele/functiile din librarie
print(math.factorial(5))

from math import factorial #import o singura functie din librarie

from math import factorial as fact
# as fact inseamna ca am redenumit functia, alias
print(fact(5))

from math import *  # * inseamna everyting; CODE SMELL - importa toate functiile si incarca memoria cu ele; nu este ok

import time
print(7)
time.sleep(3)
# pune codul pe pauza 3 secunde
print(9)



import time
def functie_complicata():
    print(7)
    time.sleep(3)
    print(9)
time_start = time.perf_counter() # performance counter
functie_complicata()
time_took = time.perf_counter() - time_start
print(f"Operatiunea a durat {time_took} secunde")

# datetime - zile, luni, ani; putem afla timpul de acum

import datetime
acum = datetime.datetime.now()
print(acum)
print(acum.year)
print(acum.month)
print(acum.minute)

format_1 = acum.strftime("%Y-%B-%d")
print(format_1)
format_2 = acum.strftime("%d-%m-%y")
print(format_2)

#Tabel de formatare zile https://www.w3schools.com/python/python_datetime.asp
# documentatie oficiala datetime https://docs.python.org/3/library/datetime/html


# identare inseamna cand esti pe randul urmatorul in cuprinsul conditiei

# cum import foldere
# creez folder sda_52

main_path = 'C:/Users/ancas/Desktop'  # sa schimb sleshurile
import os
sda_52 = f"{main_path}/sda_52"   # acesta este path-ul
os.mkdir(sda_52)

# Creez un fisier txt in care scriu text_1
text_1 = "Afara este frumos, dar noi invatam programare!"
operatiunea_scriere = "w"
with open(f"{sda_52}/primul_fisier.txt", operatiunea_scriere) as filex:
    #filex este un alias la operatiunile pe care le facem cu fisierul
    filex.write(text_1)

studenti = ["Andrei", "Ana", "Maria"]
fisier_studenti = "studentii_mei.txt"
with open(f"{sda_52}/{fisier_studenti}", operatiunea_scriere) as f:
    for nume in studenti:
        f.write(f"{nume}\n")  # \n inseamna ca imi listeaza pe randul urmator

studenti_2 = ["Ion", "Elena", "Ioana"]
operatiunea.append = "a"
with open(f"{sda_52}/{fisier_studenti}", operatiunea_append) as f:
    for nume in studenti_2:
        f.write(f"{nume}\n")


# Fisiere excel
# vom instala o librarie  externa numita pandas
# in terminal vom scrie pip install pandas
# pip e o comanda care instaleaza librarii externe(mai multe la python technologies


stundenti = {"prenume": ["Elena", "Ana", "Ion"],
             "varsta": [23, 39, 20],
             "localitate": ["Brasov", "Timisoara", "New York"]}
nume_excel = "studentii_mei.xlsx"    # am definit excelul
import pandas
tabel = pandas.DataFrame(stundenti)
print(tabel)

tabel.to.excel(f"{SDA_52}/{nume_excel}", index=False)

# Citire in excel

tabel_citit = pandas.read_excel(f"{SDA_52}/{nume_excel}")
print(tabel_citit)

loc = tabel_citit["localitate"].tolist()


# daca vreau sa citesc un sheet anume din excel
tabel_grupa_42 = pandas.read_excel(f"{SDA_52}/{nume_excel}", sheet-name="grupa_42")
print(tabel_grupa_42)