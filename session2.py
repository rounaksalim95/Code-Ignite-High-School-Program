import math
import random

unsorted_list = [8,3,1,4,6,34,54,9,212,32,212]

def sort_list(unsorted_list):
	for i in range(len(unsorted_list)):
		min = unsorted_list[i]
		min_index = i
		for j in range(i, len(unsorted_list)): 
			if (unsorted_list[j] < min):
				min = unsorted_list[j]
				min_index = j
		temp_holder = unsorted_list[min_index]
		unsorted_list[min_index] = unsorted_list[i]
		unsorted_list[i] = temp_holder

sort_list(unsorted_list)

print(unsorted_list)

def solve_equation(a, b, c):
	roots = [] 
	positive_numerator = -b + math.sqrt(b**2 - 4*a*c)
	negative_numberator = -b - math.sqrt(b**2 - 4*a*c)
	denominator = 2*a
	roots.append(positive_numerator/denominator)
	roots.append(negative_numberator/denominator)
	return roots

print(solve_equation(1, 0, -1))

def create_actions():
	actions = ['Shoot', 'Dodge', 'Shot']
	user_actions = []
	for i in range(100):
		random_value = random.randint(0,2)
		if (random_value == 2 and random.randint(1,2) % 2 == 0):
			user_actions.append(actions[2])
		else:
			user_actions.append(actions[random_value])

	return user_actions

print(create_actions())