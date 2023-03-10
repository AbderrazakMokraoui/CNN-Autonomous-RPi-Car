import cv2
import numpy as np
from tensorflow.keras.models import load_model

import WebcamModule as wM
from mDev import *

car = mDEV()

# import MotorModule as mM

#######################################
steeringSen = 0.70  # Steering Sensitivity
maxThrottle = 380  # Forward Speed
# motor = mM.Motor(2, 3, 4, 17, 22, 27)  # Pin Numbers
model = load_model(
    "/home/pi/Desktop/My Files/RpiRobot/model_V1.h5"
)  # Path to our trained model on the RPi
######################################


def preProcess(img):
    img = img[54:120, :, :]
    img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
    img = cv2.GaussianBlur(img, (3, 3), 0)
    img = cv2.resize(img, (200, 66))
    img = img / 255
    return img


while True:
    img = wM.getImg(True, size=[240, 120])
    img = np.asarray(img)
    img = preProcess(img)
    img = np.array([img])
    steering = float(model.predict(img))
    steering = -steering * steeringSen
    # motor.move(maxThrottle, steering)
    convertedSteering = numMap(steering, -1, 1, 0, 180)
    car.move(maxThrottle, maxThrottle, convertedSteering)
    cv2.waitKey(1)
