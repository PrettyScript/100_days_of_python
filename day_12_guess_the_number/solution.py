from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#TODO Function to check user's guess against the actual number.
def check_answer(guess, answer):
    if guess > answer:
        print("Too high.")
    elif guess < answer:
        print("Too low.")
    else:
        print(f"You got it! The answer was {answer}.")

#TODO Make a function to set difficulty.
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

#TODO Choosing a random number between 1 and 100.
print('''Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.''')
answer = randint(1, 100)
print(f"Pssst, the correct answer is {answer}")

turns = set_difficulty()
print(f"You have {turns} attempts remaining to guess the number.") 

#TODO Let the user guess the number.
guess = int(input("Make a guess: "))

check_answer(guess, answer)

#TODO Track the number of turns and reduce by 1 if they get it wrong.
#TODO Repeat the guessing functionality if they get it wrong.

