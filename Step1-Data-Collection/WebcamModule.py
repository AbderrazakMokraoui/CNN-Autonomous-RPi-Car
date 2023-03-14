"""
-This module gets an image through the webcam
using the opencv package
-Display can be turned on or off
-Image size can be defined
"""

import cv2

cap = cv2.VideoCapture(0)
print(cap)


def getImg(display=False, size=[480, 240]):
    _, img = cap.read()
    img = cv2.resize(img, (size[0], size[1]))
    if display:
        cv2.imshow("IMG", img)
    return img
def closeWindow():
    cv2.destroyAllWindows()


if __name__ == "__main__":
    while True:
        img = getImg(True)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
