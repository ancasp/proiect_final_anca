# Exercitiul 1
# initializati o lista goala si o variabila. Adaugati pe rand 7 elemente in lista care reprezinta numarul la
# puterea index a acelui numar.
# De ex pentru 3 avem:
# [1, 3, 9, 27,...] adica [3*0, 3*1 etc]

lista_goala = []
variabila = 2

lista_goala.append(variabila**0)
lista_goala.append(variabila**1)
lista_goala.append(variabila**2)
lista_goala.append(variabila**3)
lista_goala.append(variabila**4)
lista_goala.append(variabila**5)
lista_goala.append(variabila**6)
print(lista_goala)

listx = []
nr_1 = 7

listx.append(nr_1**0) # append adauga in lista; insiruirea inseamna ca am adaugat pe rand 7 elemente;
listx.append(nr_1**1) # nr_1**0 inseamna numarul la puterea index a acelui nr, adica 7 la puterea 1, 7 la puterea 2 etc
listx.append(nr_1**2) # index inseamna nr de ordine
listx.append(nr_1**3)
listx.append(nr_1**4)
listx.append(nr_1**5)
listx.append(nr_1**6)

print(listx)


# Exercitiul 2
# Aveti o lista de 7 localitati. Extrageti primele 3 localitati in variabila loc_3

localitati = ["Barcelona", "Madrid", "Valencia", "Alicante", "Malaga", "Sevilla", "Castellon"]
print(localitati[:3])

loc_3 = ["Bucuresti", "Ploiesti", "Timisoara", "Cluj", "Iasi", "Suceava", "Arad"]
print(loc_3[:3])

# ultimele 3 localitati
print(localitati[-3:])

# alta varianta
loc_7 = []
loc_7.append(["Iasi", "Constanta", "Bucuresti", "Timisoara"])
# print(loc_7)
print(loc_7[2:])

# Apoi extrageti ultimele 3 litere ale localitatii a 4-a in variabila lit_3

lit_3 = loc_3 [3][-3:]
print(lit_3)

localitati = ["Barcelona", "Madrid", "Valencia", "Alicante", "Malaga", "Sevilla", "Castellon"]
localitati = localitati[5][:2]
print(localitati)

# In lista cu localitati, modificati prima localitate sa aiba valoarea "Caracal"
loc_3[0] = "Caracal"
print(loc_3)

# schimbati a treia cu "Bucuresti"

localitati = ["Barcelona", "Madrid", "Valencia", "Alicante", "Malaga", "Sevilla", "Castellon"]
localitati[3] = "Bucuresti"
print(localitati)

# Generati un raport despre lungimea listei de localitati, de genul:
# "Lista cu localitati are 7 elemente"
# Hint: f-strings si len(lista)
print(len(loc_3))
print(f"Lista cu localitati are {len(loc_3)} elemente")

orase = ["Barcelona", "Madrid", "Valencia"]
print(len(orase))
print(f" Lista cu orase are{len(orase)} elemente")


# sortati lista de localitati in ordine alfabetica inversa, de la z-a
loc_3.sort(reverse=True)
print(loc_3)

orase = ["Madrid", "Barcelona", "Valencia"]
orase.sort(reverse=True)
print(orase)

# adaugati 3 noi localitati in lista de localitati.
loc_3 = ["Bucuresti", "Ploiesti", "Timisoara", "Cluj", "Iasi", "Suceava", "Arad"]
localitati_noi = ("Satu Mare", "Deva", "Galati")
loc_3.extend(localitati_noi)
print(loc_3)

oraseRo = ["Satu Mare", "Deva", "Galati"] # de ce aici am pus [] si mai jos () ?????
orase_noi = ("Cluj", "Timisoara", 1)
oraseRo.extend(orase_noi)
print(oraseRo)


# Exercitiul 3
#Creati un dictionar cu membrii familiei voastre fictive. Dictionarul trebuie sa contina urmatoarele informatii:
#Nume, prenume, nickname, data nasterii, mancaruri preferate, 3-4 locuri care le-a vizitat,
#adresa curenta, cei mai buni 2 prieteni (despre prieteni spuneti numele, data nasterii)

familia =  {"Nume": "Soare",
        "Prenume": ["Maria", "Ion", "Andrei", "Andreea"],
        "nickname": ["Mary", "Jhon", "Andi", "Andre"],
        "DOB": ["01 martie 1965", "15 aprilie 1960", "20 septembrie 1990", "21 iunie 1995"],
        "mancaruri preferate": ["supa", "musaca", "sarmale", "peste"],
        "locuri": ["Suceava", "Ploiesti", "Berlin", "Barcelona", "Roma"],
        "adresa": ["Bucuresti", "Calea Victoriei", "nr": 100 ],
        "prieteni": {"nume_pr": "Catalin"}}        }

print(DOB.keys())

# Accesati data nasterii a celui de-al 2-lea prieten

# Accesati ultimul loc vizitat

# Adaugati inca un membru al familiei

# verifica daca data nasterii a tatalui este "1976-12-29"

# extrageti toate cheile de nivel 1 ale dictionarului.



# Exercitiul 4
#Construiti un dictionar care sa contina date de tip string, int, float, bool si list. Poate fi despre orice
#doriti acest dictionar (animale, meteo, bursa de valori, retete de mancare whatever)





