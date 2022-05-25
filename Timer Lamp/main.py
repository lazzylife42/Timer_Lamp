from rotary import Rotary
import utime as time
from utime import sleep
import tm1637
from machine import Pin, Timer

val = 1
rotary = Rotary(0,1,2)
mydisplay = tm1637.TM1637(clk=Pin(16), dio=Pin(17))
led = Pin(15, Pin.OUT)
button = Pin(3, Pin.IN, Pin.PULL_DOWN)
start_blink = False

def blink(timer):
    led.toggle()

def rotary_changed(change):
    global val
    if change == Rotary.ROT_CW:
        val = val + 1
        print(val)
    elif change == Rotary.ROT_CCW:
        val = val - 1
        print(val)
    elif change == Rotary.SW_PRESS:
        print('PRESS')
    elif change == Rotary.SW_RELEASE:
        print('RELEASE')
        machine.reset()

rotary.add_handler(rotary_changed)

while True:
    mydisplay.number(val)
    time.sleep(0.1)
    if button.value():
        print("Button Press")
        start_blink = True
        time.sleep(0.5)
    elif val >= 60:
        val = 1
    elif val <= 0:
        val = 59
    elif start_blink == True:
        '''print("Start Blink")
        time.sleep(0.5)'''
        time.sleep(val/2)
        led.on()
        time.sleep(val/2)
        led.off()