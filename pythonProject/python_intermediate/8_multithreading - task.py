### Multithreading ###

###################
# 1. Numbers divided by x
# 	a. create a function that counts how many numbers can be
# 	divided by 3 from 1 to n
# 	b. create a function that counts how many numbers are
# 	palindrom from 1 to n (121, 1234321)
# 	c. create a function that counts how many prime numbers
# 	are from 1 to n
# 	d. create THREADS to run all 3 functions at the same time
# 	e. create PROCESSES to run all 3 function at the same time


# 2. run each point(a, b, c) from ex.2(iterators and generators) using:
# 	a. threads
# 	b. processes
###################

import threading
import multiprocessing
from math import sqrt

# punct a
def nr_div3(n):
	j = 0

	for nr in range(1, n+1):
		if nr % 3 == 0:
			#print(nr)
			j += 1
	print(f"{j} nr divizibile cu 3")

#b. create a function that counts how many numbers are
# 	palindrom from 1 to n (121, 1234321)

def palindrom(n):

	j = 0
	palindrom = []
	for nr in range(1, n+1):
		if str(nr) == str(nr)[::-1]:
			j += 1
			palindrom.append(nr)
		#return j, palindrom
	print(f"Sunt {j} palindroame: {palindrom}")

# 	c. create a function that counts how many prime numbers
# 	are from 1 to n



def nr_prime(n):
	j = 0   # acesta este un contor

	for i in range(2, n+1):
		is_prime = True
		for nr in range(2, int(sqrt(i)) + 1):
			if i % nr == 0:
				is_prime = False
				break

		if is_prime:
			j += 1
			print(i)
	print(f"Sunt {j} numere prime!")

def main():
	# nr_div3(200)
	#palindrom()
	nr_prime(200)

### creating threads ###
# 	t1 = threading.Thread(target=nr_div3, args=(200,))
# 	palindrom_thread = threading.Thread(target=palindrom, args=(200,))

# 	t1.start()
# 	palindrom_thread.start()

# 	t1.join()
# 	palindrom_thread.join()
#
# ### creating processes ###
# 	p1 = multiprocessing.Process(target=nr_div3, args=(200,))
# 	palindrom_processing = multiprocessing.Process(target=palindrom, args=(200,))

# 	p1.start()
# 	palindrom_processing.start()

# 	p1.join()
# 	palindrom_processing.join()


if __name__ == "__main__":
		main()
