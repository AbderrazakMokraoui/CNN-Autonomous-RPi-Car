"""
-This module gets an image through the webcam
using the opencv package
-Display can be turned on or off
-Image size can be defined
"""

import cv2
from threading import Thread


cap = cv2.VideoCapture(0)

def getImg(display=False, size=[480, 240]):
    _, img = cap.read()
    img = cv2.resize(img, (size[0], size[1]))
    if display:
        cv2.imshow("IMG", img)
    return img
def closeWindow():
    cv2.destroyAllWindows()

""" class WebcamModule:
   
    Class that continuously gets frames from a VideoCapture object with
    a dedicated thread.
    
    
    def __init__(self, display=False, size=[480, 240], src=0,):
        self.size = size
        self.display = display
        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()
        #self.frame = cv2.resize(self.frame, (self.size[0], self.size[1]))
        self.stopped = False
        
    def start(self):
        Thread(target=self.get, args=()).start()
        return self
    
    def get(self):
        while not self.stopped:
            if not self.grabbed:
                self.stop()
            else:
                (self.grabbed, self.frame) = self.stream.read()
                self.frame = cv2.resize(self.frame, (self.size[0], self.size[1]))
                if self.display:
                    cv2.imshow("Frame", self.frame)
                
    
    def stop(self):
        self.stopped = True
        #self.stream.destroyAllWindows() """


if __name__ == "__main__":
    while True:
        img = getImg(True)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

