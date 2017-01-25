#Author: Michael Disyak
# #Having already initialized the servos to have unique ID names,
# this file will run a set of instructions that make
#the servos move for 2 mins as per requirements of > 1 min
#Will run the current control function in a new thread while the Plotter class plots data in real time


from lib_robotis_hack import *
import myLib as myLib
import plotter
import threading
import random as rand


D = USB2Dynamixel_Device(dev_name="/dev/tty.usbserial-AI03QEMU",baudrate=1000000)
s_list = find_servos(D)
s1 = Robotis_Servo(D,s_list[0])
s2 = Robotis_Servo(D,s_list[1])

myPlotter = plotter.Plotter()
myPlotter.s1 = s1
myPlotter.s2 = s2


def controlFunc(args1, plotStopEvent):

    timeEnd = time.time() + 60 * 1
    while (time.time() < timeEnd):
        randomAngle = rand.randrange(-90, 90) #random action
        randomServo = rand.randrange(0,1)
        if(randomServo == 1):#randomly select servo
            s1.move_angle(myLib.degToRad(randomAngle))
        else:
            s2.move_angle(myLib.degToRad(randomAngle))
        time.sleep(0.10) #Gives time for latency of action
    time.sleep(15) #Gives the plotting time to catch up
    plotStopEvent.set() #Signals plotting to stop


def extraTests(): #To fulfill full requirements for Module 1

    s1.disable_torque()
    s2.disable_torque()
    s1.enable_torque()
    s2.enable_torque()
    s1.move_to_encoder(500)
    s2.move_to_encoder(500)
    time.sleep(2)
    s1.move_to_encoder(800)
    s2.move_to_encoder(800)
    time.sleep(2)

extraTests()
#realTimeStop = threading.Event()
#threading.Thread(target=controlFunc, args=(1, realTimeStop)).start()
#myPlotter.indefinitePlotAllSensorsRealTime(realTimeStop)
#myPlotter.saveData()
#myPlotter.saveFigure('All Sensors')
