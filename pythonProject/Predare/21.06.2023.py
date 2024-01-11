#Comprehension

nume = ["Ion", "Vasile", "Elena", "Ana"]
#creati o lista cu numele in CAPS
#v1
nume_CAPS = []
for n in nume:
    nume_CAPS.append(n.upper())
print(nume_CAPS)

#v2  - list comprehension, o solutie pe o singura linie
nume_CAPS = [n.upper() for n in nume]
print(nume_CAPS)

"""
Sintaxa list comprehension, fara conditii
lista = [element_procesat for element in alta lista]
"""

nume = ["Ion", "Vasile", "Elena", "Ana"]
# Creaza o lista doar cu nume ce au lungimea de 3 caractere
#v1
nume_3 = []
for n in nume:
    if len(n) == 3:
        nume_3.append(n)

print(nume_3)

#v2 cu list comprehension
nume_3_v2 = [n for n in nume if len(n) == 3]
print(nume_3_v2)

"""
Sintaxa list comprehension, cu conditii
lista = [element_procesat for element in alta lista  if conditie]
"""

prenume = ["Ion", "Vasile", "Elena", "Ana", "Bo", "Jan", "Bob"]
# Adaugati acelasi nume de familie(ex Ionescu) la fiecare prenume, pt ca sunt din aceeasi familie

nume_prenume = [f"{n} Ionescu" for n in prenume]
print(nume_prenume)


#Creati o lista cu patratele fiecarui numar de la 5 la 15 inclusiv
#v1 clasica
lista_patrate = []
for n in range(5,16):
    lista_patrate.append(n**2)
print(lista_patrate)

#v2 comprehension
lista_patrate_v2 = [n**2 for n in range(5,16)]
print(lista_patrate_v2)
# list comprehension este o solutie eleganta pentru implementari simple
# Nu se recomanda list comprehension pentru solutii complexe


prenume = ["Ion", "Vasile", "Elena", "Ana", "Bo", "Jan", "Bob"]
# Creati o alta lista cu numele ce nu contin litera b sau j
prenume_filtrat = [n for n in prenume if "b" not in n.lower() and "j" not in n.lower()] # jan, bob
# O lungime aproximativ maxima acceptata pentru ca list comprehension sa fie considerata o solutie eleganta
print(prenume_filtrat)

# Dict comprehension
# Construiesc un dictionar cu numarul si patratul lui, de la 20 la 28
# v1
dx = dict()
for n in range(20, 29):
    dx[n] = n**2
print(dx)

# v 2
dx_v2 = {n: n**2 for n in range(20, 29)}
print(dx_v2)

prenume = {"Ion", "Vasile", "Elena", "Ana", "Bo", "Jan", "Bob"}
# Creati un dictionar cu prenumele si lungimea prenumelui
#v1
dx = dict()
#SAU dx = {}
#lisx = [] - 2 metode de initializare a unei liste goale
#lisx = list()

for n in prenume:
    dx[n] = len(n)
print(dx)

#v2 dictionar comprehension
dx_v2 = {n : len(n) for n in prenume}
print(dx_v2)

#tuple comprehension
# Creez un tuple cu cuburile numerelor de la 3 la 9
lisx = [x**3 for x in range(3,10)]
tupx = tuple(x**3 for x in range(3,10)) # <generator object <genexpr> at 0x0000014EAC8C35E0>
# Adica a stocat logica elementelor, nu si elemnetele propriu-zise
tupx = tuple(x**3 for x in range(3,10)) # Am extras toate elemntele din generator
print("list = ", lisx)
print("tuple = ", tupx)

#Set comprehension
# Genereaza un set cu toate cuvintele unice din acest text, case-insensitive
strx = "Afara ploua, dar cine a mai fost afara"
print(strx.split())  # ['Afara', 'ploua,', 'dar', 'cine', 'a', 'mai', 'fost', 'afara']
setx = {word.lower() for word in strx.split()}
# setx = {word for word in strx.split()} # {'mai', 'afara', 'a', 'Afara', 'cine', 'fost', 'ploua,', 'dar'}
print(setx) # {'mai', 'afara', 'a', 'cine', 'fost', 'ploua,', 'dar'}
#lower transforma in lowercase
