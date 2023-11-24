import board
import busio
import displayio
from adafruit_st7789 import ST7789

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
    colstart=53,
    backlight_pin=backlight,
)
