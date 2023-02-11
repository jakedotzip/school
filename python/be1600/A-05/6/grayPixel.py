from cImage import *

def grayPixel(oldpixel):
    intensitySum = oldpixel.getRed() + oldpixel.getGreen() + \
                   oldpixel.getBlue()
    aveRGB = intensitySum // 3

    newPixel = Pixel(aveRGB,aveRGB,aveRGB)
    return newPixel


print (grayPixel( Pixel(34,128,74) ))
print (grayPixel( Pixel(200,234,165) ))
print (grayPixel( Pixel(23,56,77) ))
