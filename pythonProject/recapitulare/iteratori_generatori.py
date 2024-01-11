lista = [1, 3, 4]
for element in lista:
    print(element)

# prin metoda iter si apoi next putem sa extragem elementele doar atunci cand avem nevoie de urmatorul
lista_iter = iter(lista)
print(next(lista_iter))


def suma_1_to_x(pana_la):
    suma = 0
    for nr in range(1, pana_la + 1):
        suma += nr
        yield suma

suma_10 = suma_1_to_x(10)
print(suma_10)

# pentru a extrage componentele dintr-un generator, putem itera pe el
for el in suma_10:
    print(el)

# exemplu de functie care returneaza


