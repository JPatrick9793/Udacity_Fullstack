import turtle

#   "x = function" "y = turtle"
def pattern(x, y):
    x(y)
    y.left(60)
    x(y)
    y.right(120)
    x(y)
    y.left(60)
    x(y)

#   x = turtle (brad)
#   defining degree koch functions
def koch0(x):
    #define distance of elementary line
    x.forward(2.5)   
def koch1(x):
    pattern(koch0, x)
def koch2(x):
    pattern(koch1, x)
def koch3(x):
    pattern(koch2, x)
def koch4(x):
    pattern(koch3, x)

def snowflake(x):
    i = 1
    while i <= 4:
        koch4(x)
        x.right(90)
        i += 1

def draw_shapes():

    #setup window with background color "black"
    window = turtle.Screen()
    window.bgcolor("black")

    #create turtle "brad"
    brad = turtle.Turtle()
    brad.shape("square")
    brad.color("white")
    brad.speed(200)

    #call snowflake function and pass brad as parameter
    snowflake(brad)

    #exits red window when clicked
    window.exitonclick()

draw_shapes()
