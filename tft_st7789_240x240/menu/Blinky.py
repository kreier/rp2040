# LED Blink T-Display rpi2040
# https://github.com/kreier/t-display/tree/main/circuitpython_rpi2040/menu

import time, board, digitalio

button_ok = digitalio.DigitalInOut(board.GP3)
button_ok.direction = digitalio.Direction.INPUT
button_ok.pull = digitalio.Pull.UP
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

timer = time.monotonic()
led.value = True
while True:
    if not button_ok.value:
        led.deinit()
        button_ok.deinit()
        exec(open("code.py").read())
    if timer + 1 < time.monotonic():
        led.value = not led.value
        timer = time.monotonic()
        print("LED", end=" ")
