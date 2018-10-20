import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER1 = 18
GPIO_ECHO1 = 15

GPIO_TRIGGER2 = 12
GPIO_ECHO2 = 16

GPIO.setup(GPIO_TRIGGER1, GPIO.OUT)
GPIO.setup(GPIO_ECHO1, GPIO.IN)

GPIO.setup(GPIO_TRIGGER2, GPIO.OUT)
GPIO.setup(GPIO_ECHO2, GPIO.IN)

# senzor cu 6 fire
def distPamant():
	GPIO.output(GPIO_TRIGGER1, True)

	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER1, False)

	StartTime = time.time()
	StopTime = time.time()

	while GPIO.input(GPIO_ECHO1) == 0:
		StartTime = time.time()
	while GPIO.input(GPIO_ECHO1) == 1:
		StopTime = time.time()

	TimeElapsed = StopTime - StartTime
	
	distance = (TimeElapsed * 34300) / 2

	return distance

def distFata():
	GPIO.output(GPIO_TRIGGER2, True)

	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER2, False)

	StartTime = time.time()
	StopTime = time.time()

	while GPIO.input(GPIO_ECHO2) == 0:
		StartTime = time.time()
	while GPIO.input(GPIO_ECHO2) == 1:
		StopTime = time.time()
	
	distance = (StopTime - StartTime) * 34300 / 2
	
	return distance
 
# se apeleaza: ./nume_prog REF_PAMANT REF_FATA
if __name__ == '__main__':
	try:
		retVal = ""			
		distP = distPamant()
		distF = distFata()
		
		diff_P = sys.argv[1] - distP
		diff_F = sys.argv[2] - distF
		
		if (diff_P > 0):
			retVal += "u"
		elif (diff_P < 0):
			retVal += "d"
		else
			retVal += "x"
		
		if (diff_F > 0):
			retVal += "b"
		elif (diff_F < 0):
			retVal += "f"
		else
			retVal += "x"
	except KeyboardInterrupt:
		print("Measurement stopped by User")
		GPIO.cleanup()

	sys.stdout.write(retVal)

#retVal e de forma "- -" 
#retVal = "u ." : go up
#retVal = "d ." : go down
#retVal = ". f" : go forward
#retVal = ". b" : go backward
#retVal = "x ." : vertical ok
#retVal = ". x" : horizontal ok
