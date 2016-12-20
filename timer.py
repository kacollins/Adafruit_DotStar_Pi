import time
from dotstar import Adafruit_DotStar

pixelCount = 30 # Number of LEDs in strip
datapin   = 10
clockpin  = 11
strip     = Adafruit_DotStar(pixelCount, datapin, clockpin, order='bgr')

strip.begin()           # Initialize pins for output
strip.setBrightness(4)  # Limit brightness

blue = 0x0000FF
green = 0x00FF00
yellow = 0xFFFF00
orange = 0xFF7F00
red = 0xFF0000
black = 0x000000

colors = [blue
          , green
          , yellow
          , orange
          , red
          , black
          ]

pomodoroCount = 2 #TODO 4
minutesInPomodoro = 30
secondsForFlash = .25
secondsPerMinute = .5 #TODO 60

#pomodoros
for pomodoro in range(0, pomodoroCount):
    #flash blue/black to indicate pomodoro is starting
    for iteration in range(0, 10):
        for pixel in range(0, pixelCount):
            colorIndex = 0 if iteration % 2 == 0 else len(colors) - 1
            strip.setPixelColor(pixel, colors[colorIndex])
            
        strip.show()
        time.sleep(secondsForFlash)

    for minute in range(0, minutesInPomodoro):
        #flash red/black to indicate when break is starting
        if minute == minutesInPomodoro * (len(colors) - 1) / len(colors):
            for iteration in range(0, 10):
                for pixel in range(0, pixelCount):
                    colorIndex = len(colors) - 2 if iteration % 2 == 0 else len(colors) - 1
                    strip.setPixelColor(pixel, colors[colorIndex])

                strip.show()
                time.sleep(secondsForFlash)

        for pixel in range(0, pixelCount):
            if pixel + minute < pixelCount or pomodoro < pomodoroCount - 1:
                colorIndex = (pixel + minute) % pixelCount / (pixelCount / len(colors))
            else:
                colorIndex = len(colors) - 1
            strip.setPixelColor(pixel, colors[colorIndex])

        print pomodoro, minute
        strip.show()
        time.sleep(secondsPerMinute)

#break
for minute in range(0, minutesInPomodoro):
    #black for break
    for pixel in range(0, pixelCount - minute):
        strip.setPixelColor(pixel, colors[len(colors) - 1])

    #next pomodoro
    for pixel in range(pixelCount - minute, pixelCount):
        colorIndex = (minute + pixel) % pixelCount / (pixelCount / len(colors))
        strip.setPixelColor(pixel, colors[colorIndex])

    print minute
    strip.show()
    time.sleep(secondsPerMinute)
    
