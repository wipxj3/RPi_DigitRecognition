RPi_DigitRecognition
====================

Digit Recognition project based on Raspberry Pi

Requirments
-----------

* Python 2.7.x
* Tesseract-OCR - http://code.google.com/p/tesseract-ocr/wiki/ReadMe
* OpenCV 2.4.3 - http://mitchtech.net/raspberry-pi-opencv/
* Pillow (Imaging Library) - https://pypi.python.org/pypi/Pillow/

of course Raspberry Pi with Debian or Raspbian latest updates.

Usage
-----

* Download / Clone / Unpack
* Create dirs:
  - ~mkdir capture
  - ~touch data.txt
  - ~cd capture
  - ~mkdir crop
  - ~mkdir clean
* Run : ./capture.sh

Additional info
---------------

Changind sleep value in <b>camera.sh</b> you can manipulate with script running intervals in seconds.

Main functionalities
--------------------

* captureImage() - captures and image (352x288) with light gain value (0.1 .. 1)(Note: GAIN support by device)
  - Captured image coverted to GRAY, threshhold applied, inverted and saved to <b>/caputre/TIMESTAMP_capture.png</b>;
* cropImage() - crops captured image with a specified box and saves to <b>/caputre/crop/cropped_TIMESTAMP.png</b>;
* cleanImage() - cleans black spaces between digits and saves to <b>/caputre/clean/cleaned_TIMESTAMP.png</b> 
(Note: use if needed);
* recognizeData() - recognizes data from each cleaned file, *.TXT results in <b>/capture/clean/output_TIMESTAMP.txt</b>
* Several verification steps: 
  - if valid string recognized -> added to dataList -> converted to INT -> added to numberList;
  - if 10 not valid attempts -> break execution;
  - if numberList not EMPTY -> mean value computed and checked with previous result;
  - if mean value exists -> sent to TELECONTROL SERVER.
* Cleaning opperations performed, to clean <b>/capture/</b> folder.
