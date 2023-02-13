import turtle as t

tim = t.Turtle()

polygon_sides = 5
polygon_angle = 360 / polygon_sides

def draw_polygon(sides, angle):
    for _ in range(sides):
        tim.forward(100)
        tim.right(angle)


for i 