# # 1. Gasiti toate cuvintele care incep cu litera a dintr-un text
#
import re
#
# text = """Ieri a fost mai frig, insa astazi a aparut soarele pe cerul
# alb si au iesit adolescentii la audiente."""
# # cuvinte_pattern= r"\b\w+\w+a\b"
# cuvinte_pattern= r"\ba\w+\b"
# cuvinte_cu_a = re.findall(cuvinte_pattern, text)
# print(cuvinte_cu_a)
#
# #2. Gasiti toate numerele dintr-un text
# text_2 = """Astazi sunt 20 de grade, ieri au fost 25, maine vor fi 30"""
# numere_pattern = r"\b\d+\b"
# numere = re.findall(numere_pattern, text_2)
# print(numere)



# 3. Gasititi toate numerele dintr-un text
# care au suma cifrelor divizibila cu 7
text_3 = """Suma cifrelor dintr-un text divizibile cu sapte: 49, 159, 
1547, 777, 895, 1548, 2451"""
divizibile_pattern = r"\b\d+\b"
divizibile = re.findall(divizibile_pattern, text_3)
def suma_cifrelor(numar):
     return sum(int(digit) for digit in str(numar))

numere_cu_suma_div_cu_7 = [int(numar) for numar in numere if suma_cifrelor(numar) % 7 == 0]
for numar in numere_cu_suma_div_cu_7:
     print(numar)


#4. Gasiti toate cuvintele care contin litera e si au cel
# putin 5 caractere

# 5. Aveti un text care contine multe denumiri de localitati. Gasitit
# toate localitatile care incep cu litera A sau B intr-un text.

#6.Gasiti toate cuvintele care contin doar vocale.

# 7. Gasiti toate numerele de telefon in formatul +xx-07xxxxxx
# in care x este o cifra

#8. Scrieti un pattern care valideaza un input de la utilizator ca CNP valid sau nu.
# probabil ca CNP are mai multe reguli, vă puteți limita la
# -numar fix de 13 caractere
# -daca doriti, inca o regulă de validate maxim.