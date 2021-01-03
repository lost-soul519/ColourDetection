import cv2
import numpy as np

# print(cv2.__version__)

img = cv2.imread("lena.jpg")
print(img.shape)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img,(7,7),10)
imgCanny = cv2.Canny(img,150,100)
imgDialation = cv2.dilate(imgCanny,np.ones((5,5),np.uint8),iterations=1)

cv2.imshow("Output",img)
cv2.imshow("Output",imgGray)
cv2.imshow("Output",imgBlur)
cv2.imshow("Output",imgCanny)
cv2.waitKey(0)

imgResize = cv2.resize(img,(300,200))
imgCropped = img[0:512,200:500] #Careful of X and Y
cv2.imshow("Output",imgResize)
cv2.imshow("Output",imgCropped)
cv2.waitKey(0)

#TODO: WARP PRESPECTIVE

imgHor = np.hstack((img,img))
imgVer = np.vstack((img,img))
cv2.imshow("Output",imgHor)
cv2.waitKey(0)

cap = cv2.VideoCapture("SampleClip.mp4")
cap.set(3,640)
cap.set(4,48)
cap.set(10,100)
while(True):
    _,img = cap.read()
    cv2.imshow("Video",img);
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break


img =np.zeros((500,500,3),np.uint8)
cv2.line(img,(0,0),(250,250),(0,0,255),3)
cv2.rectangle(img,(250,250),(400,400),(255,0,0),cv2.FILLED)
cv2.circle(img,(433,433),50,(0,255,0),4)
cv2.putText(img,"This is just Shit !",(175,130),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
cv2.imshow("Output",img)
cv2.waitKey(0)