import RPi.GPIO as GPIO
import time
import socket

#create socket and bind host
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#client_socket.connect(('172.16.51.218', 9009))
client_socket.connect(('172.16.51.218', 9011))

GPIO.setmode(GPIO.BOARD)

TRIG = 7
ECHO = 12

GPIO.setup(TRIG, GPIO.OUT)
GPIO.output(TRIG, 0)

GPIO.setup(ECHO, GPIO.IN)

print "Starting measurement..."

try:
    while 1:

        GPIO.output(TRIG, 1)
        time.sleep(0.00001)
        GPIO.output(TRIG, 0)
        
        while GPIO.input(ECHO) == 0:
            pass
        start = time.time()

        while GPIO.input(ECHO) == 1:
            pass
        stop = time.time()

        distance = (stop - start) * 17000
        time.sleep(0.1)
        if distance <= 50:
            print "STOP"
            client_socket.send("STOP")
        else:
            print "GO"
except KeyboardInterrupt:
    GPIO.cleanup()
    client_socket.close()
