import cv2
import mediapipe as mp
import math 
import numpy as np


def findAngle(img,p1,p2,p3,lmlist,draw= True):
    
    
    x1, y1 = lmlist[p1][1:]
    x2, y2 = lmlist[p2][1:]
    x3, y3 = lmlist[p3][1:]
    
    angle = math.degrees(math.atan2(y3-y2,x3-x2)  - (math.atan2(y1-y2,x1-x2)))  
    
    if angle < 0 : 
        
        angle+=360
    
    if draw==True :
        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),3)
        cv2.line(img,(x3,y3),(x2,y2),(0,0,255),3)
        cv2.circle(img, (x1,y1), 10, (0,255,255),cv2.FILLED)
        cv2.circle(img, (x2,y2), 10, (0,255,255),cv2.FILLED)
        cv2.circle(img, (x3,y3), 10, (0,255,255),cv2.FILLED)
        
        cv2.circle(img, (x1,y1), 15, (0,255,255))
        cv2.circle(img, (x2,y2), 15, (0,255,255))
        cv2.circle(img, (x3,y3), 15, (0,255,255))
        
        cv2.putText(img, str(int(angle)), (x2-40,y2+40), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,255),2)
        
        return angle
video_path = "video1.mp4"

cap = cv2.VideoCapture(video_path)

mpPose = mp.solutions.pose

pose=mpPose.Pose()

mpDraw = mp.solutions.drawing_utils

dir=0
count=0

# Video Seçme 

if "video1.mp4" in video_path :
    exercise =  "pushup"
    
elif "video2.mp4" in video_path:
    exercise = "legraise"
 
else :
    exercisex = None


while True :
    
    success,img = cap.read()
    
    imgRGB =cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    
    result = pose.process(imgRGB)
    
    lmlist = []
    
    
    if result.pose_landmarks :
        
        mpDraw.draw_landmarks(img,result.pose_landmarks,mpPose.POSE_CONNECTIONS)
        
        for id,lm in enumerate(result.pose_landmarks.landmark):
             
            h,w,_ = img.shape
             
            cx, cy = int(lm.x*w),int(lm.y*h)
             
            lmlist.append([id,cx,cy])
             
             
    #print(lmlist)
     
    
     
    if len(lmlist) != 0 and exercise:
        
        if exercise == "pushup":
        
        # angle = findangle(img, 11, 13, 15, lmlist)
        
        # per = np.interp(angle,(185,245),(0,100))
        
        # if per==100:
            
        #     if dir == 0:
        #         count += 0.5
        #         dir=1
                
        # if per==0:
                    
        #     if dir == 1:
        #         count += 0.5
        #         dir=0
                
        # print(count)    
        
        # cv2.puttext(img, str(int(count)), (45,125), cv2.font_hershey_plain, 10, (0,255,0),10)
        
        # KOŞMA
        
        angle = findAngle(img, 23, 25, 27, lmlist)
        
        per = np.interp(angle,(65,145),(0,100))
         
        if per==100:
            
             if dir == 0:
                 count += 0.5
                 dir=1
                
        if per==0:
                    
             if dir == 1:
                 count += 0.5
                 dir=0
                
        print(count)    
        
        cv2.putText(img, str(int(count)), (45,125), cv2.FONT_HERSHEY_PLAIN, 10, (0,255,0),10)
                      
                
        
        
       # print(angle)
         
             
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    cv2.imshow("img video",img)
    cv2.waitKey(10)
    
