#import packages
import cv2
import numpy as np

#optional argument
def kamera(x):
    pass
cap = cv2.VideoCapture(0)
cv2.namedWindow('gambar')
kernel = np.ones((5,5),np.uint8)

#easy assigments
hh='Hue High'
hl='Hue Low'
sh='Saturation High'
sl='Saturation Low'
vh='Value High'
vl='Value Low'

#Begin Creating trackbars for each
cv2.createTrackbar(hl, 'gambar',0,180,kamera)
cv2.createTrackbar(hh, 'gambar',0,180,kamera)
cv2.createTrackbar(sl, 'gambar',0,255,kamera)
cv2.createTrackbar(sh, 'gambar',0,255,kamera)
cv2.createTrackbar(vl, 'gambar',0,255,kamera)
cv2.createTrackbar(vh, 'gambar',0,255,kamera)

while(1):
	_,frame=cap.read()
	frame=cv2.GaussianBlur(frame,(5,5),0)
    #convert to HSV from BGR
	hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    #read trackbar positions for all
	hul=cv2.getTrackbarPos(hl, 'gambar')
	huh=cv2.getTrackbarPos(hh, 'gambar')
	sal=cv2.getTrackbarPos(sl, 'gambar')
	sah=cv2.getTrackbarPos(sh, 'gambar')
	val=cv2.getTrackbarPos(vl, 'gambar')
	vah=cv2.getTrackbarPos(vh, 'gambar')
    #make array for final values
	HSVLOW=np.array([hul,sal,val])
	HSVHIGH=np.array([huh,sah,vah])

    #apply the range on a mask
	mask = cv2.inRange(hsv,HSVLOW, HSVHIGH)
	mask1 = cv2.erode(mask, kernel)
	res = cv2.bitwise_and(frame,frame, mask =mask)
	
	cv2.imshow('gambar', res)
	cv2.imshow('erosi', mask1)
	cv2.imshow('yay', frame)
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()