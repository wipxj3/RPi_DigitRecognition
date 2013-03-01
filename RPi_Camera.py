#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'dexter'
import time
import re

import final_data

# OpenCV 2.4.3 (armf-compile) python bindings
import cv2
# Module for interaction with external modules
import subprocess
# Imaging library to perform editions over images
from PIL import Image


def getTime():  # Function that returns a Timestamp %H_%M_%S
    t = time.localtime()
    timestamp = str(t.tm_hour) + '_' + str(t.tm_min) + '_' + str(t.tm_sec)
    return timestamp


def captureImage():  # Function for capturing GRAY image and threshold transformation
    #capture from camera at location 0
    capture = cv2.VideoCapture(0)
    #set the width,height, gain
    capture.set(3, 352)
    capture.set(4, 288)
    capture.set(10, 0.5)
    time.sleep(1)
    ret, img = capture.read()
    # RGB -> GRAY color filter
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # Applying threshold
    ret, thresh = cv2.threshold(img_gray, 65, 255, 0)
    # Bit-wise matrix NOT transformation
    thresh = cv2.bitwise_not(thresh)
    # Saving the resulting image to PNG, in /capture/
    imagePath = 'capture/'
    imageIndex = imagePath + getTime() + '_capture'
    cv2.imwrite(imageIndex + '.png', thresh)
    return imageIndex


def cropImage(imageIndex):  # Function to crop the original image, desired area saved to /capture/crop
    im = Image.open(imageIndex + '.png')
    newIndex = 'capture/crop/cropped_' + getTime() + '.png'
    box = (0, 138, 350, 189)
    cropped = im.crop(box)
    cropped.save(newIndex, format='PNG')
    return newIndex


def cleanImage(imageIndex):  # Function to clean the blanks between digits, result stored in /capture/clean
    im = Image.open(imageIndex)
    newIndex = 'capture/clean/cleaned_' + getTime() + '.png'
    boxes = [(30, 0, 60, 51), (95, 0, 125, 51), (160, 0, 190, 51), (220, 0, 256, 51), (290, 0, 323, 51)]
    for box in boxes:
        im.paste('white', box)
    im.save(newIndex, format='PNG')
    return newIndex


def recognizeData(imageIndex):  # Function to recognize data from each captured file, .TXT results /capture/clean
    dataFile = 'capture/clean/output_' + getTime()
    subprocess.call(['tesseract', imageIndex, dataFile, 'digits']) # alternative to 'digits' -> '-l eng', '-psm 7'
    return dataFile


def readTxt(fileIndex):  # Each recognized data added to a check list
    f = open(fileIndex + '.txt', 'r')
    #Read whole file into data
    data = f.read()
    f.close()
    return data


if __name__ == '__main__':
    dataList = []
    numberList = []
    CHECK_RE = re.compile('[0-9]')
    temp = None
    Sum = 0
    while True:
        data = readTxt(recognizeData(cleanImage(cropImage(captureImage()))))
        value = data.split('\n', 1)
        print value[0]
        if (len(value[0]) == 6) and (CHECK_RE.match(value[0])):
        # Adding data to data list
            dataList.append(value[0])
            try:
                number = int(value[0])
            except:
                print 'STR to INT error'
            if temp is None:
                temp = number
                print temp
                #if (number <= temp + 1) or (number >= temp - 1) or (number == temp):
            numberList.append(number)
        print dataList
        print numberList
        if len(numberList) >= 5:
            break
        time.sleep(7)
    final_data.Values.append(numberList)
    for value in numberList:
        Sum = Sum + value
    mean = Sum / len(numberList)
    final_data.Means.append(mean)
