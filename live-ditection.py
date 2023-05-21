# importing all necessary library
import cv2
import os
from cvzone.HandTrackingModule import HandDetector
import numpy as np
from math import ceil
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet import preprocess_input
import numpy as np

# # Initialize hand ditector, ditect maximum one hand
hand_ditector = HandDetector(maxHands=1)
# get video capture object (moreover the camera)
cap = cv2.VideoCapture(0)
# this offset is nothing but margin in bounding box
offset = 10
# loading ASL ditection model
model = load_model("model_v2_gray2.h5")
# labels of ASL actually list of Alphabets
labels = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
# turning on a infinity loop to continuously capturing image from camera
while True:
    # capture image from camera returns two thing first one is boolean variable and second one is image
    success, img = cap.read()
    # Ditect hand from video
    hands = hand_ditector.findHands(img=img, draw=False)
    if hands:  # if hand ditected
        hand = hands[0]  # get first hand from hands list
        x, y, w, h = hand[
            "bbox"
        ]  # get location (x,y) and width , height (w,h) of bounding box of hand
        # defining crop position
        py1, py2, px1, px2 = y - offset, y + h + offset, x - offset, x + w + offset
        #     # recalculate position in case of negative value
        py1 = 0 if py1 < 0 else py1
        px1 = 0 if px1 < 0 else px1
        # croped frame of ony hand
        croped_frame = img[py1:py2, px1:px2]
        croped_frame = cv2.resize(croped_frame, (224, 224))
        croped_frame = cv2.cvtColor(croped_frame, cv2.COLOR_BGR2GRAY)
        # Merge the grayscale image with the original image's RGB channels
        croped_frame = cv2.cvtColor(croped_frame, cv2.COLOR_GRAY2BGR)
        cv2.imshow("Hand", croped_frame)
        # processing image for model input
        xs = np.expand_dims(croped_frame, axis=0)
        xs = preprocess_input(xs)
        # prediction from image
        predictions = model.predict(xs)
        index = np.argmax(predictions)
        # get alphabet from predictions
        prediction = labels[index]
        # styling bounding of prediction
        cv2.rectangle(img, (x - offset, y - offset), (x + w, y + h), (0, 225, 0), 4)
        cv2.rectangle(
            img,
            (x - offset - 2, y - offset - 40),
            (x + 50, y - offset),
            (0, 225, 0),
            cv2.FILLED,
        )
        cv2.putText(
            img,
            prediction,
            (x, y - offset - 10),
            cv2.FONT_HERSHEY_PLAIN,
            2,
            (255, 255, 255),
            2,
        )

    interrupt = cv2.waitKey(10)
    # if press q from keyboard then exit the loop (stops program)
    if interrupt and 0xFF == ord("q"):
        break
    # show video and predictions
    cv2.imshow("Americal Sign Language Ditection", img)
