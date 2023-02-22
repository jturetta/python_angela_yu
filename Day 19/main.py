import turtle

tim = turtle.Turtle()
screen = turtle.Screen()


def move_forwards():
    tim.forward(10)


screen.listen()
turtle.onkey(key="space", fun=move_forwards)
screen.exitonclick()
