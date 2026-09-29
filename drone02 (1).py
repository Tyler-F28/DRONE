from codrone_edu.drone import *

drone = Drone()
drone.pair()

drone.takeoff()
drone.hover(1)
drone.square(33, 54, 33)


drone.land()
drone.close()