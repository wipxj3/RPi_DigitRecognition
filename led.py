#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
def main():
	GPIO.setup(7, GPIO.OUT) 
	while True:
		GPIO.output(7, False) # LED OFF    
		time.sleep(1)    
		GPIO.output(7, True) # LED ON
		time.sleep(1)
	return 0

if __name__ == '__main__':
	main()

