# Creati un algoritm pentru conjectura Collatz
# https://www.scientia.ro/blogurile-scientia/safari-prin-lumea-stiintei/8287-toate-drumurile-duc-catre-1-conjectura-lui-collatz.html
# Scientia.roScientia.ro
# Conjectura lui Collatz. Toate drumurile duc către 1
# O problemă dificilă de matematică spune că urmând 2 reguli simple toate numerele inițiale ajung la numărul 1.

# Conjectura lui Collatz, cunoscută și sub numele de problema 3n+1, este o problemă simplă de matematică care spune că,
# începând de la orice număr natural pozitiv n, următoarele două reguli simple duc întotdeauna la numărul 1:
#
# Dacă n este par, împărțim n la 2.
# Dacă n este impar, înmulțim n cu 3 și adăugăm 1.
# Chiar dacă aparent simplă, conjectura lui Collatz este încă un mister în matematică și nu a fost dovedită sau
# infirmată pentru toate valorile lui n. Cu toate acestea, pentru majoritatea numerelor n testate, aceasta pare
# să fie valabilă.
#
# Iată un algoritm Python simplu care calculează șirul de numere generate de regurile conjecturii lui Collatz
# pentru un anumit număr n și numără câte operații sunt necesare pentru a ajunge la 1:

def collatz_conjecture(n):
    steps = 0  # Contor pentru numărul de pași

    while n != 1:
        if n % 2 == 0:
            n = n // 2  # Dacă n este par, împărțim la 2
        else:
            n = 3 * n + 1  # Dacă n este impar, înmulțim cu 3 și adăugăm 1

        steps += 1  # Incrementăm numărul de pași

    return steps

# Exemplu de utilizare:
n = 6  # Sau oricare alt număr natural pozitiv
steps = collatz_conjecture(n)
print(f'Numărul de pași pentru a ajunge la 1 din {n} este {steps}.')

# Acest algoritm primește un număr natural pozitiv n, aplică regulile conjecturii lui Collatz și returnează numărul de
# pași necesari pentru a ajunge la 1. Puteți testa algoritmul cu diferite valori ale lui n pentru a vedea cum funcționează.