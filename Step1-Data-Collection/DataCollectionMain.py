import WebcamModule as wM
import DataCollectionModule as dcM
import JoyStickModule as jsM

# import MotorModule as mM
import cv2
from time import sleep
from mDev import *


car = mDEV()


maxThrottle = 400
# motor = mM.Motor(2, 3, 4, 17, 22, 27)


record = 0
while True:
    joyVal = jsM.getJS()
    # print(joyVal)
    steering = joyVal["axis1"] - 0.053
    throttle = joyVal["R2"] * maxThrottle
    if (throttle == 0):
       throttle = joyVal["L2"] * -maxThrottle
       steering = joyVal["axis1"] - 0.042
    """
    throttle = -joyVal["axis2"] * 1000
    if steering != 0:
        if throttle == 0:
            throttle = 350
    """
    #print(steering)
    #!! maybe put a minus sign for the steering if it's reversed ??
    convertedSteering = numMap(-steering, -1, 1, 0, 180)
    
    print(steering)
    
    if joyVal["share"] == 1:
        if record == 0:
            print("Recording Started ...")
        record += 1
        sleep(0.300)
    if record == 1:
        img = wM.getImg(True, size=[240, 120])
        dcM.saveData(img, steering)
    elif record == 2:
        dcM.saveLog()
        record = 0

    # motor.move(throttle, -steering)
    car.move(throttle, throttle, convertedSteering)
    #car.setServo("2", convertedSteering)
    #car.setServo("1", convertedSteering)
    cv2.waitKey(1)

