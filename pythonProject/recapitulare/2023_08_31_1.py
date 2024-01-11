a = 1 # int
print(type(a))
print(isinstance(a, str))
b = True #bool
c1 = "salut"
c2 = 'salut'
c_multiline = """Salutare,
Azi e o zi frumoasa.
Ieri a plouat."""

d = 2.3 # float
from math import pi
print(pi, type(pi)) #am accesat valoarea lui pi prin import

d_2 = 2.123456789987654321  # afiseaza doar 16 caractere dupa virgula
print(d_2)

#tipuri de date complexe
lista = [1,2,3, 3.4, "ceva", False, [33,22]]
set_x = {1,2,3,2,1,1,2,1,2,3}
print(set_x)   # contine doar elementele unice {1, 2, 3}

tuple_x = (2,3,"ceva")

dict_x = {"cheie_1": "valoare_1",
          "cheie_2": True,
          "adresa": {"strada": "abc",
                     "nr":12,
                     "loc": "Iasi"}}

print(2+3)
print("abc"*3)  # string inmultit cu integer, repeta stringul; "abc"*3.2  sau "abc" * "def" - nu merge, da eroare

print(29 // 5) # impartire fara rest
print(29 % 5) # restul impartirii este 4

print(3 != 4) #!= inseamna este diferit

a = 40 + 14
b = 50 + 4
print(a != b) # False
print(a == b) # True, verific egalitatea
print(not a != b) # not este opusul; NOT FALSE = TRUE

print(a > 101) # False
print(a >= 54) # True

# Operatii cu string
nume = "ioNescU"
print(nume.upper())
print(nume.lower())
print(nume.title()) # primaa litera mare restul mici
print(nume.capitalize())  # primaa litera mare restul mici
print(f"{nume} vAlenTINo".title())   # Ionescu Valentino
print(f"{nume} vAlenTINo".capitalize())   # Ionescu valentino

nume_2 = "Ionescu Valentin"
print(nume_2.startswith("ion"))  #  este fals pt ca trebuia sa inceapa cu litera mare; este case sensitive
print(nume_2.lower().startswith("iOn".lower()))  # transform ambele strings in lowercase

text = """Aici este un text cu mai multe randuri.
Vreau sa inlocuiesc abc cu def"""
print(text.replace("abc", "def"))

# Extrag toate cuvinetele separtate de " " spatiu
cuvinte = text.split()
print(cuvinte)

#\n inseamna newline character
# \t inseamna tab character, adica 4 spatii
print("Salut\tce faci")
#\r return
print("Salut\rce faci\r cum esti") # scrie fiecare din aceste 3 elemente separat
# dupa care le suprascrie pe fiecare cu urmatorul

nume_lista = ["Ana", "Ion", "Vasile"]
nume_string = ";".join(nume_lista)
print(f"Stringul creat din lista {nume_lista} = {nume_string}")

print(nume_lista[0]) # indexarea/numararea in python incepe de la 0
print(nume_lista[1]) # al doilea caracter

nume_lista = ["Ana", "Ion", ["Ion2", "Ana2"], "Vasile"]
print(nume_lista[2][1])
print(nume_lista[-1]) # ultimul element din lista
print(nume_lista[-2]) # penultimul element din lista
#print(nume_lista[11]) # eroare pt ca nu avem atatea elemente in lista

for nume in nume_lista:
    print(nume)

for index, nume in enumerate(nume_lista):
    print(index, nume)
    # accesam indexul si valoarea fiecarui element
    # cand folosim enumerate, mereu avem ordinea index, element

print(list(enumerate(nume_lista)))  # fiecare pereche se printeaza cu indexul sau;
# ex: [(0, 'Ana'), (1, 'Ion'), (2, ['Ion2', 'Ana2']), (3, 'Vasile')]

#slicing - accesarea doar a unei parti din lista

nume_lista = ["Ana", "Ion", ["Ion2", "Ana2"], "Vasile", "Ana3", "Ion3"]
print(nume_lista[-3:]) # accesam ultimele 3 elemente
print(nume_lista[:3])  # accesam primele 3 elemente
print(nume_lista[2:4])   #extrage elemntul index 2 si 3, 4 exclude

string_cautat_1 = "Ana"
if string_cautat_1 in nume_lista:
    print("gasit") # a gasit elementul
else:
    print(f"{string_cautat_1} nu este in lista")

string_cautat_1 = "Ana2"
if string_cautat_1 in nume_lista:
    print("gasit")
else:
    print(f"{string_cautat_1} nu este in lista")
    # aici nu a gasit elementul pt ca la iterare vede ["Ion2", "Ana2"] ca un singur element

str_x = "Studentii de la SDA sunt foarte atenti"
str_cautat = "sunt"
if str_cautat in str_x:
    print("Am gasit")
print(str_cautat in str_x, type(str_cautat in str_x))

a = 5-4
if a:
    print("da")
#expresia este exhivalenta cu:
if True:
    print("da")


b = a - 1
if b:  # if False nu se printeaza si executia intra in else
    print("da")
else:
    print("nu")

verificare = 4 < 5
if verificare:
    print("da")
else:
    print("nu")

# if var1 and var2 and var3:
# putem stoca conditiile in variabile pentru o scriere mai eleganta a conditiilor multiple

e = [23]
if e: # verifica daca variabila e este True sau 1 sau are o valoare
    print("da")
else:
    print("nu")

s = ""
if s: # verifica daca stringul este gol
    print("da")
else:
    print("nu")

if len(s) > 0:
    pass   # fratele ne-elegant al if s:

# initializarea list, tuple, set, dict
a_1 = []
a_1 = list()
a_2 = tuple() # initializeaza un tuple gol
a_3 = {}
print(type(a_3)) # dict
a_3 = set() # initializeaza un dictionar gol
a_4 = dict()

a = True
b = False
print(a and b) # aici ca sa fie True, toate valorile trebuie sa fie True
# afara ploua and afara nu ploua - False

print(a or b) # cand cel putin una din valori este True, a or b or c etc..... = True

print(not a) # negatia; not True = False

# transformarea tipurilor de date
a = "cinci"
print(int(2))  # aici da eroare
a_7 = "5"
print(int(a_7))  # a_1 se poate transfora in integer

cifra = input("Ghiceste o cifra de la 1 la 10 = ")
print(f"cifra ta plus 10 = {int(cifra)} + 10 = {int(cifra) + 10}")
# daca scriu un string ne-convertibil in integer, am eroare

print(bool(0)) # False
print(bool(1)) # True
print(bool(12)) # True
print(bool(3431)) # True

el = [1, 2, 3]
print(isinstance(el, list)) # verifica daca el este obiect de tip lista

a_1 = "Ionel"
if isinstance(a_1, int):
    # isinstance verifica daca tipul de date al variabilei corespunde cu tipul de date specificat ca argument al functiei
    # isinstance(a_1, int)  - verifica daca a_1 este de tip integer
    print(a_1 * 2)
else:
    print(a_1.title())


a_2 = 7 > 23
print(a_2) # False
print(isinstance(a_2, str))  # False
print(isinstance(a_2, bool))  # True
print(isinstance(a_2, int)) # True, pt ca False = 0



