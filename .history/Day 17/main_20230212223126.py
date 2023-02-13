import turtle as t

tim = t.Turtle()

def draw_polygon(polygonb, angle):
    angle = 360 / polygonb
    for _ in range(polygonb):
        tim.forward(100)
        tim.right(angle)


for i in range(3, 11):
    draw_polygon(i, polygon_angle)
    
    