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

for i in range(polygon_sides):
    tim.forward(100)
    tim.right(polygon_angle)