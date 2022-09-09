# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Internal RGB LED red, green, blue example"""
print("Start")
import time
import board

if hasattr(board, "APA102_SCK"):
    import adafruit_dotstar

    led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
else:
    import neopixel

    led = neopixel.NeoPixel(board.NEOPIXEL, 1)

led.brightness = 0.5

'''while True:
    for i in range(0,255,10):
        for j in range(0,255,10):
            for k in range(0,255,10):
                led[0] = (i, j, k)
                time.sleep(0.05)
            time.sleep(0.05)
        time.sleep(0.05)

    #time.sleep(0.5)
    #led[0] = (0, 255, 0)
    #time.sleep(0.5)
    #led[0] = (0, 0, 255)
    #time.sleep(0.5)
    break'''
led[0] = (0, 255, 0)
time.sleep(1)
for i in range (4):
    for i in range (3):
        led[0] = (255, 0, 0)
        time.sleep(0.2)
        led[0] = (0, 0, 255)
        time.sleep(0.2)

    led[0] = (255, 0, 0)
    time.sleep(0.2)
    led[0] = (0, 255, 0)
    time.sleep(0.2)
    led[0] = (0, 0, 255)
    time.sleep(0.2)
    led[0] = (0, 255, 0)
    time.sleep(0.2)

    for i in range(5, 0, -1):
        led.brightness = i/10
        led[0] = (255, 0, 0)
        
        time.sleep(0.3)
        
    for i in range(5, 0, -1):
        led.brightness = i/10
        led[0] = (0, 0, 255)
        
        time.sleep(0.3)

    for i in range(5, 0, -1):
        led.brightness = i/10
        led[0] = (0, 255, 0)
        
        time.sleep(0.3)

print("Done")
