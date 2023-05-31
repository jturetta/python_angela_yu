import turtle

tim = turtle.Turtle()
screen = turtle.Screen()


def move_backwards():
    tim.backward(10)


def move_forwards():
    tim.forward(10)


def turn_left():
    tim.left(45)


def turn_right():
    tim.right(45)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
turtle.onkey(key="s", fun=move_backwards)
turtle.onkey(key="w", fun=move_forwards)
turtle.onkey(key="a", fun=turn_left)
turtle.onkey(key="d", fun=turn_right)
turtle.onkey(key="c", fun=clear)
screen.exitonclick()
