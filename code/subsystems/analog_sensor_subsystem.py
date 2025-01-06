import wpilib
import libraries.p212
from subsystems.sensor_subsystem import SensorSS

import logging
logger = logging.getLogger("AnalogSensorSS")

class AnalogSensorSS(SensorSS):
    """
    The sensor demo includes one analog sensor so far: an ultrasonic
    rangefinder.

    In normal use, such a sensor would be part of some subsystem.  Within that
    subsystem, the sensor would be used to indicate a value to the subsystem,
    such as the distance to the wall.  So these sensors are normally only a
    small part of the whole subsystem.

    However, for the sensor demo, our subsystem class will contain the sensor
    and hardly anything else.  For this purpose, the sensors are only
    distinguished by the following characteristics:
     * sensor name
     * sensor's hard-wired DIO port
     * sensor range (lower and upper values that correspond to 0V and +5V)
     * number of digits of precision to round displayed values to
    """

    SENSOR_CLASS = libraries.p212.AnalogSensor
    SMARTDASHBOARD_PUT_METHOD = wpilib.SmartDashboard.putNumber
