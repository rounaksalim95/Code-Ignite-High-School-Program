'''
Steps 1 through 4 are below:
'''

# Step 1
import random

randomValue = random.randint(0,2)

print(randomValue)

# Step 1 - Extended test
for i in range(10):
    randomValue = random.randint(0,2)
    print(randomValue),

print
print

# Step 2
totalLength = 10
# Make sure you have imported random!!

# Step 3
actions = ['Attack', 'Defend', 'Retreat']   # Your list of actions

# Prints out each of the different actions - note that lists start at 0
print actions[0]
print actions[1]
print actions[2]


# Step 4 - just the integers

# Create an upper limit of how big you want the list to be
totalActions = 100

# Initialize the list
action_List4 = []

# Fill the list
def create_List4():
    for i in range(totalActions):
        randomValue = random.randint(0,3)
        action_List4.append(randomValue)
    return action_List4

print(create_List4())

# Step 5
totalActions5 = 100
action_List5 = []

def create_List5():
    actions = ['Attack', 'Defend', 'Retreat']
    for i in range(totalActions5):
        randomValue = random.randint(0, 2)
        action_List5.append(actions[randomValue])

    return action_List5

print(create_List5())


'''
Below are actual solutions, in varying levels of completedness/different ways of solving the problem.
'''

# FULL VERSION BELOW, INCLUDES STEP 6
action_List_Final = []
def create_and_score_completed():
    actions = ['Attack', 'Defend', 'Retreat']
    for i in range(totalActions):
        randomValue = random.randint(0, 2)
        action_List_Final.append(actions[randomValue])

    # Step 6
    totalPoints = 0
    for i in range(totalActions):
        if action_List_Final[i] == 'Attack':
            totalPoints += 5
        if action_List_Final[i] == 'Defend':
            totalPoints += 3
        if action_List_Final[i] == 'Retreat':
            totalPoints += -2

    return totalPoints

print(create_and_score_completed())