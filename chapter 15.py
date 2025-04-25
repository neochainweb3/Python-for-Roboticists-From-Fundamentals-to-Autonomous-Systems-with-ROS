# Chapter 15 - OpenCV camera processing
import cv2
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    # process and display
