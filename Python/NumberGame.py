# Week 3 Activity - Program a number game
# Generate a random number between 1 - 10
# Prompt user for a number between 1 -10
# match?
# If match print "Congratulations"
# If no match print "too high" or "too low" and "try again"
# prompt for user to input number again

# Start the game
print("Shall we play a game?")

# Generate random number
import random
answer=random.randint(1,10)

# Functions for prompting the user for an answer
def user_guess_prompt():
    global user_guess
    user_guess = int(input("I have chosen a number between 1 and 10. What is your guess: "))

# Functions for checking user_guess 
def incorrect_answer():
    if answer > user_guess:
        print("Your guess is too low human, try again.")
    elif answer < user_guess:
        print("Your guess is too high human, try again.")
    user_guess_prompt()

def correct_answer():
    if answer == user_guess:
        print("Congratulations human, you have beaten me. {0} was the correct answer.\nUntil next time...".format(answer))

# Start loop
# Call user_guess_prompt function
user_guess_prompt()
# Check answer
while answer != user_guess:
    incorrect_answer()
correct_answer()