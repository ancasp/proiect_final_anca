class Contact:  # am definit o clasa

    def __init__(self, prenume, telefon):   # am initializat parametrii
        #  __init__ - este o metoda speciala a Clasei care imi initiializeaza parametrii obiectului pe care il voi crea
        # obiect = instanta a clasei, de ex un contact anume pentru Clasa Contact
        # self - parametru special utilizat in definitia si accesarea parametrilor unui oboect
        # self se foloseste independent in alte metode, fara a mai declara inca o data parametrii calsei

        self.prenume = prenume   # aici am initializat clasa
        self.telefon = telefon

    def afisare_contact(self):
        # metode - functii care imi dau voie sa procesez parametrii Clasei, efecueaza operatii cu parametrii
        # de ce aici am doar self
        print(f"{self.prenume} are telefonul {self.telefon}")

    def afisare_in_telefon(self):
        if self.prenume:  # daca i-am dat valoare prenumelui
            print(f"suna pe {self.prenume}")
        else:
            print(f"suna pe {self.telefon}")

Ion = Contact(prenume = "Ionica", telefon = "+40777444555")
#Ion = ....am initializat clasa contact pt Ion
Ion.afisare_contact()

Elena = Contact(prenume = "Lenutza",
                telefon = "+40777888999")
Elena.afisare_contact()
Elena.afisare_in_telefon()

Cineva_fara_nume = Contact(prenume = None, telefon="0788899955")
Cineva_fara_nume.afisare_in_telefon()



class Animal:

    def __init__(self, dieta: str, varsta: int, domestic: bool, vertebrat: bool):
        self.dieta = dieta
        self.varsta = varsta
        self.domestic = domestic
        self.vertebrat = vertebrat

    def botez(self):
        numele = input("Cum il cheama pe animal? = ")
        print(f"{numele} este un animal {'vertebrat' if self.vertebrat else 'nevertebrat'}")
        # 'vertebrat' if self.vertebrat else 'nevertebrat' = adica imi va da vertebrat daca self.vertebrat = True,
        # in caz invers = nevertebrat
        # Putem folosi in acelasi f string ghilimele " si ', doar ca una trebbuie sa fie in interiorul altuia
Ursuletul = Animal(dieta = "omnivor",
                   varsta = 12,
                   domestic = False,
                   vertebrat = True)
print(Ursuletul)  # imi printeaza asta <__main__.Animal object at 0x0000028B7DB02390>, adica imi indica locul in PC
Ursuletul.botez()

Rama_mea = Animal(dieta = "pamant",
                  varsta = 0.3,
                  domestic = False,
                  vertebrat = False)
Rama_mea.botez()


