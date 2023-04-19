# importing all necessary library
import cv2
import os
from cvzone.HandTrackingModule import HandDetector
import numpy as np
from math import ceil
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet import preprocess_input
import numpy as np

# get video capture object (moreover the camera)
cap = cv2.VideoCapture(0)
# Initialize hand ditector, ditect maximum one hand
hand_ditector = HandDetector(maxHands=1)
# this offset is nothing but margin in bounding box
offset = 20
# loading ASL ditection model
model = load_model("model_2.h5")
# labels of ASL actually list of Alphabets
labels = [chr(i) for i in range(ord("A"),ord("Z")+1)]
# turning on a infinity loop to continuously capturing image from camera
while True:
    # capture image from camera returns two thing first one is boolean variable and second one is image
    success,img = cap.read()
    # Ditect hand from video
    hands = hand_ditector.findHands(img,draw=False)
    if hands: # if hand ditected
        hand = hands[0] # get first hand from hands list
        x,y,w,h = hand["bbox"] # get location (x,y) and width , height (w,h) of bounding box of hand
        # defining crop position
        py1,py2,px1,px2 = y-offset,y+h+offset,x-offset,x+w+offset
        # recalculate position in case of negative value
        py1 = 0 if py1<0 else py1
        px1 = 0 if px1<0 else px1
        # croped frame of ony hand
        croped_frame = img[py1:py2,px1:px2]
        # making a white screen
        white_screen = np.ones((300,300,3),np.uint8)*255
        # positioning croped frame into white screen
        hand_ratio = w/h
        if hand_ratio > 1:
            wcal = ceil(300/hand_ratio)
            croped_frame = cv2.resize(croped_frame,(300,wcal))
            gap = ceil((300-wcal)/2)
            white_screen[0+gap:wcal+gap,0:300] = croped_frame
        else:
            hcal = ceil(300*hand_ratio)
            croped_frame = cv2.resize(croped_frame,(hcal,300))
            gap = ceil((300-hcal)/2)
            white_screen[0:300,0+gap:hcal+gap] = croped_frame
        # processing image for model input
        xs = np.expand_dims(white_screen, axis=0)
        xs = preprocess_input(xs)
        # prediction from image
        predictions = model.predict(xs)
        # get alphabet from predictions
        prediction = labels[np.argmax(predictions[0],axis=0)]
        # styling bounding of prediction
        cv2.rectangle(img,(x-offset,y-offset),(x+w,y+h),(0,225,0),4)
        cv2.rectangle(img,(x-offset-2,y-offset-40),(x+50,y-offset),(0,225,0),cv2.FILLED)
        cv2.putText(img,prediction,(x,y-offset-10),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),2)
        # # show the croped frame
        # cv2.imshow("Croped frame",white_screen)
    interrupt = cv2.waitKey(10)
    # if press q from keyboard then exit the loop (stops program)
    if interrupt and 0xFF==ord("q"):
        break
    # show video and predictions
    cv2.imshow("Americal Sign Language Ditection",img)