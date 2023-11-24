import time
import board
import busio
import terminalio
import displayio
import digitalio
from adafruit_display_text import label
from adafruit_st7789 import ST7789

print("Setup done.")

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    print('LED on')
    time.sleep(1)
    led.value = False
    print('LED off')
    time.sleep(1)
    pass

# Release any resources currently in use for the displays
displayio.release_displays()

tft_dc    = board.LCD_DC
tft_cs    = board.LCD_CS
spi_clk   = board.LCD_CLK
spi_mosi  = board.LCD_MOSI
tft_rst   = board.LCD_RESET
backlight = board.LCD_BACKLIGHT
spi = busio.SPI(spi_clk, spi_mosi)

display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_rst)

display = ST7789(
    display_bus,
    rotation=270,
    width=240,
    height=135,
    rowstart=40,
    colstart=54,
    backlight_pin=backlight,
)

# Make the display context
splash = displayio.Group()
display.show(splash)

color_bitmap = displayio.Bitmap(240, 135, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x00FF00  # Bright Green

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(200, 95, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0xAA0088  # Purple
inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=20, y=20)
splash.append(inner_sprite)

# Draw a label
text_group = displayio.Group(scale=2, x=50, y=60)
text = "Hello World!"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00)
text_group.append(text_area)  # Subgroup for text scaling
splash.append(text_group)

print("Setup done.")

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    print('LED on')
    time.sleep(1)
    led.value = False
    print('LED off')
    time.sleep(1)
    pass
