#tipuri de date in python:
#int, float
#str
#bool
#List, Tuple
#Dict
#Set

#Variabile & Operatori

#Operatiuni cu strings

#Collections

#Control flow: while, for, if

#Functions

#Modules

# functie care genereaza reversul unui string
def reversul(textul):
    return textul[::-1]
strx = "Ionel e baiat bun"
print(reversul(strx))

#secventa collatz
# pentru orice nr, daca facem urmatoarele operatii cu el, oricand ajungem la 1
# luam numarul N, daca e par ->/2, altfel 3*N + 1

N = 7
while N !=1:
    print(N, end= ", ")
    if N % 2 ==0:
        N = N//2
    else:
        N = N*3 + 1
    print(N, end=", ")

#File Ops