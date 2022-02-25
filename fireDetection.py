import numpy as np
import cv2
import serial
import time


fire_cascade = cv2.CascadeClassifier('cascade.xml')


ser1 = serial.Serial('COM3',9600)

cap = cv2.VideoCapture(0)
while 1:
    ser1.write(str.encode('0'))
    ret, img = cap.read()
    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    fire = fire_cascade.detectMultiScale(img, 1.2, 5)
    for (x,y,w,h) in fire:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        print('Fire is detected..!')
        ser1.write(str.encode('p'))
        time.sleep(0.2)
        
    cv2.imshow('img',img)
    ser1.write(str.encode('s'))
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
