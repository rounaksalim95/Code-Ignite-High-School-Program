# Think of a number from 1 to 100 and I'll guess your number 
# Usage : python number_guess.py

# Flag used to keep track of whether or not we've guessed the user's number (used to iterate using the while loop)
number_guessed = False
lower_bound = 1     # Lower bound for number that can be guessed
upper_bound = 101   # Upper bound for the number that can be guessed (101 so that we accomodate for 100 as a user guessed number; using our current logic if the user thinks of the number 100 then we'll be stuck on 99 as a guess)
guess = 50          # Initial guess 

print("Think of a number between 1 and 100 and I'll guess your number!")

# Keep looping until we've guessed the number 
while(not number_guessed):
    user_answer = raw_input("Is your number " + str(guess) + "? (y/n)")
    # If the user thought of this number then we're done, so set the flag accordingly 
    if (user_answer == "y"):
        number_guessed = True
    # If we didn't guess the number correctly then ask the user whether the number is lesser than or greater than our guess 
    else: 
        lesser_or_greater = raw_input("Is your number lesser than or greater than " + str(guess) + "? (l/g)")
        # If the number is lesser than our guess then set the upper bound to our guess since we know it's not larger than that number 
        # and set the guess as the number between the new upper and lower bound 
        if (lesser_or_greater == "l"):
            upper_bound = guess
            guess = (lower_bound + upper_bound) / 2
        else:
        # Same thing as above except this time we update the lower bound since the number is greater than our guess
            lower_bound = guess
            guess = (lower_bound + upper_bound) / 2


# If we're our of the loop then that means that we've guessed the user's number correctly! 
print("I've guessed your number! It's " + str(guess))