from datetime import datetime
year = datetime.now().year

class Om:
    MAX_MODIFICARE_NUME = 3
    def __init__(self, prenume, an_nastere, numar_modificari=0):
        # numar_modificari va fi bydefault =0, adica nu trebuie sa il mai initializam daca nu avem nevoie
        self.prenume = prenume
        self.an_nastere = an_nastere
        self.numar_modificari = numar_modificari

    def intro_yourself(self):
        print(f"Ma numesc {self.prenume} si am {year - self.an_nastere} ani.")

    def modificare_nume(self, nume_nou):
       if self.numar_modificari >= Om.MAX_MODIFICARE_NUME:
           raise Exception("gata, ai modificat de prea multe ori!") # mesaj ca nu se mai poate modifica

 #  raise Exception - ne returneaza o eroare, Detalii mai multe in intermediate

        self.prenume = nume_nou
       self.numar_modificari += 1