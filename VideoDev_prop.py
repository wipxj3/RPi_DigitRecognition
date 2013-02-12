import cv2

capture = cv2.VideoCapture(0)
prop=[]
for i in range(0,19):
    prop.append(capture.get(i))
print prop