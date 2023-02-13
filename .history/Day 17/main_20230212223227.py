import turtle as t

tim = t.Turtle()


def draw_polygon(polygon_sides):
    polygon_angle = 360 / polygon_sides
    for _ in range(polygon_sides):
        tim.forward(100)
        tim.right(polygon_angle)


for i in range