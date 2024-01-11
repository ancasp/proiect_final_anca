print(7+9)
print("Salut ce mai faci")
#comentariile in python incep cu #, inseamna ca putem scrie orice, nu se va executa
a=7
# a este variabila, este o eticheta pe care o dam unei valori stocate in memoria calculatorului
# 7 este numar intreg adica int si calss inseamna cum il claseaza/califica/denumirea
print(type(a))
b=7.2
print(type(b))
#float, adica numar rational/real, cu virgula (in python se utilizeaza . ca delimitator)
c="ceva text"
print(c, type (c)) #str=string=text. Tipul de date text este mereu cu ghilimele
d='ceva text 2'
print(d, type(d)) #gilimelele " si ' sunt fix la fel pt strings, adica tipul de date text
e=""""iata aici
am ceva
text pe mai multe randuri"""
print(e,type(e))
#f="ceva aici" \
 # "pe mai multe" \
  #"randuri" #pt text pe mai multe randuri putem folosi doar ghilimele triple
#print(f, type(f))
#pt a comenta mai multe linii deodata, selectam randurile si apasam CTRL+/
"""
Comentarii pe mail multe linii cu triple ghilimele
codul in comentarii va fi ignorat de program, este pt utilizator
niciodata comentariile nu se vor executa
print(2+3) nu se va executa pentru ca e comentraiu"""

g=True
print(g,type(g)) #bool, adica tip de date True sau False

h=False
print(h, type(h)) #tip de date bool, adica tip de date logic adevarat/fals

i=None
print(i, type(i)) #NoneType, adica este tip de date gol

#int, float, str, bool, NoneType

nr_complex=complex(3,4) #3 + 4i
print("Partea reala a numarului complex este =", nr_complex.real)
print("Partea imaginara cu i este =", nr_complex.imag)

nr_complex_v2=3+4j #o alternativa de a scrie un numar complex
print(nr_complex_v2, type(nr_complex_v2))

#denumirea variabilelor
#doar cifre, litere mici si mari si underscore
#nu pot incepe cu cifre
abc9="salut"
print(abc9)

#dpdv estetic, variabilele cu mai multe cuvinte sunt:
snake_case=""
CamelCase=""

var_1 : int=5 #int este un type hint, adica un indiciu al tipului de date intentionat
print(var_1, type(var_1))
var_1:str="cinci"
print(var_1, type(var_1))
var_1:str=4.567 #type hinting nu este o restrictie, ci doar indiciu non obligatoriu
print(var_1, type(var_1))

var_2=3
var_3=4.5
var_4="text"
print(var_2*var_3)
#print(var_3*var_4)
print(var_2+var_4)
var_3 = 4.5
print(type(var_3))
var_7 = 5 + 7j
print(type(var_7))

#print("text"*"ceva")