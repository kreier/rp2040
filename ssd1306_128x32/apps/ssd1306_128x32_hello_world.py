# PLEASE DO NOT EDIT OR DELETE. USE THE main.py INSTEAD
# Raspberry Pico 2040 start script to activate the oLed display 128x32
# https://github.com/kreier/rp2040 2022-11-28

import time, board, busio, displayio, digitalio, terminalio
import adafruit_displayio_ssd1306
from adafruit_display_text import label

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True

# i2c = busio.I2C(board.SCL, board.SDA)
i2c = busio.I2C(board.GP1, board.GP0)    # Pi Pico RP2040

displayio.release_displays()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3c)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=32)

# Make the display context
splash = displayio.Group()
display.show(splash)

color_bitmap = displayio.Bitmap(128, 32, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFFFFFF  # White

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(118, 24, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x000000  # Black
inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=5, y=4)
splash.append(inner_sprite)

# Draw a label
text = "Hello World!"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00, x=28, y=15)
splash.append(text_area)

led.value = False

while True:
    pass
