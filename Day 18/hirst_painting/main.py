# import colorgram

# image = 'Day 19/hirst_painting/image.jpg'

# rgb_colors = []
# colors = colorgram.extract(image, 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

import turtle
import random

turtle.colormode(255)
tim = turtle.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

colors_list = [(240, 240, 239), (230, 232, 237), (232, 238, 235), (239, 233, 236), (187, 161, 122), (14, 25, 57), (67, 94, 134), (145, 87, 55), (139, 158, 184), (139, 73, 94), (68, 15, 6), (186, 141, 160), (24, 51, 126), (71, 110, 85), (129, 29, 51),
               (149, 21, 8), (183, 148, 46), (138, 169, 151), (215, 206, 136), (62, 18, 30), (93, 118, 178), (187, 93, 115), (187, 97, 82), (14, 34, 29), (97, 146, 129), (222, 174, 188), (33, 84, 64), (162, 208, 183), (180, 186, 211), (91, 145, 154)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(colors_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle.Screen()
screen.exitonclick()
