# Solito Company
# 		1. connect to database and create "solito" database

import mysql.connector as mysql

import os
from sqlalchemy import create_engine, inspect, text, func, desc, and_, or_, not_, join
from sqlalchemy.orm import declarative_base, sessionmaker
from model_exercitiu import Base, Departamente, Proiecte, Angajati, AsignareAngajatiPeProiecte, Bonusuri
import datetime

CONNECTION_STRING = f"mysql+mysqlconnector://root:password@localhost:3306/solito"

engine = None
inspector = None
session = None

def connect_to_database():
    global engine
    global inspector
    global session
    global CONNECTION_STRING

    engine = create_engine(CONNECTION_STRING)
    inspector = inspect(engine)
    session = sessionmaker(bind=engine)()

def create_database():
    print("\n\nCreating to database...\n")

    global engine
    with engine.connect() as conn:
        conn.execute(text("CREATE DATABASE IF NOT EXISTS solito"))


def create_table():
    global engine
    Base.metadata.create_all(engine)
    print(f"\n\n - success")


def insert_into_table():
    global session

    lista_departamente = [
        Departamente(nume="HR", descriere="Do the recruitment."),  # 1 #
        Departamente(nume="Software", descriere="Do the code."),  # 2 #
        Departamente(nume="Marketing", descriere="Do the marketing for our products."),  # 3 #
        Departamente(nume="Sales", descriere="Do the sales."),  # 4 #
        Departamente(nume="Operations", descriere="Do the logistics and other stuff needed."),  # 5 #
    ]

    lista_proiecte = [
        Proiecte(nume="Recrutare de primavara", descriere="Fill available positions.", id_departament_responsabil=1,
                 start_date="2023-01-10", end_date="2023-04-10", priority="medium", cost=1500, profit=4500),  # 1 #
        Proiecte(nume="Code refactor", descriere="Refactor code for old projects.", start_date="2023-05-10",
                 id_departament_responsabil=2, end_date="2023-07-10", priority="low", cost=1500, profit=4500),  # 2 #
        Proiecte(nume="Deliver 100% code", descriere="Deliver projects to all clients.", start_date="2023-01-10",
                 id_departament_responsabil=2, end_date="2023-12-10", priority="high", cost=0, profit=0),  # 3 #
        Proiecte(nume="Visibility 10M", descriere="Make our products visible to 10M people.", start_date="2023-04-10",
                 id_departament_responsabil=3, end_date="2023-08-10", priority="high", cost=250000, profit=500000),# 4 #
        Proiecte(nume="Achieve 1M B2B", descriere="Do sales of 1M $ to B2B partners.", start_date="2023-01-10",
                 id_departament_responsabil=4, end_date="2023-12-10", priority="high", cost=100000, profit=500000),# 5 #
        Proiecte(nume="Improve workflow", descriere="Find new ways to do things faster", id_departament_responsabil=5,
                 start_date="2023-02-10", end_date="2023-07-10", priority="medium", cost=3000, profit=0),  # 6 #
    ]

    lista_angajati = [
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

    lista_asignare_angajati_proiecte = [
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

    lista_bonusuri = [
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

    session.add_all(lista_departamente)
    session.add_all(lista_proiecte)
    session.add_all(lista_angajati)
    session.add_all(lista_asignare_angajati_proiecte)
    session.add_all(lista_bonusuri)

    session.commit()

    print(f"\n\n - success")


# a.  Print (nume proiecte, prioritate) - sortate dupa prioritate

def select_table_specific_columns():
    global session
    rows = session.query(Proiecte.nume, Proiecte.priority).order_by(Proiecte.priority.desc()).all()
    print(f"Proiecte:\n")
    for row in rows:
        print(row)

# b.  Promote 'Stan Alina' as team leader (change position to "HR TL" and is_team_leader to True)

def select_promote_condition():
    global session
    promote = session.query(Angajati).where(Angajati.nume =="Stan Alina").first()
    promote.is_team_leader = True
    promote.pozitie = "HR TL"
    session.commit()
    print("Rezolvat cu succes!")

# c.  Print team leaders list

def select_team_leaders_list():
    global session
    team_leaders = session.query(Angajati.nume, Angajati.is_team_leader).\
        where(Angajati.is_team_leader.like("1")).all()

    for el in team_leaders:
        print(el)


# d.  "Doi-Degeaba Si-Unu-n-Plus" was fired! Delete him from Angajati

def delete_angajat():
    global session
    delete = session.query(Angajati).where(Angajati.nume == "Doi-Degeaba Si-Unu-n-Plus").all()
    for nume in delete:
        session.delete(nume)
    session.commit()

# e.  Print (nume, pozitie, salariu_de_baza, bonus) list with all employees

def print_angajati():
    global session
    angajati = session.query(Angajati.nume, Angajati.pozitie, Angajati.salariu_de_baza, Bonusuri.suma). \
                join(Bonusuri).all()
    for angajat in angajati:
        print(angajat)


# f.  Print lista  nume angajat, pozitie, status team leader, nume departament, nume proiect unde e asignat, data angajarii

def alt_print_angajati():
    global session

    alti_angajati = session.query(Angajati.nume, Angajati.pozitie, Angajati.is_team_leader, Departamente.nume, Proiecte.nume, Angajati.data_angajarii) \
        .join(Departamente, Departamente.id == Proiecte.id_departament_responsabil) \
        .join(AsignareAngajatiPeProiecte, AsignareAngajatiPeProiecte.id_proiect == Proiecte.id) \
        .join(Angajati, Angajati.id == AsignareAngajatiPeProiecte.id_angajat) \
        .all()

    for angajat in alti_angajati:
        print(angajat)

connect_to_database()
create_database()
create_table()
# insert_into_table()
print("\n\n EXERCITIUL 4")
print("\n\n - exercitiul a")
select_table_specific_columns()
print("\n\n - exercitiul b")
print("\n\n - Stan Alina a fost promovata!")
print("\n\n - exercitiul c")
select_team_leaders_list()
print("\n\n - exercitiul d")
select_promote_condition()
print("\n\n - exercitiul e")
delete_angajat()
print("\n\n - exercitiul f")
print_angajati()
print("\n\n - exercitiul ")
alt_print_angajati()
print("\n\n FINAL")

