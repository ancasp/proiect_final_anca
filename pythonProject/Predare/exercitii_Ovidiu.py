# 1. Afișați în consolă rezultatul expresiei: 9 * (12-5) - 2**3
var_1 = (9 * (12-5) - 2**3)
print(var_1)

# 2. Se știe că Andrei are 7 mere. Ana are de 3 ori mai multe mere decât Andrei,
# iar Ștefan are de 49 de ori mai multe mere decât Andrei. Să se afle câte mere au cei
# trei copii în total folosindu-se o expresie care conține adunarea, înmulțirea și ridicarea la putere (+,*,**).

andrei = 7
print(andrei)
ana = andrei*3
print(ana)
stefan = andrei*(7**2)
print(stefan)
mere_total = andrei+ana+stefan
print(mere_total)

# 3. Creați un convertor de timp, transformând astfel orele și minutele introduse de la tastatură în secunde.
# Exemplu: Pentru ore=5, minute=54, se va tipări 21240 de secunde.

ore = int(input("Va rugam sa introduceti numarul de ore aici: "))
minute = int(input("Va rugam sa introduceti numarul de minute aici: "))
# ore_minute = [int(input("ore: ")), int(input("minute: "))]
secunde = (ore * 3600) + (minute * 60)

print(f"Rezultatul este {secunde} secunde")

# 4. Alex a încheiat o cursă pe locul al x-lea (x - variabila introdusă de la tastatură).
# La sosire Alex a aflat că fiecare al y-lea alergător a fost descalificat. Pe ce loc este Alex acum?
# Exemplu: x=2012, y=7; se tipărește: "Alex a terminat pe locul 1725".

x = int(input("Alex a ocupat initial locul: "))
y = int(input("Au fost descalificati: "))
loc_nou_Alex = x-x // y   # folosim // pentru ca rez sa fie nr intreg, in caz de impartire simpla rez era cu virgula
print(loc_nou_Alex)

# 5. Citim de la tastatură un nr natural a. Puteți calcula suma numerelor naturale mai mici sau egale cu a?

a = int(input("Introduceti un numar natural: "))
suma_nr_naturale = (a*(a+1)) / 2
print(f"Suma numerelor naturale mai mici sau egale cu {a} este {suma_nr_naturale}")


# 6. Folosind un număr de 5 cifre, scrieți un program care să afișeze numărul obținut prin inversarea primelor două
# cifre ale sale cu ultimele două cifre. Exemplu: Pentru numărul 12345, obținem numărul 45312.

# folosim functia de concatenare

nr = input("Te rog sa introduci un nr de 5 cifre: ")
primele_doua = nr[:2]
ultimele_doua = nr[-2:]
inversarea = ultimele_doua + primele_doua

print("Daca inversam, rezultatul este:", inversarea)

####################################################################

nr = input("Te rog sa introduci un nr de 5 cifre: ")
primele_doua = nr[:2]
ultimele_doua = nr[-2:]
# print(primele_doua)
# print(ultimele_doua)
inversarea1 = nr.replace("primele_doua", "ultimele_doua")
print(inversarea1)


# 7. Fie x un număr natural de exact 4 cifre. Să se calculeze produsul cifrelor sale.
# Exemplu: pentru x=2147 se va afișa 56 (2*1*4*7=56).

nr_natural = int(input("Te rog sa introduci un nr. natural de 4 cifre: "))

produs = 1  # am initiaizat produsul cu 1, nu poate fi 0 pt ca e inmultire

while nr_natural > 0:
    indexul = nr_natural % 10
    produs *= indexul
    nr_natural //= 10

print(produs)


# 8. Cifru
# Fifi primește cadou de la fratele mai mare un jurnal. Pentru a-l putea deschide trebuie introdus un cifru,
# număr natural format din 4 cifre. Fratele lui Fifi îi spune un număr de patru cifre și îi precizează că cifrul este
# cel mai mare număr care se obține din acesta prin permutarea circulară cu o poziție a cifrelor numărului.
# Știind numărul, ajutați-l pe Fifi să găsească cifrul pentru a putea deschide jurnalul.
# Exemplu: dacă numărul spus de fratele lui Fifi este 1234, cifrul este 4123 (prin permutarea circulară cu o poziție
# se obțin numerele 2341, 3412, 4123, 1234, iar maximul este 4123).


# 9. Se citește un număr "n" de la tastatură. Dacă acesta aparține intervalului [1, 100], se va afișa mesajul:
# "Este cuprins între 1 și 100". În caz contrar se va afișa: "Nu este cuprins între 1 și 100".

un_nr = input("Introduceti un numar:")
if un_nr in range(1, 101):
    print("Numarul este cuprins intre 1 si 100")
else:
    print("Numarul nu este cuprins intre 1 si 100")


# 10. Se citesc numerele naturale x şi y. Să se calculeze produsul lor, fără a utiliza operatorul de înmulţire.

x = 7
y = 3
produs = 0
for _ in range(y):   # aici am copiat
    produs += x
print(produs)


# 11. Fie n un număr natural cu cel puțin două cifre și maxim nouă cifre. Să se verifice dacă numărul n și numărul
# obținut din n prin interschimbarea primei cifre cu ultima cifră sunt ambele numere prime.
# Exemplu: numărul 137 nu îndeplinește condițiile deoarece 731 (nr obținut după interschimbarea cifrelor)nu este prim.
# Numărul 179 îndeplinește condițiile deoarece și 179 și 971 sunt numere prime.


# 12. Într-o cutie se află 300 de bile, numerotate cu numere începând de la unu, din trei în trei.
# Toate bilele cărora le corespund numere pare sunt verzi. Să se afle câte bile verzi sunt.

count_bile_verzi = 0

for numar in range(1, 301, 3):
    if numar % 2 == 0:
        count_bile_verzi += 1

print(" Sunt", count_bile_verzi, "bile verzi.")

# 13. Verificați dacă un șir de caractere citit are sau nu lungimea mai mare decât 20.

sir = "afara"
if len(sir) < 20:
    print("Sirul este mai scurt.")
else:
    print("Sirul este mai lung.")


# 14. Se introduce un șir de caractere. Afișați-l cu majuscule, citit de la dreapta la stânga.

sir = "Afara este cald"
sir_majuscule = sir.upper()
for caracter in sir_majuscule[::-1]:
    print(caracter, end="")


# 15. Se citește un șir de caractere. Afisați câte caractere are șirul.

sir_15 = "Afara este cald."
lungime_sir_15 = len(sir_15)
print(lungime_sir_15)

# 16. Se citește o propoziție de la tastatură. Să se afișeze câte vocale, respectiv câte consoane se află în aceasta.
# Exemplu: Fred merge pe plajă. Se afișează: 10 consoane și 6 vocale.

propozitie = input("Introduceti o propozitie: ")

vocale = "aeiouAEIOU"
nr_vocale = 0
nr_consoane = 0

for caracter in propozitie:
    if caracter.isalpha():  # isalpha verifica daca caracterul este  o litera
        if caracter in vocale:
            nr_vocale += 1
        else:
            nr_consoane += 1

print("Numarul de consoane in propozitie:", nr_consoane)
print("Numarul de vocale in propozitie:", nr_vocale)

# 17. Alfabetul pythonistilor. Noi, pythoniștii, ne-am întelege mult mai bine într-o limbă, a noastră, for fun!
# E o regulă foarte simplă: după fiecare cuvânt, se adaugă respectivul cuvânt, dar scris invers. Realizează programul!
# Exemplu:se citește "Noi suntem informaticieni." --- se traduce ca: "Noiion suntemmetnus informaticieniineicitamrofni."

exemplu = "Ion are prune"
cuvinte = exemplu.split()
exemplu_invers = ""
   for cuvant in cuvinte:
     cuvant_inversat = cuvant[::-1]
     exemplu_invers += cuvant + cuvant_inversat + " "
print(exemplu_invers)


# 18. Să se afle câte numere impare se găsesc între 24 și 800.

numere_pare = 0

for numar in range(24, 800):
    if numar % 2 == 0:
        numere_pare += 1

print(" Sunt", numere_pare, "numere pare.")

# 19. Campionatul mondial de Formula 1 a decis să penalizeze anumiți piloți pentru încălcarea regulilor.
# Astfel se acordă poziții de penalizare pe grila de start în funcție de gravitatea abaterii.
# Se cere să se ordoneze clasamentul după acordarea tuturor penalizărilor.
# Date de intrare: fiecare pilot are un cod unic format din mai multe părți astfel:
# Prima cifră reprezintă numărul echipei din care face parte pilotul
# A doua cifră și a treia cifră formează numărul de cursă al pilotului
# A patra și a cincea cifră reprezintă poziția de pe grila de start a pilotului
# Ultimele două cifre reprezintă numărul de poziții cu care este penalizat pilotul
# Se vor citi 10 astfel de coduri, unul pentru fiecare pilot.
# Date de ieșire: se va afișa în ordinea poziției după acordarea penalizărilor, separat printr-un spațiu,
# numărul echipei din care face parte pilotul și numărul acestuia. Se va trece la un rând nou după fiecare rezultat.


# 20. Proiect - Oracol.
# Scrieți un program care să creeze un fișier text cu rol de jurnal personal.
# Programul trebuie să afișeze/informeze utilizatorul la fiecare pas, să verifice existența fișierului și să afișeze
# "Am creat fișierul!"; "Fișierul există, ce doriți să faceți? Introduceți 1 pentru citire, 2 pentru adăugări,
# 3 pentru ștergerea definitivă a fișierului, 0 pentru ieșire".
# Atenție! Folosiți modulul datetime (documentați-vă pe Internet): from datetime import date
# și data = date.today() sau folosiți o altă metodă (citire de la tastatură) pentru a putea insera data curentă
# la începutul fiecărei adăugări.
