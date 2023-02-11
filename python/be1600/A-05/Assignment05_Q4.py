from cImage import *

def BnW(oldPixel):
  avgIntensity = (oldPixel.getRed() + oldPixel.getGreen() + oldPixel.getBlue())/3
  if (avgIntensity > 140):
    newPixel = Pixel(255,255,255)
  else:
    newPixel = Pixel(0,0,0)
  return newPixel

def changePixel(imageFile):
  oldImage = FileImage(imageFile)
  width = oldImage.getWidth()
  height = oldImage.getHeight()

  myImageWindow = ImageWin("Black-White", width * 2, height)
  oldImage.draw(myImageWindow)
  newImage = EmptyImage(width, height)

  for row in range(height):
    for col in range(width):
      oldPixel = oldImage.getPixel(col, row)
      newPixel = BnW(oldPixel)
      newImage.setPixel(col, row, newPixel)

  newImage.setPosition(width, 0)
  newImage.draw(myImageWindow)
  myImageWindow.exitOnClick()

changePixel("butterfly.gif")