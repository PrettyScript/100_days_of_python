from turtle import Turtle


class Scoreboard(Turtle):
    
    def __init__(self):
        self.score = 0
    
    def score(self):
        self.score += 1
        self.write("Score:", align="center")