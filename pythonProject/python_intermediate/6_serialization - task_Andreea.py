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
import re

# Exercitiul 1. Pickle

def pickle_ser():
    city = {"Tokyo": "38000000",
            "Seul": "26000000",
            "Shanghai": "25000000",
            "Karachi": "24000000",
            "Guangzhou": "24000000",
            "Delhi": "22000000",
            "Mexico City": "22000000",
            "Lagos": "21000000",
            "Beijing": "21100000",
            "Sao Paulo": "20900000"
            }

    with open('C:/Users/andreea/Desktop/Python/Python Intermediate/data.pickle', 'wb') as my_file:
        pickle.dump(city, my_file)


def pickle_deser():

    with open('C:/Users/andreea/Desktop/Python/Python Intermediate/data.pickle', 'rb') as my_file:
        data = pickle.load(my_file)

    print("\n\n")
    for key in data:
        print(f"{key}: {data[key]}")
    print("\n\n")



# Exercitiul 2. CSV

def write_csv():
    stud = {"Andreea": {"grade": 9.5,
                        "school": "UBB",
                        "profile": "Statistica"
                        },
            "Cristian": {"grade": 8.67,
                         "school": "ASE",
                         "profile": "ECTS"
                         },
            "Vlad": {"grade": 9.95,
                     "school": "Nicolae Balcescu",
                     "profile": "Istorie"
                     },
            "Amalia": {"grade": 7.83,
                       "school": "Petru Rares",
                       "profile": "Bio-chimie"
                       },
            "Ramona": {"grade": 8.75,
                       "school": "UPET",
                       "profile": "Management"
                       },
            "Andrei": {"grade": 6.65,
                       "school": "Ecaterina Teodoroiu",
                       "profile": "Mate-info"
                       },
            "Alexandru": {"grade": 10,
                          "school": "UPET",
                          "profile": "Inginerie"
                          },
            "Carina": {"grade": 8,
                       "school": "Mihai Viteazu",
                       "profile": "Filologie"
                       },
            "Emilia": {"grade": 4,
                       "school": "Stefan Cel Mare",
                       "profile": "Economie"
                       },
            "Sebastian": {"grade": 9,
                          "school": "Matei Corvin",
                          "profile": "Psihologie"
                          }
            }

    with open("C:/Users/andreea/Desktop/Python/Python Intermediate/students.csv", mode="w", newline='') as out_file:

        writer = csv.writer(out_file)
        writer.writerow(["Name", "Grade", "School", "Profile"])

        for key in stud:
            #print(f"\n{key}")
            writer.writerow([key, stud[key]["grade"], stud[key]["school"], stud[key]["profile"]])
            # print([key, stud[key]["grade"], stud[key]["school"], stud[key]["profile"]])

def read_csv():
    with open("students.csv") as my_file:
        reader = csv.DictReader(my_file)
        studenti = {}

        for row in reader:
            name = row["Name"]
            grade = row["Grade"]
            school = row["School"]
            profile = row["Profile"]

            studenti[name] = dict()
            studenti[name]['grade'] = float(grade)
            studenti[name]['school'] = school
            studenti[name]['profile'] = profile

    # print(studenti)
    for key in studenti:
        print(f"\n\n{key}")
        for element in studenti[key]:
            if key[0] == "S":
                # print(type(studenti[key]['grade']))
                studenti[key]['grade'] += 0.5

            print(f"    {element}: {studenti[key][element]}")

def main():

    pickle_ser()
    pickle_deser()
    write_csv()
    read_csv()

if __name__ == "__main__":
                main()



