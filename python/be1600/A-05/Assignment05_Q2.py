from cImage import *

def enhanceRed(oldPixel):
  oldRed = oldPixel.getRed()
  if (oldRed < 80):
    newRed = oldRed
  else:
    newRed = 255
  newGreen = oldPixel.getGreen()
  newBlue = oldPixel.getBlue()
  newPixel = Pixel(newRed, newGreen, newBlue)
  return newPixel

def changePixel(imageFile):
  oldImage = FileImage(imageFile)
  width = oldImage.getWidth()
  height = oldImage.getHeight()

  myImageWindow = ImageWin("Enhanced Red", width, height)
  newImage = EmptyImage(width, height)

  for row in range(height):
    for col in range(width):
      oldPixel = oldImage.getPixel(col, row)
      newPixel = enhanceRed(oldPixel)
      newImage.setPixel(col, row, newPixel)

  newImage.setPosition(0, 0)
  newImage.draw(myImageWindow)
  myImageWindow.exitOnClick()

changePixel("butterfly.gif")