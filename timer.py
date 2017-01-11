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

pomodoroCount = 4
minutesInPomodoro = 30
secondsForFlash = .25
secondsPerMinute = 6 #TODO: change back to 60 after demo

def flash_color(color):
    for iteration in range(0, 10):
        for pixel in range(0, pixelCount):
            strip.setPixelColor(pixel, color if iteration % 2 == 0 else black)
            
        strip.show()
        time.sleep(secondsForFlash)    

while True:
    #pomodoros
    for pomodoro in range(0, pomodoroCount):
        #flash blue/black to indicate pomodoro is starting
        flash_color(blue)

        for minute in range(0, minutesInPomodoro):
            #flash red/black to indicate when break is starting
            if minute == minutesInPomodoro * (len(colors) - 1) / len(colors):
                flash_color(red)

            for pixel in range(0, pixelCount):
                if pixel + minute < pixelCount or pomodoro < pomodoroCount - 1:
                    color = colors[(pixel + minute) % pixelCount / (pixelCount / len(colors))]
                else:
                    color = black

                strip.setPixelColor(pixel, color)

            print pomodoro, minute
            strip.show()
            time.sleep(secondsPerMinute)

    #break
    for minute in range(0, minutesInPomodoro):
        #black for break
        for pixel in range(0, pixelCount - minute):
            strip.setPixelColor(pixel, black)

        #next pomodoro
        for pixel in range(pixelCount - minute, pixelCount):
            color = colors[(minute + pixel) % pixelCount / (pixelCount / len(colors))]
            strip.setPixelColor(pixel, color)

        print minute
        strip.show()
        time.sleep(secondsPerMinute)
        
