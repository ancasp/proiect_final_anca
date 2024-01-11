### Decorators Task ###

###################
"""
	1. create a main function that calls the following functions:
	a. eat breakfast (everyday between 8-10)
	b. eat lunch (everyday between 13-15)
	c. eat dinner (everyday between 18-20)
	d. go to work (everyday between 9-11)
	e. clean apartment (every saturday)
	f. have fun (every sunday)
	g. pay bills (every month on 1st and 15th)
	h. create a global variable that we can manually enter the date that simulate datetime.now()


2. create a dictionary with the following categories:
	a.	create the same functions that we have at ex. 1 (above)
	b.	activity_feeling = {
			'breakfast': 'eating and feeling good!'
			'lunch': 'eating and feeling good!'
			'dinner': 'eating and feeling good!'
			'go to work': 'I feel like sleeping and do nothing all day BUT I NEED TO WORK!'
			'clean apartment': 'I wish I could afford a maid!'
			'have fun': 'This is the life I deserve!'
			'pay bills': 'Being poor sucks!'
		}

	c. print on the screen the message for each function when the function is called. USE a decorator for this.
"""

###################
import datetime
NOW = datetime.datetime(2023, 8, 1, 10)

# print(NOW.hour)
###def eat_breakfast():
	###print("I'm eating breakfast")
activity_feeling = {
			'breakfast': 'eating and feeling good!',
			'lunch': 'eating and feeling good!',
			'dinner': 'eating and feeling good!',
			'go to work': 'I feel like sleeping and do nothing all day BUT I NEED TO WORK!',
			'clean apartment': 'I wish I could afford a maid!',
			'have fun': 'This is the life I deserve!',
			'pay bills': 'Being poor sucks!'
		}

def breakfast(from_, to_):
	def decorator(func):
		def wrapper():
			global NOW
			ora_mic_dejun = NOW.hour
			if from_ <= ora_mic_dejun <= to_:
				func()

		return wrapper
	return decorator

@breakfast(8,10)
def mic_dejun():
	print("Micul dejun este cea mai importanta masa a zilei!")



def lunch(from_=13, to_=15):
	def decorator(func):
		def wrapper():
			global NOW
			ora_pranz = NOW.hour
			if from_ <= ora_pranz <= to_:
				func()

		return wrapper
	return decorator

@lunch()
def pranz():
	print("Pauza de masa binemeritata!")



def dinner(from_=18, to_=20):
	def decorator(func):
		def wrapper():
			global NOW
			ora_cina = NOW.hour
			if from_ <= ora_cina <= to_:
				func()

		return wrapper
	return decorator

@dinner()
def cina():
	print("Mananca ceva usor inainte de culcare!")



def go_to_work(from_=9, to_=11):
	def decorator(func):
		def wrapper():
			global NOW
			mergi_la_lucru = NOW.hour
			if 9 <= mergi_la_lucru <= 11:
				func()

		return wrapper
	return decorator

@go_to_work()
def munceste():
	print("Fa bani!")



def clean(from_=5, to_=6):
	def decorator(func):
		def wrapper():
			global NOW
			curata = NOW.weekday()
			if curata == from_ or curata == to_:
				func()

		return wrapper
	return decorator


@clean(5)
def curata():
	print("O casa ingrijita te face sa te simti mai bine!")


def have_fun():
	def decorator(func):
		def wrapper():
			global NOW
			distreaza_te = NOW.weekday()
			if distreaza_te == 6:
				func()
		return wrapper
	return decorator

@have_fun()
def distreaza_te():
	print("Muncim dar ne mai si distram!")

def pay_bills():
	def decorator(func):
		def wrapper():
			global NOW
			facturi = NOW.day
			if facturi == 1 or facturi == 15:
				func()
		return wrapper
	return decorator

@pay_bills()
def facturi():
	print("Si s-au dus cativa $$$ ... :(")


def main():
	mic_dejun()
	pranz()
	cina()
	munceste()
	curata()
	distreaza_te()
	facturi()

if __name__ == "__main__":
	main()


