#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'dexter'

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)


def ledOn():
    GPIO.output(8, False) # LED OFF
    time.sleep(1)
    GPIO.output(8, True) # LED ON
    return 1

def ledOff():
    GPIO.output(8, True) # LED OFF
    time.sleep(1)
    GPIO.output(8, False) # LED ON
    return 1
'''
if __name__ == '__main__':
    print 'Turning LED ON'
    ledOn()
    print 'Turning LED OFF'
    ledOff()
'''