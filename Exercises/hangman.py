# Notes: 
# Note 0: The , is being used at the end of the print statement (lines 36, 39) so that we don't skip to the newline. Make sure you don't use (); let the kids know about this since they've been using () [since they're using python2 () aren't needed]
# Note 1: Remind the kids that you can't concatenate an integer to a string since they're different types (line 66). Show them how to convert an integer to a string so that they can concatenate the int [str(int_variable)]
# Note 2: If you get errors running this script then you're machine's path for python probably points to python3; use python2 hangman.py in that case

# Ask for the user's name 
name = raw_input("What is your name? ")

print("Hello, " + name + "! It's time to play hangman!")

print("Start guessing...")

# Set the secret word 
# Can show them that we can set a list of words and randomly pick one but that might be for a later session
word = "secret"

# String used to keep track of all the guesses the user has made so far 
# Initially start off with an empty string since the user hasn't made any guesses yet; we'll add the guesses later in the loop
guesses = ''

# Number of turns the user can make in a game
turns = 10

# Keep looping until the number of turns remaining is above 0
while turns > 0:         

    # Keep a flag to keep track of whether or not every letter has been guessed 
    # Start with True and if we find a character that hasn't been guessed then we'll switch the flag to False
    word_guessed = True

    # Go through every character in the word  
    for character in word:      
    # Check if the character has been guessed by the user, i.e., is it in the guesses string
        if character in guesses:    
        # If the character has been guessed then print it out *[Note 0]
            print character,    
        else:
            # The character hasn't been guessed yet so we'll put a dash instead *[Note 0]
            print "_",  
            # Since there is a character that hasn't been guessed yet we'll set the flag (word_guessed) to False
            word_guessed = False

    # For formatting; to get to new line
    print

    # Check if the word has been guessed; if it has then we exit the loop
    if (word_guessed == True):
        # Word has been guessed, congratulate the user
        print("Good job! You guessed the word!") 
        # Break out of the loop 
        break

    # Ask the user for their guess 
    guess = raw_input("Guess a character : ") 

    # Add the character guessed to the string keeping track of all the guesses the user has made 
    guesses += guess                    

    # Check if the user's guess is in the word; if it isn't then we decrement the number of turns the user has left
    if guess not in word:  
    # Decrement the number of turns 
        turns = turns - 1
    # Let the user know their guess was wrong
        print("Wrong guess")    
    # Let the user know how many turns they have left *[Note 1]
        print("You have " + str(turns) + " left")

    # Check whether the user has run out of turns and let them know if they are 
        if(turns == 0):
            print("Sorry, you're out of turns. Better luck next time!")