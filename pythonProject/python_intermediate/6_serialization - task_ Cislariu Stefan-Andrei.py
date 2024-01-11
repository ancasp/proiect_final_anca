### Serialization Task ###

###################
"""
1. Pickle:
	a. create a dictionary with city: population (10 cities)
	b. write data in a file using pickle
	c. read data from file using pickle and print it

2. CSV
	a. create a dictionary with student_name: {grade: "8.6", school: "Gh. Lazar", profile:"mate-info"}
	b. write data inside a csv file (Name | School | Profile | Grade)
	c. read data from csv file and lower the grade with 0.5 for students that their name starts with letter "S"
	d. print data

3. JSON
	a. create a JSON with 10 students: {name:"solo", sex:"M", grade:"8.5"} and 10 cars: {id: 0, model: "Dacia", year: "2022", price: 17000}
	b. write all students in a json and all cars in a json
	c. write a json with students that are boys and a json with students that are girls and a json with top-students (grade >= 9.5)
	d. write a json with luxury-cars (price >= 70000)
"""
###################

import pickle
import csv
import json

#################EX_1#################
def ex_1():
    scriere_pickle(creare_dict())
    citire_pickle()

def creare_dict():
    orase_pop = {
        "Moscova": 12500000,
        "Istanbul": 15500000,
        "Londra": 8900000,
        "Paris": 2100000,
        "Madrid": 3300000,
        "Berlin": 3600000,
        "Roma": 2800000,
        "Atena": 3100000,
        "Varșovia": 1800000,
        "Praga": 1300000
    }
    for oras in orase_pop:
        print(f"Populația din {oras}: {orase_pop[oras]} loc.")
    return orase_pop

def scriere_pickle(orase_pop):
    with open('orase_pop.pickle', 'wb') as fisier:
        pickle.dump(orase_pop, fisier)

def citire_pickle():
    with open('orase_pop.pickle', 'rb') as my_file:
        orase_pop = pickle.load(my_file)

    print("\n\n")
    for oras in orase_pop:
        print(f"{oras}: {orase_pop[oras]}")
    print("\n\n")

#################EX_1#################


#################EX_2#################
def ex_2():
    elevi = {
        "Ion Popescu": {
            "School": "Liceul A",
            "Profile": "Științe",
            "Grade": 9.5
        },
        "Ana Maria": {
            "School": "Colegiul B",
            "Profile": "Arte",
            "Grade": 8.7
        },
        "Mihai Ionescu": {
            "School": "Liceul C",
            "Profile": "Matematică-Informatică",
            "Grade": 9.9
        },
        "Elena Vasilescu": {
            "School": "Colegiul D",
            "Profile": "Limbi Străine",
            "Grade": 8.0
        },
        "Andrei Georgescu": {
            "School": "Liceul E",
            "Profile": "Științe Sociale",
            "Grade": 9.2
        },
        "Larisa Munteanu": {
            "School": "Colegiul F",
            "Profile": "Arte",
            "Grade": 8.5
        },
        "Alexandru Popa": {
            "School": "Liceul G",
            "Profile": "Matematică-Informatică",
            "Grade": 9.7
        },
        "Diana Iacob": {
            "School": "Colegiul H",
            "Profile": "Limbi Străine",
            "Grade": 8.3
        },
        "Radu Andrei": {
            "School": "Liceul I",
            "Profile": "Științe",
            "Grade": 9.0
        },
        "Ioana Stan": {
            "School": "Colegiul J",
            "Profile": "Matematică-Informatică",
            "Grade": 8.8
        }
    }

    with open("students.csv", mode="w", newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(["Name", "School", "Profile", "Grade"])

        for elev in elevi:
            writer.writerow([elev, elevi[elev]['School'], elevi[elev]['Profile'], elevi[elev]['Grade']])

    ################
    with open("students.csv") as my_file:
        reader = csv.DictReader(my_file)
        data = {}

        for line in reader:
            name = line["Name"]
            school = line["School"]
            profile = line["Profile"]
            grade = line["Grade"]

            data[name] = dict()
            data[name]['School'] = school
            data[name]['Profile'] = profile
            data[name]['Grade'] = float(grade)-0.5 if ("S" in name) else float(grade)


        for elev in data:
            print(f"{elev}: {data[elev]}")
        print("\n\n")
#################EX_2#################

#################EX_3#################
def ex_3():
    read_json()
    separare_categorii()
    sortare_studenti()
    masini_lux()
    pass

def read_json():

    global doc_json

    with open("doc_json.json") as fisier:
        doc_json = json.load(fisier)

    for categorie in doc_json:

        print(f"\n{categorie.title()}")

        for cat in doc_json[categorie]:
            for key in cat:
                print(f"{key} - {cat[key]}")
            print(cat, end="\n\n")
    print("\n\n")

def separare_categorii():

    global doc_json

    for categorie in doc_json:

        text_file = f"{categorie}.json"
        with open(text_file, "w") as fisier:
            json.dump(doc_json[categorie], fisier, indent=2)

# c. write a json with students that are boys and a json with students that are girls and a json with top-students (grade >= 9.5)
def sortare_studenti():
    with open("studenti.json") as fisier:
        studenti = json.load(fisier)

    baieti = []
    fete = []
    std_top = []
    for student in studenti:
        if student['sex'] == 'M':
            baieti.append(student)
        elif student['sex'] == 'F':
            fete.append(student)
        else:
            raise TypeError

        if student['grade'] >= 9.5:
            std_top.append(student)
    # print(baieti, fete, std_top, sep="\n\n")

    fisiere=[baieti, fete, std_top]
    den = ['baieti', 'fete', 'std_top']
    i = 0
    for tip_sort in fisiere:
        text_file = f"{den[i]}.json"
        i += 1
        with open(text_file, "w") as fisier:
            json.dump(dict(zip(range(len(tip_sort)), tip_sort)), fisier, indent=2)

#	d. write a json with luxury-cars (price >= 70000)
def masini_lux():
    with open("masini.json") as fisier:
        masini = json.load(fisier)

    top_cars = []
    for masina in masini:
        if masina['price'] >= 70000:
            top_cars.append(masina)

        text_file = "masini_lux.json"
        with open(text_file, "w") as fisier:
            json.dump(dict(zip(range(len(top_cars)), top_cars)), fisier, indent=2)


doc_json = dict()

#################EX_3#################
def main():
    ex_1()
    ex_2()
    ex_3()

if __name__ == "__main__":
    main()
