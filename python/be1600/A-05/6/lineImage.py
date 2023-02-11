from cImage import *
myImWin = ImageWin("Line Image",300,300)
lineImage = EmptyImage(300,300)
whitePixel = Pixel(255,0,0)
for i in range(300):
    lineImage.setPixel(i,i,whitePixel)
lineImage.draw(myImWin)
lineImage.save("lineImage.gif")
myImWin.exitOnClick()
