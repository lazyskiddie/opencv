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

        red_f = red_band.astype(np.float32)
        nir_f = nir_band.astype(np.float32)

        denom = nir_f + red_f
        denom[denom == 0] = 1e-5  # Avoid div by zero
        ndvi = (nir_f - red_f) / denom

        # Normalize for visualization (0-255)
        ndvi_vis = cv2.normalize(ndvi, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

        # Apply a colormap to make small objects "pop" (e.g., plants look green)
        ndvi_colored = cv2.applyColorMap(ndvi_vis, cv2.COLORMAP_JET)

        # 4. Detect Small Objects
        _, thresh = cv2.threshold(ndvi_vis, 160, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


