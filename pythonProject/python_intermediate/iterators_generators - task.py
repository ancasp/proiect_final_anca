### Iterators and Generators Task ###

###################
# 1. Numbers that can be divided by 7
# 	a. generate with normal iteration function first 100.000 numbers that can be divided by 7
# 	b. do the same thing with an iterator
# 	c. do the same thing with a generator
# 	d. measure the time for each option

from math import sqrt
import timeit
import time

def is_divizibil(n):
    if n % 7 == 0:
        return True

    return False
def get_n_divizibile(n):
    divizibile_cu7 = []
    i = 7
    while len(divizibile_cu7) < n:
        if is_divizibil(i):
            divizibile_cu7.append(i)

        i += 1
    return divizibile_cu7
def div_7_generator(n):
    number = 1
    generated_numbers = 0

    while generated_numbers < n:

        if number % 7 == 0:
            yield number
            generated_numbers += 1

        number += 1
class DivizibileIterator:
    def __init__(self, n):
        self.n = n
        self.numere_generate = 0
        self.numar = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.numar += 7

        if self.numere_generate >= self.n:
            raise StopIteration
        elif is_divizibil(self.numar):
            self.numere_generate += 1
            return self.numar
        return self.__next__()
def genereaza_divizibile_cu7_normal():
    print("NORMAL ITERATION FUNCTION:")
    divizibile_cu7 = get_n_divizibile(100_000)
    print(f"len(divizibile: {len(divizibile_cu7)}")

    i = 7
    for element in divizibile_cu7:
        print(f"{element}   ---   {i}", end="\r")
        i += 1

    # print(divizibile_cu7)

def genereaza_divizibile_cu7_iterator():
    print("ITERATOR OPTION:")
    divizibile_no_iterator = DivizibileIterator(100_000)
    i = 0
    for element in divizibile_no_iterator:
        print(f"{element} ----   {i}", end="\r")
        i += 1
    print ("                                 Divizibile generate! ")

def genereaza_divizibile_cu_7_generator():
    div_7_no_generator = div_7_generator(100_000)
    i = 0
    for element in div_7_no_generator:
        print(f"{element}   ---   {i}", end="\r")
        i += 1

    print("Divizibile cu 7 prin generator  !")

def main():

    genereaza_divizibile_cu7_normal()
    genereaza_divizibile_cu7_iterator()
    genereaza_divizibile_cu_7_generator()

# 2. Control digit
# 	a. re-create point a, b, c from ex.1 but this time with control digit for first 100.000 numbers
# 	control digit = sum all digits of a number until you get 1 digit (ex: 476 => CD = 4+7+6 = 17 -> 1+7 = 8)
###################


if __name__ == "__main__":
    main()

# functia zip - iterez din prima lista cu cele din a doua lista
# odd numbers -  sunt numerele impare
# even numbers - sunt numerele pare