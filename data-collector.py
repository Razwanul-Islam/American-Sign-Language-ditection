# importing all necessary library
import cv2
import os
from cvzone.HandTrackingModule import HandDetector
import numpy as np
from math import ceil
# get video capture object (moreover the camera)
cap = cv2.VideoCapture(0)
# Initialize hand ditector, ditect maximum one hand
hand_ditector = HandDetector(maxHands=1)
# this offset is nothing but margin in bounding box
offset = 20
# directory of saved data
directory='dataset_2/train/'
# A infinity loop to continiously capture image and process
while True:
    # capture image from camera returns two thing first one is boolean variable and second one is image
    success,img = cap.read()
    # count image on each directory
    count = {
             'a': len(os.listdir(directory+"/A")),
             'b': len(os.listdir(directory+"/B")),
             'c': len(os.listdir(directory+"/C")),
             'd': len(os.listdir(directory+"/D")),
             'e': len(os.listdir(directory+"/E")),
             'f': len(os.listdir(directory+"/F")),
             'g': len(os.listdir(directory+"/G")),
             'h': len(os.listdir(directory+"/H")),
             'i': len(os.listdir(directory+"/I")),
             'j': len(os.listdir(directory+"/J")),
             'k': len(os.listdir(directory+"/K")),
             'l': len(os.listdir(directory+"/L")),
             'm': len(os.listdir(directory+"/M")),
             'n': len(os.listdir(directory+"/N")),
             'o': len(os.listdir(directory+"/O")),
             'p': len(os.listdir(directory+"/P")),
             'q': len(os.listdir(directory+"/Q")),
             'r': len(os.listdir(directory+"/R")),
             's': len(os.listdir(directory+"/S")),
             't': len(os.listdir(directory+"/T")),
             'u': len(os.listdir(directory+"/U")),
             'v': len(os.listdir(directory+"/V")),
             'w': len(os.listdir(directory+"/W")),
             'x': len(os.listdir(directory+"/X")),
             'y': len(os.listdir(directory+"/Y")),
             'z': len(os.listdir(directory+"/Z"))
             }
    # track count of image by putting text on the frame
    cv2.putText(img, "a : "+str(count['a']), (10, 100), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(img, "b : "+str(count['b']), (10, 110), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(img, "c : "+str(count['c']), (10, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(img, "d : "+str(count['d']), (10, 130), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(img, "e : "+str(count['e']), (10, 140), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(img, "f : "+str(count['f']), (10, 150), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(img, "g : "+str(count['g']), (10, 160), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(img, "h : "+str(count['h']), (10, 170), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(img, "i : "+str(count['i']), (10, 180), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(img, "i : "+str(count['j']), (40, 180), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(img, "k : "+str(count['k']), (10, 190), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(img, "l : "+str(count['l']), (10, 200), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(img, "m : "+str(count['m']), (10, 210), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(img, "n : "+str(count['n']), (10, 220), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(img, "o : "+str(count['o']), (10, 230), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(img, "p : "+str(count['p']), (10, 240), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(img, "q : "+str(count['q']), (10, 250), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(img, "r : "+str(count['r']), (10, 260), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(img, "s : "+str(count['s']), (10, 270), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(img, "t : "+str(count['t']), (10, 280), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(img, "u : "+str(count['u']), (10, 290), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(img, "v : "+str(count['v']), (10, 300), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(img, "w : "+str(count['w']), (10, 310), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(img, "x : "+str(count['x']), (10, 320), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(img, "y : "+str(count['y']), (10, 330), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(img, "z : "+str(count['z']), (10, 340), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # Ditect hand from video
    hands = hand_ditector.findHands(img,draw= False)
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
        # positioning croped frame into white screen for a fixed size image of (300,300)
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
        # show fixed size image (300,300) of only hand
        cv2.imshow("Croped frame",white_screen)
        # wait 10ms to get key pressed event from keyboard
        interrupt = cv2.waitKey(10)
        # when a key pressed save current whiteframe(fixed size hand gesture image
        # ) to defined related path
        if interrupt & 0xFF == ord('a'):
            cv2.imwrite(directory+'A/'+str(count['a'])+'.png',white_screen)
        if interrupt & 0xFF == ord('b'):
            cv2.imwrite(directory+'B/'+str(count['b'])+'.png',white_screen)
        if interrupt & 0xFF == ord('c'):
            cv2.imwrite(directory+'C/'+str(count['c'])+'.png',white_screen)
        if interrupt & 0xFF == ord('d'):
            cv2.imwrite(directory+'D/'+str(count['d'])+'.png',white_screen)
        if interrupt & 0xFF == ord('e'):
            cv2.imwrite(directory+'E/'+str(count['e'])+'.png',white_screen)
        if interrupt & 0xFF == ord('f'):
            cv2.imwrite(directory+'F/'+str(count['f'])+'.png',white_screen)
        if interrupt & 0xFF == ord('g'):
            cv2.imwrite(directory+'G/'+str(count['g'])+'.png',white_screen)
        if interrupt & 0xFF == ord('h'):
            cv2.imwrite(directory+'H/'+str(count['h'])+'.png',white_screen)
        if interrupt & 0xFF == ord('i'):
            cv2.imwrite(directory+'I/'+str(count['i'])+'.png',white_screen)
        if interrupt & 0xFF == ord('j'):
            cv2.imwrite(directory+'J/'+str(count['j'])+'.png',white_screen)
        if interrupt & 0xFF == ord('k'):
            cv2.imwrite(directory+'K/'+str(count['k'])+'.png',white_screen)
        if interrupt & 0xFF == ord('l'):
            cv2.imwrite(directory+'L/'+str(count['l'])+'.png',white_screen)
        if interrupt & 0xFF == ord('m'):
            cv2.imwrite(directory+'M/'+str(count['m'])+'.png',white_screen)
        if interrupt & 0xFF == ord('n'):
            cv2.imwrite(directory+'N/'+str(count['n'])+'.png',white_screen)
        if interrupt & 0xFF == ord('o'):
            cv2.imwrite(directory+'O/'+str(count['o'])+'.png',white_screen)
        if interrupt & 0xFF == ord('p'):
            cv2.imwrite(directory+'P/'+str(count['p'])+'.png',white_screen)
        if interrupt & 0xFF == ord('q'):
            cv2.imwrite(directory+'Q/'+str(count['q'])+'.png',white_screen)
        if interrupt & 0xFF == ord('r'):
            cv2.imwrite(directory+'R/'+str(count['r'])+'.png',white_screen)
        if interrupt & 0xFF == ord('s'):
            cv2.imwrite(directory+'S/'+str(count['s'])+'.png',white_screen)
        if interrupt & 0xFF == ord('t'):
            cv2.imwrite(directory+'T/'+str(count['t'])+'.png',white_screen)
        if interrupt & 0xFF == ord('u'):
            cv2.imwrite(directory+'U/'+str(count['u'])+'.png',white_screen)
        if interrupt & 0xFF == ord('v'):
            cv2.imwrite(directory+'V/'+str(count['v'])+'.png',white_screen)
        if interrupt & 0xFF == ord('w'):
            cv2.imwrite(directory+'W/'+str(count['w'])+'.png',white_screen)
        if interrupt & 0xFF == ord('x'):
            cv2.imwrite(directory+'X/'+str(count['x'])+'.png',white_screen)
        if interrupt & 0xFF == ord('y'):
            cv2.imwrite(directory+'Y/'+str(count['y'])+'.png',white_screen)
        if interrupt & 0xFF == ord('z'):
            cv2.imwrite(directory+'Z/'+str(count['z'])+'.png',white_screen)
    # show main frame
    cv2.imshow("Hand Ditector",img)