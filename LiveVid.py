import cv2

def draw_rectangle(event, x,y,flags, param):
    
    global pt1, pt2, topLeft_clicked, botRight_clicked
    
    if event == cv2.EVENT_LBUTTONDOWN:
        if topLeft_clicked == True and botRight_clicked == True:
            topLeft_clicked = False
            botRight_clicked = False
            pt1 = (0,0)
            pt2 = (0,0)
        
        if topLeft_clicked == False:
            pt1 = (x,y)
            topLeft_clicked =True
                
        elif botRight_clicked == False:
            pt2 = (x,y)
            botRight_clicked = True
                
pt1 = (0,0)
pt2 = (0,0)
topLeft_clicked = False
botRight_clicked = False

capture = cv2.VideoCapture(0)

cv2.namedWindow('Video')
cv2.setMouseCallback('Video', draw_rectangle)

while True:
    ret, frame = capture.read()
    
    if topLeft_clicked:
        cv2.circle(frame, center=pt1, radius=5, color=(0,0,255), thickness=-1)
    
    if topLeft_clicked and botRight_clicked:
        cv2.rectangle(frame, pt1, pt2, (0,0,255), 2)
        
   
    cv2.imshow('Video', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

        
capture.release()
cv2.destroyAllWindows()
#END of all things