# open terminal -> pip install sqlalchemy
# open terminal -> pip install mysqlclient
# open terminal -> pip install mysql-connector-python

import mysql.connector as mysql

import os
from sqlalchemy import create_engine, inspect, text, func, desc, and_, or_, not_, join
from sqlalchemy.orm import declarative_base, sessionmaker
from models_final import Base, Cars, Clients, Bookings
import datetime

######################################################################################################################
### SQL Basics ###
    # db_connection = None
    # cursor = None
######################################################################################################################


######################################################################################################################
### SQL Alchemy ###

### dialect+driver://username:password@host:port/database ###
CONNECTION_STRING = f"mysql+mysqlconnector://root:password@localhost:3306/car_rental"               ### use it before creating database car_rental ###
# CONNECTION_STRING = f"mysql+mysqlconnector://root:Minitehnicus7$@localhost:3306/car_rental"   ### use it after creating database car_rental ###

engine = None       ### engine represents connection to database ###
inspector = None    ### used to inspect an object for the given target ### used to get information about: table columns, database table names, databases names ###
session = None      ### session is the object that communicate with the database ###
######################################################################################################################


def show_menu():

    os.system('cls')

    print(f"\nMENU:\n")

    print(f" 1. SHOW Database")
    print(f" 2. CREATE Tables")
    print(f" 3. SHOW Tables Names")
    print(f" 4. SHOW Table Description")
    print(f" 5. DROP Table")
    print(f" 6. INSERT INTO Table")
    print(f" 7. SELECT Table")
    print(f" 8. SELECT specific Columns from Table")
    print(f" 9. SELECT where CONDITION")
    print(f"10. DELETE Table")
    print(f" 0. Exit")

    print(f"\n\n\nYOUR choice:")


def make_a_choice():

    print("Choose an option:")
    option = input()

    return option


def connect_to_database():

    ######################################################################################################################
    ### SQL Basics ###
        # global cursor
        # global db_connection
        # print("\n\nConnecting to database...\n")

        # ##########################################################################
        # ### create database connection ###
        # # connecting to the database using 'connect()' method
        # # it takes 3 required parameters 'host', 'user', 'passwd'
        # # after creating a database add parameter 'database'
        # db_connection = mysql.connect(
        #         host="localhost",
        #         user="root",
        #         password="Minitehnicus7$",
        #         database="solo_academy"
        # )

        # print(db_connection)  # it will print a connection object if everything is fine
        # ##########################################################################


        # ##########################################################################
        # ### create cursor ###
        # ## creating an instance of 'cursor' class which is used to execute the 'SQL' statements in 'Python'
        # cursor = db_connection.cursor()
        # ##########################################################################
    ######################################################################################################################

    ######################################################################################################################
    ### SQL Alchemy ###
    global engine
    global inspector
    global session
    global CONNECTION_STRING

    ### create connection to database ###
    engine = create_engine(CONNECTION_STRING)

    ### create inspector object ### helpful to get some info about database, tables ###
    inspector = inspect(engine)

    ### instantiate session object ###   
    session = sessionmaker(bind=engine)()
    ######################################################################################################################


def create_database():

    print("\n\nCreating to database...\n")
    
    ######################################################################################################################
    ### SQL Basics ###
        # ##########################################################################
        # ### create database ###
        
        # ### query: CREATE DATABASE IF NOT EXISTS database_name ###
        # ### 'execute()' method is used to compile a 'SQL' statement ###
        # cursor.execute("CREATE DATABASE IF NOT EXISTS solo_academy")
        # ##########################################################################
    ######################################################################################################################


    ######################################################################################################################
    ### SQL Alchemy ###
    global engine

    ### create database car_rental ###
    with engine.connect() as conn:
        conn.execute(text("CREATE DATABASE IF NOT EXISTS car_rental"))

        # rows = conn.execute(text("SELECT * from solo_academy.studenti"))

        # for row in rows:
        #     print(row)
    ######################################################################################################################


def show_database():

    ######################################################################################################################
    ### SQL Basics ###
        # global cursor
        # print("\n\nShowing database...\n")

        # ### execute SQL QUERY ###
        # cursor.execute("SHOW DATABASES")

        # ## 'fetchall()' method fetches all the rows from the last executed statement
        # ## 'fetchone()' method fetches only the first row from the last executed statement
        # databases = cursor.fetchall() ## it returns a list of all databases present


        # #################################
        # ## printing the list of databases
        # print("\n\n----------------------------------------------")
        # print("Databases list:\n")
        # print('type:', type(databases))
        # print(databases)
        # print("----------------------------------------------\n\n")
        # #################################


        # #################################
        # ## showing one by one database
        # print("\n\n----------------------------------------------")
        # print("Databases one by one:\n")
        # for database in databases:
        #     print(f"{database[0]}  -  type:{type(database[0])}")
        # print("----------------------------------------------\n\n")
        # #################################
    ######################################################################################################################
    

    ######################################################################################################################
    ### SQL Alchemy ###
    global inspector

    ### show databases from root path ###
    print(inspector.get_schema_names())
    ######################################################################################################################

    print(f"\n\n  -  success!")


def create_tables():
    
    ######################################################################################################################
    ### SQL Basics ###
        # global cursor
        # print("\n\nCreating Tables...\n")

        # ######################################################################
        # ### TASK ###
        # ### creating a tables called 'studenti' and 'note_studenti' in the 'solo_academy' database ###
        # ### tables: studenti, note_studenti ###
        # ######################################################################
        
        # ######################################################################
        # ### HINT ### COLUMNS ###
        # ### studenti columns: id, nume, prenume, email, telefon, data_nasterii ###
        # ### note_studenti columns: id, student_id, nota, materie ###
        # ######################################################################


        # ######################################################################
        # ### option 1 ### write sql instruction inside the cursor.execute ###

        # cursor.execute("CREATE TABLE IF NOT EXISTS studenti (id INT PRIMARY KEY AUTO_INCREMENT, nume VARCHAR(100) NOT NULL, prenume VARCHAR(100) NOT NULL, \
        #                 email VARCHAR(100) UNIQUE, telefon VARCHAR(100), data_nasterii DATE)")
        # ######################################################################


        # ######################################################################
        # ### option 2 ### write sql instruction inside a variable and after that use the variable with cursor.execute ###

        # create_table_note_studenti = """
        #     CREATE TABLE IF NOT EXISTS note_studenti (
        #           id INT PRIMARY KEY AUTO_INCREMENT,
        #           student_id INT,
        #           nota DECIMAL(4,2),
        #           materie VARCHAR(255) NOT NULL
        #     );"""

        # cursor.execute(create_table_note_studenti)
        # ######################################################################
    ######################################################################################################################


    ######################################################################################################################
    ### SQL Alchemy ###
    global engine

    ### create all tables ###
    Base.metadata.create_all(engine)

    ### create only 1 table ### table cars ###
    # Cars.__table__.create(engine)
    ######################################################################################################################

    print(f"\n\n  -  success!")


def show_tables_names():

    ######################################################################################################################
    ### SQL Basics ###
        # global cursor
        # print("\n\nShowing Tables Names...\n")

        # ### getting all tables from our selected database ###
        # cursor.execute("SHOW TABLES")

        # ### returns a list of tables present in our selected database ###
        # tables = cursor.fetchall()

        # ### showing all the tables one by one ###
        # print("\n\n----------------------------------")
        # print("Tables list:\n")
        # for table in tables:
        #     print(table)
        # print("----------------------------------\n\n")
    ######################################################################################################################


    ######################################################################################################################
    ### SQL Alchemy ###
    global inspector

    ### show tables names ###
    print(inspector.get_table_names())
    ######################################################################################################################

    print(f"\n\n  -  success!")


def show_table_description():

    ######################################################################################################################
    ### SQL Basics ###
        # global cursor
        # print("\n\nShowing table description...\n")

        # ### choose table name ###
        # table_name = make_a_choice()

        # ### query: DESC table_name ###
        # ### get all columns information from selected table ###
        # cursor.execute(f"DESC {table_name}")

        # ### returns list of tuples with each column information ###
        # ### (Column, Type, is Null, KEY, Defauld, Extra) ###
        # results = cursor.fetchall()

        # print("\n\n--------------------------------")
        # print("Column Description:\n")
        # for result in results:
        #     print(result)

        # print("--------------------------------\n\n")
    ######################################################################################################################


    ######################################################################################################################
    ### SQL Alchemy ###
    global inspector

    ### choose table name ###
    table_name = make_a_choice()

    ### get table description ###
    columns = inspector.get_columns(table_name)

    ### print ###
    for column in columns:
        print("\n\n")
        for detail in column:
            print(f"{detail}: {column[detail]}")
    ######################################################################################################################

    print(f"\n\n  -  success!")


def drop_table():

    ######################################################################################################################
    ### SQL Basics ###
        # global cursor
        # print("\n\nDropping table...\n")

        # ### choose table name ###
        # table_name = make_a_choice()

        # ### query: DROP TABLE IF NOT EXISTS table_name ###
        # cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
    ######################################################################################################################


    ######################################################################################################################
    ### SQL Alchemy ###
    global engine

    ### choose table name ###
    table_name = make_a_choice()

    if table_name == 'all':
        ### drop all tables ###
        Base.metadata.drop_all(engine)

    elif table_name == 'cars':
        ### drop table cars ###
        Cars.__table__.drop(engine)

    elif table_name == 'clients':
        ### drop table clients ###
        Clients.__table__.drop(engine)

    elif table_name == 'bookings':
        ### drop table bookings ###
        Bookings.__table__.drop(engine)
    ######################################################################################################################

    print(f"\n\n  -  success!")


def insert_into_table():

    ######################################################################################################################
    ### SQL Basics ###
        # global cursor
        # global db_connection
        # print("\n\nInserting into table...\n")

        # #######################################################################
        # ### single line ###

        # ### query: INSERT INTO table name (column1, column2, ...) VALUES (val1, val2, ...) ###
        # ## use %s in VALUES to give dinamic values using a variable ###
        # query_studenti = "INSERT INTO studenti (nume, prenume, email, telefon, data_nasterii) VALUES (%s, %s, %s, %s, %s)"
        # query_note= "INSERT INTO note_studenti (student_id, nota, materie) VALUES (%s, %s, %s)"

        # ### storing values in a variable -> TUPPLE ###
        # values_studenti_single_line = ("solo", "bogdan", "solo_bogdan@gmail.com", "0755777555", datetime(1992, 1, 7))
        # values_note_single_line = ("1", 8.5, "limba_matematica")

        # ## executing the query with values
        # cursor.execute(query_studenti, values_studenti_single_line)
        
        # ## print how many rows were added
        # print(cursor.rowcount, "records inserted into studenti table")

        # cursor.execute(query_note, values_note_single_line)
        # print(cursor.rowcount, "records inserted into note_studenti table")

        # ### save changes to our database ###
        # db_connection.commit()
        # #######################################################################


        # #######################################################################
        # ### multi lines ###

        # values_studenti_multi_line = [
        #     ("stan", "alina", "stan_alina@gmail.com", "0755333111", datetime(1994, 5, 10)),         #2
        #     ("popescu", "ionut", "popescu_ionut@gmail.com", "0755111222", datetime(1992, 7, 13)),   #3
        #     ("stropinel", "vasile", "stropi@gmail.com", "0755111333", datetime(1998, 8, 23)),       #4
        #     ("mfede", "leusteniu", "mfede@gmail.com", "0755111444", datetime(2002, 12, 22)),        #5
        # ]

        # values_note_multi_line = [
        #     (2, 10, "limba_matematica"),
        #     (3, 5.5, "limba_matematica"),
        #     (4, 3.5, "limba_matematica"),
        #     (5, 7.7, "limba_matematica"),
        # ]

        # ### when adding multiple lines use cursor.executemany(query, values) ###
        # cursor.executemany(query_studenti, values_studenti_multi_line)
        # print(cursor.rowcount, "records inserted into studenti table")

        # cursor.executemany(query_note, values_note_multi_line)
        # print(cursor.rowcount, "records inserted into note_studenti table")

        # ### save changes to our database ###
        # db_connection.commit()
        # #######################################################################
    ######################################################################################################################


    ######################################################################################################################
    ### SQL Alchemy ###
    global session

    cars_list = [
        Cars(producer="Dacia", model="1310", year="1973", horse_power="72", price_per_day="10"),            # 1 #
        Cars(producer="Trabant", model="din 68'", year="1968", horse_power="55", price_per_day="5"),        # 2 #
        Cars(producer="Toyota", model="Yaris", year="2017", horse_power="92", price_per_day="15"),          # 3 #
        Cars(producer="BMW", model="Seria 5", year="2008", horse_power="167", price_per_day="70"),          # 4 #
        Cars(producer="Mercedes", model="GLE", year="2010", horse_power="194", price_per_day="70"),         # 5 #
        Cars(producer="Hyundai", model="Tucson", year="2019", horse_power="112", price_per_day="30"),       # 6 #
        Cars(producer="Honda", model="e", year="2023", horse_power="134", price_per_day="30"),              # 7 #
        Cars(producer="Volvo", model="XC40", year="2021", horse_power="154", price_per_day="50"),           # 8 #
        Cars(producer="Lamborghini", model="Urus", year="2020", horse_power="243", price_per_day="150"),    # 9 #
        Cars(producer="Mazda", model="CX-3", year="2020", horse_power="163", price_per_day="50"),           # 10 #
        Cars(producer="Suzuki", model="Swift", year="2005", horse_power="92", price_per_day="30"),          # 11 #
        Cars(producer="Ford", model="Fiesta", year="2013", horse_power="85", price_per_day="30"),           # 12 #
        Cars(producer="Volkswagen", model="Polo", year="2000", horse_power="85", price_per_day="30"),       # 13 #
        Cars(producer="Renault", model="Zoe", year="2022", horse_power="120", price_per_day="40"),          # 14 #
        Cars(producer="Skoda", model="Octavia", year="2018", horse_power="92", price_per_day="30"),         # 15 #
        Cars(producer="Opel", model="Astra", year="2016", horse_power="92", price_per_day="30"),            # 16 #
        Cars(producer="Kia", model="Sportage", year="2021", horse_power="112", price_per_day="40"),         # 17 #
        Cars(producer="Peugeot", model="208", year="2002", horse_power="85", price_per_day="15"),           # 18 #
        Cars(producer="Peugeot", model="2008", year="2022", horse_power="122", price_per_day="40"),         # 19 #
    ]

    clients_list = [
        Clients(name="bogdan", surname="solo", address="mihai viteazu nr.7", city="sibiu"),                 # 1 #
        Clients(name="alina", surname="stan", address="stefan cel mare nr.7", city="bucuresti"),            # 2 #
        Clients(name="andreea", surname="balan", address="vlad tepes nr.7", city="zalau"),                  # 3 #
        Clients(name="mihai", surname="bendeac", address="baiazid nr.7", city="baia mare"),                 # 4 #
        Clients(name="mihai", surname="bobonete", address="hassan pasa nr.7", city="bucuresti"),            # 5 #
        Clients(name="dorel", surname="japoniaaa", address="mihai eminescu nr.7", city="brasov"),           # 6 #
    ]

    bookings_list = [
        Bookings(client_id="1", car_id="2", start_date="2023-01-05", end_date="2023-01-06", total_amount=5),        # 1 day #
        Bookings(client_id="1", car_id="1", start_date="2023-01-10", end_date="2023-01-12", total_amount=20),       # 2 days #
        Bookings(client_id="1", car_id="2", start_date="2023-01-15", end_date="2023-01-18", total_amount=15),       # 3 days #
        Bookings(client_id="3", car_id="4", start_date="2023-01-05", end_date="2023-01-06", total_amount=70),       # 1 day #
        Bookings(client_id="2", car_id="5", start_date="2023-01-10", end_date="2023-01-12", total_amount=140),      # 2 days #
        Bookings(client_id="2", car_id="9", start_date="2023-01-15", end_date="2023-01-18", total_amount=450),      # 3 days #
        Bookings(client_id="4", car_id="11", start_date="2023-01-20", end_date="2023-01-24", total_amount=120),     # 4 days #
        Bookings(client_id="5", car_id="16", start_date="2023-01-05", end_date="2023-01-06", total_amount=30),      # 1 day #
        Bookings(client_id="6", car_id="9", start_date="2023-01-05", end_date="2023-01-06", total_amount=150),      # 1 day #
        Bookings(client_id="6", car_id="5", start_date="2023-01-10", end_date="2023-01-12", total_amount=140),      # 2 days #
        Bookings(client_id="6", car_id="4", start_date="2023-01-15", end_date="2023-01-18", total_amount=210),      # 3 days #
        Bookings(client_id="6", car_id="8", start_date="2023-01-20", end_date="2023-01-24", total_amount=200),      # 4 days #
        Bookings(client_id="6", car_id="2", start_date="2023-01-25", end_date="2023-01-30", total_amount=25),       # 5 days #
        Bookings(client_id="1", car_id="18", start_date="2023-01-25", end_date="2023-01-30", total_amount=75),       # 5 days #
    ]

    ### add each list into table ### session know which list to add in which table by the objects declared inside the variables ###
    session.add_all(cars_list)
    session.add_all(clients_list)
    session.add_all(bookings_list)

    ### add only 1 line ###
    # session.add(
    #     Clients(name="rares", surname="sss", address="doamna stanca nr.7", city="constanta"),           # 7 #
    #     )

    ### commit after each insert/update/delete ###
    session.commit()
    ######################################################################################################################

    print(f"\n\n  -  success!")


def select_table():

    ######################################################################################################################
    ### SQL Basics ###
        # global cursor
        # print("\n\nSelecting table...\n")

        # ### SELECT * FROM table name ###
        # query_studenti = "SELECT * FROM studenti"
        # query_note = "SELECT * FROM note_studenti"

        # cursor.execute(query_studenti)
        # studenti_records = cursor.fetchall()

        # cursor.execute(query_note)
        # note_studenti_records = cursor.fetchall()

        # print("\n\n--------------------------------")
        # print("Studenti:\n")
        # for record in studenti_records:
        #     print(record)
        # print("--------------------------------\n\n")


        # print("\n\n--------------------------------")
        # print("Note:\n")
        # for record in note_studenti_records:
        #     print(record)
        # print("--------------------------------\n\n")
    ######################################################################################################################


    ######################################################################################################################
    ### SQL Alchemy ###
    global session

    ### choose table name ###
    table_name = make_a_choice()

    if table_name == 'all':
        ### select all tables ###
        rows_cars = session.query(Cars).all()
        rows_clients = session.query(Clients).all()
        rows_bookings = session.query(Bookings).all()

    elif table_name == 'cars':
        ### select table cars ###
        rows = session.query(Cars).all()

    elif table_name == 'clients':
        ### select table clients ###
        rows = session.query(Clients).all()

    elif table_name == 'bookings':
        ### select table bookings ###
        rows = session.query(Bookings).all()

    else:
        ### table name unknown ###
        print(f"Selection unknown!")
        return


    ### print all tables ###
    if table_name == 'all':
        for result in [[rows_cars, 'Cars:'], [rows_clients, 'Clients:'], [rows_bookings, 'Bookings:']]:
            print(f"\n\n---------------------------------------")
            print(f"{result[1]}\n")
            for row in result[0]:
                print(row)
            print(f"---------------------------------------\n\n")

    ### print 1 table ###
    else: 
        print(f"\n\n---------------------------------------")
        print(f"{table_name.title()}:\n")
        for row in rows:
            print(row)
        print(f"---------------------------------------\n\n")
    ######################################################################################################################

    print(f"\n\n  -  success!")


def select_table_specific_columns():

    ######################################################################################################################
    ### SQL Basics ###
        # global cursor
        # print("\n\nSelecting table with specific columns...\n")

        # query = "SELECT nume from studenti"
        # cursor.execute(query)
        
        # # names = cursor.fetchone()
        # # print(names)

        # names = cursor.fetchall()
        # print("\n\n--------------------------------")
        # print("Names:\n")
        # for name in names:
        #     print(name)
        # print("--------------------------------\n\n")
    ######################################################################################################################


    ######################################################################################################################
    ### SQL Alchemy ###
    global session

    rows = session.query(Cars.producer, Cars.model).all()   ### returns a list of tuples ###

    print(f"\n\n---------------------------------------")
    print(f"Cars:\n")
    for row in rows:
        print(row)
    print(f"---------------------------------------\n\n")
    ######################################################################################################################

    print(f"\n\n  -  success!")


def select_where_condition():

    ######################################################################################################################
    ### SQL Basics ###
        # global cursor
        # print("\n\nSelecting table where condition...\n")

        # ### SELECT * FROM table_name WHERE condition ###

        # ###########################################################
        # ### option 1 ### select students where id = 5 ###
        # ### option 2 ### select students ordered by nume ###
        # ### option 3 ### select students order by data nasterii from oldest to youngest ###
        # ### option 4 ### select 1st student (nume, nota, materie) with the highest grade in limba matematica ###
        # ### option 5 ### select 1st student with the highest grade in limba matematica ###
        # ###########################################################

        # option = make_a_choice()

        # if option == '1':
        #     query = "SELECT * FROM studenti WHERE id = 5"

        # elif option == '2':
        #     query = "SELECT * FROM studenti ORDER BY nume"

        # elif option == '3':
        #     query = "SELECT * FROM studenti ORDER BY data_nasterii"

        # elif option == '4':
        #     query = """
        #             SELECT s.nume as castigatorul, ns.nota, ns.materie
        #             FROM note_studenti ns 
        #             JOIN studenti s ON s.id = ns.student_id
        #             WHERE ns.materie = 'limba_matematica'
        #             ORDER BY ns.nota DESC
        #             LIMIT 1
        #         """

        # elif option == '5':
        #     query = """
        #             SELECT s.nume as castigatorul, ns.nota, ns.materie
        #             FROM note_studenti ns 
        #             JOIN studenti s ON s.id = ns.student_id
        #             WHERE ns.materie = 'limba_matematica'
        #             ORDER BY ns.nota DESC
        #         """

        # else:
        #     print("Selection unknown!")
        #     return

        # cursor.execute(query)
        # if option == '5':
        #     records = cursor.fetchone()
        #     print("\n\n--------------------------------")
        #     print("My search:\n")
        #     print(records)
        #     print("--------------------------------\n\n")

        # else:
        #     records = cursor.fetchall()

        #     print("\n\n--------------------------------")
        #     print("My search:\n")
        #     for record in records:
        #         print(record)
        #     print("--------------------------------\n\n")
    ######################################################################################################################


    ######################################################################################################################
    ### SQL Alchemy ###
    global session

    ###########################################################
    ### option 1 ### count how many cars are in total ###
    ### option 2 ### select all clients where surname starts with letter 's' ###
    ### option 3 ### select most expensive car by price per day ###
    ### option 4 ### select clients that had a car in their possesion on 10th of January 2023 ### (surname, car_producer, car_model, booking_start_date, booking_end_date) ###
    ### option 5 ### select all cars that do NOT have the manufacture year between 2000 - 2010 ### (producer, model, year) ###
    ### option 6 ### set horse_powers = 230 to Car: Trabant(producer) ###
    ### option 7 ### delete car from fleet: Peugeot 208 ###
    ###########################################################

    option = make_a_choice()

    if option == '1':
        ### rezultat ### 14 ###
        print("\n\nHow many cars are in our CAR fleet?")
        
        total = session.query(Cars).count()
        print(f"Total: {total}")


    elif option == '2':
        ### rezultat ### solo bogdan | stan alina ###
        print("\n\nClients that their surname starts with 's':")
        rows = []

        ### filter ###
        rows = session.query(Clients).filter(Clients.surname.like("s%")).all()
        
        ### where ###
        # rows = session.query(Clients).where(Clients.surname.like("s%")).all()
        
        ### filter by ###
        # print(session.query(Clients).filter_by(name="mihai").first())

        for row in rows:
            print(row)


    elif option == '3':
        ### rezultat ### Lamborghini  -  Urus  -  2020  -  243CP  -  $150.00 ###
        print("\n\nMost expensive car (by daily price rate):")

        most_expensive_car = session.query(Cars).order_by(desc(Cars.price_per_day)).first()
        print(most_expensive_car)


    elif option == '4':
        ### rezultat ### 
        ### ('solo', 'Dacia', '1310', datetime.date(2023, 1, 10), datetime.date(2023, 1, 12)) ###
        ### ('stan', 'Mercedes', 'GLE', datetime.date(2023, 1, 10), datetime.date(2023, 1, 12)) ###
        ### ('japoniaaa', 'Mercedes', 'GLE', datetime.date(2023, 1, 10), datetime.date(2023, 1, 12)) ###
        print("\n\nClients that had a car in their possesion on 10th of January 2023:")


        ### and ###
        targeted_clients = session.query(Clients.surname, Cars.producer, Cars.model, Bookings.start_date, Bookings.end_date).\
                           join(Bookings, and_(Bookings.start_date <= '2023-01-10', '2023-01-10' <= Bookings.end_date, Clients.id == Bookings.client_id)). \
                           join(Cars, and_(Cars.id == Bookings.car_id)).\
                           all()

        for client in targeted_clients:
            print(client)


    elif option == '5':
        ### rezultat ### look at the manufacture year (they are 14 in total) ###
        print("\n\nCars that do NOT have manufacture year between 2000 - 2010:")

        ### year is not betweeen 2000 - 2010 ### using filter + or_ ###
        targeted_cars = session.query(Cars.producer, Cars.model, Cars.year).filter(or_(Cars.year < 2000, Cars.year > 2010)).order_by(Cars.year).all()

        ### year is not betweeen 2000 - 2010 ### using where + or_ ###
        # targeted_cars = session.query(Cars.producer, Cars.model, Cars.year).where(or_(Cars.year < 2000, Cars.year > 2010)).order_by(Cars.year).all()

        ### year is not betweeen 2000 - 2010 ### using filter + between + not_ ###
        # targeted_cars = session.query(Cars.producer, Cars.model, Cars.year).filter(not_(Cars.year.between(2000, 2010))).order_by(Cars.year).all()

        ### year is between 2000 - 2010 ### using between ###
        # targeted_cars = session.query(Cars.producer, Cars.model, Cars.year).filter(Cars.year.between(2000, 2010)).order_by(Cars.year).all()

        i = 0
        for car in targeted_cars:
            i += 1
            print(f"{i}.{car}")


    elif option == '6':
        ### rezultat ### check after with select function ###
        print("\n\nSet 230CP to Trabant:")

        my_car = session.query(Cars).where(Cars.producer == 'Trabant').first()
        my_car.horse_power = 230
        session.commit()


    elif option == '7':
        ### rezultat ### check after with select function ###
        print("\n\nDelete Peugeot 208 from our car fleet:")

        my_cars = session.query(Cars).where(and_(Cars.producer == "Peugeot", Cars.model == '208')).all()

        for car in my_cars:
            session.delete(car)
        session.commit()

    else:
        ### option unknown ###
        print("Selection unknown!")
        return
    ######################################################################################################################

    print(f"\n\n  -  success!")


def delete_table():

    ######################################################################################################################
    ### SQL Basics ###
        # global cursor
        # global db_connection
        # print("\n\nDeleting table...\n")

        # ### DELETE FROM table_name ###
        # ### DELETE FROM table_name WHERE condition ###

        # query_studenti = "DELETE FROM studenti"
        # query_note_studenti = "DELETE FROM note_studenti where nota < 5"

        # cursor.execute(query_studenti)
        # cursor.execute(query_note_studenti)

        # db_connection.commit()
    ######################################################################################################################


    ######################################################################################################################
    ### SQL Alchemy ###
    global session

    ### choose table name ###
    table_name = make_a_choice()

    if table_name == 'cars':
        ### delete table cars ###
        session.query(Cars).delete()

        ### save - commit ###
        session.commit()

    elif table_name == 'clients':
        ### delete table clients ###
        session.query(Clients).delete()

        ### save - commit ###
        session.commit()

    elif table_name == 'bookings':
        ### delete table clients ###
        session.query(Bookings).delete()

        ### save - commit ###
        session.commit()

    else:
        print(f"Selection unknown!")

    ######################################################################################################################

    print(f"\n\n  -  success!")


def update_table():

    ######################################################################################################################
    ### SQL Basics ###
        # global cursor
        # global db_connection
        # print("\n\nUpdating table where condition...\n")
        
        # ### query: UPDATE table_name SET col1 = val1, col2 = val2, ... WHERE condition ###
        # ### TASK: Update nota lui Stan la limba matematica cu 2 ###
        # query = "UPDATE note_studenti SET nota = 2 WHERE student_id = 2 and materie = 'limba_matematica'"

        # cursor.execute(query)
        # db_connection.commit()
    ######################################################################################################################


    ######################################################################################################################
    ### SQL Alchemy ###

    ######################################################################################################################

    print(f"\n\n  -  success!")


def main():

    ###################
    ### SQL Basics ###
        # global cursor
        # global db_connection
    ###################
    
    ###################
    global engine
    global session
    ###################

    connect_to_database()
    create_database()

    while True:

        show_menu()

        choice = input()

        if choice == '0':
            ###################
            ### SQL Basics ###
                # db_connection.close()
            ###################

            ###################
            ### SQL Alchemy ###
            session.close()
            ###################

            break

        elif choice == '1':
            show_database()

        elif choice == '2':
            create_tables()

        elif choice == '3':
            show_tables_names()

        elif choice == '4':
            show_table_description()

        elif choice == '5':
            drop_table()

        elif choice == '6':
            insert_into_table()

        elif choice == '7':
            select_table()

        elif choice == '8':
            select_table_specific_columns()

        elif choice == '9':
            select_where_condition()

        elif choice == '10':
            delete_table()

        else:
            print("Selection unknown!")

        input()

if __name__ == '__main__':
    main()