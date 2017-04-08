import random

number = 0
guesses = 0

# Generates a random number
def genNum():
    global number
    number = random.randint(1,100)

# Attempts a guess with number g
# Returns 0 if correct, 1 if too high, -1 if too low
def guess(g):
    print("You guessed %d." % g)
    if g == number:
        print("Correct!")
        print("You used %d guesses." % guesses)
        return 0
    if g < number:
        print ("Your guess is too low.")
        return -1
    if g > number:
        print ("Your guess is too high.")
        return 1

# Prompts user for input and runs guess
def prompt():
    num = int(input("Enter your guess > "))
    return guess(num)

# Manually play the game
def playGame():
    global guesses
    guesses += 1
    res = prompt()
    while (res != 0):
        guesses += 1
        res = prompt()

# Write an AI to play the game
def playAI():
    global guesses
    cur = -1
    # ------------------------------
    # vvv Add Variables Here vvv
    # ------------------------------



    # ------------------------------

    while (cur != 0):
        guesses += 1
        # ------------------------------
        # vvv Add Loop Code Here vvv
        # ------------------------------



        # ------------------------------

genNum()
print("I'm thinking of a secret number between 1 and 100 (inclusive). Try and guess it!")

# Uncomment this if manually playing game
playGame()

# Uncomment this if running AI
# playAI()
