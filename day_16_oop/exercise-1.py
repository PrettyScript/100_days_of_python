from turtle import Turtle, Screen
from prettytable import PrettyTable

# timmy = Turtle()
# timmy.shape('turtle')
# timmy.color('DarkSeaGreen1')
# timmy.forward(100)

# my_screen = Screen()
# #my_screen.canvheight
# my_screen.exitonclick()

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtke", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = 'c'
print(table)