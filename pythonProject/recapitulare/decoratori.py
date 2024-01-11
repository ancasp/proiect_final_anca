from time import perf_counter, sleep
from random import randint, choices
import string
# randint ma ajuta sa aleg un nr random de la a la b
# perf counter - ne ajuta  sa calculam performanta, cat timp dureaza o anumita executie
def masoara_performanta(func):
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        rezultatul = func(*args, **kwargs)
        took_time = perf_counter() - start_time
        print(f"Functia s-a executat in {took_time} secunde")
        return rezultatul
    return wrapper

@masoara_performanta
def f_1():
    print("S-a inceput")
    # iau o pauza de la executare
    sleep(3)
    print("S-a executat")
f_1()


#1,1,2,3,5,8,13,21......  asta e sir fibonacci
@masoara_performanta
def fibonacci_recursiv(n):
    if n in [1,2]:
        return 1
    else:
        return fibonacci_recursiv(n-1) + fibonacci_recursiv(n-2)
print(fibonacci_recursiv(20))
# decoratorul de masurare a performantei nu  functioneaza pt functii recurente, adica care se apeleaza pe ele insele

# creez o functie cu un nr de elemente avand litere random
@masoara_performanta
def lista_elemente_random(size):
    lista = []
    for i in range(size):
        lungimea_cuv = randint(3,12)
        cuvant_random = "".join(choices(string.ascii_letters, k=lungimea_cuv))
        lista.append(cuvant_random)
    return lista
l_1 = lista_elemente_random(10**6)
print(l_1[:3])

# decorator care imi zice la ce ora s-a inceput executarea functiei si la ce ora s-a terminat
from datetime import datetime
now = datetime.now()
print(now)

def inceput_final_ora(func):
    # func este functia pe care o voi decora
    def wrapper(*args, **kwargs):
        # *args, **kwargs - acestea sunnt argumentele functiei pe care o voi decora
        ora_inceput = datetime.now()
        print(f"Executarea {func.__name__}s-a inceput la ora {ora_inceput}")

        rez = func(*args, **kwargs)

        ora_final = datetime.now()
        print(f"Executarea {func.__name__}s-a terminat la ora {ora_final}")
        return rez
    return wrapper

@inceput_final_ora
def lista_elemente_random(size):
    lista = []
    for i in range(size):
        lungimea_cuv = randint(3,12)
        cuvant_random = "".join(choices(string.ascii_letters, k=lungimea_cuv))
        lista.append(cuvant_random)
    return lista
