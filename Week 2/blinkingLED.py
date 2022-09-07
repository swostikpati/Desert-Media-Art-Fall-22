print("A for apple!!!")

import board
import digitalio  # gives access to the pin
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = (
    digitalio.Direction.OUTPUT
)  # determines whether the pin is used for input or output

while True:
    led.value = True
    time.sleep(0.5 / 4)
    led.value = False
    time.sleep(0.5 / 4)

print("Done")
