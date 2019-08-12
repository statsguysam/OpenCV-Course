# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 14:50:29 2019

@author: Salim
"""

import cv2

# Lists to store the points
pt1=[]
pt2=[]

def drawRectangle(action, x, y, flags, userdata):
  # Referencing global variables 
  global pt1, pt2
  # Action to be taken when left mouse button is pressed
  if action==cv2.EVENT_LBUTTONDOWN:
    pt1=[(x,y)]
    cv2.rectangle(source, pt1[0], (pt1[0][0]+0,pt1[0][1]+0), (255,255,0), 2, cv2.LINE_AA )

  # Action to be taken when left mouse button is released
  elif action==cv2.EVENT_LBUTTONUP:
    pt2=[(x,y)]
    cv2.rectangle(source, pt1[0], pt2[0], (0,255,0),2, 
                    cv2.LINE_AA)
    cv2.imwrite("face.png",source[pt1[0][1]:pt2[0][1],pt1[0][0]:pt2[0][0]])
    cv2.imshow("Window",source)
        
source = cv2.imread("sample.jpg",1)
# Make a dummy image, will be useful to clear the drawing
dummy = source.copy()
cv2.namedWindow("Window")
# highgui function called when mouse events occur
cv2.setMouseCallback("Window", drawRectangle)
k = 0
# loop until escape character is pressed
while k!=27 :
  
  cv2.imshow("Window", source)
  cv2.putText(source,'''Choose top left corner, and drag, 
                      Press ESC to exit and c to clear''' ,
              (10,30), cv2.FONT_HERSHEY_SIMPLEX, 
              0.7,(255,255,255), 2 );
  k = cv2.waitKey(20) & 0xFF
  # Another way of cloning
  if k==99:
    source= dummy.copy()


cv2.destroyAllWindows()

