# Reference: Adafruit - RGB Led
import board
import time
print("Start")

if hasattr(board, "APA102_SCK"):
    import adafruit_dotstar

    led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
else:
    import neopixel

    led = neopixel.NeoPixel(board.NEOPIXEL, 1)

led.brightness = 0.5  # setting initial brightness


# defining colors used repeated
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

# There are two parts to the song which are repeated many times


def part1():
    # starting alternating beats
    for i in range(3):
        red()
        time.sleep(0.2)
        blue()
        time.sleep(0.2)

    # small bridge before the beginning of the next section
    red()
    time.sleep(0.2)
    green()
    time.sleep(0.2)
    blue()
    time.sleep(0.2)
    green()
    time.sleep(0.2)

    # fading brightness of different colors to showcase the repeated fading music
    for i in range(5, 0, -1):
        led.brightness = i/10
        red()
        time.sleep(0.3)

    for i in range(5, 0, -1):
        led.brightness = i/10
        blue()
        time.sleep(0.3)

    for i in range(5, 0, -1):
        led.brightness = i/10
        green()
        time.sleep(0.3)

# part two of the music - the music was more cheerful here so vibrant colors have been used


def part2():
    # starts with a fade in as the music increases
    for i in range(1, 6):
        led.brightness = i/10
        aqua()
        time.sleep(0.3)

    # fade-outs to depict the repeated fading music again
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


# Main Program
# Gives the cue to the user to start the music
white()
time.sleep(1)

# Music Sequence
for i in range(4):
    part1()

part2()

for i in range(2):
    part1()

part2()

for i in range(2):
    part1()

# Depicts end of music
white()
time.sleep(1)
print("Done")
