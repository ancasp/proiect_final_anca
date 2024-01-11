# args, kargs

def suma_1(a, b):
    return a + b
# print(suma_1(a, b)) nu merge asa

def suma_2(*args):  # *args inseamna un nr nedeterminat de argumente
    suma = 0   # initializez intai suma
    for a in args:
        suma += int(a)
    return suma

print(suma_2(2,3, 7, 10))


def catalog(**kwargs):   # **kwargs - keyword arguments, un fel de dictionar
    for key, value in kwargs.items():
        print(f"{key} are varsta de {value}")

catalog(Ion=20, Ana=22)    # trebuie sa apelez functia


dictx = {"cheie_1":1,
        "cheie_2":True,
        "adresa": {"strada":"Unirii",
                   "nr":23}}
# pentru a accesa o valoare a dictionarului, o facem prin accesarea cheii
print(dictx["cheie_1"])
print(dictx["adresa"]["nr"])
print(dictx)


import json
print(dictx)
dictx_frumos = json.dumps(dictx, indent=2 )
print(dictx_frumos)


folder = "C:/Users/ancas\PycharmProjects"
# operatiunea de scriere a dictionarului ca strin intr-un fisier
# folderul poate fi oriunde la mine pe PC
with open(f"{folder}/exemplu_json.txt", "w") as f:
    json.dump(dictx, f)
# operatiunea de citire a unui stri g dictionar-valid
with open(f"{folder}/exemplu_json.txt", "r") as f:
    datele_citite = json.load(f)
print(datele_citite)
print(type(datele_citite))


import os
print(os.getcwd())   # printeaza current working direcctory, adica locatia unde se executa codul

#list comprehension
# creez o lista cu cuburile de la a la b

lista = []
for x in range(2, 10):
    lista.append(x**3)
print(lista)

lista_cuburi_v2 = [x**3 for x in range(2,10)]
# in varianta 2 am folosit list comprehension
print(lista_cuburi_v2)


#creez o lista cu numerele divizibile cu 7 intr-un range
lista_7 = [x for x in range(2, 100) if x % 7 == 0]
print(lista_7)

# sau
lista_7 = []
for x in range(2,100):
    if x % 7 == 0:
        lista_7.append(x)
print(lista_7)

#cream o lista cu elementele comune din alte doua liste
lista_1 = [2, 3, 4, 5, 6, 7]
lista_2 = [1, 2, 7, 8, 9]
comune = [x for x in lista_1 if x in lista_2]
# pentru fiecare element din lista 1 verific daca exista in lista 2
print(comune)

# extragem toate literele majuscule dintr-un string
sx = "Afara ploua, dar Umbrela mea e la Vasile"
majuscule = [x for x in sx if x.isupper()]
print(majuscule)

# dictionare comprehension
# cream un dictionar cu cheile numere de la a la b, iar valorile sa fie patratele sale
numere_dict = {x: x**2 for x in range(2,10)}
print(numere_dict)  # {2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# daca vreau sa adaug si pt nr pare adaug dupa range if x % 2 == 0 (restul impartirii la 2 este 0)

# creez un dictionar care imi scrie lungimea fiecarui cuvant dintr-o propozitie
sx = "Afara ploua, dar Umbrela mea e la Vasile"
print(sx.split(" "))
dict_lungime_cuv = {x: len(x) for x in sx.split (" ")}
print(dict_lungime_cuv)

# daca vreau sa unesc continutul listelor intr- o singura lista
matrice = [[1, 2, 3], [4, 5, 6], [11, 22, 33]]
flattened = [x for linie in matrice for x in linie]
print(flattened)


# break, continue, pass

for x in range(2,10):
    if x == 5:
        continue  # cand ajunge la continue, sare la urmatoarea valoare, fara a executa (printa) codul ramas
    print(x)


for x in range(2,10):
    if x == 5:
        break  # atunci cand ajunge la break, iese brusc din bucla
    print(x)

for x in range(2,10):
    if x == 5:
        pass  # cand ajunge la pass, nu face nimic; nu are nicio actiune/influenta
    # pass se foloseste pt a reveni la cod mai traziu pt ca nu face nimic
    print(x)

# functii lambda

def suma_patratelor(a, b):
    return a**2 + b*b
suma_patratelor_2 = lambda a, b: a**2 + b*b
print(suma_patratelor(3,4))
print(suma_patratelor_2(3, 4))


divizibil_23_check = lambda nr: nr % 23 == 0
print(divizibil_23_check(46))

ultimele_x_chars = lambda strx, ultimele_x : strx[len(strx) - ultimele_x:]
str_ex = "Afara ploua, dar Umbrela mea e la Vasile"
print(ultimele_x_chars(str_ex, 5))


lista = [1, 2, "abc", "salut", 3]
suma_numere_lista = lambda listx : sum([x for x in listx if isinstance(x, int)])
print(suma_numere_lista(lista))
