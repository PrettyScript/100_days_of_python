#TODO Create a function that will loop through the game data and provide the two comparisons
from game_data import data
from random import choice
from art import logo, vs
  

def compare(): 
    correct = True
    # Score will increase each time user gets a true and stop once user recieves a false
    score = 0
    choice_a = choice(data)
    choice_b = choice(data)
    while correct:
        #TODO print logos for game            
        print(logo)
        print(f"Compare A: {choice_a['name']}, a {choice_a['description']} from {choice_a['country']}")   
        print(vs) 
        print(f"Against B: {choice_b['name']}, a {choice_b['description']} from {choice_b['country']}")        
        response = input("Who has more followers? Type 'A' or 'B': ").upper()  

        if response == 'A':
            print(f"response == 'A', response: {response}")
            if choice_a['follower_count'] > choice_b['follower_count']:
                score += 1
                choice_a = choice_b
                choice_b = choice(data)             
                print(f"You're right! Current score: {score}")
            else: 
                correct = False
                print(f"Sorry, that's wrong. Final score: {score}")
                
        elif response == 'B':
            print(f"response == 'B', response: {response}")
            if choice_b['follower_count'] > choice_a['follower_count']:
                score += 1
                choice_a = choice_b
                choice_b = choice(data)             
                print(f"You're right! Current score: {score}")
            else: 
                correct = False
                print(f"Sorry, that's wrong. Final score: {score}")

compare()