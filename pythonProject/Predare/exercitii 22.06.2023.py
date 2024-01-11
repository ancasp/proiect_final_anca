# Definiti o functie care returneaza suma patratelor a doua numere

nr_1 = 10
nr_2 = 5
def patratul_sumelor(nr_1, nr_2):
    rezultat = nr_1**2 + nr_2**2
    return rezultat
print(patratul_sumelor(nr_1, nr_2))

x = 3
y = 2
z = 4
def patrate(x, y, z):
    rezultat = x**2 + y**2 + z**2
    return rezultat
print(patrate(x, y, z))


# Definiti o functie care printeaza suma patratelor a doua numere, dar nu returneaza nimic

nr_1 = 10
nr_2 = 5
def patratul_sumelor(nr_1, nr_2):
    rezultat = nr_1**2 + nr_2**2
    # return rezultat !!! pt a nu returna nimic, adica None, nu se va executa return
print(patratul_sumelor(nr_1, nr_2))


# Definiti o functie care returneaza suma patratelor a X (nedefinit) numere, doar daca sunt impare

def patrate_impare(*args):
    rezultat = 0
    for x in args:
        if x % 2 == 1:
            rezultat = rezultat + x**2
    return rezultat
var = patrate_impare(1, 2, 3)
print(var)

def patrate_pare(*args):
    rezultat = 0
    for x in args:
        if x % 2 == 0:
            rezultat = rezultat + x**2
    return rezultat
var = patrate_pare(1, 2, 3)
print(var)

# Functie care ia un numar nedefinit de strings si returneaza lungimea totala a lor

strx = "Ion este casatorit cu Maria."
def lungime_strx(*args):
    lungime_total = 0
    for strx in args:
        return lungime_total
print(len(strx))

# Functie care returneaza cate vocale are un string

strx = ("Ion este in baie.")
def vocale(strx):
    vocale_in_text = 0   # de ce pun asta?
    for vocala in strx.lower() :
        if vocala in "a,e, i,o,u" :
            vocale_in_text += 1   # de ce pun asta?
    return vocale_in_text
print(vocale(strx))


# Creati o functie care va returneaza un email promotional, fiti creativi :slightly_smiling_face:

def email_promotional(prenume, valoare_cumparaturi, magazin):
    emailul = f"""
    Salut {prenume}, 
    Cumprataurile tale au depasit {valoare_cumparaturi} lei si dorim sa iti oferim un voucher cadou in valoare de
    {valoare_cumparaturi * 0.1} lei valabil pana la data de 31.12.2023.
   
    Cu respect,
    Magazinul {magazin}
    """
    return emailul
lisprenume = ["Ion", "Maria", "Andrei"]
lisvaloare_cumparaturi = [500, 100, 350]
magazin = ["Berceni", "Titan", "Unirii"]
for index, element in enumerate(lisprenume):
    print(email_promotional(element, lisvaloare_cumparaturi[index], magazin[index]))


# Scrieti o functie care returneaza lista de pasi/secventa Collatz pentru un anumit numar

d_collatz = dict()
for n in range(1,10):
    nr_initial = n
    list_secv = [n]
    while n!=1:
        if n%2 == 0:
            n = int(n/2)
        else:
            n=3*n+1
        list_secv.append(n)

    if len(list_secv)>10:
        d_collatz[nr_initial] = len(list_secv)

print(d_collatz)

# rezolvarea buna
def collatz_numar(nr):
    listx = [nr]
    while nr !=1:   # !=1 inseamna diferit de 1
        if nr % 2 == 0:
            nr = nr //2
        else:
            nr = nr * 3 + 1
        listx.append(nr)
    return listx
print(collatz_numar(7))

# Scrieti o functie care returneaza inversul unui string

def reversul(textul):
    return textul[::-1]
strx = "Ionel e baiat bun"
print(reversul(strx))

# Scrieti o functie care returneaza True daca numarul dat e divizibil cu 13, False otherwise.

def divcu13(26):
    divizibil = [0]
    for nr in divcu13:
        if nr % 13 ==0:
            return True
        else:
            return False
print(divcu13)


# Scrieti o functie care returneaza media aritmetica a unui numar nedefinit de numere

# Scrie o functie care returneaza numarul minim si maxim dintr-un sir de numere date functiei ca argumente
