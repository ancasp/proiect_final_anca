# pentru denumirea functiilor folosim snake_case
def adunare_numere(a, b):
    return a + b

# penntru denumirea claselor, folosim CamelCase
class AdunareNumere:
    pass

# https://peps.python.org/pep-0008/  - PEP8 sugestie de stil in python oficiale
# https://google.github.io/styleguide/pyguide.html

l_1 = [1, 2, 3]
l_2 = l_1  # shallow copy of an object, am creat doua etiche pt acelasi obiect in memorie
print(l_1 == l_2)
l_1.append(23)
print(l_1 == l_2)
print(l_1 is l_2)  # True, adica aceste doua variabile/etichete ocupa acelasi spatiu in memorie
print(id(l_1))  # accesez id-ul obiectului in memorie
print(id(l_2)) # l_1 si l_2 au acelasi id

from copy  import deepcopy
l_3 = deepcopy(l_1)
print(l_1 == l_3)
print(l_1 is l_3) # False, obiecte diferire
print(id(l_1))
print(id(l_3))

a: int = 1
a: str = "unu"  # type hints sunt mai mult info pt developeri, nu si restrictii in executarea codurilor
print(a)

def multiplicare_numar(numar: int, lista:list[float]) -> float:

    rez = 0
    for el in lista:
        rez += numar * el

    return rez
print(multiplicare_numar(2, [3.0, 4]))
print(type(3 * 3.0)) # este float
print(type(3 * 3))  # este integer

exemplu_path = "C:/Users/ancas\PycharmProjects"
print(exemplu_path)

# Operatiuni cu fisiere
folder = r"C:\Users\ancas\PycharmProjects" #raw string, nu interpreteaza caracterele precum \n

# Modul python de a scrie un path(o adresa in memoria calculatorului) este cu /
folder = "C:/Users/ancas\PycharmProjects"

# Creez un folder
import os
os.mkdir(f"{folder}/SDA_52")

text_de_scris = "Salut, ce faci?"
with open(f"{folder}/SDA_52/fisier_text_1.txt", "w") as fisier:
     fisier.write(text_de_scris)

"""
In operatiunea cu fisiere putem avea mai multe tipuri de operatii:
"r" - read
"w" - write
"a" - append
"b" - bytes
"""

a = 5
b = 6
c = 9
a, b, c = 5, 6, 9  # un fel de tuple unpaking
print(b)

# adaugare elemente in lista
list_1 = [1, 2]
print(f"Lista {list_1} are {len(list_1)} elemente")
list_1.append([4, 5])  # se adauga elementul ca un singur element
print(f"Lista {list_1} are {len(list_1)} elemente")
list_1.extend([11, 22, 33])
print(f"Lista {list_1} are {len(list_1)} elemente")

sters = list_1.pop(2) # sterge dupa index si poate stoca valoarea stearsa intr-o variabila
print(f"Elementul sters este {sters} si noua lista = {list_1}")

list_1.remove(33) # sterge dupa valoare
print(list_1)

lis_2 = [11, 22, 33, 22, 33]
lis_2.remove(33)  # sterge doar un sngur element din lista
# in caz ca nu mai avem elemente, eroare
# ValueError: list.remove(x): x not in list
print(lis_2)


lis_2 = [11, 22, 33, 22, 33]
del lis_2[2]
print(lis_2)

lis_2 = [x for x in lis_2 if x != 33]  # sterge toate elementele cu aceeasi valoare
print(lis_2)

def adauga_element(numar, lista = []):
    # nu folositi argumente default listele
    lista.append(numar**2)
    return lista
print(adauga_element(3))  # rezultat asteptat este = [9], printat de fapt =[9]
print(adauga_element(4))  # rezultat asteptat este = [16], printat de fapt =[9, 16]


def adauga_element_v2(numar, lista = None):
    # in loc sa declar valoarea default lista = []
    if not lista:   #in cazul asta not None = True
        lista = []
    lista.append(numar**2)
    return lista
print(adauga_element_v2(3))  # rezultat asteptat este = [9], printat de fapt =[9]
print(adauga_element_v2(4))  # rezultat asteptat este = [16], printat de fapt =[16]

