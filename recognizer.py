import cv2, numpy as np;
import xlwrite

import time
import sys

start=time.time()
period=8

cap = cv2.VideoCapture(0);
recognizer = cv2.face.LBPHFaceRecognizer_create();
face_cas = cv2.CascadeClassifier('haarcascade_eye.xml')
recognizer.read('trainer.yml');
flag = 0;
id_=0;
filename='filename';
dict_ = {
            'item1': 1,
            
                      
}
#font = cv2.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 5, 1, 0, 1, 1)
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, img = cap.read();
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
    faces = face_cas.detectMultiScale(gray, 1.3, 7);
    print(faces)
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2);
        id_,conf=recognizer.predict(roi_gray)
        print(id_,conf)
        if(conf > 100):
         if(id_==1):
            id_='Neeraj Singh'
            if((str(id_)) not in dict_):
                print("Neeraj")
                filename=xlwrite.output('Attendance','class1',1,id_,'yes');
                dict_[str(id_)]=str(id_);
                
         elif(id_==2):
            id_ = 'Milind Monam'
            if ((str(id_)) not in dict_):
                filename =xlwrite.output('Attendance', 'class1', 2, id_, 'yes');
                dict_[str(id_)] = str(id_);

         elif(id_==3):
            id_ = 'Mukesh Goyal'
            if ((str(id_)) not in dict_):
                filename =xlwrite.output('Attendance', 'class1', 3, id_, 'yes');
                dict_[str(id_)] = str(id_);

         elif(id_==4):
            id_ = 'Unknown'
            if ((str(id_)) not in dict_):
                filename =xlwrite.output('Attendance', 'class1', 4, id_, 'yes');
                dict_[str(id_)] = str(id_);

        else:
             id = 'Unknown, can not recognize'
             flag=flag+1
             break
        
        cv2.putText(img,str(id_)+" "+str(conf),(x,y-10),font,0.55,(120,255,120),1)
        #cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,(0,0,255));
    cv2.imshow('frame',img);
    #cv2.imshow('gray',gray);
    if flag == 10:
        
        print("Transaction Blocked")
        break;
    if time.time()>start+period:
        break;
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break;

cap.release();
cv2.destroyAllWindows();
