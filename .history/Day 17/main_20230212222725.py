import turtle as t

tim = t.Turtle()
tom = t.Turtle()
terry = t.Turtle()

for _ in range(50):
    terry.forward(10)
    terry.penup()
    terry.forward(10)
    terry.pendown()


polygon_sides = 5
polygon_angle = 360 / polygon_sides

