import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

imagefiles = ["sandeep.jpeg", "sandeep.jpeg", "sandeep.jpeg"]

images = []
for filename in imagefiles:
    img = cv2.imread(filename)
    if img is None:
        print(f"Error loading {filename}")
        continue
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    images.append(img)

num_images = len(images)

plt.figure(figsize=[15, 5])
num_cols = 3
num_rows = math.ceil(num_images / num_cols)

for i in range(num_images):
    plt.subplot(num_rows, num_cols, i + 1)
    plt.axis("off")
    plt.imshow(images[i])

# Stitching
stitcher = cv2.Stitcher_create()
status, result = stitcher.stitch(images)

