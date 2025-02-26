import turtle

oscar = turtle.Turtle()
oscar.getscreen().bgcolor('beige')

def star(oscar):
    for j in range(5):
        for i in range(5):
            oscar.forward(200)
            oscar.left(216)
        star(oscar)

star(oscar)

turtle.done()