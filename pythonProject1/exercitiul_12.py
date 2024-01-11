# Rezolvați folosind Comprehension:
# Creati o lista cu toate numerele de la 10 la 10 mii, care sunt divizibile cu 7 si se termină cu 4.

# Puteți crea o listă cu toate numerele de la 10 la 10.000 care sunt divizibile cu 7 și se termină cu 4 utilizând o
# list comprehension în Python. Iată cum puteți face acest lucru:
numbers = [num for num in range(10, 10001) if num % 7 == 0 and num % 10 == 4]
print(numbers)

# Această list comprehension creează o listă numită numbers care conține toate numerele de la 10 la 10.000 care
# îndeplinesc condițiile:
# num % 7 == 0: Numărul este divizibil cu 7.
# num % 10 == 4: Numărul se termină cu 4.
# Rezultatul este o listă care conține toate aceste numere.


# Generati o listă cu toate cuvintele mai mici de 4 caractere dintr-un text.
# Pentru a genera o listă cu toate cuvintele mai mici de 4 caractere dintr-un text folosind o
# list comprehension în Python, puteți utiliza următorul cod:
text = "Acesta este un text de exemplu cu cuvinte mai mici de 4 caractere."
words = text.split()  # Divizăm textul în cuvinte

short_words = [word for word in words if len(word) < 4]

print(short_words)
# Acest cod face următoarele etape:
# Definește un text dat în variabila text.
# Utilizează metoda split() pentru a împărți textul în cuvinte și le stochează în lista words.
# Utilizează o list comprehension pentru a crea lista short_words, care conține doar cuv cu mai puțin de 4 caractere.
# Afișează lista short_words, care conține cuvintele căutate.
# Rezultatul va fi o listă cu toate cuvintele din text care au mai puțin de 4 caractere.



# Generați o listă cu toate perechile posibile de numere întregi de la 1 la 10, de ex [(0,0), (1,9), (2,2)....]
# Pentru a genera o listă cu toate perechile posibile de numere întregi de la 1 la 10 folosind o list comprehension
# în Python, puteți utiliza următorul cod:
pairs = [(x, 10 - x) for x in range(11)]
print(pairs)
# Această list comprehension creează o listă numită pairs care conține toate perechile posibile de numere întregi
# de la 1 la 10. Folosim range(11) pentru a itera prin numerele de la 0 la 10, iar apoi construim perechile (x, 10 - x)
# pentru fiecare valoare x din acest interval.
# Rezultatul va fi o listă de perechi de numere, cum ar fi [(0, 10), (1, 9), (2, 8), ...].


# Generați o listă cu toate perechile de nr întregi de la 1 la 10, cu condiția ca primul nr să fie mai mic ca al doilea
# Pentru a genera o listă cu toate perechile posibile de numere întregi de la 1 la 10, cu condiția ca primul număr să
# fie mai mic decât al doilea, puteți utiliza o list comprehension în Python astfel:
pairs = [(x, y) for x in range(1, 11) for y in range(x + 1, 11)]
print(pairs)

# Această list comprehension generează toate perechile posibile de numere întregi de la 1 la 10, unde primul număr x
# este mai mic decât al doilea număr y. Iterăm prin toate valorile posibile pentru x în intervalul [1, 10],
# iar pentru fiecare x, iterăm prin toate valorile posibile pentru y în intervalul [x+1, 10]. Astfel,
# obținem toate perechile dorite.
# Rezultatul va fi o listă de perechi de numere, cum ar fi [(1, 2), (1, 3), (1, 4), ...].

# Generati o listă cu toate fișierele dintr-un folder care au extensia .pdf (hint: os.listdir(folder) si endswith)
# Pentru a genera o listă cu toate fișierele dintr-un folder care au extensia .pdf folosind o list comprehension în
# Python, puteți utiliza următorul cod, având în vedere că biblioteca os este folosită pentru manipularea fișierelor
# și directoarelor:

import os

folder_path = "C:/Users/ancas\Desktop\docs SDA"  # Înlocuiți cu calea către folderul dorit

pdf_files = [f for f in os.listdir(folder_path) if f.endswith(".pdf")]

print(pdf_files)

# Asigurați-vă că înlocuiți "calea_catre_folderul_tau" cu calea către folderul în care doriți să căutați fișierele PDF.
# Această list comprehension va crea o listă cu toate fișierele din folderul specificat care au extensia .pdf.