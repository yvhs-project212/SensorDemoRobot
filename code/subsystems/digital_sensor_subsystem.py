import wpilib
import commands2
from constants import ELEC
from libraries.p212 import DigitalSensor


class DigitalSensorSS(commands2.Subsystem):
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
    def __init__(self, dio_port, sensor_name, invert=False) -> None:
        """
        Creates a new DigitalSensorSS.

        Parameters: see the DigitalSensor class in the p212.py library.
        """
        super().__init__()
        self.switch = DigitalSensor(dio_port, sensor_name, invert=invert)

    def activated(self):
        """
        Return True if the digital sensor is activated, False if not.

        This method passes the call through to the underlying sensor's value()
        method, so it honors the :invert: setting.
        """
        return self.switch.value()

    def periodic(self):
        """
        Update the SmartDashboard if the robot is enabled.

        All DigitalSensorSSes will log their data on WPILib's SmartDashboard.
        """
        if wpilib.RobotState.isEnabled():
            data_field_name = f"{self.switch.name} (#{self.switch.io_port})"
            wpilib.SmartDashboard.putData(data_field_name, self.switch.sensor)
