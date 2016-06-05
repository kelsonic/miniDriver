# miniDriver
This is a Dev Bootcamp final project to program a self-driving rc car.

## Steps
### Day 1
As none of us had (much) experience with Python, we decided to concentrate on learning Python for the first half of the day. We flew through [this Udemy python bootcamp course](https://www.udemy.com/complete-python-bootcamp/) and together developed a solid understanding of Python fundamentals and data structures.

In the second half of the day, we concentrated on discovering and installing machine learning libraries (mostly OpenCV). We also delved into neural networks and found [this incredible repo](https://github.com/FlorianMuellerklein/Machine-Learning) that contains machine-learning algorithms for [perceptrons](http://neuralnetworksanddeeplearning.com/chap1.html).

In the evening (and night), we built a track for the rc car and aggregated resources for Day 2 to learn more about using Raspberry Pi with both RC cars and machine-learning libraries.

### Day 2
The morning consisted of studying more about machine-learning and neural networks. We also (finally) successfully installed OpenCV, mostly thanks to [this tutorial](https://www.youtube.com/watch?v=U49CVY8yOxw).

We then aggregated both positive and negative images for stop-lights and stop-signs. Using OpenCV, we then generated classifiers for both and tested it using our computers' webcams, which worked (though our algorithms definitely need more refining with extra positive and negative images).

Later in the evening, we had a visit from a data scientist who explained to us the power of both (numpy)[http://www.numpy.org/] and (matplotlib)[http://matplotlib.org/] python libraries.

### Day 3
We received the RC car in the early afternoon and quickly started taking apart the RC car controller. We connected a raspberry pi with the RC car controller while other members were working on getting the raspberry pi camera to send video to our computers via web sockets (a TCP server).

We were able to control the car from a remote computer via python commands. We spent the rest of the day training our classifiers for pedestrians.

We also wrote the python script to control the ultrasonic sensors and built out the hardware to incorporate both the ultrasonic sensors and the camera module.

### Day 4
In the morning, we got the video data from the camera module to send its data (a string of binaries) to our computer via the TCP server. We then converted each frame of the video data to a jpg file. As soon as we could convert the data to jpg files, we easily implemented our stop-sign classifier to recognize stop-signs in our streaming video (and we print out the width of the stop-sign in the jpg frames so that we can signal to the RC car to stop once it gets close enough to the stop-sign). 


