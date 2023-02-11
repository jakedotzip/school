import turtle
import math
t = turtle.Turtle()
def drawCircle():
  t.up()
  t.color('blue')
  for i in range(360):
    x = 100 * math.cos(math.radians(i))
    y = 100 * math.sin(math.radians(i))
    t.goto(x,y)
    t.dot()
  turtle.done()

drawCircle()