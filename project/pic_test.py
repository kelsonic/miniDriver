import io
import socket
import struct
import cv2
import numpy as np
from PIL import Image

# Start a socket listening for connections on 0.0.0.0:8000 (0.0.0.0 means
# all interfaces)
server_socket = socket.socket()
port = 8007
server_socket.bind(('172.16.51.218', port))
server_socket.listen(0)
print("Server is listening at port %s" %port)

# Accept a single connection and make a file-like object out of it
connection = server_socket.accept()[0].makefile('rb')

stopCascade = cv2.CascadeClassifier('C:\OpenCV-3.1.0\opencv\sources\data\haarcascades\stop_sign.xml')


try:
    while True:
        # Read the length of the image as a 32-bit unsigned int. If the
        # length is zero, quit the loop
        image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
        if not image_len:
            break
        # Construct a stream to hold the image data and read the image
        # data from the connection
        image_stream = io.BytesIO()
        image_stream.write(connection.read(image_len))
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
                print("GO")
            elif (w>100):
                print("STOP")
            else:
                print("GO")

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


        # cv2.imshow('image', image)
        # cv2.waitKey(10)
        # print(image)

        # print('Image is %dx%d' % image.size)
        # image.verify()
        # print('Image is verified')
finally:
    connection.close()
    server_socket.close()