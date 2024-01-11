### Multithreading ###
"""
1. MultiThreading
    Python allows different parts of your code to be executed simultaneously by using threads. 
    They are sequences of program statements that can be executed independently of the rest of the code. 
    We use the threading module for this.

2. GIL (Global Interpreter Lock)
    It only allows one thread to execute at a time. 
    The exceptions are I/O (input/output) operations, as they are not blocked by it. 

3. MultiProcessing
    If we want to parallelize calculations, we can use the multiprocessing module, which runs the code on subprocesses. 
    Each of them gets their own interpreter and memory space, so GIL won't be a problem. 
    Thanks to this, we can use many processors in the computer.
"""
import threading
import time
import multiprocessing

my_name_list = ['bobonete', 'popesco', 'mincu', 'toma', 'micutzu', 'bendeac', 'bucalae']
my_city_list = ['berlin', 'nairobi', 'helsinki', 'bogota', 'tokyo', 'rio', 'moscow']
my_store_list = ['zara', 'h&m', 'c&a', 'decathlon', 'sh', 'adidas', 'hummel']

def iterate_names(names):

    for name in names:
        print(f"watching {name}")
        time.sleep(2)


def iterate_cities(cities):

    for city in cities:
        print(f"visiting {city} and it is beautiful")
        time.sleep(3)


def iterate_stores(stores, stars):

    for store, star in zip (stores, stars):
        print(f"{store} has {star} stars")
        time.sleep(1)


def iterate_odd_numbers(n):
    
    print("Start searching for odd numbers:")
    j = 0
    for i in range(0, n+1):
        if i % 2 == 1:
            # print(i)
            j += 1
    print(f"{j} odd numbers were FOUND!")


def iterate_even_numbers(n):
    
    print("Start searching for even numbers:")
    j = 0
    for i in range(0, n+1):
        if i % 2 == 0:
            # print(i)
            j += 1

    print(f"{j} even numbers were FOUND!")


def main():

    global my_name_list
    global my_city_list
    global my_store_list

    stars = [1, 2, 3, 2, 5, 3, 2]

    ########################################################################################
    ### run one by one ### v1 ###
    iterate_names(my_name_list)
    print("\n\n")
    iterate_cities(my_city_list)
    print("\n\n")
    iterate_stores(my_store_list, stars)
    print("\n\n")
    ########################################################################################

    print("\n\nPress ENTER to continue!\n\n")
    input()

    ########################################################################################
    ### run by threads ### v1 ###

    ### creating threads ###
    t1 = threading.Thread(target=iterate_names, args=(my_name_list,))
    t2 = threading.Thread(target=iterate_cities, args=(my_city_list,))
    t3 = threading.Thread(target=iterate_stores, args=(my_store_list, stars))


    ### starting threads ###
    t1.start()
    t2.start()
    t3.start()

    ### joining threads ###
    t1.join()
    # t2.join()
    t3.join()
    ########################################################################################


    print("\n\nDONE!\n\n")

    print("\n\nPress ENTER to continue!\n\n")
    input()

    ########################################################################################
    ### run by threads ### v2 ###

    ### creating threads ###
    t4 = threading.Thread(target=iterate_odd_numbers, args=(200_000_000,))
    t5 = threading.Thread(target=iterate_even_numbers, args=(200_000_000,))

    ### starting threads ###
    t4.start()
    t5.start()

    ### joining threads ###
    t4.join()
    t5.join()
    ########################################################################################


    print("\n\nDONE!\n\n")

    print("\n\nPress ENTER to continue!\n\n")
    input()


    ########################################################################################
    ### run by process ### v2 ###

    ### creating processes ###
    p1 = multiprocessing.Process(target=iterate_odd_numbers, args=(200_000_000,))
    p2 = multiprocessing.Process(target=iterate_even_numbers, args=(200_000_000,))

    ### starting processes ###
    p1.start()
    p2.start()

    ### joining processes ###
    p1.join()
    p2.join()
    ########################################################################################


    print("\n\nDONE!\n\n")

    print("\n\nPress ENTER to continue!\n\n")
    input()

if __name__ == "__main__":
    main()