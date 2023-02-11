
from cImage import*
def horizontalFlip(oldimage):
    oldw = oldimage.getWidth()
    oldh = oldimage.getHeight()
    newim = EmptyImage(oldw, oldh)
    maxp = oldh - 1
    for col in range(oldw):
        for row in range(oldh):
            oldpixel = oldimage.getPixel(col, maxp - row)
            newim.setPixel(col, row, oldpixel)
    return newim

oldImage = FileImage("butterfly.gif")
width = oldImage.getWidth()
height = oldImage.getHeight()
newImage = horizontalFlip(oldImage)

myImageWindow = ImageWin("HorizontalFlip", 2 * width  , height)
oldImage.draw(myImageWindow)  
    
newImage.setPosition(width + 1,0)
newImage.draw(myImageWindow)
myImageWindow.exitOnClick()





