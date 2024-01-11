a = 7
# int
print(type(a))
b = 7.3 # float
c = "string text" #str
d True # bool

e = "7" # nu se poate sa scriem sapte, nu se executa
f = int(e)
print(f, type(f))

#verificam tipul de date
#v1
a = 7
print(type(a) is str)
#v2
print(isinstance(a, str))
#!
print(isinstance(True, False)) # print(isinstance(True, int)) echivalent cu print(isinstance(1, int))

listx = ["b", 1, False, [1,2,3]]
tuplex = ("b", 1, False, [1,2,3])
listx[1] = "Altceva"
print(listx)
tuplex[1] = "Altceva" # nu o sa mearga
print(tuplex) # nu putem schimba elementele tuple-ului

setx = {2, 3, 45, 66}   # la set se folosesc {}
# set e tip de date unice, neordonate(nu le putem accesa dupa index)
print(setx[2])   # TypeError: 'set' object is not subscriptable


lis_2 = [1, 2, 3, 2, 3, 2, 45]
lis_2_unice = list(set(lis_2))
print(lis_2_unice)

# sau

lis_2 = [1, 2, 3, 2, 3, 2, 45]
lis_2_unice = set(lis_2)
print(lis_2_unice)



dictx = {"cheie_1": 12, "Andrei":25,
         "Ionel":[23,23],
         "adresa": {"strada":"Fericirii", "nr":12}}
#accesarea datelor se poate face prin indexare sau prin iterare

# indexare
listx = ["b", 1, False, [1,2,3]]
print(listx[0])
tupx = tuple(["b", 1, False, [1,2,3]])
print(tupx[0])

nume_strada_dictionar = dictx["adresa"]["strada"]
print(nume_strada_dictionar)

#json = dictionar

# iterare
for el in listx:   # el = aici pun ce denumire vreau
print(el)
# enumerate ne ofera posibilitatea sa accesam indexii valoare in acelasi timp
for index, el in enumerate(listx):  # index poate fi scris cum vrem noi, de ex ix, veta etc  !!! conteaza ordinea si logica
    print(f"Elementul cu indexul {index} are valoarea {el}")

print(list(enumerate(listx)))  # asa se printeaza [(0, 'b'), (1, 1), (2, False), (3, [1, 2, 3])]

lista_complexa = [["Ana", 23, "skiul"], ["Elena", 27, "sahul"], ["Ion", 29, "videogames"]]
for nume, varsta, hobby in lista_complexa:
    # list unpacking functioneaza doar daca avem aceleasi numar de valori; daca de exemplu nu aveam o valoare
    # la una dintre cele 3 liste, imi printeaza pana unde vede corect si apoi da eroare
    print(f" nume = {nume}, varsta = {varsta}, hobby = {hobby}")


listx = ["b", 1, False, [1,2,3]]
print(3 in listx)  # false pt ca [1,2,3] este un element unitar, adica nu il desparte
print(1 in listx)

#iterarea pe dictionar
dictx = {"cheie_1": 12, "Andrei":25,
         "Ionel":[23,23],
         "adresa": {"strada":"Fericirii", "nr":12}}
#doar cheile
for cheie in dictx.keys():
    print(cheie)
#doar pe valori
for val in dictx.values():
    print(val)
# iterare atat pe chei cat si pe valori
for cheie, val in dictx.items():
    print(f"Cheia {cheie} are valoarea {val}")

# pentru a itera pe dictionarul ce apartine de cheia adresa
for cheie, val in dictx["adresa"].items():
    print(f"Cheia {cheie} are valoarea {val}")


text_1 = "salut ion"
print(text_1.capitalize())
print(text_1.upper())

listx = ["b", 1, False, [1,2,3]]
print(len(listx))
print(len(text_1))

nr = 86778548
print(len(str(nr)))  # str transforma elementul in string, len este lungimea

#operatori aritmetici: +, -, *, /, mai avem
# // impartire fara rest
# % restul impartirii
# ** ridicare la putere
# \n newline
print(171%10)
print(171//10)
print(171 ** 10)

# la variabile putem sa dam atat valori cat si expresii de calculare
check_1 = 5>7
print(check_1)

# slicing (taierea)
strx_1 = "Ana e eleva cuminte"
print(strx_1[5:9])


lis_1 = [1,2,3,4,5,6,7]
print(lis_1[2:5])
print(strx_1[::-1])  # [::-1]) asta inverseaza un string, o lista

# range imi creaza un fel de liste de la nr pana la nr cu un step
# range(from, to, step)
for i in range(1, 100, 3):
    print(i)

for i in range(1, 11):
    print(i)

for i in range(10, 0, -1): # punem -1 ca sa il ia in ordine descrescatoare
    print(i)

# identarea inseamna distanta de la margine; trebuie sa fim atenti la identare, sa avem comenzile identate


# De ce nu merge \ in path-uri
exemplu_path