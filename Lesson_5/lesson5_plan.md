#	Review 2
-	Henry Cavill video
-	While loops
-	Lists
	-	append
	-	remove
	-	length
	-	accessing an element (indexing)
	-	emphasize type agnosticism
	-	looping through a list (foreach)
	-	strings are lists
-	Random
	-	Importing modules
	-	Generate a list with random and three strings
	-	Create a list of actions and iterate through list to find score

# Challenge Activity! Attack, Defend, Retreat
- This activity will use many different elements that you have learned
- Overview:
	- You're going to create a program that has basic point systems, incorporating random, lists, and if statements
	- We want to have a list that is randomly full of "Attack", "Defend", and "Retreat"
	- Attack is worth 5 points, Defend is worth 3 points, and Retreat is worth -2 points
	- At the end, we're going to add up all the points according to your list, and then see who has the highest score!

- Steps:
	- Step 1: Create something that will generate random numbers, 0 - 2
		- Hint: Python uses libraries, which means that you will have to import random, in order to get all those different random functions

	- Step 2: Create general parameters: the range (length of list), make sure that you have imported random
		- Hint: Where do you have to declare general parameters? How do you declare a variable in Python?

	- Step 3: Create an actions list. Assign the value 0 to Attack, 1 to Defend, and 2 to Retreat, according to the index of the actions list
		- Hint: use actions = [??, ??, ??], replacing the ?? with the right strings.
		- Test it: Try printing out each action, using the format actions[0], actions[1], and actions[2]. What do you get each time?

	- Step 4. Create a list that contains random integers 0 through 2, as is as long as the universal length value.

	- Step 5. Make a list that contains as actions, and has as many actions as are in the range parameter. Each time that we add a member to the list, it should be one of the three different Actions from the Actions list
		- Hint: use the actions[??] where actions is your random integer, and then append it to the list!
		- Test it: try printing out the first 10 values of the list

	- Step 6: Add up all the points you won, according to the scoring system above!
		- Hint: use a new variable that can "store" all of the points that your program is accumulating! Try testing it over the first five Actions, and see if the point values are correct!

	- Step 7: Congratulations! You have managed to tie together everything that we have learned so far!! Try modifying the program in a few ways:
		- Test out changing the range, try different point values, or try incorporating booleans. What's the most creative thing you can think of?
