#First importing turtle libraries
import turtle

bob = turtle.Turtle() #this creates a new instance(obj) of the 'Turle' class
#And the new obj is assigned to bob var

#bob.color("blue") #this method is used to take the color of the pix
#u can allso paste in hex value of colors

#Now if u want two diff colors, one for border and one for middle fill then,
bob.color('blue', 'cyan')
#first arg for the border_color, sec arg for fill_color


bob.begin_fill() #used to fill up the enclused shape, called just before the shape is drawn


bob.forward(100) #forward() is a func in Turtle class which moves the turle 100 pixs
bob.setheading(90) #this func turns the turtle and takes in angle in deg as input
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)

#now if u want ot draw two diff shapes then we have a pen up and pen down func for that
bob.penup()
bob.forward(100)
bob.pendown()

bob.forward(100) 
bob.left(90) 
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)


bob.end_fill() #called when done drawing the shape

turtle.done() #end the turtle file, keeps our animation window open so that we can see..