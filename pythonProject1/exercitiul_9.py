# Scrieti o functie care returnează aria si perimetrul unei figuri regulate (cu lungimea tuturor laturilor aceiasi)
# pentru figuri de la 3 la 7 laturi.
# Rezultatul la return trebuie să fie un dicționar de genul
# {"nr_of_sides":x, "length of side":y, "area":z, "perimeter": px}

# Puteți crea o funcție Python care să calculeze aria și perimetrul unei figuri regulate cu un număr specific de laturi
# (de la 3 la 7) și să returneze rezultatul sub forma unui dicționar. Iată cum puteți face acest lucru:

import math

def calculate_area_and_perimeter(nr_of_sides, length_of_side):
    if nr_of_sides < 3 or nr_of_sides > 7:
        return {"error": "Numărul de laturi trebuie să fie între 3 și 7 inclusiv."}

    if length_of_side <= 0:
        return {"error": "Lungimea laturii trebuie să fie un număr pozitiv mai mare decât zero."}

    # Calculăm perimetrul
    perimeter = nr_of_sides * length_of_side

    # Calculăm aria
    if nr_of_sides == 3:  # Triunghi echilateral
        area = (math.sqrt(3) / 4) * length_of_side ** 2
    elif nr_of_sides == 4:  # Pătrat
        area = length_of_side ** 2
    elif nr_of_sides == 5:  # Pentagon regulat
        area = (5 / 4) * length_of_side ** 2 * (1 / math.tan(math.pi / 5))
    elif nr_of_sides == 6:  # Hexagon regulat
        area = (3 * math.sqrt(3) / 2) * length_of_side ** 2
    elif nr_of_sides == 7:  # Heptagon regulat
        area = (7 / 4) * length_of_side ** 2 * (1 / math.tan(math.pi / 7))

    return {"nr_of_sides": nr_of_sides, "length of side": length_of_side, "area": round(area, 2),
            "perimeter": round(perimeter, 2)}


# Exemplu de utilizare:
result = calculate_area_and_perimeter(4, 5)
print(result)

# Această funcție calculate_area_and_perimeter primește numărul de laturi și lungimea laturii ca argumente și
# calculează aria și perimetrul pentru figuri regulate cu 3 până la 7 laturi. Dacă numărul de laturi sau lungimea
# laturii nu sunt valide, funcția returnează un dicționar cu o eroare corespunzătoare. Altfel, funcția returnează
# dicționarul cu valorile cerute.