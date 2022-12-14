from art import logo
print(logo)
import random

#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

print('''Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.''')
correct_number = random.randint(1,100)
# print(f"Pssst, the correct answer is {correct_number}")
easy_attempts = 10
hard_attempts = 5
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ") 


def guess_number(user_attempts):
    while user_attempts > 0:
        user_guess = int(input("Make a guess: "))
        if  user_guess != correct_number:
            user_attempts -= 1
            if user_attempts == 0:
                print("You've run out of guesses, you lose.")
            elif user_guess > correct_number:
                print("Too high.\nGuess again.")  
                print(f"You have {user_attempts} attempts remaining to guess the number.") 
            else:
                print("Too low.\nGuess again.")  
                print(f"You have {user_attempts} attempts remaining to guess the number.")
        else:
            print(f"You got it! The answer was {correct_number}.")
            break

if difficulty == 'easy':
    print(f"You have {easy_attempts} attempts remaining to guess the number.")
    guess_number(easy_attempts)
elif difficulty == 'hard':
    print(f"You have {hard_attempts} attempts remaining to guess the number.")
    guess_number(hard_attempts)

print(easy_attempts)
print(hard_attempts)