#!/usr/bin/env python3
########################################################################
# Filename    : BreathingLED.py
# Description : Breathing LED
# Author      : www.freenove.com
# modification: 2024/07/29
########################################################################
from gpiozero import PWMLED
import time

led = PWMLED(17 ,initial_value=0 ,frequency=1000)
def loop():
    while True:
        for b in range(0, 101, 20):    # make the led brighter in steps of 10
            led.value = b / 100.0      # set dc value as the duty cycle
            time.sleep(1)              # stay at each level for 1 second
        for b in range(100, -1, -20):  # make the led darker in steps of 10
            led.value = b / 100.0      # set dc value as the duty cycle
            time.sleep(1)              # stay at each level for 1 second
    
if __name__ == '__main__':     # Program entrance
    print ('Program is starting ... ')
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        print("Ending program")
    finally:
        led.close()
