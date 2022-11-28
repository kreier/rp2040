import time
import board
import digitalio
from adafruit_debouncer import Debouncer

long_press = 0.1

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
key = digitalio.DigitalInOut(board.A0)    # boot switch - choose and select
key.direction = digitalio.Direction.INPUT
key.pull = digitalio.Pull.UP
button = Debouncer(key, interval=0.05)

while True:
    button.update()
    if button.fell:
        pressed = time.monotonic()
    if button.rose:    # button released
        time_pressed = time.monotonic() - pressed
        if time_pressed > long_press:
            led.value =  not led.value
            if led.value:
                print("LED off")
            else:
                print("LED on")
