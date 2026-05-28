import cv2

# so i am going to use GOTURN tracking algo let see how it wok !!
"""
   main frame
    _______
   |       | \
   |       |   \
   |_______|    \
                |---------|------------- |---------|
    _______     |_________|              |         | predected frame
   |       |   / neural network          |_________|
   |       |  /
   |_______| /
  next frame
"""

import cv2
import numpy as np
# Create matrix
mat = np.random.randint(0, 256, (100, 100), dtype=np.uint8)
# Save directly
cv2.imshow('output_image.png', mat)

cv2.waitKey(0)
cv2.destroyAllWindows()
