def draai_rechts():
    pass
speed = 80
basic.show_icon(IconNames.HEART)

def on_forever():
    if maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_M) == 1:
        maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.ALL_MOTOR,
            maqueenPlusV2.MyEnumDir.FORWARD,
            50)
    elif maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_L1) == 0 and maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_R1) == 1:
        maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.LEFT_MOTOR,
            maqueenPlusV2.MyEnumDir.FORWARD,
            40)
        maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.RIGHT_MOTOR,
            maqueenPlusV2.MyEnumDir.FORWARD,
            10)
    elif True:
        pass
basic.forever(on_forever)
