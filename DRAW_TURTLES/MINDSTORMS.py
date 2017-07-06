import turtle

def draw_shapes():

    #setup window with background color "red"
    window = turtle.Screen()
    window.bgcolor("black")

    #create turtle "Brad"
    brad = turtle.Turtle()
    brad.shape("square")
    brad.color("red")
    brad.speed(1)
    #Command Brad to draw a square
    i = 1
    while i <= 4:
        brad.forward(100)
        brad.right(90)
        i += 1
        
    #create instance "angie"
    angie = turtle.Turtle()
    angie.shape("circle")
    angie.color("white")
    angie.speed(1)
    #command angie to draw circle
    angie.right(10)
    angie.circle(100)

    #initialize instance "winston"
    winston = turtle.Turtle()
    winston.shape("arrow")
    winston.color("blue")
    winston.speed(1)
    #comand winston to draw triangle
    winston.right(135)
    i = 1
    while i <= 3:
        winston.forward(150)
        winston.right(120)
        i += 1

    #exits red window when clicked
    window.exitonclick()

draw_shapes()
