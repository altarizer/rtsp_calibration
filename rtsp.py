
import cv2
from threading import Thread, Lock

class rtsp(Thread):

  def __init__(self, EP):
    Thread.__init__(self)
    self.vcap = cv2.VideoCapture()
    self.vcap.open(EP)
    self.endpoint = EP
    self.frame = None
    self.lock = Lock()
    self.daemon = True

  def run(self):
    while True:

      result, frame = self.vcap.read()
      if result :
        self.lock.acquire()
        self.frame = frame
        self.lock.release()


  def get_frame(self):

    self.lock.acquire()
    frame = self.frame
    self.lock.release()
    return frame
