import io
import socket
import SocketServer
import threading
import struct
import cv2
import numpy as np
import time
#


sensor_data = False
controller_sock = ''

class ObjectDetection(object):

    def detect(self, cascade_classifier, gray, image):
        stop = cascade_classifier.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        # Draw a rectangle around the stop
        for (x, y, w, h) in stop:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            return w
            # if (w>110):
            #     print("GO")
            # elif (w>40):
            #     controller_sock.send("STOP")
            #     print("STOP")
            # else:
            #     print("GO")

class VideoStreamHandler(SocketServer.StreamRequestHandler):

    stop_classifier = cv2.CascadeClassifier('C:\OpenCV-3.1.0\opencv\sources\data\haarcascades\stop_sign.xml')
    object_detection = ObjectDetection()
    # rc_send = RCSend()

    def handle(self):
        stream_bytes = ' '
        global sensor_data
        try:
            while True:
                stream_bytes += self.rfile.read(1024)
                first = stream_bytes.find('\xff\xd8')
                last = stream_bytes.find('\xff\xd9')
                if first != -1 and last != -1:
                    jpg = stream_bytes[first:last+2]
                    stream_bytes = stream_bytes[last+2:]
                    image = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_UNCHANGED)

                    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

                    width = self.object_detection.detect(self.stop_classifier, gray, image)

                    cv2.imshow('Video', image)

                    if sensor_data is True:
                        print("Stop, obstacle in front")
                        controller_sock.send("STOP")
                        sensor_data = False
                        time.sleep(0.1)
                        print("I've just woken up")
                    elif 1 < width < 110:
                        print("Stop sign ahead")
                        controller_sock.send("STOP")
                    else:
                        print("GO")
                        controller_sock.send("GO")

                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
        finally:
            print 'connection closed at video thread'

class SensorDataHandler(SocketServer.BaseRequestHandler):

    data = " "

    def handle(self):
        global sensor_data
        try:
            while self.data:
                self.data = self.request.recv(20)
                if(self.data == "STOP"):
                    # controller_sock.send("STOP OBSTACLE")
                    sensor_data = True
                print self.data
        finally:
            print "Connection closed on sensor data"

class ThreadedServer(object):

    def video_thread(host, port):
        server = SocketServer.TCPServer((host, port), VideoStreamHandler)
        print("Server is listening to the video stream at port %s" %port)
        server.serve_forever()

    def sensor_thread(host, port):
        server = SocketServer.TCPServer((host, port), SensorDataHandler)
        server.serve_forever()

    def receiving_thread(host, port):
        global controller_sock
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host, port))
        s.listen(1)
        while True:
            sock, addr = s.accept()
            print("Client connected at %s" %port)
            controller_sock = sock

    # def ras_controller_thread(host, port):

    HOST, PORT = '172.16.51.218', 9009

    distance_thread = threading.Thread(target=sensor_thread, args=(HOST, PORT + 2))
    distance_thread.start()

    stop_thread = threading.Thread(target=video_thread, args=(HOST, PORT))
    stop_thread.start()

    receiving_thread = threading.Thread(target=receiving_thread, args=(HOST, PORT + 4))
    receiving_thread.start()
# controller_thread = threading.Thread(target=ras_controller_thread, args=(ip, port))

if __name__ == '__main__':
    ThreadedServer()
