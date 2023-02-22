import turtle as t
import random

tim = t.Turtle()

colors = [
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen",
]


def draw_polygon(polygon_sides):
    polygon_angle = 360 / polygon_sides
    for _ in range(polygon_sides):
        tim.forward(100)
        tim.right(polygon_angle)


for i in range(3, 9):
    tim.color(random.choice(colors))
    draw_polygon(i)
