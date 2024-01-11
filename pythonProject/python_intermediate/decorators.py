### Decorators ### https://www.youtube.com/watch?v=BE-L7xu8pO4 ###
"""
Decorators in Python are based primarily on two assumptions:
    a. a function may take another function as an argument
    b. you can create a function inside another function
"""

import datetime

# my_date = datetime.datetime.now()
#
# print(my_date)
# print(my_date.hour)
# print(my_date.minute)

USER = input("insert username:")


def disable_at_night(func):
    def wrapper():
        if 9 <= datetime.datetime.now().hour <= 22:
            print("A intrat decoratorul!")
            func()

    return wrapper


def run_only_between(from_=7, to_=22):
    def decorator(func):
        def wrapper():
            if from_ <= datetime.datetime.now().hour <= to_:
                func()

        return wrapper

    return decorator


def run_only_for_users(func):
    def wrapper():

        if USER in ["solo", "bogdan", "bobonete"]:
            func()
        else:
            print("You don`t have privileges for running fac ce vreau!")

    return wrapper


# @disable_at_night
@run_only_between(12, 15)
def say_something():
    print("Hello World!")
    print("How are you?\n\n")


# @disable_at_night
@run_only_for_users
@run_only_between(13, 22)
def say_something_else():
    print("Fac ce vreau!\n\n")

#
# STUDENT = 'solo'
#
# def test():
#     global STUDENT
#
#     STUDENT = 'vasile'
#     print(STUDENT)


# my_current_day_name = datetime.datetime.now().strftime("%A") ## Tuesday
# my_current_day_no = datetime.datetime.now().day     ### 11 if date is 11 march 2023
# print(f"current_day: {my_current_day_name}")
# print(f"current_day: {my_current_day_no}")


def main():
    # global STUDENT
    #
    # test()
    # print(STUDENT)

    print("\n")
    print("START!")
    print("\n")

    say_something()
    # say_something_else()


if __name__ == "__main__":
    main()