# Definiti o functie care returneaza suma patratelor a doua numere
# Definiti o functie care printeaza suma patratelor a doua numere, dar nu returneaza nimic
# Definiti o functie care returneaza suma patratelor a X (nedefinit) numere, doar daca sunt impare
# Functie care ia un numar nedefinit de strings si returneaza lungimea totala a lor
# Functie care returneaza cate vocale are un string
# Creati o functie care va returneaza un email promotional, fiti creativi :slightly_smiling_face:
# Scrieti o functie care returneaza lista de pasi/secventa Collatz pentru un anumit numar
# Scrieti o functie care returneaza inversul unui string
# Scrieti o functie care returneaza True daca numarul dat e divizibil cu 13, False otherwise.
# Scrieti o functie care returneaza media aritmetica a unui numar nedefinit de numere
# Scrie o functie care returneaza numarul minim si maxim dintr-un sir de numere date functiei ca argumente

# 12. Scrieti un program care ghiceste un numar, zicand daca esti foarte departe, departe sau foarte aproape de numarul de ghicit

import random
def ghiceste_numar():
    numar_ghicit = random.randint(1,10)

    while True:
        ghicire = int(input("Ghicește numărul(1-10):"))

        if ghicire < numar_ghicit:
            print("Ești departe.")
        elif ghicire > numar_ghicit:
            print("Ești departe.")
        else:
            print("Felicitări! Ai ghicit.")
            break
ghiceste_numar()

# alta varianta de rezolvare
numar_de_ghicit = 12
print("Am ales un numar de la 1 la 100. Acum ghiceste numarul!")
while True: # bucla tehnic infinita, trebuie sa iesm din ea manual la o anume conditie
    numar_ghicit = input("Introdu un numar de la 1-100 =")
    try:
        numar_ghicit = int(numar_ghicit) # incearca sa converteasca in integer
    except:
        print("Mai da un numar valid")
        continue
        # cu try except ma asigur ca numarul e convertibil din str in int
    diferenta = abs(numar_de_ghicit - numar_ghicit) # abs(x) = |x|, de ex |5| = |-5| = 5

    if diferenta>20:
        print("Foarte departe! Mai incearca!")
    elif diferenta > 5: # intre 5 exclusiv si 20 inclusiv
        print("Departe si totusi aproape")
    elif diferenta > 0: # intre 0 exclusiv si 5 inclusiv
        print("Foarte foarte aproape")
    else: # adica diferenta = 0, a ghicit
        print(f"Bravo! Numamrul era {numar_de_ghicit}")
        break
print("Uraaaaa")

# 13.Creati un program care scrie cate secunde au mai ramas, gen countdown timer.
# Hint: folositi from time import sleep

import time
def countdown_timer(seconds):
    while seconds > 0:
        print("Au mai rămas {} secunde.".format(seconds))
        time.sleep(1)
        seconds -= 1

    print("Timpul a expirat!")

secunde_ramas = int(input("Introduceți numărul de secunde pentru cronometru: "))
countdown_timer(secunde_ramas)

# alta varianta
from time import sleep
secunde = int(input("Secunde Timer: "))
for secunda in range(secunde,0,-1):
    print(secunda)
    sleep(1)

# 14. Aveti 2 liste de nume: studenti inscrisi la curs si studenti prezenti azi. Creati o functie care face prezenta.
# (Nu dau instructiuni detaliate, va las sa fiti creativi)

studenti_inscrisi = ["Ionescu", "Popescu", "Spirea"]
studenti_prezenti = ["Ionescu", "Spirea"]
def prezenta(studenti_inscrisi, studenti_prezenti):
    for student in studenti_inscrisi:
        if student in studenti_prezenti:
            print(student, "prezent")
        else:
            print(student, "absent")

prezenta(studenti_inscrisi, studenti_prezenti)

# 15. Creati o functie care valideaza un email (daca string-ul respectiv e valid pentru a fi considerat email)
import re
def validare_email(email):
    email_valid = r'ab@yahoo.com'
    if re.match(email_valid, email):
        print("Emailul", email, "este valid.")
    else:
        print("Emailul", email, "nu este valid.")

adresa_email = input("Introduceți adresa de email: ")
validare_email(adresa_email)

# Alta varianta de rezolvare
exemplu = "andrei@sda.ro"
# print(email.split("@"))

# Reguli de validare, non-exhaustive (doar cateva reguli)
# are un singur @
# username are lungime >= 3
# domeniu (ex - sda) sa aiba lungime >= 2
# .something are o lungime >=2

if email.count(@) != 1 :
    print("false")
else:
    username, dupa_arond = email.split("a")
    domeniul, dupa_punct = dupa_arond.split(".")
    # fiindca email.split("@") are doua elemente, le putem desface "unpacking" in doua variabile direct
    if len(username) < 3:
        print("false")
    if len(domeniul) < 2:
        print("false")
    if len(dupa_punct)<2:
        print(false)

text = "Ionel, Mia, Ioana"
lista_nume = text.split(", ")
print(lista_nume) # split a creat o lista cu 3 elemente, despartind dupa ", "
nume_1, nume_2, nume_3 = lista_nume
#echivalent cu
nume_1 = lista_nume[0]
nume_2 = lista_nume [1]
print(nume_1)

un_email = "andreea.ionescu@gmail.com"
print(un_email.split("@"))
inainte_arond, dupa_arond = un_email.split("@")
inainte_p, dupa_p = dupa_arond.split(".")
print(f"inainte_arond = {inainte_arond}")
print(f"dupa_arond = {dupa_arond}")
print(f"inainte_p = {inainte_p}")
print(f"dupa_p = {dupa_p}")

text_localitati = "Iasi - Paris - Bucuresti - New York"
localitati_lista = text_localitati.split("-")
print(localitati_lista)

email_rau = "ion@gmail.com@guvern"
print(email_rau.split("@"))


# 16.Aveti o un dictionar cu nume si varsta, fiecare are cate 4 elemente.
# Creati un fisier care sa contina text cu numele si varsta fiecarei persoane, in modul urmator, exemplu:
# Andrei are 20 ani, deci e nascut in 2003
# Ion are...
# ...
# ...

persoane = {"Andrei":20, "Ioana":23, "Vasile":12, "Ana":24}
folder = "C:\Users\ancas\Desktop"
path_file = f"{folder}/studenti_ex16.txt"
# path file este o variabila default, pot sa o schimb

def scrie_persoane(un_dictionar):
    with open(path_file, "w") as f:
        for cheie, valoare in persoane.items():
            f.write(f"{cheie} are {valoare} ani, deci e nascut(a) in {2023-valoare}")

scrie_persoane(persoane)

# 17. Aveti acest fisier cu notele a 3 elevi. Creati alt fisier care scrie media aritmetica a fiecarui elev. fisier_cu_note.txt
# Andrei 4,10,9,4
# Vasile 10,9,10,5
# Elena 3, 2, 10, 10, 8, 9, 4

path_fisier_note =
with open(path_fisier_note, "r") as f:
    linii = f.readlines()
print(linii)
list_nume = []
list_notele = []
for l in linii:
    Numele, Notele = l.split(" ")
    Notele = Notele.replace("r\n", "")
    Notele = Notele.split(", ")
    list_nume.append(Numele)
    list_notele.append(Notele)
print(list_nume)

for index, el in enumerate(lista_nume):
    # trebuie sa convertesc valorile din string in integer
    list_notele_int = [int(nota) for nota in list.notele[index]]
    # codul de mai sus converteste fiecare element din list notele in integer
    print(list_notele_int)
    media = mean(list_notele_int)
    # ca sa rotunjesc, folosesc functia round(numar, decimale
    print(f"{el} are notele {round(media, 2)}\n"

# 18. Creati o functie care calculeaza produsul (n+1) dintr-o functie la elementele float&int
# De exemplu pentru lista ["Ion", 2, 3.5, "Ana"] avem rezultatul (2+1) x (3.5+1)= 3 * 4.5 = 13.5
# Hint: Folsiti isintance(n,int) sau float.

def produs_int_float(*args):
    produs = 1
    for element in args:
        if type(element) is int or type(element) is float:
            produs *= (element+1)
    return produs
print(produs_int_float(4, True, "Mircea", 1.2, "Dorel", 3))


# 19. Scrieti o functie care calculeaza factorialul unui numar

from math import factorial as fact
def factorial(numar):
    factorial_x = fact(numar)
    return f"Factorialul lui {numar} este {factorial_x}"
print(factorial(4))

