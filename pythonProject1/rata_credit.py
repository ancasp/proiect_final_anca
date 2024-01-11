def calcul_rata_credit(principal, numar_luni, rata_dobanda_anuala):
    # Convertiți rata dobânzii anuale într-o rată dobândă lunară
    rata_dobanda_lunara = (rata_dobanda_anuala / 100) / 12

    # Calculează rata lunară de rambursare utilizând formula creditului fix
    rata_lunara = (principal * rata_dobanda_lunara) / (1 - (1 + rata_dobanda_lunara) ** -numar_luni)

    return rata_lunara

try:
    # Introduceți manual valorile creditului, numărul de luni și rata dobânzii
    principal = float(input("Introduceți valoarea creditului: "))
    numar_luni = int(input("Introduceți numărul de luni pentru rambursare: "))
    rata_dobanda_anuala_str = input("Introduceți rata dobânzii pe an: ")

    # Eliminați semnul de procent și convertiți în float
    rata_dobanda_anuala = float(rata_dobanda_anuala_str.rstrip('%'))

    # Calculați rata lunară
    rata_lunara = calcul_rata_credit(principal, numar_luni, rata_dobanda_anuala)

    # Afișați rata lunară
    print(f"Rata lunară de rambursare este: {rata_lunara:.2f}")
except ValueError:
    print("Introduceți o valoare validă pentru rata dobânzii.")
