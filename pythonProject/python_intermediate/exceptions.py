### Exceptions ### https://www.youtube.com/watch?v=MImAiZIzzd4 ###
"""
1. AssertionError
2. AttibuteError
3. IOError
4. IndexError
5. ImportError
6. KeyError
7. NameError
8. ValueError
9. ZeroDivisionError
10. Custom Exception
"""

import math


class ExceptieSmechera(Exception):
    pass


#############################################################
### assertion error ###
try:
    x = "Hello World!"
    assert x == "Hello World", "Invalid Text"

### the error provided by user gets printed ###
except AssertionError as err:
    print(f"Assertion Error: |{err}|")
#############################################################


#############################################################
### attribute error ###
try:
    x = "ceva ceva"
    x.y = 2

except AttributeError as err:
    print(f"Attribute Error: |{err}|")
#############################################################


#############################################################
### io error ###
try:
    with open("demo.txt", "r") as file:
        my_file_content = file.read()
        print(my_file_content)

except IOError as err:
    print(f"IO Error: |{err}|")
#############################################################


#############################################################
### combine 2 exceptions with 1 except handling ###
try:
    ### index error ###
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(my_list[0])
    print(my_list[8])

    ### key error ###
    students = {'solo': 9, 'bobonete': 10, 'bordea': 7}
    print(students['solo'])
    print(students['bogdan'])

except (IndexError, KeyError) as err:
    print(f"Index or Key Error: |{err}|")
#############################################################


#############################################################
### import error ###
try:
    import solo

except ImportError as err:
    print(f"Import Error: |{err}|")
#############################################################


#############################################################
### name error ###
try:
    print(solo)

except NameError as err:
    print(f"Name Error: |{err}|")
#############################################################


#############################################################
### combine 1 try with more possible errors handling ###
try:
    ### value error ###
    print(math.sqrt(-100))

    ### zero division error ###
    a = 1
    b = 0
    print(a / b)

    ### name error ###
    print(solo)


except ValueError as err:
    print(f"Value Error: |{err}|")


except ZeroDivisionError as err:
    print(f"ZeroDivision Error: |{err}|")                    #??? de ce nu printeaza nimic aici


### except default ### trateaza orice tip de eroare ###
except Exception as err:
    print(f"This exception is not defined yet!: |{err}|")


finally:
    print("All exceptions have been handled!")
#############################################################


#############################################################
### custom exception ### solo ###
try:
    name = input("Insert a name:")

    if name == 'solo':
        raise ExceptieSmechera()
    else:
        print(f"{name} is a valid name!")

except ExceptieSmechera:
    print("Name is invalid!")
#############################################################








