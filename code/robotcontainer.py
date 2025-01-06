# Copyright (c) YVHS Robotics Booster Club and Project 212 (#7137).
# Open Source Software; you can modify and/or share it under the terms of
# license file in the root directory of this project.
#

import wpilib
import commands2

from constants import ELEC
from subsystems.digital_sensor_subsystem import DigitalSensorSS
from subsystems.analog_sensor_subsystem import AnalogSensorSS
from subsystems.talonfx_encoder_subsystem import TalonFXEncoderrSS


class RobotContainer:
    """
    This class is where the bulk of the robot should be declared.  Since
    Command-based is a "declarative" paradigm, very little robot logic should
    actually be handled in the :class:`.Robot` periodic methods (other than
    the scheduler calls). Instead, the structure of the robot (including
    subsystems, commands, and button mappings) should be declared here.
    """

    def __init__(self):
        """
        The container for the robot. Contains subsystems, user controls,
        and commands.
        """
        # The robot's subsystems
        self.limit_sw = DigitalSensorSS(ELEC.limit_sw_DIO, "Limit Switch", invert=True)
        self.beam_break = DigitalSensorSS(ELEC.beam_break_DIO, "Beam Break")
        self.hall_eff = DigitalSensorSS(ELEC.hall_eff_DIO, "Hall Effect", invert=True)
        #self.ir = DigitalSensorSS(ELEC.IR_sensor_DIO, "IR Proximity Sensor")

        us_max_range = 512.0 / 2.54  # ultrasonic sensor max range: 512 cm
        self.ultra = AnalogSensorSS(ELEC.ultrasonic_sensor_AIO, "Ultrasonic range finder", low=0.0, high=us_max_range, round=1)

        self.encoder = TalonFXEncoderrSS(ELEC.talonfx_CAN_ID, "TalonFX encoder")

    def getAutonomousCommand(self):
        return None

    # No other code is needed!  Each subsystem updates the Smart Dashboard via
    # its periodic() method as long as the robot is enabled.
