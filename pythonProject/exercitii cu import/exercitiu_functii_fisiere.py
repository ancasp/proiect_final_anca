def creaza_fisiere_cu_nume(folder, *nume):
    #*args este o conventie, dar putem pune si alta denumire
    for n in nume:
        with open(f"{folder}/{n}.txt", "w") as file:
            # (f"{folder}/{n}.txt" - am creat fullpath la fisier
            file.write(f"{n} are {len(n)} caractere")

path_folder = 'C:/Users/ancas/Desktop/sda_52'
creaza_fisiere_cu_nume(path_folder, "ion", "ana", "nathan", "catalin")


def adauga_text_in_fisiere(folder, *args):
    for file in args:
        with open(f"{folder}/{file}.txt", "a") as fisier_existent:
            fisier_existent.write("\n2Astazi e o zi faina")

adauga_text_in_fisiere(path_folder, "ion", "ana", "nathan")