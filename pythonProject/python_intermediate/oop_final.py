### OOP ###
"""
1. Abstract Method
2. Inheritance + Multiple Inheritance --- MRO -> Method Resolution Order - it is a concept used in inheritance
3. Polymorphism
4. dataclass
5. deep and shallow copy
6. class and static methods
"""

from abc import abstractmethod
from dataclasses import dataclass
from copy import deepcopy
import inspect


class Figure:

    def __init__(self):
        ### atributes ###
        self.materie = "matematica"
        self.capitol = "figuri geometrice"
        self.utilitate = "ne ajuta sa invatam copiii despre figuri geometrice"

    ### method ###
    @abstractmethod
    def calculate_area(self):
        pass


class Dreptunghi(Figure):
    def __init__(self, lungime, latime):
        self.lungime = lungime
        self.latime = latime

    def calculate_area(self):
        return self.lungime * self.latime


class Triunghi(Figure):
    def __init__(self, baza, l_2, l_3, h):
        self.baza = baza
        self.l_2 = l_2
        self.l_3 = l_3
        self.h = h

    def calculate_area(self):
        return (self.baza * self.h)/2

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def show_finance(self):
        pass

    ### print method ###
    def __str__(self):
        return f"{self.name} is {self.age} years old"


### Because Student and Employee are involved in multiple inheritance ###
### we use specific class insted of super inside class Student and class Employee ###
class Employee(Person):
    def __init__(self, name, age, rate, num_of_hours):
        Person.__init__(self, name, age)  ### for Person class ###
        self.rate = rate
        self.num_of_hours = num_of_hours

    def show_finance(self):
        return self.rate * self.num_of_hours

    def __str__(self):
        return f"{self.name} is {self.age} years old and finance: {self.show_finance()}"


### Because WorkingStudent has multiple inheritance we use specific class instead of super() ###
class Student(Person):
    def __init__(self, name, age, scholarship):
        Person.__init__(self, name, age)
        self.scholarship = scholarship

    def show_finance(self):
        return self.scholarship

    """
    A class method is called for the whole class, not an instance, and takes the class as the first argument - we usually call it cls, and wrap the method with the @classmethod decorator.
    """

    @classmethod
    def create_from_string(cls, sentence):
        name, age, scholarship = sentence.split()
        age, scholarship = int(age), float(scholarship)
        if cls.is_name_correct(name):
            return cls(name, age, scholarship)

    """
	A static method does not operate on a specific class instance. It has no self parameter, but it is decorated with @staticmethod
    """

    @staticmethod
    def is_name_correct(name):
        if name[0].isupper() and name[1:].islower():
            return True
        return False

    ### __eq__ = equals, gt = greater(>), ge = greater or equal (>=) , lt(<), le(<=)
    def __eq__(self, obj):
        if isinstance(obj, Student) and (self.name, self.age, self.scholarship) == (obj.name, obj.age, obj.scholarship):
            return True
        return False

    def __ge__(self, obj):
        if isinstance(obj, Student) and self.age >= obj.age:
            return True

        return False


### Because class Somer is NOT involved in multiple inheritance we can use super() ###
class Somer(Person):
    def __init__(self, name, age, ajutor_somaj):
        super().__init__(name, age)
        self.ajutor_somaj = ajutor_somaj


class WorkingStudent(Employee, Student):
    def __init__(self, name, age, rate, num_of_hours, scholarship):
        Employee.__init__(self, name, age, rate, num_of_hours)
        Student.__init__(self, name, age, scholarship)

    def show_finance(self):
        return self.rate * self.num_of_hours + self.scholarship


@dataclass  ### automatically generates several common methods such as __init__, __eq__, __repr__ ###
class Sportiv(Person):
    name: str
    age: int
    sport_practicat: str

    def __str__(self):
        return f"{self.name} is practicing {self.sport_practicat}"

    def __eq__(self, obj):
        if self.name == obj.name:
            return True

        return False


class Sportiv(Person):

    def __init__(self, name, age, sport_practicat):
        super().__init__(name, age)
        self.sport_practicat = sport_practicat

    ### if you don`t have a __str__ method implemented in your class (or inherited classes) then __repr__ will be called ###
    ### https://www.digitalocean.com/community/tutorials/python-str-repr-functions ###
    def __repr__(self):
        return f"{self.name} is practicing {self.sport_practicat}"


### Polimorf function take as a parameter different objects and return something ###
### condition: objects that are given as parameter MUST have the methods and attributes used inside function ###
def check_finance(obj):
    print(f"{obj.name}: {obj.show_finance()}")


def main():
    obj = Somer("solo", 52, 600)
    obj_1 = Person("John", 54)  ### instantiere
    obj_2 = Employee("Jack", 36, 20, 160)
    obj_3 = Student("Agatha", 22, 1000)
    obj_4 = WorkingStudent("Monica", 24, 9.5, 70, 550)
    obj_5 = Student.create_from_string("Max 21 600")
    obj_6 = Student("Agatha", 22, 1000)
    obj_7 = Student.create_from_string("max 21 600")
    obj_8 = Sportiv("solo", 22, "handball")
    obj_9 = Sportiv("solo", 24, "handball")

    my_list = [1, obj_6, 3]
    shallow_copy = my_list
    deep_copy = deepcopy(my_list)

    my_list[1].name = "solo"

    print(f"shallow_copy: {shallow_copy[1]}")
    print(f"deep_copy: {deep_copy[1]}")

    print(f"Somer: {obj}")
    print(obj_1)
    print(obj_2)
    print(obj_3)
    print(obj_4)
    print(obj_5)
    print(obj_6)
    print(obj_7)
    print(obj_8)

    print("\n\n")

    check_finance(obj_3)
    check_finance(obj_4)

    print("\n\n")

    print(obj_3 == obj_6)
    print(obj_8 == obj_9)

    print("\n\n")

    ### get a list with all methods implemented inside class
    class_methods = inspect.getmembers(Sportiv, inspect.isfunction)
    for element in class_methods:
        print(element)

    print("\n\n")


if __name__ == "__main__":
    main()