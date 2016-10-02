# Client Leap Motion RPi
from BrickPi import *
import socket
import pypot.dynamixel
import itertools

# init dynamixel
def init_dynamixel():
    ports = pypot.dynamixel.get_available_ports()
    if not ports:
        raise IOError('no port found!')
    print('ports found', ports)
    print('connecting on the first available port:', ports[0])
    dxl_io = pypot.dynamixel.DxlIO(ports[0])
    ids = dxl_io.scan()
    models = dxl_io.get_model(ids)
    positions = dict(zip(ids, dxl_io.get_present_position(ids)))
    print positions
    ################################################
    dxl_io.enable_torque(ids)
    speed = dict(zip(ids, itertools.repeat(200)))
    dxl_io.set_moving_speed(speed)


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
            elif r == 'ok':
                print 'move the arm'
                # TODO move the dynamixel here
            else:
                BrickPi.MotorSpeed[PORT_A] = 0
                BrickPi.MotorSpeed[PORT_D] = 0
finally:
    s.close()
