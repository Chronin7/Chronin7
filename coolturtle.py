import turtle
turtle.colormode(255)
t=turtle.Turtle()
t.color((14, 199, 113))
for x in range(3,20):
    for y in range(0,x):
        t.forward(50)
        t.left(360/x)