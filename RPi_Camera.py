#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'dexter'

import cv2
import time


class CaptureImage():
    def __init__(self):
        #capture from camera at location 0
        capture = cv2.VideoCapture(0)
        #set the width and height
        capture.set(3, 352)
        capture.set(4, 288)

        self.ret, self.img = capture.read()
        time.sleep(2)
        self.imagePath = 'capture/'
        self.imageIndex = self.imagePath + self.getTime() + '_capture'
        #cv2.cv.SaveImage(self.imageIndex + '.png', self.img)
        cv2.imwrite(self.imageIndex + '.png', self.img)
        cv2.VideoCapture(0).release()

    def getImageIndex(self):
        return self.imageIndex

    def getTime(self):
        t = time.localtime()
        timestamp = str(t.tm_hour) + '_' + str(t.tm_min) + '_' + str(t.tm_sec)
        return timestamp


'''
if __name__ == '__main__':
    capture = CaptureImage()
    image = capture.getImageIndex()
    print 'Saved as ' + image
'''