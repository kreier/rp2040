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
#display.rotation = 270

# Create a bitmap with 256 colors
bitmap = displayio.Bitmap(display.width, display.height, 256)

def hsv_to_rgb(h, s, v):
    if s == 0.0: v*=255; return (v, v, v)
    i = int(h*6.)
    f = (h*6.)-i; p,q,t = int(255*(v*(1.-s))), int(255*(v*(1.-s*f))), int(255*(v*(1.-s*(1.-f)))); v*=255; i%=6
    if i == 0: ret = (65536*v + 256*t + p)
    if i == 1: ret = (65536*q + 256*v + p)
    if i == 2: ret = (65536*p + 256*v + t)
    if i == 3: ret = (65536*p + 256*q + v)
    if i == 4: ret = (65536*t + 256*p + v)
    if i == 5: ret = (65536*v + 256*p + q)
    #return f"{ret:06X}"
    return ret

# Create a 256 color palette
palette = displayio.Palette(256)
for i in range(256):
    #palette[i] = random.randrange(16777216)
    palette[i] = hsv_to_rgb(i/256, 1, 1)
palette[0] = 0


# Create a TileGrid using the Bitmap and Palette
tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette)

# Create a Group
group = displayio.Group()

# Add the TileGrid to the Group
group.append(tile_grid)

# Add the Group to the Display
display.show(group)

# Draw even more pixels
#for c in range(len(palette)):
#    for x in range(display.width):
#        for y in range(display.height):
#            bitmap[x, y] = (x + y) % 256

minX = -2.1
maxX = 0.6
width = display.width
height = display.height
aspectRatio = 1
ITERATION = 50
yScale = (maxX-minX)*(float(height)/width)*aspectRatio

for y in range(height):
    for x in range(width):
        c = complex(minX+x*(maxX-minX)/width, y*yScale/height-yScale/2)
        z = c
        for iter in range(ITERATION):
            if abs(z) > 2:
                break
            z = z*z+c
        if iter == ITERATION - 1:
            pixelcolor = 0
        else:
            pixelcolor = iter *5
        bitmap[x, y] = pixelcolor


# Loop forever so you can enjoy your image
while True:
    pass
