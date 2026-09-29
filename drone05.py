from codrone_edu.drone import *

drone = Drone()
drone.pair()
drone.get_battery()
print(drone.get_battery())              

battery = drone.get_battery()           
print("Battery:", battery, "%")
drone.takeoff()
drone.hover(1)
drone.set_pitch(30)                        # lean forward, gently
distance = drone.get_front_range()

while distance > 50 and distance != 999:
    drone.move()
    distance = drone.get_front_range()      # update it, or the loop never changes
else:
    drone.set_pitch(0)                         # stop pushing forward
    drone.hover(1)
    drone.land()
drone.drone_LED_off()
drone.close()