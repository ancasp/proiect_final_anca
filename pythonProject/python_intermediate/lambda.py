### Lambda Expressions ### https://www.youtube.com/watch?v=KR22jigJLok ###
"""
The lambda expression is an anonymous function.
It has no name and is defined where it is used.
It does not use the def keyword.
"""

### lower, upper text and title text ###
lower_text = lambda x: x.lower()
upper_text = lambda x: x.upper()
title_text = lambda x: x.title()

print(lower_text("HEHEHE"))
print(upper_text("wow!"))
print(title_text("solomon ionut"))
print("\n\n")



### power^2 and equals ###
square_lambda = lambda x: x*x
equals_lambda = lambda x,y: x==y

print(square_lambda(4))
print(equals_lambda("abc", "bca"))
print(equals_lambda("abc", "abc"))
print("\n\n")


### map, reduce, filter ###
items = [1, 2, 3, 4, 5]

squared_temp = map(lambda x: x*x, items)
squared = list(map(lambda x: x*x, items))
odds_temp = filter(lambda x: x%2 == 1, items)
odds = list(filter(lambda x: x%2, items))

print(f"items:{items}")
print(f"squared_temp:{squared_temp}")
print(f"squared:{squared}")
print(f"odds_temp:{odds_temp}")
print(f"odds:{odds}")

from functools import reduce
items_sum = reduce(lambda x,y: x+y, items)
print(f"sum:{items_sum}")

print("\n\n")


### sorted, max, min ###
pairs = [(1, 10), (2, 9), (3, 8)]

sorted_pairs = sorted(pairs, key=lambda x: x[1])
sorted_pairs_0 = sorted(pairs, key=lambda x: x[0], reverse=True)
sorted_pairs_1 = sorted(pairs, key=lambda x: reduce(lambda z,y: z+y, x))
sorted_pairs_2 = sorted(pairs, key=lambda x: x[0] + x[1]) ### alternativa la _1 ###

																				#????? nu inteleg cum sorteaza
print(f"pairs: {pairs}")

print(f"sorted_pairs by [0] reversed: {sorted_pairs_0}")
print(f"sorted_pairs by [1]: {sorted_pairs}")
print(f"sorted_pairs by sum: {sorted_pairs_1}")
print("\n\n")


min_pairs = min(pairs)
min_pairs_1 = min(pairs, key=lambda x: x[1])

max_pairs_0 = max(pairs, key=lambda x: x[0])
max_pairs_1 = max(pairs, key=lambda x: x[1])

print(f"min_pairs: {min_pairs}")
print(f"min_pairs_1: {min_pairs_1}")

print(f"max_pairs_0: {max_pairs_0}")
print(f"max_pairs_1: {max_pairs_1}")
print("\n\n")

students = {
	'solo': 8.5,
	'bobonete': 10,
	'popesco': 7,
	'bordea': 9
}

list_of_sorted_keys = sorted(students)

pairs_sorted_by_keys_1 = sorted(students.items())
pairs_sorted_by_keys_2 = sorted(students.items(), key=lambda x: x[0])   #### ????? nu inteleg cum sorteaza
pairs_sorted_by_value = sorted(students.items(), key=lambda x: x[1])

dict_sorted_by_keys_1 = dict(sorted(students.items()))
dict_sorted_by_keys_2 = dict(sorted(students.items(), key=lambda x: x[0]))
dict_sorted_by_value = dict(pairs_sorted_by_value)

print(f"list_of_sorted_keys: {list_of_sorted_keys}")
print("\n")

print(f"pairs_sorted_by_keys_1: {pairs_sorted_by_keys_1}")
print(f"pairs_sorted_by_keys_2: {pairs_sorted_by_keys_2}")
print(f"pairs_sorted_by_value: {pairs_sorted_by_value}")
print("\n")

print(f"dict_sorted_by_keys_1: {dict_sorted_by_keys_1}")
print(f"dict_sorted_by_keys_2: {dict_sorted_by_keys_2}")
print(f"dict_sorted_by_value: {dict_sorted_by_value}")
print("\n\n")
