#!/usr/bin/env python
import time

import cv2


def getTime():
    t = time.localtime()
    timestamp = str(t.tm_hour) + '_' + str(t.tm_min) + '_' + str(t.tm_sec)
    return timestamp


def captureImage():
    #capture from camera at location 0
    capture = cv2.VideoCapture(0)
    #set the width and height
    capture.set(3, 352)
    capture.set(4, 288)
    #capture.set(7, 1)
    capture.set(10, 0.01)
    #capture.set(15, 0.15)
    time.sleep(1)

    ret, img = capture.read()
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    #cv2.rectangle(self.img_gray, (0,65),(350,150), (192, 192, 192), 2, 8, 0)
    #self.ret,self.thresh = cv2.threshold(self.img_gray, 88, 255, 2)
    ret, thresh = cv2.threshold(img_gray, 65, 255, 0)
    thresh = cv2.bitwise_not(thresh)
    #cv2.rectangle(thresh, (5, 145), (320, 65),0)


    imagePath = 'capture/'
    imageIndex = imagePath + getTime() + '_capture'
    cv2.imwrite(imageIndex + '.png', thresh)
    #cv2.VideoCapture(0).release()


if __name__ == '__main__':
    while True:
        captureImage()
        time.sleep(10)
