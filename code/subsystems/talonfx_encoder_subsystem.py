import libraries.p212
from subsystems.sensor_subsystem import SensorSS

import logging
logger = logging.getLogger("TalonFXEncoderSS")

class TalonFXEncoderSS(SensorSS):
    """
    The sensor demo includes the built-in encoder from a TalonFX motor
    controller.
    """

    SENSOR_CLASS = libraries.p212.TalonFXEncoderSensor
    SMARTDASHBOARD_PUT_METHOD = wpilib.SmartDashboard.putNumber
