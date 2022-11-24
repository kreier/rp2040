from sys import implementation
from os import uname
import board
import time
import displayio
import terminalio
import busio
import adafruit_ili9341
from adafruit_display_text import label

print('=======================')
print(implementation[0], uname()[3])

displayio.release_displays()

TFT_WIDTH = 320
TFT_HEIGHT = 240

#tft_cs = board.GP13
#tft_dc = board.GP15
#tft_res = board.GP14
#spi_mosi = board.GP7
#spi_miso = board.GP4
#spi_clk = board.GP6

tft_cs   = board.GP17 # changed
tft_dc   = board.GP15
tft_res  = board.GP14
spi_mosi = board.GP19 # changed
spi_miso = board.GP16
spi_clk  = board.GP18 # SCK

spi = busio.SPI(spi_clk, MOSI=spi_mosi)

display_bus = displayio.FourWire(
    spi, command=tft_dc, chip_select=tft_cs, reset=tft_res)

display = adafruit_ili9341.ILI9341(display_bus,
                    width=TFT_WIDTH, height=TFT_HEIGHT,
                    rowstart=0, colstart=0)
display.rotation = 90

# Make the display context
splash = displayio.Group(max_size=10)
display.show(splash)
