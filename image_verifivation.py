import cv2


image = cv2.imread("sandeep.jpeg")
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

faces = face_cascade.detectMultiScale(image, 1.3, 5)
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 0), 3)
    cv2.putText(image, "Sandeep", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (149, 6, 6), 4)
cv2.imshow('Face Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()