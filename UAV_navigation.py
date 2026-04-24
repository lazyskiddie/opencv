import cv2
import numpy as np


def run_live_uav_detection():
    cap = cv2.VideoCapture(0)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    print("Starting Live Multispectral Detection. Press 'q' to exit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        height, width, _ = frame.shape
        mid = width // 2
        red_band = cv2.cvtColor(frame[:, :mid], cv2.COLOR_BGR2GRAY)
        nir_band = cv2.cvtColor(frame[:, mid:], cv2.COLOR_BGR2GRAY)

