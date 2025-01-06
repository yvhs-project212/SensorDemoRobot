import wpilib
import commands2

import logging
logger = logging.getLogger("SensorSS")

class SensorSS(commands2.Subsystem):
    """
    SensorSS is a class to represent a commands2.Subsystem which essentially
    contains a sensor and nothing else.  The sensor reports its reading to
    the SmartDashboard periodically, when the robot is enabled.

    In normal use, a sensor is typically a small part of some subsystem.
    Within that subsystem, the sensor would be used to indicate a value to
    the subsystem, such as the distance to the wall or whether the subsystem
    has moved beyond its range.  In this normal use, a sensor is used with
    other sensors and actuators to perform the subsystem's function, such as
    moving an elevator between various stop points, or opening and closing
    a gripping mechanism, or activating an intake.

    However, for the sensor demo, our subsystem class will contain the sensor
    and hardly anything else.
    """

    # Subclasses of SensorSS must define their SENSOR_CLASS.  Examples of
    # likely SENSOR_CLASS values include libraries.p212.AnalogSensor,
    # libraries.p212.DigitalSensor, etc.  SENSOR_CLASS must define a value()
    # method that returns the underlying hardware sensor's value.  The class
    # must accept a constructor of the form called from SensorSS.__init__,
    # and have data members :name:, :io_port:, and :hardware_sensor:.
    #
    SENSOR_CLASS = None                # e.g. libraries.p212.AnalogSensor

    # Subclasses of SensorSS must define their SMARTDASHBOARD_PUT_METHOD,
    # depending on the type of data returned by SENSOR_CLASS's value()
    # method.  Examples of likely SMARTDASHBOARD_PUT_METHOD values include
    # wpilib.SmartDashboard.putNumber, wpilib.SmartDashboard.putBoolean, etc.
    #
    SMARTDASHBOARD_PUT_METHOD = None   # e.g. wpilib.SmartDashboard.putNumber

    def __init__(self, io_port, sensor_name, log_values_every_n_seconds=None,
                 **kwargs) -> None:
        """
        Creates a new SensorSS.

        Parameters: see the Sensor class in the p212.py library.
        """
        super().__init__()
        self.sensor = self.SENSOR_CLASS(io_port, sensor_name, **kwargs)
        self.log_values_every_n_secs = log_values_every_n_seconds

    def value(self):
        """
        Return the sensed value, as per the underlying AnalogSensor.
        """
        return self.sensor.value()

    def periodic(self):
        """
        Update the SmartDashboard if the robot is enabled.

        All AnalogSensorSSes will log their data on WPILib's SmartDashboard.
        """
        if wpilib.RobotState.isEnabled():
            data_field_name = f"{self.sensor.name} (#{self.sensor.io_port})"
            wpilib.SmartDashboard.putData(
                data_field_name, self.sensor.hardware_sensor)
            self.SMARTDASHBOARD_PUT_METHOD(data_field_name, self.sensor.value())

        if self.log_values_every_n_secs and wpilib.RobotState.isEnabled():
            if not hasattr(self, "count"):
                self.count = 0
                self.counts_between_logs = int(50*self.log_values_every_n_secs)
            self.count += 1
            if not self.count % self.counts_between_logs:
                logger.info(f"{self.sensor.name:>30} value is {self.sensor.value()}")
