import turtle
sq = turtle.Turtle()

def draw(myTurtle, x, y, length):
    myTurtle.up()
    myTurtle.goto(x,y)
    myTurtle.down()
    for i in range(4):
        myTurtle.forward(length)
        myTurtle.left(90)
    
def main():
    x = 10
    y = 10
    l = 300
    for i in range(10):
        draw(sq,x*(i+1),y*(i+1),l-((i*2)*10))
    turtle.done()

main()