import numpy as np
from math import *
import argparse
import time
import cv2
import os

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
args = vars(ap.parse_args())

img = cv2.imread(args['image'], 0)

thresh = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

blur = cv2.GaussianBlur(thresh ,(11,11),0)
edges = cv2.Canny(blur,10,200)

im2, contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for i in range(len(contours)):
	cnt = contours[i]
	area = cv2.contourArea(cnt)
	
	if area > 10:
		draw = np.zeros((512,512,3), dtype='uint8')
		
		#epsilon = 0.1*cv2.arcLength(cnt,True)
		#approx = cv2.approxPolyDP(cnt,epsilon,True)
		
		rect = cv2.minAreaRect(cnt)
		box = cv2.boxPoints(rect)
		box = np.int0(box)
		im = cv2.drawContours(draw,[box],0,(0,0,255),2)

		print(90 + rect[-1])
		
		cv2.drawContours(draw, contours, i, (0,255,0), -1)
		cv2.imshow("Black", draw)
		cv2.waitKey(0)


draw = np.zeros((512,512,3), dtype='uint8')
im = cv2.drawContours(draw, contours , -1, (0,0,255), 2)

cv2.imshow("Edges", edges)
cv2.imshow("Image", img)
cv2.imshow("Black", draw)
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)
