from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from random import randint


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.turtlesize(stretch_wid=1.5, stretch_len=3)

    
    # def cars(self):
        
