import sys
import socket
import select
import RPi.GPIO as GPIO
from time import sleep
import atexit

go_pin = 7 #Change pin accordingly
GPIO.setmode(GPIO.BOARD)
GPIO.setup(go_pin, GPIO.OUT)
GPIO.output(go_pin, GPIO.LOW)

def controller_client():

    host = '172.16.51.218'
    port = 9013

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

   # connect to remote host
    try:
       s.connect((host, port))
    except:
       print 'Unable to connect'
       sys.exit()
        

   # print 'Connected to remote host. You can start sending messages'
   # sys.stdout.write('[Me] '); sys.stdout.flush()
    
    while True:
       socket_list = [sys.stdin, s]

       # Get the list sockets which are readable
       read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])

       for sock in read_sockets:
           if sock == s:
               # incoming message from remote server, s
               data = sock.recv(1024)
               if not data:
                   print '\nDisconnected from chat server'
                   sys.exit()
               elif data == "STOP":
                   GPIO.output(go_pin, GPIO.LOW)
                   print data
                   sleep(3)
               elif data == "GO":
                   GPIO.output(go_pin, GPIO.HIGH)
                   print data
                   sleep(0.1)

               #elif data == "STOP OBSTACLE":
                   #GPIO.output(go_pin, GPIO.LOW)
               else:
                   sys.stdout.flush()
        
if __name__ == "__main__":
    atexit.register(GPIO.cleanup)
    sys.exit(controller_client())
    
    
