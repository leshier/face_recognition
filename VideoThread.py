from UI_Window import Ui_MainWindow
from PyQt5.QtCore import *
import cv2
import numpy 
from PyQt5.QtGui import QImage
from PyQt5.QtCore import QThread
import face_recognition
import time
import configparser

class VideoThread(QThread,Ui_MainWindow):

    VideoFrame = pyqtSignal(QImage)
    OpenVideoFlag = pyqtSignal (bool)
    
    OpenInfoThread = pyqtSignal(list,numpy.ndarray)

    def __init__(self):
        super().__init__()

        


    def run(self):
        Config = configparser.ConfigParser()
        Config.read("Config.ini")
        self.fx = Config.get("face_location", "fx")
        self.fy = Config.get("face_location", "fy")
        self.number_of_times_to_upsample  = Config.get("face_location", "number_of_times_to_upsample")
        modelIndex  = int(Config.get("face_location", "model"))
        if modelIndex == 0:
            self.model = "hog"
        else:
            self.model = "cnn"
            
        self.Run_Video_Flag = 1
        self.cap = cv2.VideoCapture(0)
        if self.cap.isOpened():
            while self.Run_Video_Flag:
                ret, image = self.cap.read()
                # convert image to RGB format
                if ret:
                    processedimage = self.processedFrame(image)

                    # get image infos
                    height, width, channel = processedimage.shape
                    step = channel * width
                    # create QImage from image
                    qImg = QImage(processedimage.data, width, height, step, QImage.Format_RGB888)
                    if self.Run_Video_Flag:
                        self.VideoFrame.emit(qImg)
                    else:
                        break
                    time.sleep(0.02)
                else:
                    print("摄像头已打开，但无法read帧")

            self.cap.release()
            self.quit()   
        else:
            self.OpenVideoFlag.emit(self.cap.isOpened())
            
    def processedFrame(self,frame):
        small_frame = cv2.resize(frame, (0, 0), fx=float(self.fx), fy=float(self.fy))
        rgb_small_frame = small_frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_small_frame,number_of_times_to_upsample=int(self.number_of_times_to_upsample),model= self.model)#这里已经处理好了帧，将其缩小4倍，转为RGB

        if face_locations:
            self.OpenInfoThread.emit(face_locations,rgb_small_frame)
 
        for (top, right, bottom, left) in (face_locations):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom), (right, bottom), (0, 0, 255), cv2.FILLED)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return frame
    
    def Stop_Video(self):
        
        self.Run_Video_Flag = 0

