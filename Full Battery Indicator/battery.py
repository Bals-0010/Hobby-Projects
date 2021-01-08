import psutil
from playsound import playsound

while True:
	bat=psutil.sensors_battery()
	per=int(bat.percent)
	if per==100:
		playsound('speak.mp3')
		break