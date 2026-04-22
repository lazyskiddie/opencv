import cv2
import pytesseract

image = cv2.imread("WhatsApp Image 2025-06-28 at 23.06.45.jpeg")

extracted_text = pytesseract.image_to_string(image)
print(extracted_text)
cv2.imshow("image", image)
cv2.waitKey(0)