import cv2

def nothing(x): pass

image = cv2.imread("F:\OPEN CV\Shape_Detection\images\All_images.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.namedWindow("Trackbar")
cv2.createTrackbar("Thresh", "Trackbar", 0, 255, nothing)

while True:
    thresh_val = cv2.getTrackbarPos("Thresh", "Trackbar")
    _, thresh = cv2.threshold(gray, thresh_val, 255, cv2.THRESH_BINARY_INV)
    
    cv2.imshow("Trackbar", thresh)
    
    if cv2.waitKey(1) & 0xFF == 27:  # press ESC to exit
        break

cv2.destroyAllWindows()
