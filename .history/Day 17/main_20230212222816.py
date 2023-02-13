import turtle as t

tim = t.Turtle()

polygon_sides = 5
polygon_angle = 360 / polygon_sides

for _ in range(polygon_sides):
    tim.forward(100)
    tim.right(polygon_angle)