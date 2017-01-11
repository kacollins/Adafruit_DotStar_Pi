import time
from dotstar import Adafruit_DotStar

pixelCount = 30 # Number of LEDs in strip
datapin   = 10
clockpin  = 11
strip     = Adafruit_DotStar(pixelCount, datapin, clockpin, order='bgr')

strip.begin()           # Initialize pins for output
strip.setBrightness(4)  # Limit brightness

for pixel in range(0, pixelCount):
    strip.setPixelColor(pixel % pixelCount, 0)

strip.show()
