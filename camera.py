from time import sleep
from threading import Lock
import cv2


class UsbCamera:
    def __init__(self):
        self.capture_ = cv2.VideoCapture(0)
        if not self.capture_.isOpened():
            raise("IO Error")

    def get_frame(self):
        ret, image = self.capture_.read()
        if not ret:
            print('Error frame')
        return cv2.imencode('.jpg', image)[1].tobytes()


class Mp4Camera:
    def __init__(self, filename):
        self.capture_ = cv2.VideoCapture(filename)
        if not self.capture_.isOpened():
            raise("IO Error")

    def get_frame(self):
        sleep(0.066)
        ret, image = self.capture_.read()
        if not ret:
            print('Error frame')
        return cv2.imencode('.jpg', image)[1].tobytes()


class WebCamera:
    def __init__(self, url):
        self.capture_ = cv2.VideoCapture(url)
        if not self.capture_.isOpened():
            raise("IO Error")

    def get_frame(self):
        ret, image = self.capture_.read()
        if not ret:
            print('Error frame')
        return cv2.imencode('.jpg', image)[1].tobytes()
