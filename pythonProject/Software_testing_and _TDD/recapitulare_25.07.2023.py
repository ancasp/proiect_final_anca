"""
Recapitulare:
- toate structurile de date din python sunt OBIECTE

 Variabila:
-  o variabila este un simbol(nume) ce reprezinta un set de valori sau o valoare dintr-un program
- o variabila nu poate fi declarata incepand cu un numar sau un simbol
NU POT FI declarate: !salut = 'salut', 3 = 'trei'
- putem sa face operatii cu ajutorul lor
- variabilele sunt definite de un nume, semnul = si appoi valoarea sau setul de valori
Exemple variabile:
variabila1 = 'data'
x = 6
y = 7
z = [3,4,5,6]

Tipuri de date:
Integer, Float, Bool, String, Liste, Tuple, Dictionare, Set
1. String - (sir de caractere)
- stringurile sunt definite cu ghilimele simple sau ghilimele duble
Exemple:
'Mara are mere'
"Salut"
'3 + 4 = 7'

Operatii de baza:
Slicing(start, step, stop)
Cu ajutorul operatiei de slicing putem crea subseturi ale unui string

- cum aflam prima litera dintr-un string?
Cu ajutorul operatorului de indexare: []
var1 = 'Acesta este un string'
var1[0]
0 reprezinta primul index

- Cum aflam prima litera si urmatoarele 6 folosind slicing?
print(var1[:7]

- Cum putem afla daca un substring se afla intr-un string?
Cu ajutorul cuvantului in. Acesta ne va intoarce un Bool care este False sau True in functie de situatie
print('cuvantul'  in stringul-meu)

 - Cum transformam un sir de caractere in litere mici?
 exemplu_string = "Ana are Mere"
 exemplu_string.lower()

 - Cum transformam un sir de caractere in litere mari?
  exemplu_string = "Ana are Mere"
 exemplu_string.upper()

  - Lungimea unui string?
  len(exemplu_string)

- Cum inlocuim un string cu un substring?
exemplu_string = "Ana are mere si portocale"
exemplu_string = exemplu_string.replace("portocale", "pere")
!!!.replace nu inlocuieste continutul ci returneaza un nou string
Pentru a inlocui variabila, rezultatul trebuie asignat variabilei.

-Cum putem afla lista de cuvinte dintr-un string?
ex = 'Ana are Mere si portocale'
ex.split()

- Cum putem intoarce un string de la ultimul element la primul?
ex = 'Ana are Mere si portocale'
ex[::-1]
Folosim slicing cu step -1 pentru a lista de la ultimul element la primul.
list(reversed(ex)) - folosim reversed

Operatii cu string
 - concatenare:
 nume = 'Anca'
 prenume = 'Spirea'
 nume_prenume = nume + prenume

 - inmultire:
 nume*3 - si ne listeaza numele de 3 ori

2. Bool
Ce este un bool?
Este un tip de date care poate lua doua valori: True(1) si False(2)

Folosim bool pentru comparatii ==

3. Integer (int) numere intregi:
 - numere intregi fara virgula
 - reprezinta toate numere intregi, atat pozitive cat si negative

 x = 5
 y = 723999
 z = -23232

 Operatii cu int:
a=3
b=5
Adunare: a + b
Scadere: a - b
Inmulltire: a * b
Impartire: a / b
Impartirea intreaga: a // b
Restul impartirii: a % b
Ridicarea la putere: a ** b
Operatiile logice: <, >, ==, <=, >=, !=

4. Float(Numerele cu zecimale, fractii)
 - sunt reprezentate cu virgula (punct) mobila
 a = 3.4
 b = 7.2323

 Pot fi reprezentate pana la 16 cifre dupa punct
 Daca este executata o operatie aritmetica intre un int si un float, rezultatul este de tip float de fiecare data

 Formatare float:
 pi = 3.141592653589793
 Pentru a obtine numarul si primele 2 zecimale:
 round(pi, 2)
 f"{pi:.2f}
 "%.2f" % pi


5. Liste ( O structura de date care stocheaza o cloectie ordonata de elemente)
Cum definim o lista?
 - cu paranteze patrate []

 list1 = [] # o lista goala
 list2 = [1, 2, 3, 4] o lista plina
  - primul element din lista?
  lista1[0]
   - ultimul element din lista?
   lista1[-1]
   - cum stergem un element dintr-o lista?
   l = [1, 2, 3, 4, 5, 6]
   l.remove(1) - remove nu intoarce elementul sters si ia valoare ca parametru
   l.pop(0) - pop intoarce elementul la index 0, a index ca parametru

 - Cum sortam o lista?
 l = [3, 5, 7, 6, 2, 1]
 l.sort()
 .sort: sorteaza lista si o si asigneaza catre aceasta
sorted(l)
sorted(l, reverse=True), Pentru a intoarce de la mai mare la mai mic
Sorted nu asigneaza noile valori catre variabila

Cum adaugam un nou element intr-o lista?
l.append(8).
Append adauga la sfarsitul listei

 - Cum adaugam un nou element intr-o lista la un anumit index
 l.insert(2, 10)

  - Cum inlocuim un element dintr-o lista?
- pentru elemente ce contin string putem folosi list comprehension si replace
l = ['mar', 'par', 'banan']
'l = [item.replace('mar', 'castravete' form item in l]'
l[0] = 'castravete' # inlocuim valoarea indexului

6. Tupla
Tupla este o structura de date ordonate ce nu poate fi modificata.
Cum definim o tupla?
 - cu paranteze rotunde
 tupla1 = (1, 2, 3, 4, 5)
  - cum obtinem primul element?
  tupla1[0]

- Nu se pot adauga sau sterge elemente dintr-o tupla. O tupla este imutabila.
!!! O tupla este mult mai rapida si mai eficienta dpdv al stocarii datelor

7. Set
Setul este o structura de date neorodonata care stocheaza elemente unice
Definim un set cu {}
set1 = set() - pt a evita crearea unui dictionar gol
set2 = {1, 2, 3, 4, 5}

Cum putem adauga intr-un set?
set1.add(1)
daca adaugam un element ce exista deja, nu va primi eroare, dar nu va fi duplicat

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

Operatii cu set:
uniunea:
union_set = set1 | set2
intersectia:
intersectie_set = set1 & set2 - apar elementele comune
diferentele
dif1 = set1 - set2  - elementele din set 1 care nu se regasesc in setul 2; se poate si invers set2-set1

8. Dictionar
Structura de date, neordonata, ce stocheaza perechi chei valoare.
Cheile sunt unice si imutabile: (str, int, float, tuple)

Cum definim dictionarele?
cu ajutorul {}
dic1 = {} # acesta este un dictionar gol
dict1 = dict() # aceasta genereaza un dictionar gol

Cum aflam cheile unui dictionar?

9. Functia (o sectiune de cod care poate fi apelata din alte sectiuni ale programului)
Functia grupeaza o logica sau o anumita sarcina si o face mai usor de gestionat sau utilizat

Functia poate fi definita cu ajutorul cuvantului special 'def'
Functia are un nume
Are un set de parametrii  ce pot fi optionali scrisi intre paranteze
Dupa paranteze scriem ":" douoa puncte, ceea ce indica blocul de cod din corpul functiei
Blocul de cod din corpul functiei este intotdeauna la o identare (tab sau 4 spatii) fata de detinirea acesteia.

Functia returneaza intotdeauna un rezultat cu ajutorul cuvantului return.
Funtia este apelata
Daca uitam sa specificam ce anume sa ne returneze, ea va returna None
'None' reprezinta lipsa unei valori sau a unei referinte

"""
cos_fructe = {
    'mar': 5,
    'par': 7,
    'banane': 12,
}
cos_fructe.keys()

def printeaza_ceva():
    print('Acesta este un print')

