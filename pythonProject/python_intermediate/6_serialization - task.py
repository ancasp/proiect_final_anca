### Serialization Task ###

###################
# 1. Pickle:
# 	a. create a dictionary with city: population (10 cities)
# 	b. write data in a file using pickle
# 	c. read data from file using pickle and print it

# import pickle
#
# city_population = {
#     "Bucuresti": 1000000,
#     "Timisoara": 500000,
#     "Cluj": 400000,
#     "Arad": 300000,
#     "Ploiesti": 200000,
#     "Suceava": 100000,
#     "Slatina": 50000,
#     "Craiova": 10000,
#     "Constanta": 20000,
#     "Deva": 5000}
#
# with open("city_population.pkl", "wb") as my_file:
#     pickle.dump(city_population, my_file)
#
# with open("city_population.pkl", "rb") as my_file:
#     city_population = pickle.load(my_file)
#     print("\n\n")
#     for key in city_population:
#         print(f"{key}: {city_population[key]}")
#     print("\n\n")


# 2. CSV
# 	a. create a dictionary with 10 students.
# 	student_name: {grade: "8.6",
# 	school: "Gh. Lazar",
# 	profile:"mate-info"}
# 	b. write data inside a csv file (Name | School | Profile
# 	| Grade)
# 	c. read data from csv file and lower the grade with 0.5
# 	for students that their name starts with letter "S"
# 	d. print data

import csv

student_data = {
    "Ana": {"grade": "8.6",
              "school": "Gh. Lazar",
              "profile": "mate-info"},
    "Andrei": {"grade": "9.2",
            "school": "N. Grigorescu",
            "profile": "mate-info"},
    "David": {"grade": "7.8",
            "school": "Ion Creanga",
            "profile": "economie"},
    "Stefan": {"grade": "9.5",
              "school": "M. Eminescu",
              "profile": "filologie"},
    "Anca": {"grade": "9.0",
             "school": "Gh. Lazar",
             "profile": "economie"},
    "Maria": {"grade": "7.2",
              "school": "C. Istrati",
              "profile": "filologie"},
    "Sara": {"grade": "8.1",
               "school": "M. Eminescu",
               "profile": "filologie"},
    "Mara": {"grade": "9.8",
              "school": "Gh. Lazar",
              "profile": "mate-info"},
    "Alin": {"grade": "7.5",
               "school": "C.Istrati",
               "profile": "filologie"},
    "Bianca": {"grade": "8.3",
              "school": "Gh. Lazar",
              "profile": "mate-info"}
}

with open("student_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "School", "Profile", "Grade"])
    for name, data in student_data.items():
        writer.writerow([name, data["school"], data["profile"], data["grade"]])

# read data from csv file and lower the grade with 0.5
# for students that their name starts with letter "S"

# updated_student_data = {}
# with open("student_data.csv", "r") as file:
#     csv_reader = csv.reader(file)
#     headers = next(csv_reader)
#     for row in csv_reader:
#         name = row[0]
#         grade = float(row[3])
#         if name.startswith("S"):
#             grade -= 0.5
#         updated_student_data[name] = {"school": row[1], "profile": row[2], "grade": grade}


# print("Updated Student Data:")
# for name, data in updated_student_data.items():
#     print(f"Name: {name}, School: {data['school']}, Profile: {data['profile']}, Grade: {data['grade']:.1f}")



# # # 3. JSON
# # # 	a. create a JSON with 10 students: {name:"solo", sex:"M", grade:"8.5"} and 10 cars: {id: 0, model: "Dacia", year: "2022", price: 17000}
# # # 	b. write all students in a json and all cars in a json
# # # 	c. write a json with students that are boys and a json with students that are girls and a json with top-students (grade >= 9.5)
# # # 	d. write a json with luxury-cars (price >= 70000)
# # ###################
# #
# # import json
# #
# # students = [
# #     {"name": "solo", "sex": "M", "grade": 8.5},
# #     {"name": "ana", "sex": "F", "grade": 9.2},
# #     {"name": "andrei", "sex": "M", "grade": 7.8},
# #     {"name": "alex", "sex": "M", "grade": 9.8},
# #     {"name": "maria", "sex": "F", "grade": 8.8},
# #     {"name": "adrian", "sex": "M", "grade": 9.6},
# #     {"name": "bogdan", "sex": "M", "grade": 8.1},
# #     {"name": "ioana", "sex": "F", "grade": 9.2},
# #     {"name": "catalina", "sex": "F", "grade": 8.9},
# #     {"name": "mihai", "sex": "M", "grade": 8.7}
# # ]
# #
# # cars = [
# #     {"id": 0, "model": "Dacia", "year": "2022", "price": 17000},
# #     {"id": 1, "model": "Suzuki", "year": "2023", "price": 55000},
# #     {"id": 2, "model": "Mercedes", "year": "2019", "price": 45000},
# #     {"id": 3, "model": "BMW", "year": "2018", "price": 42000},
# #     {"id": 4, "model": "Toyota", "year": "2022", "price": 56000},
# #     {"id": 5, "model": "Dodge", "year": "2015", "price": 95000},
# #     {"id": 6, "model": "Audi", "year": "2020", "price": 70000},
# #     {"id": 7, "model": "Peugeot", "year": "2019", "price": 35000},
# #     {"id": 8, "model": "Lamborghini", "year": "2018", "price": 200000},
# #     {"id": 9, "model": "Ford", "year": "2023", "price": 79000}
# # ]
# #
# # with open("students.json", "w") as students_file:
# #     json.dump(students, students_file, indent=4)
# #
# #
# # with open("cars.json", "w") as cars_file:
# #     json.dump(cars, cars_file, indent=4)
# #
# #
# # boys = [student for student in students if student["sex"] == "M"]
# # girls = [student for student in students if student["sex"] == "F"]
# # top_students = [student for student in students if student["grade"] >= 9.5]
# #
# # with open("boys.json", "w") as boys_file:
# #     json.dump(boys, boys_file, indent=4)
# #
# # with open("girls.json", "w") as girls_file:
# #     json.dump(girls, girls_file, indent=4)
# #
# # with open("top_students.json", "w") as top_students_file:
# #     json.dump(top_students, top_students_file, indent=4)
# #
# #
# # luxury_cars = [car for car in cars if car["price"] >= 70000]
# #
# # with open("luxury_cars.json", "w") as luxury_cars_file:
# #     json.dump(luxury_cars, luxury_cars_file, indent=4)
