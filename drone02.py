from codrone_edu.drone import *

drone = Drone()
drone.pair()

drone.takeoff()
drone.hover(1)

for i in range(4):                  # do this four times
    drone.move_forward(50, "cm", 1)
    drone.turn_left()               # turn 90 from where it is facing now

drone.land()
drone.close()