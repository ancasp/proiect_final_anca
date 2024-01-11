class Om:
    def __init__(self, prenume):
        self.prenume = prenume

class Angajat(Om):
    def __init__(self, prenume, functie):
        super(). __init__(prenume)
        self.functie = functie

class Student(Om):
    def __init__(self, prenume, materii_studiate):
        super().__init__(prenume)
        self.materii_studiate = materii_studiate

class AngajatStudent(Angajat, Student):
    # double inheritance
    def __init__(self, prenume, functie, materii_studiate, nr_max_ore):
        Angajat.__init__(self, prenume, functie)
        Student.__init__(self, prenume, materii_studiate)
        self.nr_max_ore = nr_max_ore

    def intro_as(self):
        intro = f"""
        Salut, ma numesc {self.prenume}. Am doua joburi:
        1. Student, invat {self.materii_studiate}
        2. Angajat, am functia {self.functie}
        Fiind studnet, am voie sa lucrez maxim {self.nr_max_ore}
        """
        print(intro)

Ionica = AngajatStudent(prenume = "Ion",
                        functie = "Ospatar",
                        materii_studiate = "Geografie, Economie",
                        nr_max_ore = 20)
Ionica.intro_as()




class Om:
    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta = varsta

class Robot:
    def __init__(self, brand, membre):
        self.brand = brand
        self.membre = membre
class Angajat:
    def __init__(self, cost, functie):
        self.cost = cost
        self.functie = functie

class AngajatOm(Om, Angajat):
    def __init__(self, nume, varsta, cost, functie):
        Om.__init__(self, nume, varsta)
        Angajat.__init__(self, cost, functie)


class AngajatRobot(Robot, Angajat):
    def __init__(self, brand, membre, cost, functie, nume_robot):
        Robot.__init__(self, brand, membre)
        Angajat.__init__(self, cost, functie)
        self.nume_robot = nume_robot

    def servire(self):
        print(f"Salut, numele meu este robot {self.nume_robot} si sunt produs de compania {self.brand}. Cu ce pot sa va servesc?")

# ion = AngajatOm("Ion", 23, 12000, "bucatar")
# print(ion.varsta)

robo_osptar_1 = AngajatRobot("Sony", 8, 30000, "Ospatar", "Willy")
print(robo_osptar_1.functie)
print(robo_osptar_1.nume_robot)
robo_osptar_1.servire()