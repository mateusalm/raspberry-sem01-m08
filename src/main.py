from machine import Pin
from utime import sleep

led = Pin(1, Pin.OUT)
btn = Pin(6, Pin.IN, Pin.PULL_UP)

light = False

while True:
    print(btn.value())
    if btn.value() == 0:
        light = not light
    if light:
        led.on()
    else:
        led.off()
    sleep(0.5)

