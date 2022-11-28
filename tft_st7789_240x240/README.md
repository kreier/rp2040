# Waveshare st7789 1.3" 240x240 TFT display

Link to the product: https://www.waveshare.com/wiki/Pico-LCD-1.3

Let's replicate the pin A and B on GPIO15 and GPIO17

| TFT   | Pico | Description                                               |
|-------|------|-----------------------------------------------------------|
| VCC   | VSYS | Power Input                                               |
| GND   | GND  | GND                                                       |
| DIN   | GP11 | MOSI pin of SPI, slave device data input                  |
| CLK   | GP10 | SCK pin of SPI, clock pin                                 |
| CS    | GP9  | Chip selection of SPI, low active                         |
| DC    | GP8  | Data/Command control pin (High for data; Low for command) |
| RST   | GP12 | Reset pin, low active                                     |
| BL    | GP13 | Backlight control                                         |
| A     | GP15 | User button A                                             |
| B     | GP17 | User button B                                             |
| X     | GP19 | User button X                                             |
| Y     | GP21 | User buttonY                                              |
| UP    | GP2  | Joystick-up                                               |
| DOWM  | GP18 | Joystick-down                                             |
| LEFT  | GP16 | Joystick-left                                             |
| RIGHT | GP20 | Joystick-right                                            |
| CTRL  | GP3  | Joystick-center                                           |

Pins for oled:
i2c GP0 and GP1

Pins for TFT
