import pypot.dynamixel
import itertools
import socket
import time

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
################################################

dxl_io.set_goal_position({1: 93.11})

t0 = time.time()
try:
    while True:
        t = time.time()
        if (t - t0) > 5:
            break

        r = s.recv(1024)
        if r == "right\n":
            print 'r'
            # move motor id 7 to the right
            #dxl_io.set_goal_position(dict(zip(ids, itertools.repeat(0))))
            dxl_io.set_goal_position({5: positions.get(5) - 50})
            dxl_io.set_goal_position({6: positions.get(6) - 50})
            time.sleep(0.02)
        elif r == "left\n":
            print 'l'
            # move motor id 7 to the left
            dxl_io.set_goal_position({5: positions.get(5) + 50})
            dxl_io.set_goal_position({6: positions.get(6) + 50})
            time.sleep(0.02)
        elif r == "forward\n":
            print 'f'
            # move motor id 1 to the forward
        elif r == "backward\n":
            print 'b'
            # move motor id 1 to the backward
finally:
    s.close()

# dxl_io.set_goal_position(dict(zip(ids, itertools.repeat(0))))
# print dict(zip(ids, dxl_io.get_present_position(ids)))
