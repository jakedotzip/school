from cImage import *

def doubleImage(oldImage):
    oldW = oldImage.getWidth()
    oldH = oldImage.getHeight()

    newIm = EmptyImage(oldW * 2, oldH * 2)

    for row in range(oldH):
        for col in range(oldW):
            oldPixel = oldImage.getPixel(col, row)

            newIm.setPixel(2 * col, 2 * row, oldPixel)
            newIm.setPixel(2 * col + 1, 2 * row, oldPixel)
            newIm.setPixel(2 * col, 2 * row + 1, oldPixel)
            newIm.setPixel(2 * col + 1, 2 * row + 1, oldPixel)

    return newIm

def makeDoubleImage(imageFile):
    oldImage = FileImage(imageFile)
    width = oldImage.getWidth()
    height = oldImage.getHeight()
    
    myWin = ImageWin("Double Size", width * 2, height * 3)
    oldImage.draw(myWin)

    #oldImage.setPosition(0 + width, 0)
    #oldImage.draw(myWin)
    
    newImage = doubleImage(oldImage)
    newImage.setPosition(0, oldImage.getHeight() + 1)
    newImage.draw(myWin)
    
    myWin.exitOnClick()
    
makeDoubleImage("butterfly.gif")
    
    
