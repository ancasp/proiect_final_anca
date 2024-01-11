# region 1. DP Structurale
"""
Adapter
Bridge
Facade
Flyweight
Proxy
Composite
Decorator
"""

# endregion

# region 2. DP structurale - teoretic

import string

"""
ADAPTER
 - folosit pt a crea o legatura intre 2 entitati aparent incompatibile
 - https://refactoring.guru/design-patterns/adapter/python/example

BRIDGE
 - sparge o ierarhie complexa in ierarhii mai mici care pot fi gestionate independent, asigurand totodata
 comunicarea intre ele
 
FARCADE
 - ofera un API = Application Program Interface = punct de acces catre un sistem complex + arata si ce optiuni exista
pt interactiunea cu acel sistem

PROXY
- functioneaza ca un API + executa o parte din cererea clientului, directionand restul catre alt serviciu
"""

# endregion

# region 3. Flyweight

"""
 - minimizeaza ocuparea memoriei in scenariul in care crearea unui obiect necesita alt oboect
 - folosit in testare, pe parcurs ce avem cate o clasa 100% testata
 
 """

class Masina:
    def __init__(self, producator, culoare, an_fabricatie):
        self.producator = producator
        self.culoare = culoare
        self.an_fabricatie = an_fabricatie
        self.motor = None

    def __str__(self):
        return f"Masina cu producator {self.producator} are culoarea {self.culoare}, anul {self.an_fabricatie} si motorul {self.motor}"

class Motor:
    def __init__(self, tip):
        self.tip = tip

    def __str__(self):
        return f" Motor id {id(self)} de tip {self.tip}"

# motor_diesel = Motor("Diesel")
# masina1 = Masina("VW", "rosu", 2018)
# masina1.motor = motor_diesel
# masina2 = Masina("BMW", "negru", 2019)
# masina2.motor = motor_diesel
# masina3 = Masina("Skoda", "gri", 2020)
# masina3.motor = motor_diesel
# print(masina1, masina2, masina3, sep = "\n")

# endregion

# region 4. Composite + Decorator

"""
Composite
 - folosit pentru a modela structuri de tip arbore
 - ex: arbore de familie sau ierarhia unei companii
 
Decorator
 - adauga o functionalitate extra unei functii la runtime, fara a modifica explicit codul functiei
 - https://realpython.com/primer-on-python-decorators/#fancy-decorators
"""
# Decorator care afiseaza cu litera mare numele departamentelor

def capitalize(func):  # decoratorul este o functie care ia ca parametru alta functie
    def wrapper(*args):  # scopul wrapper-ului este de a mapa parametrii lui func cu argumente
        return string.capwords(func(*args))

    return wrapper
class Departament:

    def __init__(self, nume_departament):   # definim construtorul
        self.nume_departament = nume_departament
        self.subdepartamente = []
# in dreapta este valoarea si in stanga este numele atributului

    def adauga_subdepartament(self, subdepartament):
        self.subdepartamente.append(subdepartament)

    @capitalize
    def get_nume(self):
        return self.nume_departament

dep = Departament("publicitate")
subdep1 = Departament("social media")
subdep2 = Departament("tv")

dep.adauga_subdepartament(subdep1)
dep.adauga_subdepartament(subdep2)

# print(f"Departamentul {dep.nume_departament} are subdepartamentele:")
# for subdep in dep.subdepartamente:
#     print(subdep.nume_departament)

print(f" Departamentul {dep.get_nume()} are subdepartamentele:")
for subdep in dep.subdepartamente:
    print(subdep.get_nume())

# endregion