import cv2


class Camera:
    def __init__(self):
        self.capture_ = cv2.VideoCapture(0)
        if not self.capture_.isOpened():
            raise("IO Error")

    def get_frame(self):
        ret, image = self.capture_.read()
        if not ret:
            print('Error frame')
        return cv2.imencode('.jpg', image)[1].tobytes()
