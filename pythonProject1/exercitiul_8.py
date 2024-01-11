# Scrieti o functie care calculează media aritmetică a tuturor numerelor întregi dintr-o listă mixtă,
# care sunt divizibile cu 3 și se termină cu 3. Rotunjiți rezultatul la 3 decimale.
# De exemplu având lista [12, 33, True, "abc", {"a":1, "b":4}, 123, 3], rezultatul va fi 53, adica (33+123+3)/3
# Folosiți try/except și logging, printre altele.

# Puteți crea o funcție care calculează media aritmetică a tuturor numerelor întregi dintr-o listă mixtă,
# care sunt divizibile cu 3 și se termină cu 3, folosind blocuri try și except pentru a gestiona excepțiile
# și biblioteca logging pentru a înregistra informații relevante. Iată cum puteți face acest lucru:

import logging

def calculate_average(lst):
    # Inițializăm suma și numărul de elemente valabile
    total = 0
    count = 0

    # Iterăm prin lista dată
    for item in lst:
        try:
            # Verificăm dacă elementul este un număr întreg și îndeplinește condițiile
            if isinstance(item, int) and item % 3 == 0 and str(item).endswith('3'):
                total += item
                count += 1
        except Exception as e:
            # Înregistram excepția folosind biblioteca logging
            logging.error(f"Excepție: {e}")

    # Calculăm media aritmetică sau returnăm 0 dacă nu avem elemente valabile
    if count > 0:
        average = total / count
        return round(average, 3)
    else:
        return 0.0

# Exemplu de utilizare:
input_list = [12, 33, True, "abc", {"a": 3, "b": 4}, 123, 3, 333]
result = calculate_average(input_list)
print(f"Media aritmetică a numerelor divizibile cu 3 și terminate cu 3 din lista este: {result}")


# Această funcție calculate_average iterează prin lista dată, verifică fiecare element și,
# dacă este un număr întreg care îndeplinește condițiile, adaugă la suma totală și numără elementul.
# Excepțiile sunt gestionate și înregistrate cu ajutorul bibliotecii logging. La final,
# funcția returnează media aritmetică a numerelor sau 0.0 dacă nu există elemente valabile în listă.





