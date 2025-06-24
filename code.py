#first project
#blinked leds

from adafruit_circuitplayground import cp
import time

while True:
    if cp.switch:
        cp.red_led= True
    else:
        cp.red_led= False
    if cp.button_a:
        cp.play_file("drum_cowbell.wav")
    if cp.button_b:
        cp.play_file("elec_hi_snare.wav")
    if cp.touch_A1:
        cp.pixels[1] = (0, 0, 255) #blue
    else:
        cp.pixels[1] = (0, 0, 0) #blue off
