#!/usr/bin/python3
# File name   : findline.py
# Description : line tracking 
# Website     : www.gewbot.com
# Author      : William
# Date        : 2019/08/28
import RPi.GPIO as GPIO
import time
import move

line_pin_right = 19
line_pin_middle = 16
line_pin_left = 20

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(line_pin_right,GPIO.IN)
    GPIO.setup(line_pin_middle,GPIO.IN)
    GPIO.setup(line_pin_left,GPIO.IN)


def run():
    status_right = GPIO.input(line_pin_right)
    status_middle = GPIO.input(line_pin_middle)
    status_left = GPIO.input(line_pin_left)

    if status_middle == 1:
        move.move(100, 'forward', 'no', 1)
    elif status_left == 1:
        move.move(100, 'forward', 'right', 0.6)
    elif status_right == 1:
        move.move(100, 'forward', 'left', 0.6)
    else:
        move.move(100, 'backward', 'no', 1)

if __name__ == '__main__':
    try:
        setup()
        move.setup()
        while 1:
            run()
        pass
    except KeyboardInterrupt:
        move.destroy()
