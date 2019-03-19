import cv2
import numpy as np
import math
import matplotlib as plt
import time

#vid = cv2.VideoCapture('testp.mp4')
cap = cv2.VideoCapture(0)
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))
past_frame = []
while True:
    #time.sleep(0.3)
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cv2.circle(gray, (100,63), 100, (255, 255,255), -1)
    try:
        delta = cv2.subtract(past_frame, gray)
    except:
        delta = gray
    past_frame = gray
    cv2.imshow('gray', delta)
    #out.write(frame)
    art = np.asarray(delta)
    total = 0
    #xrange = len(art)
    #yrange = len(art[1])
    #vol = xrange*yrange
    #for i in range(0, xrange):
        #for j in range(0, yrange):
            #total += art[i][j]
    #avg = (total/vol)
    avg = np.average(art)
    if (avg > 0.5):
        print(avg, "motion detected")
    #else:
        #print(avg, "nothing")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
#out.release()
cap.destroyAllWindows()
