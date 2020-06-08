import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time # Import the sleep function from the time module

TRIG_NS = 15
TRIG_OW = 18
ECHO_N = 31
ECHO_S = 13
ECHO_O = 29
ECHO_W = 16
StartTimeN = 0
StopTimeN = 0
StartTimeS = 0
StopTimeS = 0
# GPIO.setmode(GPIO.BCM)
# defining and  initializing
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(32, GPIO.OUT, initial=GPIO.LOW) # white LED - Set pin 32 to be an output pin and set initial value to low (off)
GPIO.setup(33, GPIO.OUT, initial=GPIO.LOW) # white LED
GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW) # red LED
GPIO.setup(36, GPIO.OUT, initial=GPIO.LOW) # yellow LED
GPIO.setup(37, GPIO.OUT, initial=GPIO.LOW) # yellow LED
# defining and nitializing ultrasonic sensors
GPIO.setup(TRIG_NS, GPIO.OUT)
GPIO.setup(TRIG_OW, GPIO.OUT)
GPIO.setup(ECHO_N, GPIO.IN)
GPIO.setup(ECHO_S, GPIO.IN)
GPIO.setup(ECHO_O, GPIO.IN)
GPIO.setup(ECHO_W, GPIO.IN)

def NSdistance():
    # set Trigger to HIGH
    GPIO.output(TRIG_NS, True)
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(TRIG_NS, False)
 
    #StartTime = time.time()
    #StopTime = time.time()
 
    # North distance
    while GPIO.input(ECHO_N) == 0:
        StartTime = time.time()
    while GPIO.input(ECHO_N) == 1:
        StopTime = time.time()
    
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    Ndistance = (TimeElapsed * 34300) / 2
    
    # South distance
    GPIO.output(TRIG_NS, True)
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(TRIG_NS, False)
    
    while GPIO.input(ECHO_S) == 0:
        StartTimeS = time.time()
    while GPIO.input(ECHO_S) == 1:
        StopTimeS = time.time()
    TimeElapsed = StopTime - StartTime
    Sdistance = (TimeElapsed * 34300) / 2
    
    print('N dis = ',Ndistance,'\t','S dis = ',Sdistance)
#    return distance

def EWdistance():
    # set Trigger to HIGH
    GPIO.output(TRIG_OW, True)
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(TRIG_OW, False)
 
    #StartTime = time.time()
    #StopTime = time.time()
 
    # North distance
    while GPIO.input(ECHO_O) == 0:
        StartTime = time.time()
    while GPIO.input(ECHO_O) == 1:
        StopTime = time.time()
    
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    Edistance = (TimeElapsed * 34300) / 2
    
    # South distance
    GPIO.output(TRIG_OW, True)
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(TRIG_OW, False)
    
    while GPIO.input(ECHO_W) == 0:
        StartTimeS = time.time()
    while GPIO.input(ECHO_W) == 1:
        StopTimeS = time.time()
    TimeElapsed = StopTime - StartTime
    Wdistance = (TimeElapsed * 34300) / 2
    
    print('East dis = ',Edistance,'\t','West dis = ',Wdistance)
    
    
while True: # Run forever
    NSdistance()
    GPIO.output(32, GPIO.HIGH) # Turn on
    GPIO.output(33, GPIO.HIGH)
    GPIO.output(7, GPIO.HIGH)
    GPIO.output(36, GPIO.LOW)
    GPIO.output(37, GPIO.LOW)
    time.sleep(1) # Sleep for 1 second
    EWdistance()
    GPIO.output(32, GPIO.LOW) # Turn off
    GPIO.output(33, GPIO.LOW)
    GPIO.output(7, GPIO.LOW)
    GPIO.output(36, GPIO.HIGH)
    GPIO.output(37, GPIO.HIGH)
    time.sleep(1) # Sleep for 1 second