"""
Pentru instalarea pytest se foloseste comanda pip install pytest
Deschidem pycharm, mergem in file-settings in casuta de cautare scriem testing
default test runner - selectam 'pytest'

un fisier de teste poate fi rulat si din terminal:
pytest .\teste_calculator

isinstance verifica daca un obiect face parte din clasa sau clasele de obiecte
la care se face comparatia

Decoratorii sunt functii care extind sau modifica comportamentul unei alte functii
"""

print(isinstance('cinci', (str, int)))
print(isinstance('cinci', (str)))
print(type('cinci') == str)

# asignari multiple
a = 10
b = 20
c = 30
print(a, b, c)
# SAU

x, y, z = (10, 20, 30)
print(x, y, z)

"""
Despachetarea in Python
"""

iterabil = (2, 3)
def adunare(a, b):
    return a + b

print(adunare(2,3))
print(adunare(*iterabil))

# Typing

"""
Typing este o adnotare in python:
 - specifica tipul de date pentru a atentiona folosirea corecta, sau gresita, 
 dupa caz.
 Se adauga punct si tipul de typing dupa punct.
 Typing poate fi folosit pentru a specifica ce returneaza o functie sau 
 
 """

import typing

from typing import List

o_lista = ['mere', 'pere']

o_lista_typing: List = ['mere', 'pere']

o_lista = 'Petrica'

o_lista_typing = 'Petrica'

string: str = 'Bucuresti'
string = 5343434

#suntem atentionati ca lista contine elemente de tip str si nu int
o_lista_typing: List[int] = ['mere', 'pere']
#nu mai suntem atentionati
o_lista_typing: List[int] = [2323, 44423]

from typing import Union
def adunare(*args: Union[int, float]) -> Union[int, float]:
    return sum(args)

print(adunare(5, 3, 2.3))
