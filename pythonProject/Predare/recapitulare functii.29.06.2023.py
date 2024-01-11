# forma simpla
suma = 3+4+5
print(suma)

def suma_3(a, b, c):   # a b c sunt argumente, asa se numesc
    suma = a + b + c
    print(suma)

suma_3()
print(suma_3)  # nu merge asa, imi zice unde este stocata in memorie
# functia trebuie apelata
suma_3(3,5,9)

def suma_3_cu_default(a, b=1, c=2):
    suma = a + b + c
    print(suma)
suma_3_cu_default(3)
suma_3_cu_default(3,5)
suma_3_cu_default(10,20,30) #60

#functiile pot fi predefinite in python, precum len, sum, dict, append
# sau pot exista din librariile importate, de ex math.factorial(x)
# sau po fi create de mine, cum am facuut mai sus


# o functie poate executa doar cod sau poate si returna o valoare

var_1 = suma_3_cu_default(1,2,3)
print(var_1) # va printa 6, None - adica executa comenzile din functie, dar nu returneaza nimic


# functie care calculeaza suma unir numere, apoi* 2

def suma_numere_x2(*args):
    # *args inseamna r nedefinit de argumente, adica pot da functii 2, 3 sau 13 argumente
    suma = 0
    for a in args:
        suma += a
    print("un print")
    print("alt print")
    return suma *2
# in return pot pune atat o valoare calculata cat si o operatie de calculare
var_2 = suma_numere_x2(1,2,3)
print(var_2) # va executa tot codul, plus returneaza valoare


# scriu o functie care returneaza 3 valori
# suma, produsul si media a unui nr nedefinit de argumente intregi

def suma_produs_media(*args):
    suma = 0
    produs = 1
    for a in args:
        suma += a # suma imi creste cu a
        produs *= a
    media = suma/len(args)
    return{"suma": suma, "produs": produs, "media":media}
var_3 = suma_produs_media(2,3,4)
print(var_3)


# alta metoda de return

def suma_produs_media_v2_return(*args):
    suma = 0
    produs = 1
    for a in args:
        suma += a # suma imi creste cu a
        produs *= a # aici se inmulteste
    media = suma(len(args))
    # len(args) - nr de argumente pe care le dam functiei, adica imi zice cat trebuie sa impart, d-aia pun len
    return suma, produs, media
# am returnat 3 valori deodata care constituie un tuplu ordonat
var_4 = suma_produs_media_v2_return(2,3,4)
print(var_4)

# asta de mai sus nu merge


# cum dam unei functii un nr nedefinit de argumente cu chei

def exemplu_keywords(**kwargs):
    # kwargs = key-word argument
    for key, value in kwargs.items():
        print(f"Cheia = {key}, valoarea = {value}")
exemplu_keywords(nume="Ion", varsta=15, localitate="Brasov")



def email_personalizat(nume, voucher_procent, *args, **kwargs):
    # in args imi stochez valoarea cumparaturilor, ca apoi sa calculez totalul
    suma_totala = 0
    for cump in args:
        suma_totala += cump

    # magazinele unde poate primi un voucher de 20% din suma totala cumparata pana acum
    magazinele = "" # am initializat un string gol
    for key, value in kwargs.items():
        magazinele += f"Magazinul {key} la adresa {value}\n"
    email_promo = f"""
    Salut {nume}, 
    Iti multumim ca pana acum ai facut cumparaturi in valoare totala de {suma_totala} lei.
    Pentru asta iti multumim cu un voucher de {round(suma_totala * voucher_procent)} lei.
    Acest voucher poate fi folosit la urmatoarele magazine:
    {magazinele}
    
    Cu respect,
    Ion Ionescu
    Manager Lidl
    """.replace("  ", "")
    return email_promo

promo_1 = email_personalizat("Vasile Cumparescu",
                             0.02, 45, 670, 1000,
                             Bucuresti = "strada Vasile Alecsandri",
                             Brasov="Piata Mare")
print(promo_1)


promo_2 = email_personalizat("Shakira",
                             0.12,
                             3000, 20000, 100000, 67890, 1889203,
                             Paris = "Arcul de Triumf",
                             New_York = "Manhatan",
                             Tokyo = "Piata Mare",
                             Bucuresti = "Obor",
                             Stockolm = "Strada Mare")
# *args - nr nedefinit de valori
# **kwargs - nr nedefinit de chei si valoare
print(promo_2)


dictionar = {"nume": "Andrei",
             "localitate": "Budapesta",
             "inaltime": 178}
#cheile
for cheie in dictionar.keys():
    print(cheie)

# valorile
for valoare in dictionar.values():
    print(valoare)

# cheile si valorile
for cheie, valoare in dictionar.items():
    print(f"Cheia {cheie} are valoare {valoare}")





def suma(a,b):
    suma_mea = a+b
    return suma_mea
var_8 = suma(3,4)
print(var_8)



# cu printuri
def suma(a,b):
    suma_mea = a+b
    print("Rezultatul este")
    print(f"rezultatul din functie = {suma_mea}")
    print("Gata")
    return suma_mea
var_8 = suma(3,4)
print(f"Rezultatul stocat in variabila = {var_8}")



def comanda_resturant(**kwargs):
    for produs, cantitate in kwargs.items():
        print(f"Produsul {produs} a fost pregatit cu {cantitate} portii")
    return "Pofta mare"
mananc_azi = comanda_resturant(icre=3, paste=2)
if mananc_azi is None:  # is none inseamna ca nu are valoare, adica nu a dat return vreo valoare
    print("Nu mananci nimic")
else:
    print(mananc_azi)