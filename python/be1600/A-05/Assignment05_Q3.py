from cImage import *

def doubleImage2(oldImage, x, y):
    oldW = oldImage.getWidth()
    oldH = oldImage.getHeight()

    newIm = EmptyImage(oldW * x, oldH * y)

    for row in range(newIm.getHeight()):
        for col in range(newIm.getWidth()):
            originalCol = col // x
            originalRow = row // y
            oldPixel = oldImage.getPixel(originalCol, originalRow)

            newIm.setPixel(col, row, oldPixel)

    return newIm

def makeDoubleImage2(imageFile, x, y):
    oldImage = FileImage(imageFile)
    width = oldImage.getWidth()
    height = oldImage.getHeight()
    
    myWin = ImageWin("Double Width", width * x, height * y)
    
    newImage = doubleImage2(oldImage, x, y)
    newImage.setPosition(0, 0)
    newImage.draw(myWin)

    myWin.exitOnClick()

x = int(input("X: "))
y = int(input("Y: "))
makeDoubleImage2("butterfly.gif", x, y)    
