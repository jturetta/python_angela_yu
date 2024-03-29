from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
screen.textinput(title="Make your bet!",
                 prompt="Which turtle is going to win? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-120, -80, -40, 0, 40, 80]

for turtle_index in range(6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230, y=y_positions[turtle_index])

screen.exitonclick()
