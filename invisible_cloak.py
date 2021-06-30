import cv2
import numpy as np

cap = cv2.VideoCapture(0)
back = cv2.imread('./image.jpg')
kernel = np.ones((5,5), np.uint8)

while cap.isOpened():
    # take each frame
    ret, frame = cap.read()
    frame  == cv2.flip(frame , 1)
    if ret:
        # how do we convert rgb to hsv?
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # cv2.imshow("hsv", hsv)
        # how to get hsv value?
        # lower: hue - 10, 100, 100, higher: h+10, 255, 255
        red = np.uint8([[[0,0,255]]]) # bgr value of red
        hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
        # get hsv value of red from bgr
        # print(hsv_red)

        # threshold the hsv value to get only red colors
        l_red = np.array([0, 100, 100])
        u_red = np.array([10, 255, 255])

        mask = cv2.inRange(hsv, l_red, u_red)
        # cv2.imshow("mask", mask)

        # all things red
        part1 = cv2.bitwise_and(back, back, mask=mask)
        # cv2.imshow("part1", part1)

        mask = cv2.bitwise_not(mask)

        # part 2 is all things not red
        part2 = cv2.bitwise_and(frame, frame, mask=mask)
        # cv2.imshow("mask", part2)

        cv2.imshow("cloak", part1 + part2)

        img_erosion = cv2.erode(part1 + part2, kernel, iterations=1) 
        img_dilation = cv2.dilate(part1 + part2, kernel, iterations=1)
        img_opening = cv2.morphologyEx(part1 + part2, cv2.MORPH_OPEN, kernel)
        img_closing = cv2.morphologyEx(part1+part2, cv2.MORPH_CLOSE, kernel)

        #cv2.imshow('Input', back) 
        #cv2.imshow('Dilation', img_dilation) 
        #v2.imshow('Erosion', img_erosion)
        #cv2.imshow('mg_opening', img_opening)
        #cv2.imshow('img_closing', img_closing)
        if cv2.waitKey(5) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()        