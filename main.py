import cv2
from cv2 import rectangle
image = cv2.imread("sandeep.jpeg")
print(image)
#
# if image is not None:
#     height, width, channels = image.shape
#     print(height)
#     print(width)
#
#     # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     center = (700, height // 2,)
#     # # pt2 =
#     #
#     cv2.circle(image, center, 200, (255, 0, 0), 2)
#     cv2.imshow("image", image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
# else:
#     print("No image")
#
# image = cv2.imread("sandeep.jpeg")
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
#
# faces = face_cascade.detectMultiScale(image, 1.3, 5)
#
# for (x, y, w, h) in faces:
#     cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 2)
#     cv2.putText(image, "Sandeep", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)
# cv2.imshow('Face Detection', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# cap = cv2.VideoCapture(0)
# while True:
# #     ret, frame = cap.read()
#
#     # if not ret:
#     #     print("could not read frame")
#     #     break
#     #
#     # flipped_frame = cv2.flip(frame, 1)
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#     for (x, y, w, h) in faces:
#         cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
#     # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     flipped_frame = cv2.flip(faces, 1)
#     # if (flipped_frame == image ).all():
#     cv2.imshow('frame',image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

# cap.release()
# cv2.destroyAllWindows()