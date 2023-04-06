# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials NeoPixel example"""
import time
import board
from rainbowio import colorwheel
import neopixel

pixel_pin = board.GP6
num_pixels = 16

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

def color_chase(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.1) 


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = colorwheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)


RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

while True:
    timestep = 0.3
    pixels.fill(RED)
    pixels.show()
    print("RED")
    # Increase or decrease to change the speed of the solid color change.
    time.sleep(timestep)
    pixels.fill(GREEN)
    pixels.show()
    time.sleep(timestep)
    pixels.fill(BLUE)
    pixels.show()
    time.sleep(timestep)

    chasestep = 0.01
    print("Colorchase")
    color_chase(RED, chasestep)  # Increase the number to slow down the color chase
    color_chase(YELLOW, chasestep)
    color_chase(GREEN, chasestep)
    color_chase(CYAN, chasestep)
    color_chase(BLUE, chasestep)
    color_chase(PURPLE, chasestep)

    print("rainbow")
    rainbow_cycle(0)  # Increase the number to slow down the rainbow
