# PLEASE DO NOT EDIT OR DELETE. USE THE main.py INSTEAD
# Raspberry Pico 2040 start script to activate the oLed display
# https://github.com/kreier/rp2040 2022-11-15

import time
import board
import busio
import displayio
import digitalio
import adafruit_ssd1306

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True

# i2c = busio.I2C(board.SCL, board.SDA)
i2c = busio.I2C(board.GP1, board.GP0)    # Pi Pico RP2040

displayio.release_displays()

display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)

#oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)  # old and deprecated

import adafruit_ssd1306
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
oled.fill(1)
oled.show()

time.sleep(0.3)

oled.fill(0)
oled.show()
led.value = False
i2c.unlock()
time.sleep(2)

print("Starting main.py")
exec(open("main.py").read())
