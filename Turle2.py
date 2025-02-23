import turtle
import math

deep = turtle.Turtle()

deep.color('red', "yellow")

deep.begin_fill()

deep.speed(1)

for i in range(20, 30, 2):
    deep.right(90)
    deep.forward(i)
    deep.right(270)
    deep.pendown()
    deep.circle(i)
    deep.penup()
    deep.home() #This was the main catch here, thsi func sets the coordinated back to (0, 0), that is the pointer goes back to the centre

    # deep.forward(200)
    # deep.left(175)
    # deep.forward(200)
    # deep.left(175)
    # deep.forward(200)
    # deep.left(175)
    # deep.forward(200)


# for i in range(100):
#     deep.forward(math.sin(i)*100)
#     deep.left(45)
#     # deep.forward(200)
#     # deep.left(175)
#     # deep.forward(200)
#     # deep.left(175)
#     # deep.forward(200)
#     # deep.left(175)
#     # deep.forward(200)

deep.end_fill()

turtle.done()