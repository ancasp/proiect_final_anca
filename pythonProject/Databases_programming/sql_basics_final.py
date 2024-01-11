# importing 'mysql.connector' as mysql for convenient
# open terminal -> pip install mysql-connector-python

import os
from datetime import datetime 
import mysql.connector as mysql

db_connection = None
cursor = None



def show_menu():

    os.system('cls')

    print(f"\nMENU:\n")

    print(f" 1. SHOW Database")
    print(f" 2. CREATE Tables")
    print(f" 3. SHOW Tables Names")
    print(f" 4. SHOW Table Description")
    print(f" 5. DROP Table")
    print(f" 6. DROP Column")
    print(f" 7. ADD Column")
    print(f" 8. INSERT INTO Table")
    print(f" 9. SELECT Table")
    print(f"10. SELECT specific Columns from Table")
    print(f"11. DELETE Table")
    print(f"12. UPDATE Table")
    print(f"13. SELECT where CONDITION")
    print(f"14. Exercitiu")
    print(f" 0. Exit")

    print(f"\n\n\nYOUR choice:")


def make_a_choice():

    print("Choose an option:")
    option = input()

    return option


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
            database="solo_academy"
    )

    print(db_connection)  # it will print a connection object if everything is fine
    ##########################################################################


    ##########################################################################
    ### create cursor ###
    ## creating an instance of 'cursor' class which is used to execute the 'SQL' statements in 'Python'
    cursor = db_connection.cursor()
    ##########################################################################


def create_database():

    print("\n\nCreating to database...\n")
    
    ##########################################################################
    ### create database ###
    
    ### query: CREATE DATABASE IF NOT EXISTS database_name ###
    ### 'execute()' method is used to compile a 'SQL' statement ###
    cursor.execute("CREATE DATABASE IF NOT EXISTS solo_academy")
    ##########################################################################


def show_database():

    global cursor
    print("\n\nShowing database...\n")

    ### execute SQL QUERY ###
    cursor.execute("SHOW DATABASES")

    ## 'fetchall()' method fetches all the rows from the last executed statement
    ## 'fetchone()' method fetches only the first row from the last executed statement
    databases = cursor.fetchall() ## it returns a list of all databases present


    #################################
    ## printing the list of databases
    print("\n\n----------------------------------------------")
    print("Databases list:\n")
    print('type:', type(databases))
    print(databases)
    print("----------------------------------------------\n\n")
    #################################


    #################################
    ## showing one by one database
    print("\n\n----------------------------------------------")
    print("Databases one by one:\n")
    for database in databases:
        print(f"{database[0]}  -  type:{type(database[0])}")
    print("----------------------------------------------\n\n")
    #################################
    
    print(f"\n\n  -  success!")


def create_tables():
    
    global cursor
    print("\n\nCreating Tables...\n")

    ######################################################################
    ### TASK ###
    ### creating a tables called 'studenti' and 'note_studenti' in the 'solo_academy' database ###
    ### tables: studenti, note_studenti ###
    ######################################################################
    
    ######################################################################
    ### HINT ### COLUMNS ###
    ### studenti columns: id, nume, prenume, email, telefon, data_nasterii ###
    ### note_studenti columns: id, student_id, nota, materie ###
    ######################################################################


    ######################################################################
    ### option 1 ### write sql instruction inside the cursor.execute ###

    cursor.execute("CREATE TABLE IF NOT EXISTS studenti (id INT PRIMARY KEY AUTO_INCREMENT, nume VARCHAR(100) NOT NULL, prenume VARCHAR(100) NOT NULL, \
                    email VARCHAR(100) UNIQUE, telefon VARCHAR(100), data_nasterii DATE)")
    ######################################################################


    ######################################################################
    ### option 2 ### write sql instruction inside a variable and after that use the variable with cursor.execute ###

    create_table_note_studenti = """
        CREATE TABLE IF NOT EXISTS note_studenti (
              id INT PRIMARY KEY AUTO_INCREMENT,
              student_id INT,
              nota DECIMAL(4,2),
              materie VARCHAR(255) NOT NULL
        );"""

    cursor.execute(create_table_note_studenti)
    ######################################################################

    print(f"\n\n  -  success!")


def show_tables_names():

    global cursor
    print("\n\nShowing Tables Names...\n")

    ### getting all tables from our selected database ###
    cursor.execute("SHOW TABLES")

    ### returns a list of tables present in our selected database ###
    tables = cursor.fetchall()

    ### showing all the tables one by one ###
    print("\n\n----------------------------------")
    print("Tables list:\n")
    for table in tables:
        print(table)
    print("----------------------------------\n\n")

    print(f"\n\n  -  success!")


def show_table_description():

    global cursor
    print("\n\nShowing table description...\n")

    ### choose table name ###
    table_name = make_a_choice()

    ### query: DESC table_name ###
    ### get all columns information from selected table ###
    cursor.execute(f"DESC {table_name}")

    ### returns list of tuples with each column information ###
    ### (Column, Type, is Null, KEY, Default, Extra) ###
    results = cursor.fetchall()

    print("\n\n--------------------------------")
    print("Column Description:\n")
    for result in results:
        print(result)

    print("--------------------------------\n\n")

    print(f"\n\n  -  success!")


def drop_table():

    global cursor
    print("\n\nDropping table...\n")

    ### choose table name ###
    table_name = make_a_choice()

    ### query: DROP TABLE IF EXISTS table_name ###
    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

    print(f"\n\n  -  success!")


def drop_column():

    global cursor
    print("\n\nDropping column...\n")

    ### query: ALTER TABLE table_name DROP column_name ###
    ### TASK: drop id column from studenti table ###
    cursor.execute("ALTER TABLE studenti DROP COLUMN id")

    print(f"\n\n  -  success!")


def add_column():

    global cursor
    print("\n\nAdding column...\n")

    ### query: ALTER TABLE table_name ADD COLUMN column_name TYPE ###
    ### TASK: add id column to studenti table with type: int, primary key and auto increment as the first column inside the table ###
    cursor.execute("ALTER TABLE studenti ADD COLUMN id INT PRIMARY KEY AUTO_INCREMENT FIRST")
    # cursor.execute("ALTER TABLE studenti ADD COLUMN id INT PRIMARY KEY AUTO_INCREMENT AFTER prenume")

    print(f"\n\n  -  success!")


def insert_into_table():

    global cursor
    global db_connection
    print("\n\nInserting into table...\n")

    #######################################################################
    ### single line ###

    ### query: INSERT INTO table name (column1, column2, ...) VALUES (val1, val2, ...) ###
    ## use %s in VALUES to give dinamic values using a variable ###
    query_studenti = "INSERT INTO studenti (nume, prenume, email, telefon, data_nasterii) VALUES (%s, %s, %s, %s, %s)"
    query_note = "INSERT INTO note_studenti (student_id, nota, materie) VALUES (%s, %s, %s)"

    ### storing values in a variable -> TUPPLE ###
    values_studenti_single_line = ("solo", "bogdan", "solo_bogdan@gmail.com", "0755777555", datetime(1992, 1, 7))
    values_note_single_line = ("1", 8.5, "limba_matematica")

    ## executing the query with values
    cursor.execute(query_studenti, values_studenti_single_line)
    
    ## print how many rows were added
    print(cursor.rowcount, "records inserted into studenti table")

    cursor.execute(query_note, values_note_single_line)
    print(cursor.rowcount, "records inserted into note_studenti table")

    ### save changes to our database ###
    db_connection.commit()
    #######################################################################


    #######################################################################
    ### multi lines ###

    values_studenti_multi_line = [
        ("stan", "alina", "stan_alina@gmail.com", "0755333111", datetime(1994, 5, 10)),         #2
        ("popescu", "ionut", "popescu_ionut@gmail.com", "0755111222", datetime(1992, 7, 13)),   #3
        ("stropinel", "vasile", "stropi@gmail.com", "0755111333", datetime(1998, 8, 23)),       #4
        ("mfede", "leusteniu", "mfede@gmail.com", "0755111444", datetime(2002, 12, 22)),        #5
    ]

    values_note_multi_line = [
        (2, 10, "limba_matematica"),
        (3, 5.5, "limba_matematica"),
        (4, 3.5, "limba_matematica"),
        (5, 7.7, "limba_matematica"),
    ]

    ### when adding multiple lines use cursor.executemany(query, values) ###
    cursor.executemany(query_studenti, values_studenti_multi_line)
    print(cursor.rowcount, "records inserted into studenti table")

    cursor.executemany(query_note, values_note_multi_line)
    print(cursor.rowcount, "records inserted into note_studenti table")

    ### save changes to our database ###
    db_connection.commit()
    #######################################################################

    print(f"\n\n  -  success!")


def select_table():

    global cursor
    print("\n\nSelecting table...\n")

    ### SELECT * FROM table name ###
    query_studenti = "SELECT * FROM studenti"
    query_note = "SELECT * FROM note_studenti"

    cursor.execute(query_studenti)
    studenti_records = cursor.fetchall()

    cursor.execute(query_note)
    note_studenti_records = cursor.fetchall()

    print("\n\n--------------------------------")
    print("Studenti:\n")
    for record in studenti_records:
        print(record)
    print("--------------------------------\n\n")


    print("\n\n--------------------------------")
    print("Note:\n")
    for record in note_studenti_records:
        print(record)
    print("--------------------------------\n\n")

    print(f"\n\n  -  success!")


def delete_table():

    global cursor
    global db_connection
    print("\n\nDeleting table...\n")

    ### DELETE FROM table_name ###
    ### DELETE FROM table_name WHERE condition ###

    query_studenti = "DELETE FROM studenti"
    query_note_studenti = "DELETE FROM note_studenti where nota < 5"

    cursor.execute(query_studenti)
    cursor.execute(query_note_studenti)

    db_connection.commit()

    print(f"\n\n  -  success!")


def select_table_specific_columns():

    global cursor
    print("\n\nSelecting table with specific columns...\n")

    query = "SELECT nume from studenti"
    cursor.execute(query)
    
    # names = cursor.fetchone()
    # print(names)

    names = cursor.fetchall()
    print("\n\n--------------------------------")
    print("Names:\n")
    for name in names:
        print(name)
    print("--------------------------------\n\n")

    print(f"\n\n  -  success!")


def select_where_condition():

    global cursor
    print("\n\nSelecting table where condition...\n")

    ### SELECT * FROM table_name WHERE condition ###

    ###########################################################
    ### option 1 ### select students where id = 5 ###
    ### option 2 ### select students ordered by nume ###
    ### option 3 ### select students order by data nasterii from oldest to youngest ###
    ### option 4 ### select 1st student (nume, nota, materie) with the highest grade in limba matematica ###
    ### option 5 ### select 1st student with the highest grade in limba matematica ###
    ###########################################################

    option = make_a_choice()

    if option == '1':
        query = "SELECT * FROM studenti WHERE id = 5"

    elif option == '2':
        query = "SELECT * FROM studenti ORDER BY nume"

    elif option == '3':
        query = "SELECT * FROM studenti ORDER BY data_nasterii"

    elif option == '4':
        query = """
                SELECT s.nume as castigatorul, ns.nota, ns.materie
                FROM note_studenti ns 
                JOIN studenti s ON s.id = ns.student_id
                WHERE ns.materie = 'limba_matematica'
                ORDER BY ns.nota DESC
                LIMIT 1
            """

    elif option == '5':
        query = """
                SELECT s.nume as castigatorul, ns.nota, ns.materie
                FROM note_studenti ns 
                JOIN studenti s ON s.id = ns.student_id
                WHERE ns.materie = 'limba_matematica'
                ORDER BY ns.nota DESC
            """

    else:
        print("Selection unknown!")
        return

    cursor.execute(query)
    if option == '5':
        records = cursor.fetchone()
        print("\n\n--------------------------------")
        print("My search:\n")
        print(records)
        print("--------------------------------\n\n")

    else:
        records = cursor.fetchall()

        print("\n\n--------------------------------")
        print("My search:\n")
        for record in records:
            print(record)
        print("--------------------------------\n\n")


    print(f"\n\n  -  success!")


def update_table():

    global cursor
    global db_connection
    print("\n\nUpdating table where condition...\n")
    
    ### query: UPDATE table_name SET col1 = val1, col2 = val2, ... WHERE condition ###
    ### TASK: Update nota lui Stan la limba matematica cu 2 ###
    query = "UPDATE note_studenti SET nota = 2 WHERE student_id = 2 and materie = 'limba_matematica'"

    cursor.execute(query)
    db_connection.commit()

    print(f"\n\n  -  success!")


def exercitiu():

    global cursor
    print("\n\nExercitiu...\n")


    ######################################################################
    ### TASK ###
    ### creating tables called 'studenti', 'profesori' and 'note_studenti' inside 'solo_academy' database ###
    ### tables: studenti, profesori, note_studenti ###
    ### create constraints for FOREIGN KEY student_id and profesor_id from note_studenti table ###
    ######################################################################
    
    ######################################################################
    ### HINT ### COLUMNS ###
    ### studenti columns: id, nume, prenume, email, telefon, data_nasterii ###
    ### profesori columns: id, nume, prenume, an_acreditare, materie_predata ###
    ### note_studenti columns: id, student_id, profesor_id, nota, materie ###
    ######################################################################

    ######################################################################
    ### table studenti ###

    create_table_studenti = """
    CREATE TABLE IF NOT EXISTS studenti (
      id INT AUTO_INCREMENT PRIMARY KEY,
      nume VARCHAR(100) NOT NULL,
      prenume VARCHAR(100) NOT NULL,
      email VARCHAR(100) UNIQUE,
      telefon VARCHAR(100),
      data_nasterii DATE);"""

    cursor.execute(create_table_studenti)
    ######################################################################


    ######################################################################
    ### table profesori ###

    create_table_profesori = """
    CREATE TABLE IF NOT EXISTS profesori (
      id INT AUTO_INCREMENT PRIMARY KEY,
      nume VARCHAR(255) NOT NULL,
      prenume VARCHAR(255) NOT NULL,
      an_acreditare INT,
      materie_predata VARCHAR(255) );"""

    cursor.execute(create_table_profesori)
    ######################################################################


    ######################################################################
    ### table note_studenti ###

    create_table_note_studenti = """
    CREATE TABLE IF NOT EXISTS note_studenti (
      id INT AUTO_INCREMENT PRIMARY KEY,
      student_id INT,
      profesor_id INT,
      nota DECIMAL(4,2),
      materie VARCHAR(255) NOT NULL,
      CONSTRAINT studentul_caruia_apartine_nota FOREIGN KEY (student_id) REFERENCES studenti(id),
      CONSTRAINT profesor_la_clasa FOREIGN KEY (profesor_id) REFERENCES profesori(id)
      );"""

    cursor.execute(create_table_note_studenti)
    ######################################################################

    print(f"\n\n  -  success!")


def main():

    global cursor
    global db_connection
    
    connect_to_database()
    create_database()

    while True:

        show_menu()

        choice = input()

        if choice == '0':
            db_connection.close()
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
            drop_column()

        elif choice == '7':
            add_column()

        elif choice == '8':
            insert_into_table()

        elif choice == '9':
            select_table()

        elif choice == '10':
            select_table_specific_columns()

        elif choice == '11':
            delete_table()

        elif choice == '12':
            update_table()

        elif choice == '13':
            select_where_condition()

        elif choice == '14':
            exercitiu()

        else:
            print("Selection unknown!")

        input()

if __name__ == '__main__':
    main()