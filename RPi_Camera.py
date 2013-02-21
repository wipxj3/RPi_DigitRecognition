#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'dexter'
import cv2
import time

class CaptureImage():
    def __init__(self):
        #capture from camera at location 0
        capture = cv2.VideoCapture(-1)
        #set the width and height
        capture.set(3, 352)
        capture.set(4, 288)

        self.ret, self.img = capture.read()
	self.img_gray = cv2.cvtColor(self.img, cv2.COLOR_RGB2GRAY)
	cv2.rectangle(self.img_gray, (0,65),(350,150), (192, 192, 192), 1, 8, 0)
	ret,thresh = cv2.threshold(imgray,127,255,0)
	time.sleep(1)
        self.imagePath = 'capture/'
        self.imageIndex = self.imagePath + self.getTime() + '_capture'
        #cv2.cv.SaveImage(self.imageIndex + '.png', self.img)
        cv2.imwrite(self.imageIndex + '.png', self.tocrop)
	cv2.VideoCapture(0).release()

    def getImageIndex(self):
        return self.imageIndex

    def getTime(self):
        t = time.localtime()
        timestamp = str(t.tm_hour) + '_' + str(t.tm_min) + '_' + str(t.tm_sec)
        return timestamp



if __name__ == '__main__':
    capture = CaptureImage()
    image = capture.getImageIndex()
    print 'Saved as ' + image
''''''
