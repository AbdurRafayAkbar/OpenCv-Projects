import cv2

image=cv2.imread("Shape_Detection\images\All_images.png")

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

_,thresh=cv2.threshold(gray,235,255,cv2.THRESH_BINARY_INV)

contors,heirarchy=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

for cont in contors:
    approx= cv2.approxPolyDP(cont,0.03*cv2.arcLength(cont,True),True)

    corners=len(approx)

    if corners==3:
        shape_name="Triangle"
    elif corners==4:
        shape_name="Square"
    elif corners>4:
        shape_name="Circle"
    else:
        shape_name="Unknown"
    cv2.drawContours(image,approx,-1,(0,255,255),2)
    x=approx.ravel()[0]
    y=approx.ravel()[1] -10
    cv2.putText(image,shape_name,(x,y),cv2.FONT_HERSHEY_COMPLEX,0.6,(255,0,255),1)
cv2.imshow("contours",image)
cv2.waitKey(0)
cv2.destroyAllWindows()