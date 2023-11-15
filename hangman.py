# importing the time module
import time

# welcoming the user
name = input("What is your name? ")
# determine the number of turns
turns = int(input("How many turns do you want for a game? "))

print("Hello, " + name, "Time to play hangman!")

# wait for 1 second
time.sleep(1)

print("Start guessing...")
time.sleep(0.5)

# here we set the secret. You can select any word to play with.
word = ("greed")

# creates an variable with an empty value
guesses = ''


def hangman(turns, guesses):
    # Create a while loop
    while turns > 0:

        # make a counter that starts with zero
        failed = 0

        # for every character in secret_word
        for char in word:

            # see if the character is in the players guess
            if char in guesses:

                # print then out the character
                print(char, end=""),

            else:

                # if not found, print a dash
                print("_", end=""),

                # and increase the failed counter with one
                failed += 1

                # if failed is equal to zero

        # print You Won
        if failed == 0:
            print("You won")
            # exit the script
            break

        # ask the user go guess a character
        guess = input("\nGuess a character:")

        # set the players guess to guesses
        guesses += guess

        # if the guess is not found in the secret word
        if guess not in word:

            # turns counter decreases with 1 (now 9)
            turns -= 1

            # print wrong
            print("Wrong")

            # how many turns are left
            print("You have", + turns, 'more guesses')

            # if the turns are equal to zero
            if turns == 0:
                # print "You Lose"
                print("You Lose")


print(hangman(turns, guesses))
