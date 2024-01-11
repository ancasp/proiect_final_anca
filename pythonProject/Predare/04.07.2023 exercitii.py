"""
Clasa Persoana
Creează o clasă Persoana cu atributele nume și varsta. Adaugă metodele afisare_nume și afisare_varsta care afișează
numele și respectiv vârsta persoanei.
"""
class Persoana:
    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta = varsta

    def afisare_nume_varsta(self):
        print(f"Ma numesc {self.nume} si am varsta de {self.varsta} ani")

Ioana = Persoana(nume = "Ioana", varsta = 20)
print(Ioana.nume)
print(Ioana.varsta)
Ioana.afisare_nume_varsta()

"""Creează o clasă Angajat care moștenește din clasa Persoana și adaugă atributul salariu. Adaugă metoda afisare_salariu
care afișează salariul angajatului."""

class Angajat(Persoana):
    def __init__(self, nume, varsta, salariu):
        Persoana.__init__(self, nume, varsta)
        self.salariu = salariu

    def afisare_salariu(self):
        print(f"Ma numesc {self.nume} si am varsta de {self.varsta}. Am un salariu de {self.salariu} lei.")

omul = Angajat(nume = "Gelu",
               varsta = 30,
               salariu = 10000)
print(omul.nume)
print(omul.varsta)
print(omul.salariu)
omul.afisare_salariu()

"""
Creează o clasă Student care moștenește din clasa Persoana și adaugă atributul facultate. Adaugă metoda afisare_facultate
care afișează facultatea studentului."""

class Student(Persoana):
    def __init__(self, nume, varsta, facultate):
        Persoana.__init__(self, nume, varsta)
        self.facultate = facultate
    def afisare_facultate(self):
        print(f"Numele meu este {self.nume} si am varsta de {self.varsta} ani. Sunt student la facultatea {self.facultate}")

cineva = Student(nume = "Dana", varsta = 20, facultate = "Politehnica")
cineva.afisare_facultate()
print(cineva.nume)
print(cineva.varsta)
print(cineva.facultate)


"""
Creează o clasă Angajat_Student care moștenește din clasele Angajat și Student. Adaugă atributul numar_ore și metoda
 afisare_numar_ore care afișează numărul de ore lucrate de angajatul student."""

class Angajat_Student(Angajat,Student):
    def __init__(self, nume, varsta, facultate, salariu, nr_ore):
        Angajat.__init__(self, nume, varsta, salariu)
        Student.__init__(self, nume, varsta, facultate)
        self.nr_ore = nr_ore

    def afisare_nr_ore(self):
        print(f"Ma numesc {self.nume} si am {self.varsta} ani. Desi am terminat {self.facultate}, am un salariu de {self.salariu},"
              f" pentru ca lucrez {self.nr_ore}.")

angstu = Angajat_Student(nume = "Geta",
                         varsta = 25,
                         facultate = "ASE",
                         salariu = 5000,
                         nr_ore = "6h")

print(angstu.nume)
print(angstu.varsta)
print(angstu.facultate)
print(angstu.salariu)
print(angstu.nr_ore)
angstu.afisare_nr_ore()


"""
Clasa Animal
Creează o clasă Animal cu atributele nume și varsta. Adaugă metodele afisare_nume și afisare_varsta care afișează
numele și respectiv vârsta animalului.
"""

class Animal:
    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta = varsta
    def afisare_nume_varsta(self):
        print(f"Numele meu este {self.nume} si am varsta de {self.varsta}.")
ceva_animal = Animal(nume = "Pluto",
                    varsta = "2 ani")
print(ceva_animal.nume)
print(ceva_animal.varsta)
ceva_animal.afisare_nume_varsta()

"""Creează o clasă Caine care moștenește din clasa Animal și adaugă atributul culoare. Adaugă metoda afisare_culoare
care afișează culoarea câinelui.
Creează o clasă Pisica care moștenește din clasa Animal și adaugă atributul greutate. Adaugă metoda afisare_greutate
care afișează greutatea pisicii."""



"""Clasa Carte
Creează o clasă Carte cu atributele titlu, autor și an_publicare. Adaugă metodele afisare_titlu, afisare_autor și
 afisare_an_publicare care afișează titlul, autorul și respectiv anul de publicare al cărții.
Creează o clasă Roman care moștenește din clasa Carte și adaugă atributul numar_pagini. Adaugă metoda
afisare_numar_pagini care afișează numărul de pagini al romanului.
Creează o clasă Poezie care moștenește din clasa Carte și adaugă atributul numar_strofe. Adaugă metoda
afisare_numar_strofe care afișează numărul de strofe al poeziei.
Clasa Masina
Creează o clasă Masina cu atributele marca și an_fabricatie. Adaugă metodele afisare_marca și afisare_an_fabricatie
care afișează marca și respectiv anul de fabricație al mașinii.
Creează o clasă SUV care moștenește din clasa Masina și adaugă atributul capacitate_motor. Adaugă metoda
afisare_capacitate_motor care afișează capacitatea motorului SUV-ului.
Creează o clasă Coupe care moștenește din clasa Masina și adaugă atributul viteza_maxima. Adaugă metoda
afisare_viteza_maxima care afișează viteza maximă a coupe-ului."""
