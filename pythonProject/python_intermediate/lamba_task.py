### Lambda Tasks ###

###################
"""
1. create a dictionary with 10 students: {"name": age}
   using lambda function:
	a. sort dictionary by name and print it
	b. sort dictionary by age and print it (descending)

2. Create a list of 10 words
	a. create a lambda function that filter all palindrom words and print it ("aba", "civic", 123454321)
	b. create a lambda function that applies .title() function for each word and print it
"""
###################

# Exercitiul 1.

studenti = {"Andreea" : 26,
			"Ionut" : 35,
			"Maria": 22,
			"Vlad": 16,
			"Daniel": 26,
			"Amalia": 18,
			"Ioana": 19,
			"Cecilia": 30,
			"Alexandru": 27,
			"Emanuel": 35
			}
sort_by_name = sorted(studenti.items(), key=lambda x: x[0])
print(sort_by_name)

sort_by_age = sorted(studenti.items(), key=lambda x: x[1], reverse=True)
print(sort_by_age)