import WebcamModule as wM
import DataCollectionModule as dcM
import JoyStickModule as jsM

# import MotorModule as mM
import cv2
import threading
from time import sleep
from mDev import *
import threading


car = mDEV()

car.setServo('3', 60)


maxThrottle = 300
# motor = mM.Motor(2, 3, 4, 17, 22, 27)

images = []
steerings = []
record = 0
while True:
    #img = wM.getImg(display=True, size=[120, 60])
    joyVal = jsM.getJS()
    # print(joyVal)
    steering = joyVal["axis1"] - 0.028
    throttle = joyVal["R2"] * maxThrottle
    if (throttle == 0):
       throttle = joyVal["L2"] * -maxThrottle
       steering = joyVal["axis1"] - 0.03
    """
    throttle = -joyVal["axis2"] * 1000
    if steering != 0:
        if throttle == 0:
            throttle = 350
    """
    #!! maybe put a minus sign for the steering if it's reversed ??
    convertedSteering = numMap(-steering, -1, 1, 0, 180)
    
    #print(steering)
    #print(joyVal["share"])
    #print(record)
    
    if joyVal["share"] == 1:
        if record == 0 : print("Recording Started ...")
        record = 1
        
    if record == 1:
        img = wM.getImg(display=True, size=[800, 400])
        #images.append(img)
        #steerings.append(steering)
        dcM.saveData(img, steering)
        if joyVal["o"] == 1:
            cv2.destroyAllWindows
            dcM.saveLog()
            record = 0        
        
    car.move(throttle, throttle, convertedSteering)
    car.setServo("2", numMap(-steering * 0.5, -1, 1, 0, 180))
    cv2.waitKey(1)

