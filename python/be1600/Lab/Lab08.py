from cImage import *

blueline = Pixel(0,0,255)
redline = Pixel(255,0,0)

myImageWindow = ImageWin("My Image",500,500)
newImage = EmptyImage(500, 500)
for i in range(500):
  newImage.setPixel(i,i,blueline)
  newImage.setPixel(499-i,i,blueline)
for i in range(250):
  newImage.setPixel(250,250+i,redline) 
newImage.draw(myImageWindow)
newImage.save("drawlines.gif")
myImageWindow.exitOnClick()
