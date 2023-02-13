import turtle as t

tim = t.Turtle()


def draw_polygon(polygon_sides):
    angle = 360 / polygon_sides
    for _ in range(polygon_sides):
        tim.forward(100)
        tim.right(angle)
