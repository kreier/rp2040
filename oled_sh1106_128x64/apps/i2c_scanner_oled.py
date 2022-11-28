# SPDX-FileCopyrightText: 2017 Limor Fried for Adafruit Industries
# SPDX-License-Identifier: MIT
# https://github.com/kreier/rp2040/blob/main/circuitpython/apps/i2c_scanner.py

import time, board, busio, displayio
import adafruit_displayio_sh1106

displayio.release_displays()

i2c = busio.I2C(board.GP1, board.GP0) # SCL SDA
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_sh1106.SH1106(display_bus, width=128, height=64, colstart=2)


#i2c = busio.I2C(board.GP1, board.GP0)    # Pi Pico RP2040

print("i2c detection range 0x00-0x7F")
print("      0 1 2 3 4 5 6 7 8 9 A B C D E F")

while not i2c.try_lock():
    pass

try:
    devices = i2c.scan()

finally:  # unlock the i2c bus when ctrl-c'ing out of the loop
    i2c.unlock()

devices.append(0)
device = 0
for row in range(0, 127, 16):
    print(f"0x{row:02x}", end=":")
    for col in range(16):
        if devices[device] == (row + col):
            print(hex(row+col)[2:], end="")
            device += 1
        else:
            print(" -", end="")
    print(" ")

while True:
    pass
