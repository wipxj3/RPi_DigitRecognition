__author__ = 'dexter'
import RPi_Camera
#import RPi_Led
import time


def rpiCapture():
    #print 'Turning LED ON'
    #led = RPi_Led.Led()

    print 'Starting capture...'
    capture = RPi_Camera.CaptureImage()
    image = capture.getImageIndex()
    print 'Saved as ' + image + '.png'
    #print 'Turning LED OFF'
    #led.ledOff()
    return 1


if __name__ == '__main__':
    while True:
        try:
            rpiCapture()
        except Exception:
            pass
        time.sleep(10)