import time
from dotstar import Adafruit_DotStar

pixelCount = 30 # Number of LEDs in strip
datapin   = 10
clockpin  = 11
strip     = Adafruit_DotStar(pixelCount, datapin, clockpin, order='bgr')

strip.begin()           # Initialize pins for output
strip.setBrightness(4)  # Limit brightness

colorCount = 6          # red, magenta, blue, cyan, green, yellow
increment = 255 / (pixelCount / colorCount)
red = 255
green = 0
blue = 0

for pixel in range(0, pixelCount):
    strip.setPixelColor(pixel % pixelCount, (red % 256)*256*256 + (green % 256)*256 + (blue % 256))
    
    if pixel < pixelCount / colorCount:
        blue = blue + increment
    elif pixel < 2 * pixelCount / colorCount:
        red = red - increment
    elif pixel < 3 * pixelCount / colorCount:
        green = green + increment
    elif pixel < 4 * pixelCount / colorCount:
        blue = blue - increment
    elif pixel < 5 * pixelCount / colorCount:
        red = red + increment
    else:
        green = green - increment

strip.show()
