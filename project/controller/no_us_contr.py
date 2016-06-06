import io
import socket
import struct
import cv2
import numpy as np
from PIL import Image
import sys
import select

HOST = '172.16.51.218'
SOCKET_LIST = []
RECV_BUFFER = 4096
PORT = 9009
stopCascade = cv2.CascadeClassifier('C:\OpenCV-3.1.0\opencv\sources\data\haarcascades\stop_sign.xml')


def control_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(2)
    SOCKET_LIST.append(server_socket)
    print "controller server started on port ", PORT
    while 1:
        ready_to_read, ready_to_write, in_error = select.select(SOCKET_LIST, [], [], 0)
        for sock in ready_to_read:
            if sock == server_socket:
                sockfd, addr = server_socket.accept()
                SOCKET_LIST.append(sockfd)
                print "Client (%s, %s) connected" % addr

            elif len(SOCKET_LIST) == 4:
                # process data recieved from client,

                camera_connection = SOCKET_LIST[1].makefile('rb')

                try:
                    # receiving data from the socket.
                    show_stream(sock, camera_connection, server_socket)

                # exception
                except:
                    broadcast(server_socket, sock, "Client (%s, %s) is offline\n" % addr)
                    continue
    server_socket.close()


def show_stream(sock, camera_connection, server_socket):
    while True:
        # Read the length of the image as a 32-bit unsigned int. If the
        # length is zero, quit the loop
        image_len = struct.unpack('<L', camera_connection.read(struct.calcsize('<L')))[0]
        if not image_len:
            break
        # Construct a stream to hold the image data and read the image
        # data from the camera_connection
        image_stream = io.BytesIO()
        image_stream.write(camera_connection.read(image_len))
        # Rewind the stream, open it as an image with PIL and do some
        # processing on it
        image_stream.seek(0)
        image = Image.open(image_stream)

        # image.show()

        image = np.array(image)
        frame = image

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        stop = stopCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        # Draw a rectangle around the stop
        for (x, y, w, h) in stop:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            if (w>110):
                broadcast(server_socket, sock, "GO")
                print("GO")
            elif (w>100):
                broadcast(server_socket, sock, "STOP")
                print("STOP")
            else:
                broadcast(server_socket, sock, "GO")
                print("GO")

        cv2.imshow('Video', frame)
        cv2.waitKey(1)
        if  cv2.waitKey(1) & 0xFF == ord('q'):
            break

def broadcast (server_socket, sock, message):
    for socket in SOCKET_LIST:
        # send the message only to peer
        if socket != server_socket and socket != sock :
            try :
                socket.send(message)
            except :
                # broken socket connection
                socket.close()
                # broken socket, remove it
                if socket in SOCKET_LIST:
                    SOCKET_LIST.remove(socket)

if __name__ == "__main__":

    sys.exit(control_server())
