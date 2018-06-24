import os
import sys

from flask import Flask, Response, render_template

import config
from camera import Mp4Camera, UsbCamera, WebCamera

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


if config.is_usbcam:
    cameras = [UsbCamera(), UsbCamera(), UsbCamera(), UsbCamera()]


if config.is_mp4:
    base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    cameras = [Mp4Camera(os.path.join(base_dir, 'sample/sample0.mp4')),
               Mp4Camera(os.path.join(base_dir, 'sample/sample1.mp4')),
               Mp4Camera(os.path.join(base_dir, 'sample/sample2.mp4')),
               Mp4Camera(os.path.join(base_dir, 'sample/sample3.mp4'))]

if config.is_rtsp:
    cameras = [WebCamera(config.rtsp_urls[0]), WebCamera(config.rtsp_urls[1]),
               WebCamera(config.rtsp_urls[2]), WebCamera(config.rtsp_urls[3])]


@app.route('/video_feed/<int:id>')
def video_feed(id):
    return Response(gen(cameras[id]), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run()
