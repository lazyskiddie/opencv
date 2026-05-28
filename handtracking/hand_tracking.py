import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    cv2.imshow('hand Detection', frame)
    cv2.waitKey(1)