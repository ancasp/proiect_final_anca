import mysql.connector as mysql
from datetime import datetime
import os

# exercitiul 1 -  connect to database and create "cineplex" database

db_connection = None
cursor = None


def connect_to_database():
    global cursor
    global db_connection
    print("\n\nConnecting to database...\n")

    ##########################################################################
    ### create database connection ###
    # connecting to the database using 'connect()' method
    # it takes 3 required parameters 'host', 'user', 'passwd'
    # after creating a database add parameter 'database'
    db_connection = mysql.connect(
        host="localhost",
        user="root",
        password="password",
        database="cineplex"
    )

    print(db_connection)  # it will print a connection object if everything is fine

    cursor = db_connection.cursor(buffered = True)

def create_database():
    print("\n\nCreating to database...\n")

    ##########################################################################
    ### create database ###

    ### query: CREATE DATABASE IF NOT EXISTS database_name ###
    ### 'execute()' method is used to compile a 'SQL' statement ###
    cursor.execute("CREATE DATABASE IF NOT EXISTS cineplex")

def create_tables():
    global cursor
    print("\n\nCreating Tables...\n")

    cursor.execute("CREATE TABLE IF NOT EXISTS clienti (id INT PRIMARY KEY AUTO_INCREMENT, nume VARCHAR(100) NOT NULL, \
                    email VARCHAR(100) UNIQUE, telefon VARCHAR(100), data_nasterii DATE)")

    print(f"\n\n  -  success!")

    cursor.execute("CREATE TABLE IF NOT EXISTS filme (id INT PRIMARY KEY AUTO_INCREMENT, nume VARCHAR(100),\
                    an_lansare INT, descriere VARCHAR(2000))")

    cursor.execute("CREATE TABLE IF NOT EXISTS sali (id INT PRIMARY KEY AUTO_INCREMENT, denumire VARCHAR(100),\
                    capacitate INT, vip BOOLEAN)")

    cursor.execute("CREATE TABLE IF NOT EXISTS bilete (id INT PRIMARY KEY AUTO_INCREMENT, film_id INT, client_id INT,\
                    sala_id INT, pret DECIMAL(4,2), data_ora DATETIME)")


def insert_into_table():
    global cursor
    global db_connection

    print("\n\nInserting into table...\n")


    query_clienti = "INSERT INTO clienti (nume, email, telefon, data_nasterii)  VALUES (%s, %s, %s, %s)"

    lista_clienti = [
                        ('Alina Popescu', 'alina_popescu@gmail.com', '0770123123', datetime(1990, 7, 15)),
                        ('Horea Pop', 'horea_pop@hotmail.com', '0770333132', datetime(1985, 12, 1)),
                        ('Anca Budeanu', 'anca_budeanu@gmail.com', '0745990123', datetime(1992, 1, 25)),
                        ('Cosmin Bucur', 'cosmin_bucur@gmail.com', '0751349008', datetime(1995, 3, 10)),
                        ('Maia Albu', 'maia_albu@gmail.com', '0730999333', datetime(1987, 11, 20)),
                        ('Camil Barna', 'camil_barna@hotmail.com', '0722010203', datetime(1999, 7, 21)),
                        ('Cristian Barbu', 'cristian_barbu@gmail.com', '0755776644', datetime(2000, 6, 6)),
                        ('Sabina Begu', 'sabina_begu@gmail.com', '0732435465', datetime(1990, 7, 1)),
                        ('Mihai Grecu', 'mihai_grecu@gmail.com', '0753435412', datetime(2002, 1, 29)),
                        ('Calin Georgescu', 'calin_georgescu@gmail.com', '0770112233', datetime(1988, 5, 19))
                    ]

    # cursor.executemany(query_clienti, lista_clienti)
    # print(cursor.rowcount, "records inserted into clienti table")

    query_filme = "INSERT INTO filme (nume, an_lansare, descriere) VALUES(%s, %s, %s)"

    lista_filme = [
        ('The Shawshank Redemption', 1994,
         'Deși declară că este nevinovat, Andy Dufresne este condamnat la închisoare pe '
         'viață pentru uciderea soției și a amantului acesteia.'),
        ('Braveheart', 1995, 'Filmul are drept subiect lupta patriotilor scotieni impotriva opresorilor englezi'),
        ('The Lord of the Rings: The Fellowship of the Ring', 2001,
         'Intr-un mic oras din Comitat, tanarului Hobbit '
         'pe nume Frodo i se incredinteaza un inel magic. El trebuie sa calatoreasca pana la Muntele Osandei '
         'pentru a distruge acest inel cu puteri periculoase.'),
        ('Avatar', 2009,
         'Jake, un veteran de război paralizat, este adus împreună cu alți pământeni pe planeta Pandora. '
         'Aceasta este locuită de o rasă umanoidă, deloc încântată de oaspeți. '
         'Jake și semenii săi trebuie să lupte pentru a-și găsi locul pe luxurianta Pandora.'),
        ('Gladiator', 2000,
         'Regizorul Ridley Scott readuce publicului de cinema bătăliile glorioase din vremea romanilor '
         'într-o poveste impetuoasă despre curaj şi revanşă.'),
        ('Chocolat', 2000,
         'Fabula comica despre modul in care degustarea placerilor vietii poate schimba un om, o relatie, un oras. '
         'Este o poveste despre iubire izbucnit intr-un orasel datorita pasiunilor '
         'si temerilor provocate de infiintarea unei misterioase cofetarii.'),
        ('True Grit', 2010,
         'Mattie, o puştoaică de 14 ani, află că tatăl ei a fost ucis de Tom Chaney, pentru un cal, 150 de dolari '
         'şi două bucăţi de aur. Mattie se îndreaptă spre Fort Smith pentru a căuta dreptate, '
         'iar aici îl angajează pe Cogburn, s-o ajute.')
    ]

    # cursor.executemany(query_filme, lista_filme)
    # print(cursor.rowcount, "records inserted into filme table")

    query_sali = "INSERT INTO sali (denumire, capacitate, vip) VALUES(%s, %s, %s)"
    lista_sali = [
        ('Sala 7', 70, 1),
        ('Sala 8', 100, 0),
        ('Sala 9', 50, 1),
        ('Sala 10', 120, 0),
        ('Sala 11', 120, 0)
    ]

    # cursor.executemany(query_sali, lista_sali)
    # print(cursor.rowcount, "records inserted into sali table")

    query_bilete = "INSERT INTO bilete ( film_id, client_id, sala_id, pret, data_ora) VALUES(%s, %s, %s, %s, %s)"

    lista_bilete = [
        (1, 7, 1, 50, datetime(2022, 4, 29, 18)),
        (1, 7, 1, 30, datetime(2023, 4, 29, 18)),
        (2, 9, 2, 20, datetime(2023, 3, 12, 22)),
        (3, 4, 2, 20, datetime(2023, 4, 28, 19)),
        (3, 4, 2, 20, datetime(2023, 2, 15, 16)),
        (7, 3, 3, 30, datetime(2023, 4, 29, 17)),
        (6, 1, 1, 30, datetime(2023, 1, 29, 20, 30)),
        (3, 2, 4, 20, datetime(2023, 2, 9, 18, 45)),
        (2, 9, 4, 20, datetime(2023, 3, 22, 18, 45)),
        (5, 10, 4, 20, datetime(2023, 5, 5, 19)),
        (4, 3, 1, 30, datetime(2023, 4, 4, 14)),
        (4, 4, 4, 20, datetime(2023, 4, 27, 21, 30)),
        (2, 5, 4, 20, datetime(2023, 1, 2, 19)),
        (3, 6, 4, 20, datetime(2022, 12, 9, 20, 30)),
        (7, 6, 3, 30, datetime(2023, 4, 26, 17)),
        (6, 9, 5, 20, datetime(2023, 3, 9, 13)),
        (5, 7, 4, 20, datetime(2023, 1, 2, 22)),
        (4, 1, 4, 20, datetime(2023, 4, 13, 16, 30)),
        (3, 8, 4, 20, datetime(2023, 5, 7, 19, 45)),
        (1, 2, 5, 20, datetime(2023, 5, 2, 20, 20)),
        (2, 8, 5, 20, datetime(2023, 4, 7, 17, 45))
    ]

    cursor.executemany(query_bilete, lista_bilete)
    print(cursor.rowcount, "records inserted into bilete table")

    db_connection.commit()

def ex_4_a():
    global cursor
    # 		a.	total incasari de anul acesta (2023) pentru filmul cu id=1 (option1: afisam "movie_id, suma_pret"
    # 		|   option2: afisam "movie_id, nume_film, suma_pret")
    print("\n\nEx. 4a...\n")

    query = """
        select bilete.film_id, filme.nume, SUM(bilete.pret) from bilete 
        join filme on bilete.film_id = filme.id
        where film_id = 1
        and YEAR(data_ora) = 2023;
    """
    cursor.execute(query)


    total_incasari = cursor.fetchall()
    print("\n\n--------------------------------")
    print("Names:\n")
    for name in total_incasari:
        print(name)
    print("--------------------------------\n\n")

    print(f"\n\n  -  success!")


def ex_4_b():
    global cursor
    # denumire sala cu cele mai slabe incasari "all time"
    print("\n\nEx. 4b...\n")

    query = """
        select bilete.sala_id, sali.denumire, SUM(bilete.pret) as total_incasari
        from bilete
        join sali on sali.id = bilete.sala_id
        group by sala_id
        order by total_incasari ASC;
    """
    cursor.execute(query)


    total_incasari = cursor.fetchone()
    print("\n\n--------------------------------")
    print(total_incasari)
    print("--------------------------------\n\n")

    print(f"\n\n  -  success!")

def ex_4_c():
    global cursor
# c. 	numele clientului si suma totala cheltuita "all time" (doar clientul cu cea mai mare suma cheltuita)
    print("\n\nEx. 4c...\n")
    query = """
        select clienti.nume, SUM(bilete.pret) as suma_cheltuita
        from bilete
        join clienti on clienti.id = bilete.client_id
        group by clienti.nume
        order by suma_cheltuita DESC;
    """
    cursor.execute(query)

    client = cursor.fetchone()

    print(client)

def ex_4_d():
    global cursor
    # toti clientii(nume si email) care au adresa de email de la 'hotmail'
    print("\n\nEx. 4d...\n")

    query = """
        select nume, email from clienti
        where email LIKE "%hotmail%";
    """

    cursor.execute(query)

    adrese_hotmail = cursor.fetchall()
    print("\n\n--------------------------------")
    print("Clientii cu adresele de mail care contin hotmail sunt:\n")
    for clienti in adrese_hotmail:
        print(clienti)
    print("--------------------------------\n\n")

    print(f"\n\n  -  success!")

def ex_4_e():
    global cursor
    # mareste capacitatea la 90 pentru sala 9
    print("\n\nEx. 4e...\n")

    query = """
        update sali
        set capacitate = 90
        where id = 3;
    """

    cursor.execute(query)
    db_connection.commit()

    # q = "SELECT * FROM sali"
    # cursor.execute(q)
    # sali = cursor.fetchall()
    # for sala in sali:
    #     print(sala)

connect_to_database()
create_database()
create_tables()
# insert_into_table()
ex_4_a()
ex_4_b()
ex_4_c()
ex_4_d()
ex_4_e()











