"""Design Patterns and Best Practices - 14h
BEST PRACTICES = recomandari pt a scrie un cod mai profi
PEP = Python Enhancement Proposal = documentatie + sfaturi, guidelines

PEP20 = Zen of Python - 19 principii de viata ale programarii python
https://inventwithpython.com/blog/2018/08/17/the-zen-of-python-explained/
"""

import this

# region 1. PEP 8

"""
PEP 8  = Style Guide - recomandari clean code
https://peps.python.org/pep-0008/

"""
# Naming Conventions
"""
1. functiile - ex: read_file (snake_case = litere mici + underscore pt despartirea cuvinetelor
2. variabile - ex: current_user (snake_case)
3. clase - ex: EmployedPerson (CamelCase/PascalCase = majuscula la inceputul cuvantului + nimic pt despartirea cuvintelor
4. constante - ex: MAX_VALUE (uppercase + underscore)
5. fisiere de cod/scripturi - ex: my_scrypt (snake_case)
6. pachete - ex: agentieturism (lowercase + fara delimitator)
"""

# Code Layout
"""
- 2 linii goale intre functii/clase
- 1 linie intre pasii aceleasi functii/metodele aceleasi clase
- lungimea maxima a unei linii de cod este de 79 caractere; daca avem o linie mai lunga, o spargem cu \
- inconjuram operatiile cu space: = , += , == , < , >  etc
"""

# Comentarii
"""
1. Comentariul inline = pe aceeasi linie cu codul si foarte succint; marcam cu #
2. Block comments = pe o linie separata, deasupra codului, explica urmatoarea linie/urmatoarele linii de cod; marcam cu #
3. Multiline comments = se marcheaza cu 3 perechi de ghilimele "/ apostrof '
* daca multiline comment apare la inceput de functie/clasa/script, atunci este vb despre un docstring
"""

# exercitiu - scrieti un comentraiiu inline, block si multiline pt urmatoarea clasa; incercati sa scrieti
# si un docstring pt ea


class Person:
    """
    aici o sa scriu la inceput si
    pe mai multe linii si ar trebui
    sa fie docstring
    """
    def __init__(self, name, cnp, age):
        self.name = name
        self.__cnp = cnp
        self.age = age

    @property
    def cnp(self):
        return self.__cnp

    # conditia pentru lungimea CNP-lui
    @cnp.setter
    def cnp(self, cnp_nou):
        if len(cnp_nou) == 13:
            """
            comentariu multiline
            facem o validare inainte de setarea atributului cnp
            """
            self.__cnp = cnp_nou
        else:
            print('CNP nevalid')

    @cnp.deleter
    def cnp(self):
        del self.__cnp

    @staticmethod
    def validate_name(n):
        if n[0].isupper() and len(n) >= 3:  # conditia
            return True
        else:
            return False
print(Person.__doc__) # prin variabila __doc__ accesam docstringurile clasei/functiei/scriptului

# endregion


# region 2. PEP 257 - docstrings

"""
 - reprezinta documentatie a codului scris de noi
 - marcam un docstring cu 3 perechi de " sau '
 - putem scrie un docstring pt o clasa/metoda/functie/script
 - pozitionam docstringul la inceput
 - accesam docstringul prin __doc__
"""

# template docstring functie
"""
def my_function(param0:
    '''
        Purpose of the function:
        
        Description of parameters + data type:
        
        Return values:
        
        Side effects: # in cazul in care functia mai e folosita altundeva
        
        Usage example: # exemplu de apel al functiei
    '''
"""

# endregion

# TEMA
# scrieti un docstring pt urmatoarea functie

def validate_name(n):

    substrings = n.split()
    print(substrings)
    for substring in substrings:
        if substring.istitle() and len(n) >= 3:
            return True
        else:
            return False

# region 3. PEP 8 - tips and tricks

# folosim metode specifice pe cat posibil
my_str = "abc"
if my_str[0] == "a":  # nu este recomandat
    print("Starts with A")
else:
    print("Starts with other letter")


if my_str.startswith("a"):   # recomandat
    print("Starts with A")
else:
    print("Starts with other letter")


# folosirea unui logical context
"""
Logical contexts:
 - (empty string) este echivalent cu False
 - 0 echivalent cu False, 1 echivalent cu True
 - [] empty list echivalent cu False
"""

if []:
    print("Ramura True")
else:
    print("Ramura False")


# folosim verificarea lui None
x = None
if x is not None:    # recomandat
    print("Not None")
else:
    print("None")
# merge si asa dar nu e chiar atat de explicit
if x:
    print("Not None")
else:
    print("None")

# endregion

# region 4. AUTOFORMATTER

# pip install black
# comanda de terminal: black nume_fisier_de_formatare.py

# endregion