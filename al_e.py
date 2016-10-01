from BrickPi import *
import socket

BrickPiSetup()

BrickPi.MotorEnable[PORT_A] = 1 # Droit
BrickPi.MotorEnable[PORT_D] = 1 # Gauche

BrickPiSetupSensors()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.101.101", 8081))

try:
    while True:
        result = BrickPiUpdateValues()
        if not result:
            r = s.recv(1024)
            if r == "right\n":
                print 'r'
                BrickPi.MotorSpeed[PORT_A] = 200
                BrickPi.MotorSpeed[PORT_D] = 0
            elif r == "left\n":
                print 'l'
                BrickPi.MotorSpeed[PORT_A] = 0
                BrickPi.MotorSpeed[PORT_D] = 200
            elif r == "forward\n":
                print 'f'
                BrickPi.MotorSpeed[PORT_A] = 200
                BrickPi.MotorSpeed[PORT_D] = 200
            elif r == "backward\n":
                print 'b'
                BrickPi.MotorSpeed[PORT_A] = -200
                BrickPi.MotorSpeed[PORT_D] = -200
            else:
                BrickPi.MotorSpeed[PORT_A] = 0
                BrickPi.MotorSpeed[PORT_D] = 0
finally:
    s.close()
