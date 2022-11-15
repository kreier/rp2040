# PLEASE DO NOT EDIT OR DELETE. USE THE main.py INSTEAD
# Raspberry Pico 2040 start script to activate the oLed display
# https://github.com/kreier/rp2040 2022-11-15

import time
import board
import busio
import displayio
import digitalio
import adafruit_displayio_sh1106

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True

# i2c = busio.I2C(board.SCL, board.SDA)
i2c = busio.I2C(board.GP1, board.GP0)    # Pi Pico RP2040

displayio.release_displays()

display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_sh1106.SH1106(display_bus, width=128, height=64, colstart=2)

led.value = False

for loop in range(3):
    time.sleep(0.1)
    led.value = True
    time.sleep(0.05)
    print(".", end="")
    led.value = False

print(" Starting main.py")
exec(open("main.py").read())
