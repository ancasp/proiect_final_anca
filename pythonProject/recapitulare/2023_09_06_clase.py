# class Contact:
#
#     def __init__(self, prenume, email, telefon):
#         self.prenume = prenume
#         self.email = email
#         self.telefon = telefon
#
#     def intro(self):
#         return f"Salutare, acesta este contactul lui {self.prenume}"
#
#     def trimite_email(self, client_email):
#         if client_email == "gmail":
#             return f"Se trimite email catre {self.email} prin google email"
#         else:
#             return f" Se trimite email catre {self.email} prin alt operator decat gmail"
#
# contact_1_ion = Contact("Ion", "i@abc.ro", "+40787821")
# contact_2_ana = Contact(prenume = "Ana",
#                         telefon = "07514",
#                         email = "a@abc.ro")
#
# print(f"Primul contact este {contact_1_ion.prenume} cu emailul {contact_1_ion.email}")
# print(f"{contact_2_ana.prenume} are nr de telefon {contact_2_ana.telefon}")
#
# contact_1_ion.intro()
# contact_1_ion.trimite_email("gmail")


# inheritance/mostenire a claselor din alte clase

class Animal:
    def __init__(self, greutate, sunet):
        self.greutate = greutate
        self.sunet = sunet

    def sunet_propriu(self):
        return f" Animalul acesta are sunetul {self.sunet}"

class Mamifere(Animal):
    def __init__(self, greutate, sunet, perioada_gestatie):
        self.perioada_gestatie = perioada_gestatie
        # super().__init__(greutate, sunet)
        Animal.__init__(self, greutate, sunet)

cimpanzeu = Mamifere(59, "ihihaha", "243 days")   # asta inseamna ca instantiem
cimpanzeu.sunet_propriu()

