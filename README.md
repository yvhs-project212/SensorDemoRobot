# Project 212 Sensor Demo Robot

This repo provides robot code to run a demonstration of several types of
sensors.  Currently, the sensors include:
* Simple digital sensors
  * a [limit switch](https://github.com/yvhs-project212/sensors/tree/main/Limit-Switches)
  * a [Hall Effect sensor](https://github.com/yvhs-project212/sensors/tree/main/Hall-Effect)
  * an [infrared proximity sensor](https://github.com/yvhs-project212/sensors/tree/main/IR-Proximity-Sensors)
  * a [beam break sensor](https://github.com/yvhs-project212/sensors/tree/main/Break-Beam)
* Analog sensors
  * an [ultrasonic rangefinder](https://github.com/yvhs-project212/sensors/tree/main/Ultrasonic)


# Code structure

Unlike a real robot where a sensor would be a small part of a subsystem, in
this code each subsystem contains one sensor and nothing else.  The `commands2`
library (which defines the Subsystem base class) allows subsystems to implement
a `periodic()` method, which will get run automatically with each update -- it
doesn't need to be called from the robot's `periodic()` method.  We use this
feature to implement `periodic()` methods that update the Smart Dashboard with
each sensor subsystem's sensor value, as long as the robot is enabled.

Since there are no user controls (such as a joystick) which could trigger
robot actions, and since each sensor subsystem reads its sensor and updates
the dashboard... that's all the robot has to do!

