# Initialize the DistanceSensor using GPIO librayy
#Trigger pin is connected to GPIO 4, Echo pin to
from gpiozero import DistanceSensor
from time import sleep
from gpiozero import LED
sensor = DistanceSensor(echo=17, trigger=4, max_distance = 2)
led=LED(18)
try:
	while True:
		dis = sensor.distance*100
		print('Distance: {:.2f} cm'.format(dis))
		sleep(0.3)
		if dis<50:
			led.on() 
except KeyboardInterrupt:
	pass
