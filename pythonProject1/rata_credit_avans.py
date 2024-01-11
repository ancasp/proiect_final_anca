def calcul_rata_credit(valoare_imobil, avans_procent, numar_luni, rata_dobanda_anuala):
    # Calculați valoarea avansului în bani
    avans = (avans_procent / 100) * valoare_imobil

    # Valoarea creditului este valoarea imobilului minus avansul
    principal = valoare_imobil - avans

    # Convertiți rata dobânzii anuale într-o rată dobândă lunară
    rata_dobanda_lunara = (rata_dobanda_anuala / 100) / 12

    # Calculează rata lunară de rambursare utilizând formula creditului fix
    rata_lunara = (principal * rata_dobanda_lunara) / (1 - (1 + rata_dobanda_lunara) ** -numar_luni)

    return rata_lunara, avans

try:
    # Introduceți manual valorile: valoarea imobilului, procentul avansului, numărul de luni și rata dobânzii
    valoare_imobil = float(input("Introduceți valoarea imobilului: "))
    avans_procent = float(input("Introduceți procentul avansului (de exemplu, 20%): "))
    numar_luni = int(input("Introduceți numărul de luni pentru rambursare: "))
    rata_dobanda_anuala_str = input("Introduceți rata dobânzii pe an (în procente, de exemplu, 6%): ")

    # Eliminați semnul de procent și convertiți rata dobânzii în float
    rata_dobanda_anuala = float(rata_dobanda_anuala_str.rstrip('%'))

    # Calculați rata lunară și valoarea avansului
    rata_lunara, avans = calcul_rata_credit(valoare_imobil, avans_procent, numar_luni, rata_dobanda_anuala)

    # Afișați rata lunară și valoarea avansului în lei
    print(f"Rata lunară de rambursare este: {rata_lunara:.2f} lei")
    print(f"Valoarea avansului este: {avans:.2f} lei")
except ValueError:
    print("Introduceți valori valide.")

