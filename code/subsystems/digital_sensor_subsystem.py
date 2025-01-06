import wpilib
import libraries.p212
from subsystems.sensor_subsystem import SensorSS

import logging
logger = logging.getLogger("DigitalSensorSS")

class DigitalSensorSS(SensorSS):
    """
    The sensor demo includes several simple digital sensors which all behave
    similarly.

    In normal use, these simple digital sensors -- for example, a limit switch
    or a Hall effect sensor -- would be part of some subsystem, such as an
    elevator or an intake.  Within that subsystem, the sensor would be used to
    indicate to the subsystem that the end of the range of motion has been
    reached.  So these sensors are normally only a small part of the whole
    subsystem.

    However, for the sensor demo, our subsystem class will contain the sensor
    and hardly anything else.  Since the programming for all these simple
    digital sensors is remarkably similar, we only need one class to describe
    them all.  The sensors are only distinguished by which DIO port they are
    plugged into (and by their names).
    """

    SENSOR_CLASS = libraries.p212.DigitalSensor
    SMARTDASHBOARD_PUT_METHOD = wpilib.SmartDashboard.putBoolean
