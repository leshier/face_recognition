from UI_Window import Ui_MainWindow
from PyQt5.QtCore import *
import cv2
import numpy 
from PyQt5.QtGui import QImage
from PyQt5.QtCore import QThread
import time
# 21

class CameraThread(QThread,Ui_MainWindow):

    CameraFrame = pyqtSignal(QImage,numpy.ndarray)
    OpenCameraFlag = pyqtSignal (bool)


    def __init__(self):
        super().__init__()

    def run(self):
    
        self.Run_Camera_Flag = 1
        self.cap = cv2.VideoCapture(0)
        if self.cap.isOpened():
            while self.Run_Camera_Flag:
                ret, image = self.cap.read()
                # convert image to RGB format
                if ret:
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                    # get image infos
                    height, width, channel = image.shape
                    step = channel * width
                    # create QImage from image
                    qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
                    # show image in img_label
                    self.CameraFrame.emit(qImg,image)
                    # self.ui.image_label.setPixmap(QPixmap.fromImage(qImg))
                    time.sleep(0.02)
                else:
                    print("摄像头已打开，但无法read帧")
            self.cap.release()
            self.quit()   
        else:
            self.OpenCameraFlag.emit(self.cap.isOpened())

    def Stop_Video(self):
        self.Run_Camera_Flag = 0

