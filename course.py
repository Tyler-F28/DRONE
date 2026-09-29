from codrone_edu.drone import *

drone = Drone()
drone.connect()

drone.takeoff()
drone.hover(2)
drone.move_forward(170, 'cm', 1)
drone.turn_right()
drone.move_forward(83,'cm', 1)
drone.turn_left()
drone.move_forward(170, 'cm', 1)
drone.turn_right()
drone.move_forward(100, 'cm', 1)
drone.land()
drone.disconnect()