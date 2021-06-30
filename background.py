import cv2

#This is for Webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, back = cap.read() #ret tell about is working => True else => False
    if ret:
        cv2.imshow("Image", back)    #Output Screen waht back is reading
        if(cv2.waitKey(2) == ord('q')):
            #Save the Image
            cv2.imwrite('image.jpg',back)
            break

cap.release()
cap.destroyAllWindows()
