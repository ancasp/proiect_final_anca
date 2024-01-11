# Recursivitate:
# Scrieți o funcție recursivă pentru a calcula suma numerelor pare de la a la b

#Pentru a calcula suma numerelor pare între două numere a și b folosind o funcție recursiva utilizam următorul cod:
def sum_of_even_numbers_recursive(a, b):
    # Verificăm cazul de bază: dacă a > b, nu avem numere pare între a și b.
    if a > b:
        return 0

    # Verificăm dacă a este un număr par și adăugăm a la suma dacă este cazul.
    if a % 2 == 0:
        return a + sum_of_even_numbers_recursive(a + 2, b)
    else:
        # Dacă a nu este par, trecem la următorul număr par mai mare sau egal cu a.
        return sum_of_even_numbers_recursive(a + 1, b)

# Exemplu de utilizare:
a = 1
b = 100
result = sum_of_even_numbers_recursive(a, b)
print(f"Suma numerelor pare între {a} și {b} este {result}")

# Această funcție sum_of_even_numbers_recursive verifică dacă a este par și, dacă este, adaugă a la suma,
# apoi se reapelează recursiv cu a + 2. Dacă a nu este par, funcția se reapelează recursiv cu a + 1.
# Această procesare continuă până când a devine mai mare sau egal cu b, moment în care funcția se oprește
# și returnează suma numerelor pare din intervalul specificat


# Scrieți o funcție recursivă pentru a calcula cel mai mare divizor comun al două numere întregi.

# Pentru a calcula cel mai mare divizor comun (CMMD) al două numere întregi folosind o funcție recursivă în Python,
# puteți utiliza Algoritmul lui Euclid, care se bazează pe următoarea relație
# b & \text{dacă } a \text{ mod } b = 0 \\
# CMMD(b, a \text{ mod } b) & \text{altfel}
# \end{cases}
# Iată cum puteți implementa acest algoritm într-o funcție recursivă:

def cel_mai_mare_divizor_recursive(a, b):
    if b == 0:
        return a
    else:
        return cel_mai_mare_divizor_recursive(b, a % b)

# Exemplu de utilizare:
num1 = 12
num2 = 6
result = cel_mai_mare_divizor_recursive(num1, num2)
print(f"Cel mai mare divizor comun al lui {num1} și {num2} este {result}")

# Această funcție gcd_recursive primește două numere întregi, a și b, și folosește recursiv algoritmul lui Euclid
# pentru a calcula CMMD. Când b devine 0, funcția se oprește și returnează a, care este CMMD-ul. Funcția se reapelează
# până când b devine 0 prin calcularea restului împărțirii lui a la b.



# Scrieți o funcție recursivă pentru a verifica dacă un număr dat este prim.
# Pentru a verifica dacă un număr dat este prim folosind o funcție recursivă în Python, puteți utiliza următorul cod:

def is_prime_recursive(n, div=2):
    # Verificăm cazurile de bază
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % div == 0:
        return False
    if div * div > n:
        return True

    # Verificăm dacă n este divizibil cu div
    if n % div == 0:
        return False
    else:
        # Continuăm cu următorul divizor potențial
        return is_prime_recursive(n, div + 1)

# Exemplu de utilizare:
num = 29  # Înlocuiți cu numărul pe care doriți să-l verificați
result = is_prime_recursive(num)
if result:
    print(f"{num} este un număr prim.")
else:
    print(f"{num} nu este un număr prim.")

# Această funcție is_prime_recursive primește un număr n și un divizor potențial div (care începe cu 2) ca argumente.
# Funcția verifică mai întâi cazurile de bază:dacă n este mai mic sau egal cu 1, nu este prim; dacă n este 2, este prim.
# În continuare, funcția începe să verifice dacă n este divizibil cu divizorul curent div. Dacă este, atunci n nu este
# prim. Dacă div depășește rădăcina pătrată a lui n, atunci n este prim. Altfel, funcția continuă cu următorul
# divizor potențial prin apelarea recursivă.
# Acest algoritm verifică toți divizorii potențiali între 2 și rădăcina pătrată a lui n, iar dacă niciunul dintre
# aceștia nu divide n, atunci n este considerat prim.



# Scrieți o funcție recursivă pentru a calcula suma cifrelor unui număr dat
# Pentru a calcula suma cifrelor unui număr dat folosind o funcție recursivă în Python, puteți utiliza următorul cod:

def sum_of_digits_recursive(n):
    # Cazul de bază: dacă n are o singură cifră
    if n < 10:
        return n
    else:
        # Se adaugă cifra curentă la suma cifrelor din numărul rezultat după eliminarea cifrei curente
        return n % 10 + sum_of_digits_recursive(n // 10)

# Exemplu de utilizare:
num = 15  # Înlocuiți cu numărul pentru care doriți să calculați suma cifrelor
result = sum_of_digits_recursive(num)
print(f"Suma cifrelor lui {num} este {result}")

# Această funcție sum_of_digits_recursive primește un număr n ca argument. În cazul de bază, când n are o singură
# cifră (adică este mai mic decât 10), funcția returnează direct n, deoarece suma cifrelor unui număr cu o singură
# cifră este însăși cifra respectivă.
# În caz contrar, funcția împarte numărul n la 10 pentru a obține cifra cea mai din dreapta (adică n % 10)
# și adaugă această cifră la suma cifrelor din numărul rezultat după eliminarea cifrei curente (n // 10).Acest proces
# continuă recursiv până când numărul n devine o singură cifră și funcția returnează suma finală a cifrelor.