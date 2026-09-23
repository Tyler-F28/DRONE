from codrone_edu.drone import *

drone = Drone()
drone.connect()

from codrone_edu.drone import *

drone = Drone()
drone.pair()

print("Battery:", drone.get_battery(), "%")
drone.set_drone_LED(0, 255, 35, 100)    # green, full brightness
drone.drone_buzzer(440, 500)    # 440 Hz for 500 milliseconds
drone.takeoff()      # lift to about 80 cm and hover
drone.hover(1)       # stay there for 3 seconds
drone.land()         # settle down

drone.close()
drone.disconnect()