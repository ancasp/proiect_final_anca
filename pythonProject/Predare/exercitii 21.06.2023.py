# Creeaza o lista cu numerele pătrate de la 1 la 100 divizibile cu 3, cu 2 metode.

# varianta list comprehension
lista_mea = [n**2 for n in range(1,101) if n % 3 == 0]
print(lista_mea)

#varianta clasica
lista_patrate = []
for n in range(1,101):
    if n % 3 == 0:
        lista_patrate.append(n**2)
print(lista_patrate)

# Avand o lista cu numere pozitive si negative, extrageti intr-o alta lista doar numerele negative.

lisx = [-9, 19, -19, 2, -3] #primul x poate avea operatii, al doilea doar pt iterare
lisx_n = [x for x in lisx if x < 0]
print(lisx_n)

# Creati o lista cu lungimea fiecarui cuvant dintr-un string. De ex pentru "Abd ha abcd" vom avea [3,2,4]

propozitia = "A venit vara si ne bucuram de soare"
list_cuv = [len(cuv) for cuv in propozitia.split()]
print(list_cuv)

#varianta altfel
strx = "Salutare ce mai faci azi"
cuvinte = strx.split()
print(cuvinte)
lis_lung = [len(x) for x in cuvinte]
print(lis_lung)

# alt exemplu about split
strx = "4587, 458741, 4587, 5874555"
numere = strx.split() #split bydefalut este impartit per spatiiu
numere = strx.split(", ")
print(numere)

#Aveti o lista de temperaturi in celsius.
# Folosind list comprehension, creati o alta lista cu temperaturile in Farenheit.
# Folosind dict comprehension, creati un dictionar cu cheile in celsiul si valorile in F, de exemplu pentru lista [12, 32] veti avea:
# {"12 grade Celsius": "53.6 grade F", "32 grade Celsius": "89.6 grade F"}

#formula (C*9/5) + 32
lis_c = [12, 32, 59, 100]
lis_f = [(c*9/5) + 32 for c in list_c]
print(list_f)

dict_f = {f"{c} grade celsius" : f"{(c * 9/5) + 32} grade F" for c in lis_c} # f string (f"")
print(dict_f)

nume = "Ion"
varsta = 24
strx = f"Salut {nume} ce mai faci? Tu esti nascut in anul {2023-varsta}, nu-i asa?"
print(strx)

nume = "Ion", "Vasile", "Elena", "Ana"
varsta = [24, 25, 78, 12]
for index, valoare in enumerate(nume):
    print(f"Salut {nume[index]}, esti nascut in {2023 - varsta[index]} ? ") # f string inglobeaza in string variabile sau
    #calcule simple cu variabilele


# Creati o lista cu divizorii lui 47 de la 10*2 la 10*3 folosind 2 metode
# v1
divx_47 = [x for x in range(10**2, 10**3 + 1) if x % 47 == 0]
print(divx_47)

# v2
div_47_v2 = []
for x in range(10**2, 10**3 + 1):
    if x % 47 == 0:
        div_47_v2.append(x)
print(div_47_v2)

# Aveti o lista de numere. Creati doua liste cu comprehension care sa contina numerele pare si cele impare respectiv.

lisx = [1, 23, 354, 4353, 54, 647]
pare = [x for x in lisx if x % 2 == 0]
impare = [x for x in lisx if x % 2 == 1]
print(pare, impare, sep="slash invers n")

# Ce inseamna \n newline, trece la linie noua


# 7. Creati o lista cu rezultatul impartirii la 13 a numerelor de la 89 la 67, rezultatele sa fie rotunjite la doua decimale
#Scrieti ambele metode

lisx = [x % 13 for x in range(89, 66, -1)]
print(lisx)

lisx_v2 = []
for x in range(89, 66, -1):
    lisx_v2.append(x % 13)
print(lisx_v2)


# 8. Creeaza o lista cu toate cifrele unui numar intreg. De ex pentru 12456 avem lista [1,2,3,4,5,6] (edited)

nr = 566824326492364329
cifre = [cif for cif in str(nr)] # int not iterable = nu merge sa extragem fiecare valoare din integer
#dar pe string merge, de aceea am transformat int in str:str(nr)
print(cifre)

# 9. Creati o lista de perechi de tuples cu numarul si patratul sau +1, pentru numere intre 2,14.
# De exemplu intre 2 si 4 avem [(2,4+1),(3,10),(4,17)

lisx = [(x, x**2 + 1) for x in range(2, 15)]
print(lisx)


#  10. Creati un dictionar cu cheia x si valoarea 3*x**2 + 7*x -8 pentru fiecare numar par de la 23 la 99

dix = {x: 3*x**2 + 7*x - 8 for x in range(23, 99) if x % 2 == 0}
print(dix)

# 11. Creati un dictionar cu valorile un tuplu ce contine x**2 -1 si x**2+1 pentru elementele intregi ale unei liste
# De exemplu pentru lista [2, "hello", 3, True, 4] avem {2:(3,5), 3:(8,10), 4:(15,17)}
# Hint: folositi functia isinstance pentru filtrare.

lisx = [2, "hello", 3, True, 4.5, 4]
dix = {x: (x**2 - 1, x**2 + 1) for x in lisx if isinstance(x, int) and not isinstance(x, bool)}
print(dix)

# 12. Creati un dictionar cu dict comprehension cu numarul de aparitii a fiecarui caracter intr-un string
# De ex: "aab" va rezulta {"a":2, "b":1}

strx = "Salutare ce mai faci mai Ionele"
dix = {lit: strx.count(lit) for lit in set(strx)}
print(dix)


# 13. Calculati suma patratelor de la 12 la 24.
# Folositi 3 metode:
# for
# while
# Si functia sum aplicata unei list comprehension

# v1
suma_patratele = sum([x**2 for x in range(12, 25)])
print(suma_patratele)

patrate = [x**2 for x in range(12, 25)]
print(sum(patrate))

# v2

suma_v2 = 0
for x in range(12, 25):
    suma_v2 += x**2
print(suma_v2)

# v3

num_de_la = 12
suma_v3 = 0
while True:
    suma_v3 += num_de_la**2
    num_de_la += 1
    if num_de_la > 24:
        break
print(suma_v3)

# 14. Conjectura Collatz, cunoscută și sub numele de conjectura 3n + 1, este o problemă nerezolvată în matematică
# care implică o secvență iterativă de numere. Conjectura afirmă că, indiferent de valoarea întreagă pozitivă
# a lui n pe care o alegi, secvența de numere va ajunge întotdeauna la 1 dacă acest algoritm este aplicat:
# Dacă n este par, împarte-l la 2 pentru a obține n/2
# Dacă n este impar, înmulțește-l cu 3 și adaugă 1 pentru a obține 3n + 1
# Creati o lista de numere rezultate in calcularea secventei pentru orice numar natural.
# ** Daca demonstati conjectura asta pentru n infinit, primiti 1 milion dolari.

n = 32
lis_secv = [n]
while n != 1:
    if n % 2 == 0:
        n = int(n / 2)
    else:
        n = 3*n + 1
    lis_secv.append(n)
print(lis_secv)