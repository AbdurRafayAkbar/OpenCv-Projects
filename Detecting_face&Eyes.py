import cv2

face_cascade=cv2.CascadeClassifier("F:\OPEN CV\Face_Detection\haarcascade_frontalface_default.xml")
eye_cascade=cv2.CascadeClassifier("Face_Detection\haarcascade_eye.xml")

cap=cv2.VideoCapture(0)

while True:
    ret, frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(gray,1.1,5)


    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame,"Face_detected",(x+w,y+h -50),cv2.FONT_HERSHEY_PLAIN,1,(1,31,142),1)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]
        eyes=eye_cascade.detectMultiScale(roi_gray,1.2,7)
        for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(frame,(x+ex,y+ey),(x + ex +ew, y + ey +eh -5),(0,0,211),1)
            cv2.putText(roi_color,"Eyes_detected",(ex + ew,ey +eh -50),cv2.FONT_HERSHEY_PLAIN,0.7,(121,212,23),1 )

        

    cv2.imshow("Face Detection",frame)

    if cv2.waitKey(1) & 0xFF==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
