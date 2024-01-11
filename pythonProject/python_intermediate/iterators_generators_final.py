### Iterators and Generators ###
"""
1. Normal
2. Iterators
3. Generators
4. Code profiling
"""
from math import sqrt
import timeit
import time

def normal_iteration():

    #############################
    ### list ###
    print("List:")
    a = [1, 2, 3, 4]
    for item in a:
        print(item)
    print("\n\n")
    #############################

    #############################
    ### string ###
    print("String:")
    a = "Alice has a cat"
    for item in a:
        print(item)
    print("\n\n")
    #############################

    #############################
    ### dictionary ###
    print("Dictionary:")
    a = {
        'name': "Adam", 
        'surname': "Smith"
    }
    for key in a:
        print(f"{key}: {a[key]}")
    print("\n\n")
    #############################


def is_prime(n):

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def get_n_primes(n):

    primes = [] # [2, 3, 5, 7, 11]
    i = 2

    while len(primes) < n:
        ### caut urmatorul numar prim ###
        if is_prime(i):
            primes.append(i)
            if len(primes) % 10000 == 0:
                print(f"i: {i} --- len(primes): {len(primes)}", end="\r")
                ### end - scrie peste acelasi rand de mai multe ori ###
        i += 1
    print("N primes generated!                     ")
    return primes


class PrimeIterator:

    def __init__(self, n):
        self.n = n
        self.generated_numbers = 0
        self.number = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        
        if self.generated_numbers >= self.n:
            raise StopIteration

        elif is_prime(self.number):
            self.generated_numbers += 1
            return self.number          ### return self.number to FOR

        return self.__next__()

def prime_generator(n):

    number = 2
    generated_numbers = 0

    while generated_numbers < n:

        if is_prime(number):
            yield number        ## se comporta ca un return ###
            generated_numbers += 1

        number += 1

def generate_normal_option():

    print("-" * 50)
    print("NORMAL OPTION:")
    prime_no_list = get_n_primes(100000)
    print(f"len(primes): {len(prime_no_list)}")
    
    ##############
    ### print ###
    i = 0
    for element in prime_no_list:
        print(f"{element}   ---   {i}", end="\r")
        # print(f"{number} -- {prime_no_list.index(element)}")
        i += 1
    ##############
    
    print("-" * 50)
    print("\n\n")

def generate_iterator_option():

    print("-" * 50)
    print("ITERATOR OPTION:")
    prime_no_iterator = PrimeIterator(100_000)
    
    ##############
    ### print ###
    i = 0
    for element in prime_no_iterator:
        print(f"{element}   ---   {i}", end="\r")
        i += 1
    ##############

    print("N primes generated!                     ")

    print("-" * 50)
    print("\n\n")


def generate_generator_option():

    print("-" * 50)
    print("GENERATOR OPTION:")
    prime_no_generator = prime_generator(100_000)
    i = 0
    for element in prime_no_generator:
        print(f"{element}   ---   {i}", end="\r")
        i += 1

    print("N primes generated!                     ")

    print("-" * 50)
    print("\n\n")


def main():

    normal_iteration()
    
    ###########################################################
    ### generate N prime numbers ### normal option ###
    start = time.time()
    generate_normal_option()
    end = time.time()
    print(f"Normal Time = {end-start}")
    ###########################################################


    ###########################################################
    ### generate N prime numbers ### iterator ###
    input("Please HIT ENTER to continue!")
    
    start = time.time()
    generate_iterator_option()
    end = time.time()
    print(f"Iterator Time = {end-start}")
    ###########################################################


    ###########################################################
    ### generate N prime numbers ### generator ###
    print("Please HIT ENTER to continue!")
    input()
    
    start = time.time()
    generate_generator_option()
    end = time.time()
    print(f"Generator Time = {end-start}")
    ###########################################################


    ###########################################################
    ### process time ### timeit ###
    print("Please HIT ENTER to continue!")
    input()
    
#     setup_mode = "from math import sqrt"
#     code_normal = """
# def get_n_primes(n):
#
#     primes = []
#     i = 2
#
#     while len(primes) < n:
#
#         if is_prime(i):
#             primes.append(i)
#         i += 1
#     """
#
#     code_iterator = """
# class PrimeIterator:
#
#     def __init__(self, n):
#         self.n = n
#         self.generated_numbers = 0
#         self.number = 1
#
#
#     def __iter__(self):
#
#         return self
#
#
#     def __next__(self):
#
#         self.number += 1
#
#         if self.generated_numbers >= self.n:
#             raise StopIteration
#
#         elif is_prime(self.number):
#             self.generated_numbers += 1
#             return self.number
#
#         return self.__next__()
#
#     """
#
#     code_generator = """
# def generate_generator_option(n):
#
#     number = 2
#     generated_numbers = 0
#
#     while generated_numbers < n:
#
#         if is_prime(number):
#             yield number
#             generated_numbers += 1
#
#         number += 1
#     """

    print(f"normal: {timeit.timeit(stmt=code_normal, setup=setup_mode, number = 100000)}")
    print(f"iterator: {timeit.timeit(stmt=code_iterator, setup=setup_mode, number= 100000)}")
    print(f"generator: {timeit.timeit(stmt=code_generator, setup=setup_mode, number = 100000)}")
    ###########################################################

if __name__ == "__main__":
    main()