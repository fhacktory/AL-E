from pypot.dynamixel import autodetect_robot

my_robot = autodetect_robot()

print my_robot

###################

def detect_robot():
    ports = pypot.dynamixel.get_available_ports()
    dxl_io = pypot.dynamixel.DxlIO(ports[0])
    ids = dxl_io.scan()

    if not ids:
        dxl_io.close()

    print ids

    models = dxl_io.get_model(ids)

    print models

    motorcls = {
        'MX': pypot.dynamixel.motor.DxlMXMotor,
        'RX': pypot.dynamixel.motor.DxlAXRXMotor,
        'AX': pypot.dynamixel.motor.DxlAXRXMotor,
        'XL': pypot.dynamixel.motor.DxlXL320Motor
    }

    motors = [motorcls[model[:2]](id, model=model)
              for id, model in zip(ids, models)]

    print motors

    c = pypot.dynamixel.controller.DxlController(dxl_io, motors)
    return c

foo = detect_robot()
print foo
