#TODO print logos for game
#TODO Have a way to track user's score 

#TODO Take in the user's answer and it is displayed as they progress in the game
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
    # print("Top")
    while correct:
        print(logo)
        print(f"Compare A: {choice_a['name']}, a {choice_a['description']} from {choice_a['country']}")   
        print(vs) 
        print(f"Against B: {choice_b['name']}, a {choice_b['description']} from {choice_b['country']}")        
        response = input("Who has more followers? Type 'A' or 'B': ").upper()  

        if response == 'A':
            print(f"response == 'A', response: {response}")
            if choice_a['follower_count'] > choice_b['follower_count']:
                # print(f"a: {choice_a}\nb: {choice_b['follower_count']}")
                # print(True)
                print(f"Before adding score. Choice B: {choice_b}")
                score += 1
                choice_a = choice_b
                choice_b = choice(data)  
                print(f"In response A block, choice a: {choice_a}\nchoice b: {choice_b}")              
                print(f"You're right! Current score: {score}")

                # response = input("Who has more followers? Type 'A' or 'B': ").upper()
            else: 
                # print(f"a: {choice_a}\nb: {choice_b['follower_count']}")
                correct = False
                print(f"Sorry, that's wrong. Final score: {score}")
                
        elif response == 'B':
            print(f"response == 'B', response: {response}")
            if choice_b['follower_count'] > choice_a['follower_count']:
                print(f"Before adding score. Choice B: {choice_b}")
                score += 1
                choice_a = choice_b
                choice_b = choice(data)  
                print(f"In response A block, choice a: {choice_a}\nchoice b: {choice_b}")              
                print(f"You're right! Current score: {score}")
              
                # response = input("Who has more followers? Type 'A' or 'B': ").upper()
            else: 
                # print(f"a: {choice_a}\nb: {choice_b['follower_count']}")
                correct = False
                print(f"Sorry, that's wrong. Final score: {score}")
                
        
     


compare()

# def choices():


    #TODO First time Compare A and Compare B and if correct, Compare B will then shift to Compare A and a new comparison will be in Compare B
    #TODO If user is correct keep shifting, if not then they lose and their final score is displayed
    #TODO The second logo is removed