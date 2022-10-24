import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]
computer_choice = random.randint(0, 2)
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

print(options[player_choice])
print("Computer chose:")
print(options[computer_choice])

player = options[player_choice]
computer = options[computer_choice]

if player == computer:
    print("It's a tie!")
elif player == rock and computer == scissors:
    print("You win")
elif player == paper and computer == rock:
    print("You win")
elif player == scissors and computer == paper:
    print("You win")
elif computer == rock and player == scissors:
    print("You lose")
elif computer == paper and player == rock:
    print("You lose")
elif computer == scissors and player == paper:
    print("You lose")
else:
    print("You lose")
