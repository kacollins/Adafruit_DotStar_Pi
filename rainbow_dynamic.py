import time
from dotstar import Adafruit_DotStar

pixelCount = 30 # Number of LEDs in strip
datapin   = 10
clockpin  = 11
strip     = Adafruit_DotStar(pixelCount, datapin, clockpin, order='bgr')

strip.begin()           # Initialize pins for output
strip.setBrightness(4)  # Limit brightness

def fixValue(value):
    if value < 0:
        value = 0
    elif value > 255:
        value = 255

    return value

def getColor(red, green, blue):
    red = fixValue(red)
    green = fixValue(green)
    blue = fixValue(blue)

    return red*256*256 + green*256 + blue

colors = [];
red = 255
green = 0
blue = 0
increment = 16

while blue < 255:
    blue = blue + increment
    colors.append(getColor(red, green, blue))

while red > 0:
    red = red - increment
    colors.append(getColor(red, green, blue))

while green < 255:
    green = green + increment
    colors.append(getColor(red, green, blue))

while blue > 0:
    blue = blue - increment
    colors.append(getColor(red, green, blue))

while red < 255:
    red = red + increment
    colors.append(getColor(red, green, blue))

while green > 0:
    green = green - increment
    colors.append(getColor(red, green, blue))

totalIterations = len(colors)
secondsBetweenIterations = 0.05

for iteration in range(0, totalIterations):
    for pixel in range(0, pixelCount):
        strip.setPixelColor(pixel, colors[(pixel + iteration) % len(colors)])

    strip.show()
    time.sleep(secondsBetweenIterations)
