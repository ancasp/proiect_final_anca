### Database programming ### SQL Alchemy ###

##################
### INFO ###
0. Data types => https://docs.sqlalchemy.org/en/14/core/types.html
0. Expressions => https://docs.sqlalchemy.org/en/14/core/sqlelement.html#column-element-foundational-constructors
0. ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_password'  ### change password ###

Cars: Clasa la care se face referire(din clasa de mai jos): nume_relatie = relationship(nume_clasa_cu_foreign_key, back_populates=nume_relatie_din_clasa_cu_foreign_key, cascade="all, delete", passive_deletes=True)

Bookings: Clasa cu foreign key: nume_relatie = relationship(nume_clasa_cu_care_are_legatura, back_populates= nume_relatie_din_clasa_cu_care_are_legatura)


###################


###################
Exercises
	Solito Company
		1. connect to database and create "solito" database
		
		2. create tables:
			a. table "departamente": id, nume, descriere
			b. table "proiecte": id, nume, descriere, id_departament_responsabil, start_date, end_date, priority, cost, profit
			c. table "angajati": id, nume, email, telefon, data_nasterii, pozitie, is_team_leader, data_angajarii, id_departament, salariu_de_baza
            d. table "asignare_angajati_pe_proiecte": id, id_angajat, id_proiect 
			e. table "bonusuri": id, id_angajat, explicatie, suma
		
		3. insert values to tables:
			a. 	lista_departamente = [
                    Departamente(nume="HR", descriere="Do the recruitment."),                                   # 1 #
                    Departamente(nume="Software", descriere="Do the code."),                                    # 2 #
                    Departamente(nume="Marketing", descriere="Do the marketing for our products."),             # 3 #
                    Departamente(nume="Sales", descriere="Do the sales."),                                      # 4 #
                    Departamente(nume="Operations", descriere="Do the logistics and other stuff needed."),      # 5 #
                ]

			b.	lista_proiecte = [
                    Proiecte(nume="Recrutare de primavara", descriere="Fill available positions.", id_departament_responsabil=1, start_date="2023-01-10", end_date="2023-04-10", priority="medium", cost=1500, profit = 4500),              # 1 #
                    Proiecte(nume="Code refactor", descriere="Refactor code for old projects.", start_date="2023-05-10", id_departament_responsabil=2, end_date="2023-07-10", priority="low", cost=1500, profit = 4500),                    # 2 #
                    Proiecte(nume="Deliver 100% code", descriere="Deliver projects to all clients.", start_date="2023-01-10", id_departament_responsabil=2, end_date="2023-12-10", priority="high", cost=0, profit = 0),                    # 3 #
                    Proiecte(nume="Visibility 10M", descriere="Make our products visible to 10M people.", start_date="2023-04-10", id_departament_responsabil=3, end_date="2023-08-10", priority="high", cost=250000, profit = 500000),     # 4 #
                    Proiecte(nume="Achieve 1M B2B", descriere="Do sales of 1M $ to B2B partners.", start_date="2023-01-10", id_departament_responsabil=4, end_date="2023-12-10", priority="high", cost=100000, profit = 500000),            # 5 #
                    Proiecte(nume="Improve workflow", descriere="Find new ways to do things faster", id_departament_responsabil=5, start_date="2023-02-10", end_date="2023-07-10", priority="medium", cost=3000, profit = 0),               # 6 #
                ]

			c. 	lista_angajati = [
                    Angajati(nume="Stan Alina", email="stan.alina@gmail.com", telefon="0755111222", data_nasterii="1994-10-10", pozitie="HR specialist", is_team_leader=False, data_angajarii="2020-01-01", id_departament=1, salariu_de_baza=7000),                  # 1 #
                    Angajati(nume="Solo Bogdan", email="solo.bogdan@gmail.com", telefon="0755111333", data_nasterii="1992-01-01", pozitie="HR specialist", is_team_leader=False, data_angajarii="2021-01-01", id_departament=1, salariu_de_baza=3000),                 # 2 #
                    Angajati(nume="Bobonete Mihai", email="bobonete.mihai@gmail.com", telefon="0755111444", data_nasterii="1994-01-01", pozitie="SD TL", is_team_leader=True, data_angajarii="2021-01-01", id_departament=2, salariu_de_baza=15000),                      # 3 #
                    Angajati(nume="Badea Dan", email="badea.dan@gmail.com", telefon="0755111555", data_nasterii="1987-01-01", pozitie="SD TL", is_team_leader=True, data_angajarii="2021-01-01", id_departament=2, salariu_de_baza=14000),                           # 4 #
                    Angajati(nume="Bojog Costel", email="bojog.costel@gmail.com", telefon="0755111666", data_nasterii="1988-01-01", pozitie="programmer", is_team_leader=False, data_angajarii="2021-01-01", id_departament=2, salariu_de_baza=7500),                   # 5 #
                    Angajati(nume="Nae Nicolae", email="nae.nicolae@gmail.com", telefon="0755111777", data_nasterii="1998-01-01", pozitie="programmer", is_team_leader=False, data_angajarii="2021-01-01", id_departament=2, salariu_de_baza=7300),                    # 6 #
                    Angajati(nume="Bendeac Mihai", email="bendeac.mihai@gmail.com", telefon="0755111777", data_nasterii="1998-01-01", pozitie="programmer", is_team_leader=False, data_angajarii="2021-01-01", id_departament=2, salariu_de_baza=7100),                  # 7 #
                    Angajati(nume="Popovici Maria", email="popovici.maria@gmail.com", telefon="0755111777", data_nasterii="1998-01-01", pozitie="programmer", is_team_leader=False, data_angajarii="2021-01-01", id_departament=2, salariu_de_baza=6900),                 # 8 #
                    Angajati(nume="Mincu Alex", email="mincu.alex@gmail.com", telefon="0755111888", data_nasterii="1997-01-01", pozitie="MKT TL", is_team_leader=False, data_angajarii="2021-01-01", id_departament=3, salariu_de_baza=12000),                        # 9 #
                    Angajati(nume="Popesco Cristi", email="popesco.cristi@gmail.com", telefon="0755111999", data_nasterii="1996-01-01", pozitie="MKT specialist", is_team_leader=False, data_angajarii="2021-01-01", id_departament=3, salariu_de_baza=6000),             # 10 #
                    Angajati(nume="Isac Radu", email="isac.radu@gmail.com", telefon="0755222111", data_nasterii="1982-01-01", pozitie="Sales TL", is_team_leader=True, data_angajarii="2021-01-01", id_departament=4, salariu_de_baza=11000),                        # 11 #
                    Angajati(nume="Nedelcu Cosmin", email="nedelcu.cosmin@gmail.com", telefon="0755222222", data_nasterii="1985-01-01", pozitie="Sales", is_team_leader=False, data_angajarii="2021-01-01", id_departament=4, salariu_de_baza=5000),                      # 12 #
                    Angajati(nume="Popa Dorian", email="popa.dorian@gmail.com", telefon="0755222333", data_nasterii="1994-01-01", pozitie="OP TL", is_team_leader=True, data_angajarii="2021-01-01", id_departament=5, salariu_de_baza=9000),                          # 13 #
                    Angajati(nume="Bordea Catalin", email="bordea.catalin@gmail.com", telefon="0755222444", data_nasterii="1993-01-01", pozitie="OP specialist", is_team_leader=False, data_angajarii="2021-01-01", id_departament=5, salariu_de_baza=4000),              # 14 #
                    Angajati(nume="Doi-Degeaba Si-Unu-n-Plus", email="doidegeaba.ununplus@gmail.com", telefon="0755888999", data_nasterii="1993-01-01", pozitie="OP specialist", is_team_leader=False, data_angajarii="2021-01-01", id_departament=5, salariu_de_baza=4000),   # 15 #
                ]

			d. 	lista_asignare_angajati_proiecte = [
                    AsignareAngajatiPeProiecte(id_angajat=1, id_proiect=1),             # 1 #
                    AsignareAngajatiPeProiecte(id_angajat=2, id_proiect=1),             # 2 #
                    AsignareAngajatiPeProiecte(id_angajat=3, id_proiect=2),             # 3 #
                    AsignareAngajatiPeProiecte(id_angajat=4, id_proiect=3),             # 4 #
                    AsignareAngajatiPeProiecte(id_angajat=5, id_proiect=2),             # 5 #
                    AsignareAngajatiPeProiecte(id_angajat=6, id_proiect=3),             # 6 #
                    AsignareAngajatiPeProiecte(id_angajat=7, id_proiect=3),             # 7 #
                    AsignareAngajatiPeProiecte(id_angajat=8, id_proiect=3),             # 8 #
                    AsignareAngajatiPeProiecte(id_angajat=9, id_proiect=4),             # 9 #
                    AsignareAngajatiPeProiecte(id_angajat=10, id_proiect=4),            # 10 #
                    AsignareAngajatiPeProiecte(id_angajat=11, id_proiect=5),            # 11 #
                    AsignareAngajatiPeProiecte(id_angajat=12, id_proiect=5),            # 12 #
                    AsignareAngajatiPeProiecte(id_angajat=13, id_proiect=6),            # 13 #
                    AsignareAngajatiPeProiecte(id_angajat=14, id_proiect=6),            # 14 #
                    AsignareAngajatiPeProiecte(id_angajat=15, id_proiect=6),            # 14 #
                ]

            e.  lista_bonusuri = [
                    Bonusuri(id_angajat=1, explicatie="extra hours", suma=3000),        # 1 #
                    Bonusuri(id_angajat=2, explicatie="baiat de treaba", suma=1000),    # 2 #
                    Bonusuri(id_angajat=3, explicatie="extra hours", suma=5000),        # 3 #
                    Bonusuri(id_angajat=4, explicatie="extra hours", suma=5000),        # 4 #
                    Bonusuri(id_angajat=5, explicatie="evolutie", suma=2000),           # 5 #
                    Bonusuri(id_angajat=6, explicatie="performanta", suma=3000),        # 6 #
                    Bonusuri(id_angajat=7, explicatie="performanta", suma=3000),        # 7 #
                    Bonusuri(id_angajat=8, explicatie="performanta", suma=3000),        # 8 #
                    Bonusuri(id_angajat=9, explicatie="extra hours", suma=5000),        # 9 #
                    Bonusuri(id_angajat=10, explicatie="performanta", suma=3000),       # 10 #
                    Bonusuri(id_angajat=11, explicatie="extra hours", suma=5000),       # 11 #
                    Bonusuri(id_angajat=12, explicatie="performanta", suma=3000),       # 12 #
                    Bonusuri(id_angajat=13, explicatie="extra hours", suma=5000),       # 13 #
                    Bonusuri(id_angajat=14, explicatie="baiat de treaba", suma=1000),   # 14 #
                ]
                

		4. To Dos: 
			a.	Print (nume proiecte, prioritate) - sortate dupa prioritate
            b.  Promote 'Stan Alina' as team leader (change position to "HR TL" and is_team_leader to True)
            c.  Print team leaders list
            d.  "Doi-Degeaba Si-Unu-n-Plus" was fired! Delete him from Angajati
            e.  Print (nume, pozitie, salariu_de_baza, bonus) list with all employees
            f.  Print lista  nume angajat, pozitie, status team leader, nume departament, nume proiect unde e asignat, data angajarii

###################


