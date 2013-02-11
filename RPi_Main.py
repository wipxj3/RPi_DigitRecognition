__author__ = 'dexter'
import RPi_Camera, RPi_Led

if __name__ == '__main__':
    while True:
        try:
            print 'Turning LED ON'
            RPi_Led.ledOn()

            print 'Starting capture...'
            capture = RPi_Camera.CaptureImage()
            image = capture.getImageIndex()
            print 'Saved as ' + image + '.png'

            print 'Turning LED OFF'
            RPi_Led.ledOff()
        except:
            print 'Capture device not available'