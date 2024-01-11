# Calculez (a*b*b....) + (a+b+c+....)
# despartim problema in sub-capitole

def inmultire_num(*args):  # args adica avem mai multe elemente nedeterminate, adica oricate
    produs = 1
    for arg in args: # pentru argumente in args
        if isinstance(arg, int):
            produs *= arg
    return produs

def adunare_num(*args):
    suma = 0
    for arg in args:
        if isinstance(arg, int):
            suma += arg
    return suma

rezultat = inmultire_num(1, 3, "ABC", 4, 5) + adunare_num(1, 3, "ABC", 4, 5)
print(rezultat)

# 20. Creati o functie care verifica daca un numar e prim

from math import sqrt
nr = 57
if nr < 2:
    print("Nu e prim")
# trebuie sa verific de la 2 pana la radical(n) + 1
for index in range(2, int(sqrt(nr)) + 1):
    if nr % index == 0:
        print("Nu e prim")
        break

#rezolvare problema 20, insa s-a inceput cu ce e mai sus si apoi s-a definit functia
def este_prim(nr):
    if nr < 2:
        return False
    for index in range(2, int(sqrt(nr)) + 1):
        if nr % index == 0:
            return False
    return True
print(este_prim(nr))


# 21. Creati o functie care primeste un numar variabil de argumente si returneaza un text cu urmatorul continut:
# "Primul argument este...
# nr. 2 = ...
# nr.3 = ...
# ..."

def numerotare_argumente(*args):
    continut = f"Primul argument este: {args[0]}\n" # Ion va fi primul argument deoarece args are index 0
    if len(args)>1: # in cazul in care lista de argumente este mai mare ca 1, variabila continut imi va stoca fiecare argument numerotat pe un rand diferit
        for index_arg in range(1, len(args)): # range-ul in care se va incadra functia for este de la 1 (indexul 0 deja l-am folosit, pana la lungimea listei, in acest caz 5
            continut = continut + f" Nr. {index_arg+1} = {args[index_arg]}\n"
    return continut
print(numerotare_argumente("Ion", 2, 4.7, "masa", 8))

# 22. Creati o functie care citeste textul dintr-un fisier .txt

def citire_text():
    path_text = r"aici pun fisierul.txt"
    with open(path_text, "r") as file_text:
        text = file_text.read()
    return text
print(citire_text())

# 23. Scrieti o functie care citeste un fisier si returneaza cate cuvinte sunt in ele (nu cate litere). Hint: folositi .split()

def numaratoare_cuvinte():
    path_text = r"aici pun fisierul.txt"
    with open(path_text, "r") as file_text:
        text = file_text.read()   # read citeste tot textul
    return len(text.split())
print(numaratoare_cuvinte())

# 24. Scrieti o functie care returneaza cate linii sunt in acest fisier

def numaratoare_linii():
    path_text = r"aici pun fisierul.txt"
    with open(path_text, "r") as file_text:
        text = file_text.readlines()   #readlines citeste liniile din text
    return f"In documentul'textul meu.txt' textul este dispus pe {len(text)} linii"
print(numaratoare_linii())


# 25. Aveti o lista cu 4 nume. Creati iterativ (cu for) fisiere .txt cu denumire fisierului numele respectiv si continutul "Numele {..} are {..} caractere"
# De exemplu pentru o lista cu ["Ana", "Ion"] se vor crea 2 fisiere Ana.txt si Ion.txt cu textul aferent.

def creare_fisiere_txt(*args):
    path_fisiere = "aici pun link-ul din calculatorul meu"
    for nume in args:
        with open (f"{path_fisiere}/{nume}.txt", "w") as file_nume:
            file_nume.write(f"Numele {nume} are {len(nume)} caractere")
creare_fisiere_txt("Ion", "Marius", "Ionela", "Tudor")

# 26. Aici aveti nevoie sa cautati pe net cum se face, sa cititi documentatie, e si asta o abilitate non-triviala a unui programator:
# Creati un fisier excel cu pandas, format dintr-un dictionat
# Apoi dintr-o lista de liste
# Scrieti aceste 2 fisiere in acelasi fisier excel, unui cu numele foii from_dict si alta foaie from_list_list
# Sortati tabelul creat din dictionar dupa una din coloane.

import pandas

path_folder = "aici pun calea folderului"
dictionar_elevi = {"nume": ["Maria", " Mirabela", "Alexandru", "Costica"],
                   "varsta": [19, 12, 15, 17]}
lista_note_BAC = [[10, 8, 5], [6, 7, 6], [7, 10, 10], [9, 10, 8], [10, 10, 10]]

tabel_dictionar = pandas.DataFrame(dictionari_elevi)
tabel_note_BAC = pandas.DataFrame(lista_note_BAC, columns=["Romana", "Mate", "Bio"])

tabel_dictionar.to_excel(f" {path_folder}/Dictionar_elevi.xlsx", index=False)
tabel_note_BAC.to_excel(f"{path_folder}/Note_BAC.xlsx", index=False)

with pandas.ExcelWriter("aici pun folderul.xlsx") as writer:
    tabel_dictionar.to_excel(writer, sheet_name = "from_dict", index=False)
    tabel_note_BAC.to_excel(writer, sheet_name = "from_list", index=False)

citire_excel = pandas.read_excel ("aici pun calea", sheet_name = "from_dict")
excel_sortat = citire_excel.sort_values(by="varsta")

with pandas.ExcelWriter ("aici pun calea.xlsx") as writer:
    excel_sortat
