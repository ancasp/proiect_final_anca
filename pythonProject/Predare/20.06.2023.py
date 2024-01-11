#Recapitulare

dx = {"prenume": ["Ion", "Vasile", "Elena"],
      "varste": [23, 29, 48]}

dx["prenume"].append("Andrei")
dx["varste"].append(50)
print(dx)

dx["prenume"].extend(["Ion Senior", "Elena Senioara"])
dx["varste"].extend([78, 90])
print(dx)

alti_bunici = {"prenume": ["George", "Anastasia"],
               "varste": [89, 90]}

dx["prenume"].extend(alti_bunici["prenume"])
dx["varste"].extend(alti_bunici["varste"])
print(dx)

#CURS
varsta = 0
while varsta <= 50:
    if varsta % 4 ==0:
        print(varsta)
        varsta += 1

#While loops executa un bloc de instructiuni atat timp cat se respecta o conditie

#Atentie la infinite loop
numar = 12
while numar <= 20: #while conditie - codul se executa atat timp cat conditia este True
    print(numar)
    numar += 1

numar = 12
while True: #while conditie - codul se executa atat timp cat conditia este True
    print(numar)
    numar += 1
    if numar > 1000:
        break #break iese din bucla/loop
#putem iesi din bucla fie din conditia de la while, fie dintr-o conditie din interiorul buclei

numar = 5
while numar <= 102:
    numar += 1
    if numar % 10 == 0: # daca numarul se divide la 10, atunci trece peste el si nu il printeaza
        continue #merge la inceputu; buclei si ignora codul de mai jos
    print(numar)
    # daca se divide inseamna ca il ignora, adica nu se printeaza

numar = 5
while numar <= 102:
    numar += 1
    if numar % 10 == 0:
        pass    #pass nu face nimic, folosit ca umplutura work in progress, cod la care vei reveni
    print(numar)

while True:
    pass #voi pune un loop care face.....
if 1==1
    pss #voi face altceva.....

#for
varste = [2, 3, 78, 49, 15, 67]  # lista este un element iterabil, adica putem sa scoatem fiecare element din el
# print(varste[5])
for element in varste:   #element il denumim cum vrem noi; for merge pe fiecare element din lista
    print(element)

    #while este nedeterminat, for este determinat de lista/iteratorul pe ccare il accesam

nume = "Alexandru"
for litera in nume:
    print(litera)

# Obiectele iterabile in python - sunt acele care au mai multe elemente individuale
#si putem itera asupra lor. A itera - extragem elementele unul cate unul cu for loop


tupx = ("Ana, "Ion", "Elena")
        for el in tupx
        print(el)

dictx = {"nume": "ion",
         "varsta": 12,
         "adresa": {"str": "ABC", "nr":12}}

for cheie in dictx.keys():
    print(cheie)

for valoare in dictx.values():
    print(valoare)
    print ("---------")

for cheia, valoare in dictx.items(): #items ne printeaza si cheile si valorile; accesam cheile si valorile simultan
    print(f"Cheia este = {cheia}, Valoarea = {valoare}")

"""
Obiecte iterabile in python sunt de urmatoarele tipuri
list
tuple
string
dictionare
set
generatoare - intermediate

Interable - un obiect in python poate fi parcurs pe fiecare element in parte cu for loop.
Interation - procesul prin care accesam fiecare element
"""

varste = [2, 3, 78, 49, 15, 67, 65, 99, 40]
for nr in varste:
    if nr % 5 != 0: #daca restul impartirii la 5 nu este 0, adica nu e divizibil cu 5
    continue #daca conditia e indeplinita, merge la urmatorul element fara a executa codul de jos
 print(nr)

 for nr in varste:
     if nr %5 == 0:
         break #iese din bucla imediat ce ajunge la un element divizibil cu 5, adica restul impartitii la 5=0
         print(nr)

for nr in varste:
    if nr % 5 == 0:
        pass # pass-ull este ignorat
    print(nr)


cuv = "Alxeandrul cel mare"
#print toate literele care sunt vocale din cuvant
for litera in cuv:
    if litera.lower() in 'aeiou': #daca nu puneam lower imi printa fara A
    print(litera, end = ", ") # imi printeaza pe acelasi rand

#print toate literele care nu sunt vocale, fara duplicitate
cuv = "Alexandrul cel mare"
lista_litere_non_vocale = []
for litera in cuv:
    if litera.lower() in "aeiou ":
        continue
    lista_litere_non_vocale.append(litera)  #shift si tab pentru a iesi din ultima conditie
print(set(lista_litere_non_vocale))

#despre set
listx = [1,2,3,1,1,2,3,2,1]
print(listx)
print(set(listx))

listx = [1,2,3,4,5,6,7]
for el in listx:
    if el % 3 == 0:                             #identari???
        print(f"{el} este divizibil cu 3")   #trebuie sa fim atenti carei structuri ii apartine fiecare actiune
        continue
    print(f"{el} nu este divizibil cu 3")

#printeaza de la 1 la 20 din 2 in 2
#for el in [1,3,5] #ar trebui introduse manual si nu introducem manual

nr = 1
while nr <= 20:
    print(nr)
    nr += 2

for el in range(1, 20, 2): #range construieste o lista cu elemennte de la start pana la end din step in step
print(el)
#range (start, end, step); de la 1 inclusiv la 20 excusiv  din 2 in 2

for el in range(1, 20): #step by default este 1, adica putem sa nu il punem si va avea valoarea implicita 1
print(el)

for el in range(200, 1, -4): #de la 200 inclusiv pana la 1 excusiv din 4 in 4 descrescator
    print(el, end=", ") #200, 196, 192, 188, 184


ceva_range = range(1,10,2)
print(ceva_range)  #range(1,10,2)
#ca sa extragem lista din obiectul range, folosim functia list

print(list(ceva_range))



nume = ["Ion", "Andreea", "Ion", "Ana", "Ana"]
for n in nume:
    indexul_n = nume.index(n)   #PRIMUL index unde se gaseste valorea; acesta este modul incorect de a accesa indexul
    print(f"Elementul cu indexul {indexul_n} are valoarea = {n}")

nume = ["Ion", "Andreea", "Ion", "Ana", "Ana"]
for index, n in enumerate(nume):
    print(f"Elementul cu indexul {index} are valoarea = {n}")

print(enumerate(nume)) #obiect logic (generator) care imi stocheaza logica de accesare a indexului si valorii
print(list(enumerate(nume)))

lista_index = [(0, 'Ion'), (1, 'Andreea'), (2, 'Ion'), (3, 'Ana'), (4, 'Ana')]
for element in lista_index:
    print(element)

for el_1, el_2 in lista_index:
    print(f"el_1 = {el_1}, el_2 = {el_2}")


studenti = [("Ion", 46, "Mecanic Auto"),
            ("Elena", 48, "Miner")]
for nume, varsta, profesie in studenti:
    print(f"{nume} are {varsta} si ocupatia de {profesie}")


# liste [  ex: listax = [1,2,3]
# index [ ex element = listax[1] asta evidentiaza al doilea element din listax
# accesarea elemntelor din dinctionar [  ex: in dictionarul dx = {"nume":"Andrei"}, putem accesa valoarea cheii cu
#valoare = dx["nume"]
#dictionarul se defineste prin { si cheie:valoare
#set { ex" sx = {1,2,3}
#tuple ( ex TX = (1,2,3)
#functii ( ex: print(123), range(1,20), string.lower()....


