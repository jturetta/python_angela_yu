import turtle as t

tim = t.Turtle()

def draw_polygon(polygon, angle):
    angle = 360 / polygon
    for _ in range(polygon):
        tim.forward(100)
        tim.right(angle)


for i in range(3, 11):
    draw_polygon(i, polygon_angle)
    
    