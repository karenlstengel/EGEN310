#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import sys, tty, termios
import time
import atexit
import pygame
import getch

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)
f = open('data.txt', 'w')
#turns off all motors
def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)

#updates the speed
def updateSpeed(dir, speed):
    if(dir == "rTurn"): #a/z
        motorOne.setSpeed(speed)
        motorTwo.setSpeed(int(speed/2))
    if(dir == "lTurn"): #d/c
        motorOne.setSpeed(int(speed/2))
        motorTwo.setSpeed(speed)
    if(dir == "equal"): #all others
        motorOne.setSpeed(speed)
        motorTwo.setSpeed(speed)
#write car data to a file
def writeFile(toWrite):
    f.write(toWrite)
    time.sleep(1)

atexit.register(turnOffMotors)

#set up motors
motorOne = mh.getMotor(1) #left side motors
motorTwo = mh.getMotor(2) #right side motors

#set motor speeds and default to forwards
motorOne.setSpeed(150)
motorTwo.setSpeed(150)

motorOne.run(Adafruit_MotorHAT.FORWARD);
motorTwo.run(Adafruit_MotorHAT.FORWARD);

#turn on motors
motorOne.run(Adafruit_MotorHAT.RELEASE)
motorTwo.run(Adafruit_MotorHAT.RELEASE)

while(True):
    #speed variable to monitor speed
    speed = 150
    toWrite = ""
    dir = "equal"
    #based off of button pushes; get keyboard press using getch()
    key = getch.getch()
        # speed changes:1 = 75; 2 = 125; 3 = 200; 4 = 250
    if(key == '1'):
        speed = 75

    if(key == '2'):
        speed = 125

    if(key == '3'):
        speed = 200

    if(key == '5'):
        speed = 250

    #w both forward
    if(key == 'w'):
        print(key)
        motorOne.run(Adafruit_MotorHAT.FORWARD);
        motorTwo.run(Adafruit_MotorHAT.FORWARD);
        dir = "equal"
        updateSpeed(dir, speed)
        toWrite = str(speed) + ',' + str(speed) + ",F,F\n"

    # both reverse
    if(key == 's'):
        print(key)
        motorOne.run(Adafruit_MotorHAT.BACKWARD);
        motorTwo.run(Adafruit_MotorHAT.BACKWARD);
        dir = "equal"
        updateSpeed(dir, speed)
        toWrite = str(speed) + ',' + str(speed) + ",B,B\n"

    #power M2 forward; less M1
    if(key == 'd'):
        print(key)
        motorTwo.run(Adafruit_MotorHAT.FORWARD);
        motorOne.run(Adafruit_MotorHAT.FORWARD);
        dir = "lTurn"
        updateSpeed(dir, speed)
        toWrite = str(.5*speed) + ',' + str(speed) + ",F,F\n"

    #power M1 forward; less M2
    if(key == 'a'):
        print(key)
        motorOne.run(Adafruit_MotorHAT.FORWARD);
        motorTwo.run(Adafruit_MotorHAT.FORWARD);
        dir = "rTurn"
        updateSpeed(dir, speed)
        toWrite = str(speed) + ',' + str(speed*.5) + ",F,F\n"

    #brake; turn off both motors
    if(key == 't'):
        turnOffMotors()
        toWrite = str(0) + ',' + str(0) + ",R,R\n"

    #M1 forwards; M2 reverse
    if(key == 'q'):
        motorOne.run(Adafruit_MotorHAT.FORWARD);
        motorTwo.run(Adafruit_MotorHAT.BACKWARD);
        dir = "equal"
        updateSpeed(dir, speed)
        toWrite = str(speed) + ',' + str(speed) + ",F,B\n"

    #M1 back M2 forwards
    if(key == 'e'):
        motorOne.run(Adafruit_MotorHAT.BACKWARD);
        motorTwo.run(Adafruit_MotorHAT.FORWARD);
        dir = "equal"
        updateSpeed(dir, speed)
        toWrite = str(speed) + ',' + str(speed) + ",B,F\n"

    # M1 back; M2 less
    if(key == 'z'):
        motorOne.run(Adafruit_MotorHAT.BACKWARD);
        motorTwo.run(Adafruit_MotorHAT.BACKWARD);
        dir = "rTurn"
        updateSpeed(dir, speed)
        toWrite = str(speed) + ',' + str(speed*.5) + ",B,B\n"

    #m2 back; m1 less
    if(key == 'c'):
        motorTwo.run(Adafruit_MotorHAT.BACKWARD);
        motorOne.run(Adafruit_MotorHAT.BACKWARD);
        dir = "lTurn"
        updateSpeed(dir, speed)
        toWrite = str(speed*.5) + ',' + str(speed) + ",B,B\n"

    # release both motors and terminate the program
    if(key == 'o'):
        print(key)
        turnOffMotors()
        f.close()
        sys.exit()

    updateSpeed(dir, speed)
    writeFile(toWrite)

print("Release")
motorOne.run(Adafruit_MotorHAT.RELEASE)
motorTwo.run(Adafruit_MotorHAT.RELEASE)
