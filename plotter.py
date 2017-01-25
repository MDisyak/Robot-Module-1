#Author: Michael Disyak
#A class that can plot in real time and store data to file from initialized dynamixels

import myLib
import matplotlib.pyplot as plt
import datetime
import csv
import threading
import numpy as np

class Plotter:

    def __init__(self):
        self.angles1 = []
        self.angles2 = []
        self.loads1 = []
        self.loads2 = []
        self.voltages1 = []
        self.voltages2 = []
        self.temperatures1 = []
        self.temperatures2 = []
        self.angleAxisArr = [0,0]
        self.loadAxisArr = [0,0]
        self.voltageAxisArr = [0,0]
        self.temperatureAxisArr = [0,0]
        self.angleFig = None
        self.loadFig = None
        self.voltageFig = None
        self.temperatureFig = None



# Angle and Load and Temperature and Voltage-------------------------------------------------------||

    def initRealTimeAllSensorsPlots(self):
        self.allFig, axisArr = plt.subplots(8)
        self.allFig.tight_layout()
        self.angleAxisArr[0] = axisArr[0]
        self.angleAxisArr[1] = axisArr[1]
        self.loadAxisArr[0] = axisArr[2]
        self.loadAxisArr[1] = axisArr[3]
        self.temperatureAxisArr[0] = axisArr[4]
        self.temperatureAxisArr[1] = axisArr[5]
        self.voltageAxisArr[0] = axisArr[6]
        self.voltageAxisArr[1] = axisArr[7]
        self.angleAxisArr[0].set_title("Angle of Servo 1")
        self.angleAxisArr[1].set_title("Angle of Servo 2")
        self.loadAxisArr[0].set_title("Load of Servo 1")
        self.loadAxisArr[1].set_title("Load of Servo 2")
        self.temperatureAxisArr[0].set_title("Temperature of Servo 1")
        self.temperatureAxisArr[1].set_title("Temperature of Servo 2")
        self.voltageAxisArr[0].set_title("Voltage of Servo 1")
        self.voltageAxisArr[1].set_title("Voltage of Servo 2")
        plt.ion()

    def plotAllSensorsRealTime(self):
        self.plotAngleS1RealTime()
        self.plotAngleS2RealTime()
        self.plotLoadS1RealTime()
        self.plotLoadS2RealTime()
        self.plotTemperatureS1RealTime()
        self.plotTemperatureS2RealTime()
        self.plotVoltageS1RealTime()
        self.plotVoltageS2RealTime()

    def indefinitePlotAllSensorsRealTime(self, stoppingEvent):
        self.initRealTimeAllSensorsPlots()
        while not stoppingEvent.is_set():
            self.plotAllSensorsRealTime()

#Angle and Voltage -------------------------------------------------------||
    def initRealTimeAngleVoltagePlots(self):
        self.angleVoltFig, axisArr = plt.subplots(4)
        self.angleVoltFig.tight_layout()
        self.angleAxisArr[0] = axisArr[0]
        self.angleAxisArr[1] = axisArr[1]
        self.voltageAxisArr[0] = axisArr[2]
        self.voltageAxisArr[1] = axisArr[3]
        self.angleAxisArr[0].set_title("Angle of Servo 1")
        self.angleAxisArr[1].set_title("Angle of Servo 2")
        self.voltageAxisArr[0].set_title("Voltage of Servo 1")
        self.voltageAxisArr[1].set_title("Voltage of Servo 2")
        plt.ion()
        

    def plotAngleVoltageRealTime(self):
        self.plotAngleS1RealTime()
        self.plotAngleS2RealTime()
        self.plotVoltageS1RealTime()
        self.plotVoltageS2RealTime()

    def indefinitePlotAngleVoltageRealTime(self, stoppingEvent):
        self.initRealTimeAngleVoltagePlots()
        while not stoppingEvent.is_set():
            self.plotAngleVoltageRealTime()

#Angle and Load -------------------------------------------------------||
    def initRealTimeAngleLoadPlots(self):
        self.angleLoadFig, axisArr = plt.subplots(4)
        self.angleLoadFig.tight_layout()
        self.angleAxisArr[0] = axisArr[0]
        self.angleAxisArr[1] = axisArr[1]
        self.loadAxisArr[0] = axisArr[2]
        self.loadAxisArr[1] = axisArr[3]
        self.angleAxisArr[0].set_title("Angle of Servo 1")
        self.angleAxisArr[1].set_title("Angle of Servo 2")
        self.loadAxisArr[0].set_title("Load of Servo 1")
        self.loadAxisArr[1].set_title("Load of Servo 2")
        plt.ion()

    def plotAngleLoadRealTime(self):
        self.plotAngleS1RealTime()
        self.plotAngleS2RealTime()
        self.plotLoadS1RealTime()
        self.plotLoadS2RealTime()

    def indefinitePlotAngleLoadRealTime(self, stoppingEvent):
        self.initRealTimeAngleLoadPlots()
        while(not stoppingEvent.is_set()):
            self.plotAngleLoadRealTime()

#Angle and Temperature -------------------------------------------------------||

    def initRealTimeAngleTemperaturePlots(self):
        self.angleTemperatureFig, axisArr = plt.subplots(4)
        self.angleTemperatureFig.tight_layout()
        self.angleAxisArr[0] = axisArr[0]
        self.angleAxisArr[1] = axisArr[1]
        self.temperatureAxisArr[0] = axisArr[2]
        self.temperatureAxisArr[1] = axisArr[3]
        self.angleAxisArr[0].set_title("Angle of Servo 1")
        self.angleAxisArr[1].set_title("Angle of Servo 2")
        self.temperatureAxisArr[0].set_title("Temperature of Servo 1")
        self.temperatureAxisArr[1].set_title("Temperature of Servo 2")
        plt.ion()

    def plotAngleTemperatureRealTime(self):
        self.plotAngleS1RealTime()
        self.plotAngleS2RealTime()
        self.plotTemperatureS1RealTime()
        self.plotTemperatureS2RealTime()

    def indefinitePlotAngleTemperatureRealTime(self, stoppingEvent):
        self.initRealTimeAngleTemperaturePlots()
        while (not stoppingEvent.is_set()):
            self.plotAngleTemperatureRealTime()
    
    # Temperature and Voltage -------------------------------------------------------||
    def initRealTimeTemperatureVoltagePlots(self):
        self.temperatureVoltFig, axisArr = plt.subplots(4)
        self.temperatureVoltFig.tight_layout()
        self.temperatureAxisArr[0] = axisArr[0]
        self.temperatureAxisArr[1] = axisArr[1]
        self.voltageAxisArr[0] = axisArr[2]
        self.voltageAxisArr[1] = axisArr[3]
        self.temperatureAxisArr[0].set_title("Temperature of Servo 1")
        self.temperatureAxisArr[1].set_title("Temperature of Servo 2")
        self.voltageAxisArr[0].set_title("Voltage of Servo 1")
        self.voltageAxisArr[1].set_title("Voltage of Servo 2")
        plt.ion()
    
    def plotTemperatureVoltageRealTime(self):
        self.plotTemperatureS1RealTime()
        self.plotTemperatureS2RealTime()
        self.plotVoltageS1RealTime()
        self.plotVoltageS2RealTime()
    
    def indefinitePlotTemperatureVoltageRealTime(self, stoppingEvent):
        self.initRealTimeTemperatureVoltagePlots()
        while (not stoppingEvent.is_set()):
            self.plotTemperatureVoltageRealTime()


    # Angle and Load and Temperature  -------------------------------------------------------||
    def initRealTimeAngleLoadTemperaturePlots(self):
        self.angleLoadFig, axisArr = plt.subplots(6)
        self.angleLoadFig.tight_layout()
        self.angleAxisArr[0] = axisArr[0]
        self.angleAxisArr[1] = axisArr[1]
        self.loadAxisArr[0] = axisArr[2]
        self.loadAxisArr[1] = axisArr[3]
        self.temperatureAxisArr[0] = axisArr[4]
        self.temperatureAxisArr[1] = axisArr[5]
        self.angleAxisArr[0].set_title("Angle of Servo 1")
        self.angleAxisArr[1].set_title("Angle of Servo 2")
        self.loadAxisArr[0].set_title("Load of Servo 1")
        self.loadAxisArr[1].set_title("Load of Servo 2")
        self.temperatureAxisArr[0].set_title("Temperature of Servo 1")
        self.temperatureAxisArr[1].set_title("Temperature of Servo 2")
        plt.ion()

    def plotAngleLoadTemperatureRealTime(self):
        self.plotAngleS1RealTime()
        self.plotAngleS2RealTime()
        self.plotLoadS1RealTime()
        self.plotLoadS2RealTime()
        self.plotTemperatureS1RealTime()
        self.plotTemperatureS2RealTime()

    def indefinitePlotAngleLoadTemperatureRealTime(self, stoppingEvent):
        self.initRealTimeAngleLoadTemperaturePlots()
        while (not stoppingEvent.is_set()):
            self.plotAngleLoadTemperatureRealTime()

    #ANGLE Plots -----------------------------------------||
    def initRealTimeAnglePlots(self):
        self.angleFig, self.angleAxisArr = plt.subplots(2)
        self.angleAxisArr[0].set_title("Angle of Servo 1")
        self.angleAxisArr[1].set_title("Angle of Servo 2")
        plt.ion()

    def plotAngleS1RealTime(self):
        angle = myLib.radToDeg(self.s1.read_angle())
        self.angles1.append(angle)
        self.angleAxisArr[0].plot(self.angles1)
        plt.pause(0.005)


    def plotAngleS2RealTime(self):
        angle = myLib.radToDeg(self.s2.read_angle())
        self.angles2.append(angle)
        self.angleAxisArr[1].plot(self.angles2)
        plt.pause(0.005)

    def plotAnglesRealTime(self):
        self.plotAngleS1RealTime()
        self.plotAngleS2RealTime()

    #LOAD Plots ----------------------------------------------||
    def initRealTimeLoadPlots(self):
        self.loadFig, self.loadAxisArr = plt.subplots(2)
        self.loadAxisArr[0].set_title("Load of Servo 1")
        self.loadAxisArr[1].set_title("Load of Servo 2")
        plt.ion()

    def plotLoadS1RealTime(self):
        load = self.s1.read_load()
        self.loads1.append(load)
        self.loadAxisArr[0].plot(self.loads1)
        plt.pause(0.005)

    def plotLoadS2RealTime(self):
        load = self.s2.read_load()
        self.loads2.append(load)
        self.loadAxisArr[1].plot(self.loads2)
        plt.pause(0.005)

    def plotLoadsRealTime(self):
        self.plotLoadS1RealTime()
        self.plotLoadS2RealTime()

    #VOLTAGE plots -----------------------------------------------||
    def initRealTimeVoltagePlots(self):
        self.voltageFig, self.voltageAxisArr = plt.subplots(2)
        self.voltageAxisArr[0].set_title("Voltage of Servo 1")
        self.voltageAxisArr[1].set_title("Voltage of Servo 2")
        plt.ion()

    def plotVoltageS1RealTime(self):
        voltage = self.s1.read_voltage()
        self.voltages1.append(voltage)
        self.voltageAxisArr[0].plot(self.voltages1)
        plt.pause(0.005)

    def plotVoltageS2RealTime(self):
        voltage = self.s2.read_voltage()
        self.voltages2.append(voltage)
        self.voltageAxisArr[1].plot(self.voltages2)
        plt.pause(0.005)

    def plotVoltagesRealTime(self):
        self.plotVoltageS1RealTime()
        self.plotVoltageS2RealTime()

    #TEMPERATURE plots --------------------------------------------||
    def initRealTimeTemperaturePlots(self):
        self.temperatureFig, self.temperatureAxisArr = plt.subplots(2)
        self.temperatureAxisArr[0].set_title("Temperature of Servo 1")
        self.temperatureAxisArr[1].set_title("Temperature of Servo 2")
        plt.ion()

    def plotTemperatureS1RealTime(self):
        temperature = self.s1.read_temperature()
        self.temperatures1.append(temperature)
        self.temperatureAxisArr[0].plot(self.temperatures1)
        plt.pause(0.005)

    def plotTemperatureS2RealTime(self):
        temperature = self.s2.read_temperature()
        self.temperatures2.append(temperature)
        self.temperatureAxisArr[1].plot(self.temperatures2)
        plt.pause(0.005)

    def plotTemperaturesRealTime(self):
        self.plotTemperatureS1RealTime()
        self.plotTemperatureS2RealTime()

    # END PLOTS ------------------------------------------------------||

    
    #Write to file in the order of ANGLE - LOAD - TEMPERATURE - VOLTAGE
    def saveFigure(self, fileName = 'Figure_from_%s.png' % datetime.datetime.now()):
        plt.savefig('figures/%s' % fileName)

    def saveData(self, fileName = 'Data_from_%s.dat' % datetime.datetime.now() ):
        fout = open('data/%s' % fileName, 'w')
        if(len(self.angles1) > 0):
            for i in range(len(self.angles1)):
                target = self.angles1[i]
                fout.write(repr(target) + ' ')
        if(len(self.angles2) > 0):
            fout.write('\n')
            for i in range(len(self.angles2)):
                target = self.angles2[i]
                fout.write(repr(target) + ' ')
                
        if (len(self.loads1) > 0):
            fout.write('\n')
            for i in range(len(self.loads1)):
                target = self.loads1[i]
                fout.write(repr(target) + ' ')
                
        if (len(self.loads2) > 0):
            fout.write('\n')
            for i in range(len(self.loads2)):
                target = self.loads2[i]
                fout.write(repr(target) + ' ')
                
        if (len(self.temperatures1) > 0):
            fout.write('\n')
            for i in range(len(self.temperatures1)):
                target = self.temperatures1[i]
                fout.write(repr(target) + ' ')
                
        if (len(self.temperatures2) > 0):
            fout.write('\n')
            for i in range(len(self.temperatures2)):
                target = self.temperatures2[i]
                fout.write(repr(target) + ' ')
                
        if (len(self.voltages1) > 0):
            fout.write('\n')
            for i in range(len(self.voltages1)):
                target = self.voltages1[i]
                fout.write(repr(target) + ' ')
                
        if (len(self.voltages2) > 0):
            fout.write('\n')
            for i in range(len(self.voltages2)):
                target = self.voltages2[i]
                fout.write(repr(target) + ' ')

        fout.close()

    def recordData(self):
        self.loads1.append(self.s1.read_load())
        self.loads2.append(self.s2.read_load())
        self.angles1.append(self.s1.read_angle())
        self.angles2.append(self.s2.read_angle())
        self.temperatures1.append(self.s1.read_temperature())
        self.temperatures2.append(self.s2.read_temperature())
        self.voltages1.append(self.s1.read_voltage())
        self.voltages2.append(self.s2.read_voltage())
        self.saveData()

    def plotAllFromFile(self, fileName):
        y = []
        with open(fileName, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
              for column in plots:
                 y.append(column[col])
        plt.plot(y)
        plt.show()

    #Plots data from file using col as data selection
    def plotColumnFromFile(self, fileName, col):
        y = []
        with open(fileName, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for column in plots:
                y.append(column[col])
        plt.plot(y)
        plt.show()

    def plotAllSensorsRealTimeWithThread(self):

        print("in plotAllSensorsRealTimeWithThread")
        while (True):
            print("in loop")
            self.plotAllSensorsRealTime()

    def _plotWithThread(self):
        print("in _plotWithThread")
        self.initRealTimeAllSensorsPlots()
        self.plotAllSensorsRealTimeWithThread()

    def plotWithThread(self):
        print("in plotWithThread")
        threading.Thread(target=self._plotWithThread).start()





# The following section is a work in progress and can be ignored! -----------------------------||
    def testinitRealTimeAllSensorsPlots(self):
        x = np.arange(0, 100, 1)
        plt.ion()
        fig1, axisArr = plt.subplots(
            4)  # self.angles1, 'b', self.loads1, 'g', self.temperatures1, 'r', self.voltages1, 'y')
        self.angleAxisArr[0] = axisArr[0]
        self.loadAxisArr[0] = axisArr[1]
        self.temperatureAxisArr[0] = axisArr[2]
        self.voltageAxisArr[0] = axisArr[3]

        self.angleAxisArr[0].set_title("Angle of Servo 1")
        self.loadAxisArr[0].set_title("Load of Servo 1")
        self.temperatureAxisArr[0].set_title("Temperature of Servo 1")
        self.voltageAxisArr[0].set_title("Voltage of Servo 1")
        plt.legend()
        plt.draw()

        fig2, axisArr = plt.subplots(
            4)  # (self.angles2, 'b', self.loads2, 'g', self.temperatures2, 'r', self.voltages2, 'y')
        self.angleAxisArr[1] = axisArr[0]
        self.loadAxisArr[1] = axisArr[1]
        self.temperatureAxisArr[1] = axisArr[2]
        self.voltageAxisArr[1] = axisArr[3]

        self.angleAxisArr[1].set_title("Angle of Servo 2")
        self.loadAxisArr[1].set_title("Load of Servo 2")
        self.temperatureAxisArr[1].set_title("Temperature of Servo 2")
        self.voltageAxisArr[1].set_title("Voltage of Servo 2")
        plt.legend()
        plt.draw()

    def testplotAllSensorsRealTime(self):
        angle = myLib.radToDeg(self.s1.read_angle())
        self.angles1.append(angle)
        self.angleAxisArr[0].plot(self.angles1)

        load = myLib.radToDeg(self.s1.read_load())
        self.loads1.append(load)
        self.loadAxisArr[0].plot(self.loads1)

        temperature = myLib.radToDeg(self.s1.read_temperature())
        self.temperatures1.append(temperature)
        self.temperatureAxisArr[0].plot(self.temperatures1)

        voltage = myLib.radToDeg(self.s1.read_voltage())
        self.voltages1.append(voltage)
        self.voltageAxisArr[0].plot(self.voltages1)

        plt.draw()

        angle = myLib.radToDeg(self.s2.read_angle())
        self.angles2.append(angle)
        self.angleAxisArr[1].plot(self.angles2)

        load = myLib.radToDeg(self.s2.read_load())
        self.loads2.append(load)
        self.loadAxisArr[1].plot(self.loads2)

        temperature = myLib.radToDeg(self.s2.read_temperature())
        self.temperatures2.append(temperature)
        self.temperatureAxisArr[1].plot(self.temperatures2)

        voltage = myLib.radToDeg(self.s2.read_voltage())
        self.voltages2.append(voltage)
        self.voltageAxisArr[1].plot(self.voltages2)

        plt.draw()

    def testindefinitePlotAllSensorsRealTime(self, stoppingEvent):
        self.testinitRealTimeAllSensorsPlots()
        while not stoppingEvent.is_set():
            self.testplotAllSensorsRealTime()
# END OF WORK IN PROGRESS
