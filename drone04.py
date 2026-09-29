from codrone_edu.drone import *

drone = Drone()
drone.connect()
data = drone.get_sensor_data()     # a list of 31 values
print(len(data))
drone.disconnect()