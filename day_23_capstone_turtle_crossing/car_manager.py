from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from random import randint, choice


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []

    
    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(choice(COLORS))
            random_y = randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)


# Create cars that are 20px high by 40px wide that are randomly generated along the y-axis 
# and move to the left edge of the screen. No cars should be generated in the top and bottom 
# 50px of the screen (think of it as a safe zone for our little turtle). Hint: generate a new 

# car only every 6th time the game loop runs. If you get stuck, check the video walkthrough in Step 4.

        
