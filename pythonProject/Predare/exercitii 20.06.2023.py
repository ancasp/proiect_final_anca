# For loop:
# 1.1. Afișează toate numerele întregi de la 0 la 10.

for numar in range(0,11):
    print(numar)
 # sau
numere_intregi = 0
while numere_intregi <= 10:
      print(numere_intregi)
        numere_intregi += 1

# 1.2. Afișează toate numerele pare de la 1 la 20.

for nr in range(1, 21):
    if nr % 2 == 0:
        print(nr, end= ", ")

# 1.3. Afișează toate numerele impare de la 1 la 20.

for nr in range(1, 21):
    if nr % 2 != 0:
        print(nr, end= ", ")

# 1.4. Calculează suma tuturor numerelor de la 1 la 100.
#V1
suma = 0
for nr in range(1,101):
    suma += nr
print(suma)

#V2
suma = sum(range(1,101))
print(suma)

#V3
suma = (100*101)/2
print(suma)

# 1.5. Calculează suma tuturor numerelor pare de la 1 la 100.
suma = 0
for nr in range(1,101):
    if nr % 2 ==0:
        suma += nr
print(suma)

# 1.6. Afișează toate literele unui șir de caractere.

sir = 'Salut ce mai faci astazi'
lit = set(sir) # setul fiind elemente unice imi extrage toate elementele unice din sir
print(lit) # set returneaza o colectie neordonata/haotica

listx = list(lit)
listx.sort()
print(listx)

# 1.7. Afișează toate literele unui șir de caractere, cu exceptia literelor: f,g,a,w,t,r,y,c
list_litere = []
for lit in sir:
  if lit not in "f,g,a,w,t,r,y,c":
        #print(litera, end= ", ")
        #SAU definesc o lista goala si folosesc append
    list_litere.append(lit.lower())

print(set(list_litere))


# 1.8. Afișează toate valorile dintr-o listă.

listx = [1, 2.3, "Hello", {2,3,4}, [44,55,66]]
for el in listx:
    print(el)

# 1.9. Afișează toate cheile și valorile dintr-un dicționar.

dicx = {"k1": 12,
        "k2": 19.2,
        "k3": [4,5,6]}
for key, value in dicx.items():
    print(f"Cheia {key} are valoarea {value}")

# 1.10. Afișează produsul tuturor elementelor dintr-o listă de numere întregi.

numere_intregi = [1, 45, 23, 2, 199]
produs = 1
for nr in numere_intregi:
    produs *= nr
print(produs)

# While loop:
# 2.1. Afișează toate numerele întregi de la 0 la 10.
#V1
nrinitial = 0
while True:
    print(nrinitial)
    nrinitial += 1
    if nrinitial>10:
        break

#V2
nri = 0
while nri <= 10:
    print(nri)
    nri += 1

# 2.2. Afișează toate numerele pare de la 1 la 20.

nri = 0
while nri <= 20:
    if nri % 2 == 0:
        print(nri)
    nri += 1
# 2.3. Afișează toate numerele impare de la 1 la 20.



# 2.4. Calculează suma numerelor de la 1 la 100.

suma = 0
nr = 1
while nr <= 100:
    suma += nr
    nr += 1
print(suma)

# 2.5. Calculează suma numerelor pare de la 1 la 100.


# 2.6. Afișează primele 10 numere al caror predecesor e divizibil cu 5 si succesor divizibil cu 13

nr_max = 10 # nr de numere pe care le printeaza, adica vom avea 10 numere printate
nr = 4  # de unde incepem numaratoarea
while True:
    if ((nr -1) % 5 == 0) and ((nr + 1) % 13 == 0):
        print(nr)
        nr_max -= 1
    nr += 1
    if nr_max == 0:
        break

# 2.7. Folosind o variabilă index, parcurge toate literele unui string și afișează-le.

strx = "'Salutare ce mai faci"
ix = 0
while ix < len(strx): # daca lungimea unui iterabil (string, list etc) este de 14 elemente ultimul index va fi 13
    print(strx[ix])  # si spatiile au index
    ix += 1

# 2.8. Folosind o variabilă index, parcurge toate elementele unei liste și afișează-le.


# 2.9. Cerere de parolă: setează o parolă și folosește while pentru a cere utilizatorului să introducă parola,
# până când aceasta este corectă.

parola_de_ghicit = "SDAhello"
while True:
    ghiceste_parola = input ("Ce parola crezi ca este =")
    if ghiceste_parola != parola_de_ghicit:
        print("Nu ai ghicit")
    else:
        print("Ai ghicit parola")
        break


# 2.10. Utilizează un loop while pentru a calcula cate numere de la 1 la 10**12 sunt divizibile cu
# 13, 17 si 23 concomitent.
pana_la = 10**8
nr = 10
counter = 0
while True:  # se executa pana cand il opresc din interiorul buclei
    #alternativ while conditie, de ex while nr < 1000:
    if nr % (13*17*23) == 0:  #am verificat daca restul impartirii nr la 13*17*23 este 0
        counter += 1 # aici stocam de cate ori a gasit un nr ce satisface conditia
    nr += 1 # am incrementat (am crescut nr cu o unitate) nr ca sa mearga de la 1 la 10**8 unu cate unu

    if nr> 10**12: # cand ajunge la limita de 10**8 se opreste bucla while
        break


print(f"Sunt {counter} numere divizibile cu 13*17*23")