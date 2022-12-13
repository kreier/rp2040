# rp2040
Example programs in CircuitPython for the Raspberry Pico 2040. We use it with 3 different external displays as more detailed optical output than just the led.

## 320x240 ili9341 3.2 inch tft

![ini9341](docs/ili9341.jpg)

[3.2 inch display at thegioiic.com](https://www.thegioiic.com/lcd-3-2inch-320x240-tft-ili9341-giao-tiep-spi-v2-0)

## 240x240 st7789 1.3 inch waveshare tft

![st7789](docs/st7789.jpg)

[1.3 tft display documentation at waveshare](https://www.waveshare.com/wiki/Pico-LCD-1.3)

## 128x64 sh1106 1.3 inch oled

![sh1106](docs/sh1106)

[1.3 inch oled at thegioiic.com](https://www.thegioiic.com/lcd-oled-1-3inch-128x64-chu-xanh-duong-4-chan-giao-tiep-iic)

## 128x32 ssd1306 oled adafruit

![adafruit oled](docs/ssh1306)

[Adafruit documentation circuitpython]()

# rp2040 and i2c sensors

We would like to just solder a 4-pin JST XH 2.54 mm pitch (0.1 ") connector to any of these boards and then use a standard XH-4 cable to connect to our ssis:bit without worrying about polarity or correct pin order:

![connector](docs/i2c_connector.jpg)

The order of pins in the 1mm QUIIC connector is different from the order of the 4 pins found in virtually every hobby board with 2.54mm pins:

![sensors](docs/i2c_order.jpg)

Hopefully we soon have a little shelf with all these different sensors for 'plug and play' and a software library on our boards.