#Creati o clasa-mama (de ex - masini), de la care alte 3 clase mostenesc (ex: Audi, Mercedes, Mercedes S Class)
# (sau puteti face alte clase cu alte derivate- flori, bucatarie, firme etc)
#La clasa mama sa aiba 2 metode, apoi la clasele ce mostenesc de la clasa-mama - cate 1 sau 2 metode specifice.
#Creati 3 obiecte ale unei clase derivate / clasa-copil, si accesati atributele obiectului prin diverse printuri
# (make it a fun statemenet :smile: )

class Masina:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def afisare_informatii(self):
        print(f"Marca: {self.brand}")
        print(f"Model: {self.model}")

    def pornire_motor(self):
        print("Motorul a fost pornit.")


class Audi(Masina):
    def __init__(self, model):
        super().__init__("Audi", model)

    def sunet_claxon(self):
        print("Audi face sunetul caracteristic al claxonului.")


class Mercedes(Masina):
    def __init__(self, model):
        super().__init__("Mercedes", model)

    def pilot_automat(self, viteza):
        print(f"Mercedes-ul cu modelul {self.model} utilizează pilot automat la {viteza} km/h.")


class MercedesSClass(Mercedes):
    def __init__(self, model):
        super().__init__(model)

    def masaj_scaune(self):
        print("Mercedes S-Class oferă masaj pentru scaune în spate.")


# Exemple de utilizare
audi_a4 = Audi("A4")
audi_a4.afisare_informatii()
audi_a4.pornire_motor()
audi_a4.sunet_claxon()

mercedes_c200 = Mercedes("C200")
mercedes_c200.afisare_informatii()
mercedes_c200.pornire_motor()
mercedes_c200.pilot_automat(120)

mercedes_s500 = MercedesSClass("S500")
mercedes_s500.afisare_informatii()
mercedes_s500.pornire_motor()
mercedes_s500.pilot_automat(150)
mercedes_s500.masaj_scaune()
