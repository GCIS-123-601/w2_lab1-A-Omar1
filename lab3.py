import turtle
def testDrive():
    turtle.forward(180)
    turtle.left(87)
    turtle.setheading(127)
    turtle.up()
    turtle.goto(50,40)
    turtle.home()
    turtle.down()
    turtle.circle(25)
def turtleState():
    v2 = turtle.isdown()
    v3 = turtle.heading()
    tXcor = turtle.xcor()
    tYcor = turtle.ycor()
    print("turtle is down?", v2)
    print("turtle heading:", v3)
    print("xcor: ",tXcor, "ycor: ", tYcor)
def main():
    testDrive()
    turtleState()

main()
