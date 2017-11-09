todo_list = []	# List that holds entered items 
command = ""	# Holder for commands entered by the user


'''
Function that asks the user for the item they want to add to the list and 
then adds it to todo_list
'''
def add_item():
	item = input("What item do you want to add? ")
	todo_list.append(item)


'''
Function that asks the user for the item they want to remove from the list and 
then removes it from the todo_list
'''
def remove_item():
	item = input("What item do you want to remove? ")
	todo_list.remove(item)


'''
Function that displays the current todo_list
'''
def show_list():
	print("The following items are in your list: ")
	print(todo_list)


# Part of our program that continues looping to get input from the user 

# One way to do this:

# while(command != "exit"):
# 	command = input("Please enter your command (exit to exit): ")
# 	if (command == "add"):
# 		add_item()
# 	elif (command == "remove"):
# 		remove_item()
# 	elif (command == "show"):
# 		show_list()
# 	else:
# 		print("Couldn't recognize input, please try again")

# print("Bye bye")


# Another way to do this: 

while(True):
	command = input("Please enter your command (exit to exit): ")
	if (command == "exit"):
		break
	elif (command == "add"):
		add_item()
	elif (command == "remove"):
		remove_item()
	elif (command == "show"):
		show_list()
	else:
		print("Couldn't recognize input, please try again")

print("Bye bye")