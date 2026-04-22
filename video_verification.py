import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    # flipped_image = cv2.flip(frame, 1)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), 3)
        cv2.putText(frame, "Human...", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (149, 6, 6), 4)
    cv2.imshow('Live Face Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
