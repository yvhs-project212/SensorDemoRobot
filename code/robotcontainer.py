# Copyright (c) YVHS Robotics Booster Club and Project 212 (#7137).
# Open Source Software; you can modify and/or share it under the terms of
# license file in the root directory of this project.
#

import wpilib
import commands2

from constants import ELEC
from subsystems.digital_sensor_subsystem import DigitalSensorSS


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
        self.limit_sw = DigitalSensorSS(ELEC.limit_sw_DIO, "Limit Switch")
        self.beam_break = DigitalSensorSS(ELEC.beam_break_DIO, "Beam Break")
        self.hall_eff = DigitalSensorSS(ELEC.hall_eff_DIO, "Hall Effect")
        self.ir = DigitalSensorSS(ELEC.IR_sensor_DIO, "IR Proximity Sensor")

    # No other code is needed!  Each subsystem updates the Smart Dashboard via
    # its periodic() method as long as the robot is enabled.
