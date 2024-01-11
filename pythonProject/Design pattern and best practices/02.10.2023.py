# region 1 LINTERS

# tool care analizeaza codul si identifica probleme care tin de PEP8
# pylint

# endregion

# region 2. Acronime

"""
SOLID
S - Single responsability = fiecare functie trebuie sa faca un singur lucru
 - se prefera mai multe functii cu roluri mici in loc de o singura functie cu mai mullte roluri

O - Open-closed principle = open to inheritance, closed to modification
 - preferam sa mostenim o clasa decat sa modificam codul clasei initiale

L - Liskov substitution principle  = obiectele clasei parinte trebuie sa poata fi inlocuite oricand cu obiectele clasei
copil fara a produce erori in aplicatie

I - Interface segregation principle = segregarea functionalitatii se face pana la cel mai specific nivel

D - Dependency Inversion principle = hihh-level modules nu trebuie sa depinda de low-level modules, ambele trebuie sa
depinda de abstractizari

"""
# initial
from abc import abstractmethod, ABC
class Bread: # low-level module
    def bake(self):
        print ("Smells like bread")

def cook(): # high-level module
    bread = Bread()
    bread.bake()

# conform Dependency inversion
class Bakable(ABC): # abstractizarea
    @abstractmethod
    def bake(self):
        pass

class Bread(Bakable): # low-level module
    def bake(self):
        print ("Smells like bread")

class Cookies(Bakable): # low-level module
    def bake(self):
        print ("Smells like cookies")
def cook(bakeable): # high-level module
    bakeable.bake()

bread = Bread()
cookies = Cookies()
cook(bread)
cook(cookies)

"""
KISS = Keep It Simple & Stupid
DRY = Don't Repeat Yourself
YAGNI = You Ain't Gonna Need It
"""


# endregion

# region 3. Design Patterns - DP - generalitati
"""
DP = solutie universala pentru o problema recurenta in procesul de dezvoltare al unei aplicatii
https://www.geeksforgeeks.org/python-design-patterns/
https://refactoring.guru/design-patterns/catalog

DP au fost clasificate de GoF(Gang of Four) in cadrul cartii denumita Design Patterns, in 3 categorii:
1. Creational = cum cream obiecte
2. Structural = cum organizam clasele
3. Behavioural = cum gestionam responsabilitatea obiectelor
"""

# endregion

# region 4. DP creationale
"""
Singleton
Builder
Factory
Factory Method
Abstract Factory
Prototype
"""

# endregions

# region 5. Singleton

# Scenariu: ete un DP folosit cand avem ca si conditie sa cream maxim un singur obiect dintr-o clasa (bun pt scenarii
# de monopol)

class MetrouRomania:

    class Singleton: # clasa interna, auxiliara pt implementarea DP Singleton
        def __init__(self, nume_metrou):
            self.nume_metrou = nume_metrou

    instance = None  # instanta unica de MetrouRomania

    def __new__(cls, nume_metrou):  # __new__ returneaza instanta, __init__ atribuie valori atributelor
        if not MetrouRomania.instance:
            MetrouRomania.instance = MetrouRomania.Singleton(nume_metrou)
            print("s-a creat o noua instanta")
        return MetrouRomania.instance

metrorex = MetrouRomania("metrorex")
print(metrorex.nume_metrou)
sda = MetrouRomania("sda")
print(sda.nume_metrou)
print(id(metrorex), id(sda))  # cu id ne printeaza locatia (zona de memorie unde se salveaza)
# endregion

# region 6. Builder

# Sceenariu: mai multe reprezentari pentru acelasi obiect - ex: la traduceri

class Builder:

    # construieste noua reprezentare caracter cu caracter
    def build(self, element):
        pass

    # returneaza reprezentarea
    def get_result(self):
        pass

class UpperBuilder(Builder):
    def __init__(self):
        self.result_upper = ""

    def build(self, element):
        self.result_upper += element.upper()

    def get_result(self):
        return self.result_upper


class LowerBuilder(Builder):
    def __init__(self):
        self.result_lower = ""

    def build(self, element):
        self.result_lower += element.lower()

    def get_result(self):
        return self.result_lower


class HexaBuilder(Builder):
    def __init__(self):
        self.result_hexa = ""

    def build(self, element):
        self.result_hexa += f"0x{ord(element):02x}"

    def get_result(self):
        return self.result_hexa

class Person:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

    def set_builder(self, builder):
        self.builder = builder

    def construct(self):
        string_to_print = f"Person {self.name} is {self.age} years old"
        print(string_to_print)

        for character in string_to_print:
            self.builder.build(character) # cream reprezentarea caracter cu caracter

    def get_person_result(self):
        return self.builder.get_result()

p = Person("Anca", 36, 1)
upper = UpperBuilder()
lower = LowerBuilder()
hexa = HexaBuilder()

for builder in [upper, lower, hexa]:
    p.set_builder(builder)
    p.construct()
    print(p.get_person_result())
    print("-----------------------------")

# endregion

# region 7. Alte DP creationale

"""
FACTORY
 - ofera implementari concrete pt o abstractizare
 - separam crearea efectiva a obiectului de referentierea sa
 
FACTORY METHOD
 - crearea familiilor de obiecte
 - ex: familia de jocuri Monopoly - in varianta board si PC
 
ABSTRACT FACTORY
 - extensie a FACTORY METHOD
 - grupuri ale aceleasi familii de obiecte
 - i se mai spune factory of factories
 
PROTOTYPE
 - imparte crearea obiectelor in dooua etape:
 1. crearea prototipului - se folosesc functiile copy() si deepcopy() pt clonarea prototipului
 copy()  - shallow copy (copie de referinte, aceeasi zona de memorie)
 deepcopy()  - deep copy (copie de obiect, zone de memorie diferite)
 2. personalizarea fiecarei clone - adaugam atributele prin care se distinge fiecare clona
"""

# endregion