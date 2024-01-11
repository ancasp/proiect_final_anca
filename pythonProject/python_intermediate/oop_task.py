### OOP Task ###

###################
#1. create classes
# a. Person (name, surname, age, phone number), Employee(Person + id, salary, position, responsibilities),
# Intern(Person, salary, scolarship, menthor)

from abc import abstractmethod
class Person:
    def __init__(self, name, surname, age, phone_number):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone_number = phone_number
    @abstractmethod
    def show_finance(self):
        pass

    @abstractmethod
    def show_expenses(self):
        pass
class Employee(Person):
    def __init__(self, name, surname, age, phone_number, employee_id, salary, position, responsibilities):
        super().__init__(name, surname, age, phone_number)
        self.employee_id = employee_id
        self.salary = salary
        self.position = position
        self.responsibilities = responsibilities

    def show_finance(self):
        return

    @abstractmethod
    def show_expenses(self):
        return

    def increase_salary(self, amount):
        self.salary += amount
class Intern(Person):
    def __init__(self, name, surname, age, phone_number, salary, scholarship, mentor):
        super().__init__(name, surname, age, phone_number)
        self.salary = salary
        self.scholarship = scholarship
        self.mentor = mentor

    def show_finance(self):
        return self.salary +self.scholarship

    @abstractmethod
    def show_expenses(self):
        return self.salary +self.scholarship

    def __eq__(self, other):
        if isinstance(other, Intern):
            return (self.name, self.surname) == (other.name, other.surname)
        return False

    def increase_salary(self, amount):
            self.salary += amount

def increase_salary_for_all(people_list, amount):
    for person in people_list:
        person.increase_salary(amount)

employee_list = [
Employee("solo", "bogdan", 30, "07xxyyyzzz", 1, 5000, "HR", "Recruiting"),
Employee("bobonete", "mihai", 28, "07xxyyyzzz", 2, 7000, "Sales", "Selling"),
Employee("bordea", "catalin", 23, "07xxyyyzzz", 3, 8000, "Sales", "Selling"),
Employee("nae", "nicolae", 45, "07xxyyyzzz", 4, 9500, "Programmer", "Coding"),
Employee("bendeac", "mihai", 33, "07xxyyyzzz", 5, 7000, "Marketing", "Promoting"),
Employee("popesco", "cristi", 23, "07xxyyyzzz", 6, 5000, "HR", "Recruiting")
]

intern_list = [
Intern("mincu", "alexandru", 21, "07xxyyyzzz", 2000, 0, "solo"),
Intern("popovici", "maria", 22, "07xxyyyzzz", 2100, 500, "bobonete"),
Intern("bojoc", "costel", 23, "07xxyyyzzz", 2200, 700, "bobonete")
]

print("Employee List:")
for employee in employee_list:
    print(f"{employee.name}, {employee.surname} - Position: {employee.position}, Salary: {employee.salary}")

print("Intern List:")
for intern in intern_list:
    print(f"{intern.name} - Age: {intern.age}, Scholarship: {intern.scholarship}")

#b. sort employee list by salary and intern list by age

sorted_employee_list = sorted(employee_list, key=lambda employee: employee.salary)

sorted_intern_list = sorted(intern_list, key=lambda intern: intern.age)

print("Sorted Employee List:")
for employee in sorted_employee_list:
    print(f"{employee.name} - Position: {employee.position}, Salary: {employee.salary}")

print("Sorted Intern List:")
for intern in sorted_intern_list:
    print(f"{intern.name} - Age: {intern.age}, Scholarship: {intern.scholarship}")


# c. print all employees from sales department

print("Employees from Sales Department:")
for employee in employee_list:
    if employee.position == "Sales":
        print(f"{employee.name} {employee.surname} - Position: {employee.position}")

# d. delete intern "popovici maria" (implement __eq__ function)

target_intern = Intern("popovici", "maria", None, None, None, None, None)
intern_list = [intern for intern in intern_list if intern != target_intern]

print("Updated Intern List:")
for intern in intern_list:
    print(f"{intern.name} {intern.surname} - Age: {intern.age}, Scholarship: {intern.scholarship}")

#e. implement a polymorfic function that increase the salary by a specific amount. amount is given as a parameter.

increase_salary_for_all(employee_list, 1000)
increase_salary_for_all(intern_list, 500)

print("Updated Salary Information:")
for employee in employee_list:
    print(f"{employee.name} {employee.surname} - Position: {employee.position}, New Salary: {employee.salary}")

for intern in intern_list:
    print(f"{intern.name} {intern.surname} - Scholarship: {intern.scholarship}, New Salary: {intern.salary}")


#f. increase salary to bobonete, nae and popesco by 1000 and bojoc by 500. print salaries to see if they were increased.

def increase_salary_for_specific(people_list, names_to_increase, amount):
    for person in people_list:
        full_name = f"{person.name} {person.surname}"
        if full_name in names_to_increase:
            person.increase_salary(amount)
names_to_increase = ["bobonete mihai", "nae nicolae", "popesco cristi", "bojoc costel"]

increase_salary_for_specific(employee_list, names_to_increase, 1000)
increase_salary_for_specific(intern_list, names_to_increase, 500)

print("Updated Salary Information:")
for employee in employee_list:
    print(f"{employee.name} {employee.surname} - Position: {employee.position}, New Salary: {employee.salary}")

for intern in intern_list:
    print(f"{intern.name} {intern.surname} - Scholarship: {intern.scholarship}, New Salary: {intern.salary}")

#g. perform a shallow and deep copy for employee bendeac and intern mincu. change the salaries and see the results with print

import copy

bendeac = None
for employee in employee_list:
    if employee.name == "bendeac":
        bendeac = employee
        break

shallow_copied_bendeac = copy.copy(bendeac)
deep_copied_bendeac = copy.deepcopy(bendeac)

mincu = None
for intern in intern_list:
    if intern.name == "mincu":
        mincu = intern
        break

shallow_copied_mincu = copy.copy(mincu)
deep_copied_mincu = copy.deepcopy(mincu)

shallow_copied_bendeac.salary += 2000
deep_copied_bendeac.salary += 2000
shallow_copied_mincu.salary += 1000
deep_copied_mincu.salary += 1000

# Print original and modified salary information
print("Original Salary Information:")
print(f"Bendeac - Original Salary: {bendeac.salary}")
print(f"Mincu - Original Salary: {mincu.salary}")

print("\nShallow Copied Salary Information:")
print(f"Bendeac - Shallow Copied Salary: {shallow_copied_bendeac.salary}")
print(f"Mincu - Shallow Copied Salary: {shallow_copied_mincu.salary}")

print("\nDeep Copied Salary Information:")
print(f"Bendeac - Deep Copied Salary: {deep_copied_bendeac.salary}")
print(f"Mincu - Deep Copied Salary: {deep_copied_mincu.salary}")

#h. create an abstract methods inside Person called show_finance(), expenses() - 80% from salary and implement
# them inside Employee and Intern

"""
	i. create a class method inside Intern class to be able to create objects with this method
	j. create a static method inside Intern class to be able to check if Intern is valid (salary needs to be max. 2500 and needs to have a menthor)


2. Create a School database using classes
	a. classes: Student, Teacher
	b. functionalities:
		i.    create a Student (id, cnp, name, surname, age, address, class_no, profile)
		ii.   create a Teacher (id, cnp, name, surname, age, specialty_subject)
		iii.  Student should have a grade notebook and we should be able to give a mark to a student at a specific subject
		iv.   we should be able to assign a subject to a specific Student
		v.    we should be able to assign a class to a specific Teacher
		vi.   we should be able to see all the classes a Teacher is assigned to teach
		vii.  we should be able to see all the teachers that a Student has
		viii. we should be able to see the AVG(grade) for each subject for each Student and AVG(all_subjects)
		ix.   create a polymorfic function that calculates the Valedictorian for each class_no
		x.    create a polymorfic function that calculates the Valedictorian for the whole school
"""
