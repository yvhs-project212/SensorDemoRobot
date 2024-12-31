import wpilib
from wpiutil import SendableBuilder


class Sensor:
  """
  This class represents a simple digital or analog sensor, plugged into one
  of the RoboRIO's DIO or AIO ports respectively.
  """
  # SENSOR_CLASS must be a Sendable, since we call SmartDashboard.putData()
  # with it.
  #
  SENSOR_CLASS = None

  def __init__(self, io_port, name) -> None:
    """
    Create a new Sensor.  Users must use the subclasses DigitalSensor or
    AnalogSensor instead of this class.
    """
    super().__init__()
    self.io_port = io_port
    self.sensor = self.SENSOR_CLASS(io_port)
    self.name = name

  def initSendable(self, builder: SendableBuilder) -> None:
    builder.setSmartDashboardType("Subsystem")
    builder.addDoubleProperty(".value", lambda: self.value(), lambda: None)

  def value(self):
    pass


class DigitalSensor(Sensor):
  """
  This class represents a subsystem consisting of a simple digital sensor,
  plugged into one of the RoboRIO's Digital I/O (DIO) ports.  The sensor
  has no external inputs (just what's onboard the sensor), and produces a
  single binary output.  Examples of these simple digital sensors include:
    * limit switches
    * IR proximity sensors
    * Hall Effect sensors
    * break-beam sensors
  """
  SENSOR_CLASS = wpilib.DigitalInput

  def __init__(self, dio_port, name, invert=False) -> None:
    """
    Create a new DigitalSensor.

    Parameters:
     dio_port (int): the RoboRIO Digital I/O port where the sensor is found
     name (str): a label identifying this sensor
     invert (boolean): whether to invert the logic sense of the sensor, i.e.
       True if 5V on the DIO port means a sensor value of False.
    """
    super().__init__(dio_port, name)
    self.invert = invert

  def value(self):
    """
    Return the (boolean) logical value of this sensor, taking into account
    the invert setting.
    """
    return (not self.sensor.get()) if self.invert else (self.sensor.get())


class AnalogSensor(Sensor):
  """
  This class represents a simple analog sensor,
  plugged into one of the RoboRIO's Analog I/O (AIO) ports.  The sensor
  has no external inputs (just what's onboard the sensor), and produces a
  single continuous-voltage output.  Examples of these simple analog sensors
  include:
    * ultrasonic sensors
  """
  SENSOR_CLASS = wpilib.AnalogInput
  def __init__(self, aio_port, name, low=0.0, high=1.0, round=None) -> None:
    """
    Create a new AnalogSensor.

    Parameters:
     aio_port (int): the RoboRIO Analog I/O port where the sensor is found
     name (str): a label identifying this sensor

     low (float): the desired minimum value to report from the sensor
     high (float): the desired maximum value to report from the sensor
     round (int or None): the optional number of decimal places to round
       the result to

    For example, if low=10 and high=20, then (on a fresh battery) a reading
    of 0V on the AIO pin will result in value() returning 10.0, and a
    reading of 5V on the AIO pin will result in value() returning 20.0.
    """
    super().__init__(aio_port, name)
    self.low = low
    self.high = high
    self.round = round

  def raw_unscaled_value(self):
    """
    Return the raw sensor reading, not adjusted for battery voltage sag and
    not scaled to the requested range (:low: to :high:).
    """
    return self.sensor.getVoltage()

  def battery_adjusted_value(self):
    """
    Return the sensor reading adjusted for battery voltage sag, but
    not scaled to the requested range (:low: to :high:).  Adjusting for the
    battery voltage sag divides the reading by the actual voltage on the
    RoboRIO's nominal-5V supply, so the adjusted value is normally between
    0 and 1.
    """
    v_batt = wpilib.RobotController.getVoltage5V()
    return self.raw_unscaled_value() / v_batt

  def value(self):
    """
    Return the sensor value adjusted for battery voltage sag and scaled to
    the requested range (:low: to :high:), optionally rounded to the number
    of decimal places specified in the constructor.

    This is the accessor method that users will most often want to call.
    """
    tempval = self.low + (
        self.battery_adjusted_value() * (self.high - self.low))
    if self.round:
        tempval = int(tempval * 10**self.round) / 10**self.round
    return tempval

