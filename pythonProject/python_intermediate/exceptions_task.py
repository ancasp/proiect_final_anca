### Exception Tasks ###

###################
"""1. Check voter eligibility
	a. input a name and an age from keyboard
	b. check if voter has minimum 18years and print if he has the right to vote or raise an exception if not

2. Check salary range by position
	a. input a name, a department and salary from keyboard
	b. check if department is in departments_list = ["HR", "Sales", "Development", "Marketing", "Logistics"]
	c. check if the salary is in range("HR": 3000-7000, "Sales": 4500-9000, "Development": 6000-15000,
	"Marketing": 4000-9000, "Logistics": 2500-6500)
"""
###################


# Exercitiul 1.
class Exceptia_mea(Exception):
	pass

try:
	name = input("Numele tau este:")
	varsta = int(input("Care este varsta ta?:"))

	if varsta < 18:
		raise Exceptia_mea()
	else:
		print(f"{name}, votul tau poate face diferenta!")
except Exceptia_mea:
	print(f"Ne pare rau {name}, nu ai varsta necesara pentru a putea vota")

# Exercitiul 2

class Exceptia_mea(Exception):
	pass

try:
	name = input("Numele tau este:")
	department = input("In ce departament lucrezi?:")
	salary = int(input("Care este salariul tau lunar?:"))

	if department not in ["HR", "Sales", "Development", "Marketing", "Logistics"]:
		raise Exceptia_mea()
	else:
		print(f"Bine ai venit {name}, din departamentul {department}!")
	if department == "HR":
		if salary in range(3000, 7000):
			print(f"{name}, din departamentul {department}, salariul tau este in conformitate cu range-ul departamentului!")
		else:
			raise Exceptia_mea()
	if department == "Sales":
		if salary in range(4500, 9000):
			print(f"{name}, din departamentul {department}, salariul tau este in conformitate cu range-ul departamentului!")
		else:
			raise Exceptia_mea()
	if department == "Development":
		if salary in range(6000, 15000):
			print(f"{name}, din departamentul {department}, salariul tau este in conformitate cu range-ul departamentului!")
		else:
			raise Exceptia_mea()
	if department == "Marketing":
		if salary in range(4000, 9000):
			print(f"{name}, din departamentul {department}, salariul tau este in conformitate cu range-ul departamentului!")
		else:
			raise Exceptia_mea()
	if department == "Logistics":
		if salary in range(2500, 6500):
			print(f"{name}, din departamentul {department}, salariul tau este in conformitate cu range-ul departamentului!")
		else:
			raise Exceptia_mea()


except Exceptia_mea:
	print(f"{name}, nu lucrezi in unul dintre departamentele de interes sau salariul tau este inafara range-ului!")
