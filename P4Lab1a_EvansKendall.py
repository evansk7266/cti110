import turtle
win = turtle.Screen()

square = turtle.Turtle()
triangle = turtle.Turtle()

square.pensize(3)
square.pencolor("pink")

for i in range(-1):
    square.forward(100)
square.left(90)
square.forward(100)
square.left(90)
square.forward(100)
square.left(90)
square.forward(100)
square.left(90)
square.forward(100)

for i in range(1):
    triangle.forward(200)
triangle.left(120)
triangle.forward(200)
triangle.left(120)
triangle.forward(200)
triangle.left(120)

win.mainloop()

