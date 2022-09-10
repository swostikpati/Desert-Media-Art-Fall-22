# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Internal RGB LED red, green, blue example"""
import board
import time
print("Start")

if hasattr(board, "APA102_SCK"):
    import adafruit_dotstar

    led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
else:
    import neopixel

    led = neopixel.NeoPixel(board.NEOPIXEL, 1)

led.brightness = 0.5


def red():
    led[0] = (255, 0, 0)


def green():
    led[0] = (0, 255, 0)


def blue():
    led[0] = (0, 0, 255)


def yellow():
    led[0] = (255, 255, 0)


def magenta():
    led[0] = (255, 0, 255)


def aqua():
    led[0] = (0, 255, 255)


def black():
    led[0] = (0, 0, 0)


def white():
    led[0] = (255, 255, 255)


def part1():
    for i in range(3):
        red()
        time.sleep(0.2)
        blue()
        time.sleep(0.2)

    #led[0] = (255, 0, 0)
    red()
    time.sleep(0.2)
    #led[0] = (0, 255, 0)
    green()
    time.sleep(0.2)
    #led[0] = (0, 0, 255)
    blue()
    time.sleep(0.2)
    #led[0] = (0, 255, 0)
    green()
    time.sleep(0.2)

    for i in range(5, 0, -1):
        led.brightness = i/10
        #led[0] = (255, 0, 0)
        red()

        time.sleep(0.3)

    for i in range(5, 0, -1):
        led.brightness = i/10
        #led[0] = (0, 0, 255)
        blue()

        time.sleep(0.3)

    for i in range(5, 0, -1):
        led.brightness = i/10
        #led[0] = (0, 255, 0)
        green()

        time.sleep(0.3)


def part2():
    for i in range(1, 6):
        led.brightness = i/10
        aqua()
        time.sleep(0.3)

    for i in range(5, 0, -1):
        led.brightness = i/10
        yellow()
        time.sleep(0.3)

    for i in range(5, 0, -1):
        led.brightness = i/10
        magenta()
        time.sleep(0.3)
    for i in range(5, 0, -1):
        led.brightness = i/10
        aqua()
        time.sleep(0.3)

    for i in range(6):
        magenta()
        time.sleep(0.25)
        yellow()
        time.sleep(0.25)


white()
time.sleep(1)
for i in range(4):
    part1()

part2()

for i in range(2):
    part1()

part2()

for i in range(2):
    part1()

white()
time.sleep(1)
print("Done")
