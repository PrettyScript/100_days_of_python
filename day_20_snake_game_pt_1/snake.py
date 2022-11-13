from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()


    def  create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape='square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)        

    def move(self):
        for segment_num in range(len(self.segments) - 1, 0, -1):
            # second to last segment
            new_x = self.segments[segment_num - 1].xcor()
            new_y = self.segments[segment_num - 1].ycor()
            # last segment
            self.segments[segment_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
        # segments[0].left(90)        



