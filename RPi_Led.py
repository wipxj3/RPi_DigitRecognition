#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'dexter'

import RPi.GPIO as GPIO
import time
import threading


GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)


class Led:
    def __init__(self):
        GPIO.output(8, False) # LED OFF
        time.sleep(1)
        GPIO.output(8, True) # LED ON

    def ledOff(self):
        GPIO.output(8, True)
        time.sleep(1)
        GPIO.output(8, False)
        time.sleep(1)
        return 1


'''
if __name__ == '__main__':
    print 'Turning LED ON'
    ledOn()
    print 'Turning LED OFF'
    ledOff()
'''