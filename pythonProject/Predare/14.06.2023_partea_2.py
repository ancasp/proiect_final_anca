# operatori aritmetici

num_1=13
num_2=5
# +,-*,/

print(13**5) # 13 la puterea 5
print(13//5) # impartirea fara rest
print(16%5) # restul impartirii

# Operatori de comparare
print(num_1==num_2) # == inseamna verificarea egalitatii
num_3=3+4
num_4=2+5
print(num_3==num_4)

print(4!=5) # !=inseamna nu este egal cu
print(4<8)
print(4>=3)

# Assignment operations
# =este cel mai clasic operator de assignment
num_5=102
num_5+=3 # += se aduna 3 la el insasi, echivalent cu a scrie num_5=num_5+3
print(num_5)

num_6=12
num_6*=3 # echivalent cu num_6=num_6*3
print(num_6)

# Operatori de identitate is&is not
var_1=7
var_2=7
print(var_1 is var_2)
# ==verifica daca doua variabile sunt egale ca valoare
# is verifica daca doua variabile fac referire la acelasi punct in memorie

var_1=6.2
var_2=3*2+0.2
print(var_1 is var_2)

# operatori logici and, or & not
var_3=7>4
# print(var_3, type(var_3))
var_4=9>8
print(var_3 and var_4) # true and True=True
var_5=9>10 # False
print(var_3 and var_5) # True and False=False
print(var_3 or var_5) # True or False= True
var_6=3>10
print(var_5 or var_6) # False or False=False. True or True=True
print(var_5 and var_6) # False and False=False, True and True= True
print(not var_3) # not True=False si vice versa

variabila_123=12
print(variabila_123)

print("Ceva" + 5)

print("Ceva" + "Frumos") #operatiunea de concatenare=uneste 2 texte
# Varianta cu spatiu
print("Ceva"+" "+"Frumos")
# Pt a edita in mai multe locuri in acelasi timp, tin apasat ALT si click unde am nevoie
print("ceva "+"Frumos")
print("Ceva"+ " Frumos")
print(3/0)

# Operatori de membership
print("doi" in "doi oameni frumosi") # True
print("Oameni" in "doi oameni frumosi")
# python este case sensitive, conteaza daca scriem cu majuscula sau litera mica

# ASCII - sistem de encoding
# are doar 127 simboluri, foarte limitar, de ex nu putem scrie cu diacritice
# Python foloseste un sistem de encoding numit utf-8, contine in jur 65mii

#Spatiile in python
var_1 = 5 # exemplu de spatiu care duce la nefunctionarea programului, syntax error
var_1 = 5 #  deseori spatiile in python sunt folosite pur pentru estetica
var_2 = 5 + 7 + 8 + 3.56 * 17 # cu spatiu arata mai bine estetic

