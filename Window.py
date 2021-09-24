from UI_Window import Ui_MainWindow
from UI_AboutSys import Ui_AboutSys
from UI_SettingUp import Ui_SettingUp
from UI_AddData import Ui_AddData
from UI_PictureRec import Ui_PictureRec

from PyQt5 import QtWidgets,QtGui
from PyQt5.QtGui import QPixmap
from VideoThread import VideoThread
from InfoThread import InfoThread
from CameraThread import CameraThread
import face_recognition
from qimage2ndarray import array2qimage
import configparser
import pymysql
import os


class AboutSys(QtWidgets.QDialog,Ui_AboutSys):
    def __init__(self):
        super(AboutSys,self).__init__()
        self.setupUi(self)
class SettingUp(QtWidgets.QWidget,Ui_SettingUp):
    def __init__(self):
        super(SettingUp,self).__init__()
        self.setupUi(self)
        Config = configparser.ConfigParser()
        ConfigPath = os.getcwd() + '/Config.ini'
        try:
            Config.read(ConfigPath)
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.warning(self,"警告","请检查配置文件Config.ini！") 
            
        fx = Config.get("face_location", "fx")
        fy = Config.get("face_location", "fy")
        number_of_times_to_upsample  = Config.get("face_location", "number_of_times_to_upsample")
        model  = Config.get("face_location", "model")

        num_jitters  = Config.get("face_encoding", "num_jitters")
        tolerance  = Config.get("face_encoding", "tolerance")
        
        
        self.Fx.setText(fx)
        self.Fy.setText(fy)
        self.Num_of_times_to_upsample.setText(number_of_times_to_upsample)
        self.Model_comboBox.setCurrentIndex(int(model))
        self.Num_jitters.setText(num_jitters)
        self.Tolerance.setText(tolerance)
    
        self.FaceLocationsButton.clicked.connect(self.Face_Location)
        self.FaceEncodingButton.clicked.connect(self.Face_Encoding)

    def Face_Location(self):
        cf = configparser.ConfigParser()
        ConfigPath = os.getcwd() + '/Config.ini'
       
        try:
            cf.read(ConfigPath)
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.warning(self,"警告","请检查配置文件Config.ini！")             
        # print(cf.sections())
        cf.set("face_location", "fx", self.Fx.text())
        cf.set("face_location", "fy", self.Fy.text())
        cf.set("face_location", "number_of_times_to_upsample", self.Num_of_times_to_upsample.text())
        cf.set("face_location", "model", str(self.Model_comboBox.currentIndex()))
        try:
            cf.write(open(ConfigPath, "w"))
        except Exception as e:
            print(e)
        self.close()
    def Face_Encoding(self):
        cf = configparser.ConfigParser()
        ConfigPath = os.getcwd() + '/Config.ini'
        try:
            cf.read(ConfigPath)
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.warning(self,"警告","请检查配置文件Config.ini！") 
            
        # print(cf.sections())
        cf.set("face_encoding", "num_jitters", self.Num_jitters.text())
        cf.set("face_encoding", "tolerance", self.Tolerance.text())
        try:
            cf.write(open(ConfigPath, "w"))
        except Exception as e:
            print(e)
        self.close()


class AddData(QtWidgets.QWidget,Ui_AddData):  
    def __init__(self):
        super(AddData,self).__init__()
        self.setupUi(self)
        self.camera = CameraThread()


        self.SelectFileButton.clicked.connect(self.selectfile)
        self.AddInfoButton.clicked.connect(self.addinfo)
        
        self.ResetButton.clicked.connect(self.reset)
        self.SetButton.clicked.connect(self.set)
        
        self.TakePictureButton.clicked.connect(self.takepicture)
        self.CameraAddInfoButton.clicked.connect(self.cameraaddinfo)

        self.camera.CameraFrame.connect(self.freshcamera)
        self.camera.OpenCameraFlag.connect(self.Un_Open)

        Config = configparser.ConfigParser()
        ConfigPath = os.getcwd() + '/Config.ini'
        try:
            Config.read(ConfigPath)
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.warning(self,"警告","请检查配置文件Config.ini！")             
        fx = Config.get("add_face", "fx")
        fy = Config.get("add_face", "fy")
        number_of_times_to_upsample  = Config.get("add_face", "number_of_times_to_upsample")
        model  = Config.get("add_face", "model")
        num_jitters  = Config.get("add_face", "num_jitters")
        tolerance  = Config.get("add_face", "tolerance")
        
        self.db_host = Config.get("db", "db_host")
        self.db_port = Config.get("db", "db_port")
        self.db_user = Config.get("db", "db_user")
        self.db_pass = Config.get("db", "db_pass")
        self.database = Config.get("db", "database")

        self.Fx.setText(fx)
        self.Fy.setText(fy)
        self.Numb_of_times_to_upsample.setText(number_of_times_to_upsample)
        self.Model_comboBox.setCurrentIndex(int(model))
        self.Num_jitters.setText(num_jitters)
        self.Tolerance.setText(tolerance)


    def selectfile(self):
        FilePath = QtWidgets.QFileDialog.getOpenFileName(self,"打开文件","/","Images(*.png *.jpg *.ico *.jpeg)")
        self.SelectFile.setScaledContents(True)

        self.SelectFile.setPixmap(QPixmap(FilePath[0]))
        self.FilePathEdit.setText(FilePath[0])
    
    def addinfo(self):
        name = self.NameEdit.text()
        sex = self.SexEdit.currentText()
        id_card = self.InfoEdit.toPlainText()

        if len(name) and len(sex) and len(id_card) and len(self.FilePathEdit.text()):
            image = face_recognition.load_image_file(self.FilePathEdit.text())
            face_encoding = face_recognition.face_encodings(image,num_jitters=int(self.Num_jitters.text()))
            if len(face_encoding):
                # print(face_encoding)
                db = pymysql.connect(host = self.db_host,port = int(self.db_port),user = self.db_user,passwd = self.db_pass,db = self.database,charset="utf8")
                cursor = db.cursor()
         
                sql = "insert into face(name,sex,id_card,encoding_0,encoding_1,encoding_2,encoding_3,encoding_4,encoding_5,encoding_6,encoding_7,encoding_8,encoding_9,encoding_10,encoding_11,encoding_12,encoding_13,encoding_14,encoding_15,encoding_16,encoding_17,encoding_18,encoding_19,encoding_20,encoding_21,encoding_22,encoding_23,encoding_24,encoding_25,encoding_26,encoding_27,encoding_28,encoding_29,encoding_30,encoding_31,encoding_32,encoding_33,encoding_34,encoding_35,encoding_36,encoding_37,encoding_38,encoding_39,encoding_40,encoding_41,encoding_42,encoding_43,encoding_44,encoding_45,encoding_46,encoding_47,encoding_48,encoding_49,encoding_50,encoding_51,encoding_52,encoding_53,encoding_54,encoding_55,encoding_56,encoding_57,encoding_58,encoding_59,encoding_60,encoding_61,encoding_62,encoding_63,encoding_64,encoding_65,encoding_66,encoding_67,encoding_68,encoding_69,encoding_70,encoding_71,encoding_72,encoding_73,encoding_74,encoding_75,encoding_76,encoding_77,encoding_78,encoding_79,encoding_80,encoding_81,encoding_82,encoding_83,encoding_84,encoding_85,encoding_86,encoding_87,encoding_88,encoding_89,encoding_90,encoding_91,encoding_92,encoding_93,encoding_94,encoding_95,encoding_96,encoding_97,encoding_98,encoding_99,encoding_100,encoding_101,encoding_102,encoding_103,encoding_104,encoding_105,encoding_106,encoding_107,encoding_108,encoding_109,encoding_110,encoding_111,encoding_112,encoding_113,encoding_114,encoding_115,encoding_116,encoding_117,encoding_118,encoding_119,encoding_120,encoding_121,encoding_122,encoding_123,encoding_124,encoding_125,encoding_126,encoding_127) values ('%s','%s','%s',%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g)"%(name,sex,id_card,face_encoding[0][0],face_encoding[0][1],face_encoding[0][2],face_encoding[0][3],face_encoding[0][4],face_encoding[0][5],face_encoding[0][6],face_encoding[0][7],face_encoding[0][8],face_encoding[0][9],face_encoding[0][10],face_encoding[0][11],face_encoding[0][12],face_encoding[0][13],face_encoding[0][14],face_encoding[0][15],face_encoding[0][16],face_encoding[0][17],face_encoding[0][18],face_encoding[0][19],face_encoding[0][20],face_encoding[0][21],face_encoding[0][22],face_encoding[0][23],face_encoding[0][24],face_encoding[0][25],face_encoding[0][26],face_encoding[0][27],face_encoding[0][28],face_encoding[0][29],face_encoding[0][30],face_encoding[0][31],face_encoding[0][32],face_encoding[0][33],face_encoding[0][34],face_encoding[0][35],face_encoding[0][36],face_encoding[0][37],face_encoding[0][38],face_encoding[0][39],face_encoding[0][40],face_encoding[0][41],face_encoding[0][42],face_encoding[0][43],face_encoding[0][44],face_encoding[0][45],face_encoding[0][46],face_encoding[0][47],face_encoding[0][48],face_encoding[0][49],face_encoding[0][50],face_encoding[0][51],face_encoding[0][52],face_encoding[0][53],face_encoding[0][54],face_encoding[0][55],face_encoding[0][56],face_encoding[0][57],face_encoding[0][58],face_encoding[0][59],face_encoding[0][60],face_encoding[0][61],face_encoding[0][62],face_encoding[0][63],face_encoding[0][64],face_encoding[0][65],face_encoding[0][66],face_encoding[0][67],face_encoding[0][68],face_encoding[0][69],face_encoding[0][70],face_encoding[0][71],face_encoding[0][72],face_encoding[0][73],face_encoding[0][74],face_encoding[0][75],face_encoding[0][76],face_encoding[0][77],face_encoding[0][78],face_encoding[0][79],face_encoding[0][80],face_encoding[0][81],face_encoding[0][82],face_encoding[0][83],face_encoding[0][84],face_encoding[0][85],face_encoding[0][86],face_encoding[0][87],face_encoding[0][88],face_encoding[0][89],face_encoding[0][90],face_encoding[0][91],face_encoding[0][92],face_encoding[0][93],face_encoding[0][94],face_encoding[0][95],face_encoding[0][96],face_encoding[0][97],face_encoding[0][98],face_encoding[0][99],face_encoding[0][100],face_encoding[0][101],face_encoding[0][102],face_encoding[0][103],face_encoding[0][104],face_encoding[0][105],face_encoding[0][106],face_encoding[0][107],face_encoding[0][108],face_encoding[0][109],face_encoding[0][110],face_encoding[0][111],face_encoding[0][112],face_encoding[0][113],face_encoding[0][114],face_encoding[0][115],face_encoding[0][116],face_encoding[0][117],face_encoding[0][118],face_encoding[0][119],face_encoding[0][120],face_encoding[0][121],face_encoding[0][122],face_encoding[0][123],face_encoding[0][124],face_encoding[0][125],face_encoding[0][126],face_encoding[0][127])
             
                try:
               
                    # 执行sql语句
                    cursor.execute(sql)
                    # 提交到数据库执行
                    db.commit()
                    QtWidgets.QMessageBox.information(self,"提示","训练完成，已成功加入数据库！") 
                    
                except Exception as e:
                    # 如果发生错误则回滚
                    db.rollback()  
                    print(e)      
                    QtWidgets.QMessageBox.warning(self,"警告","数据库连接失败") 
                    # 关闭数据库连接
                    db.close()
            else:
                QtWidgets.QMessageBox.warning(self,"警告","未能识别人脸，请重新上传")


        else:
            QtWidgets.QMessageBox.warning(self,"警告","所填内容不能为空！")
        
    def reset(self):
        self.Fx.setText("1")
        self.Fy.setText("1")
        self.Numb_of_times_to_upsample.setText("1")
        self.Model_comboBox.setCurrentIndex(0)
        self.Num_jitters.setText(1)
        self.Tolerance.setText(0.6)
    
    def set(self):
        cf = configparser.ConfigParser()

        ConfigPath = os.getcwd() +'/Config.ini'
        try:
            cf.read(ConfigPath)
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.warning(self,"警告","请检查配置文件Config.ini！") 
            
        # print(cf.sections())
        cf.set("add_face", "fx", self.Fx.text())
        cf.set("add_face", "fy", self.Fy.text())
        cf.set("add_face", "number_of_times_to_upsample", self.Numb_of_times_to_upsample.text())
        cf.set("add_face", "model", str(self.Model_comboBox.currentIndex()))
        cf.set("add_face", "num_jitters", self.Num_jitters.text())
        cf.set("add_face", "tolerance", self.Tolerance.text())
        try:
            cf.write(open(ConfigPath, "w"))
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.warning(self,"警告","请检查配置文件Config.ini！") 
            
        QtWidgets.QMessageBox.information(self,"提示","成功写入")

    def takepicture(self):
        if self.camera.isRunning():
            self.camera.Stop_Video()
        else:
            self.camera.start()

    def freshcamera(self,qImg,image):
        self.image = image
        self.CameraLabel.setPixmap(QPixmap.fromImage(qImg))
    def Un_Open(self,bool):
        QtWidgets.QMessageBox.warning(self,"警告","打开摄像头失败")
    
    def cameraaddinfo(self):
        name = self.CameraNameEdit.text()
        sex = self.CameraSexEdit.currentText()
        id_card = self.CameraInfoEdit.toPlainText()
        image = self.image
        if len(name) and len(sex) and len(id_card) and len(image):
            face_encoding = face_recognition.face_encodings(image,num_jitters=int(self.Num_jitters.text()))
            if len(face_encoding):
                db = pymysql.connect(host = self.db_host,port = int(self.db_port),user = self.db_user,passwd = self.db_pass,db = self.database,charset="utf8")
                cursor = db.cursor()
                sql = "insert into face(name,sex,id_card,encoding_0,encoding_1,encoding_2,encoding_3,encoding_4,encoding_5,encoding_6,encoding_7,encoding_8,encoding_9,encoding_10,encoding_11,encoding_12,encoding_13,encoding_14,encoding_15,encoding_16,encoding_17,encoding_18,encoding_19,encoding_20,encoding_21,encoding_22,encoding_23,encoding_24,encoding_25,encoding_26,encoding_27,encoding_28,encoding_29,encoding_30,encoding_31,encoding_32,encoding_33,encoding_34,encoding_35,encoding_36,encoding_37,encoding_38,encoding_39,encoding_40,encoding_41,encoding_42,encoding_43,encoding_44,encoding_45,encoding_46,encoding_47,encoding_48,encoding_49,encoding_50,encoding_51,encoding_52,encoding_53,encoding_54,encoding_55,encoding_56,encoding_57,encoding_58,encoding_59,encoding_60,encoding_61,encoding_62,encoding_63,encoding_64,encoding_65,encoding_66,encoding_67,encoding_68,encoding_69,encoding_70,encoding_71,encoding_72,encoding_73,encoding_74,encoding_75,encoding_76,encoding_77,encoding_78,encoding_79,encoding_80,encoding_81,encoding_82,encoding_83,encoding_84,encoding_85,encoding_86,encoding_87,encoding_88,encoding_89,encoding_90,encoding_91,encoding_92,encoding_93,encoding_94,encoding_95,encoding_96,encoding_97,encoding_98,encoding_99,encoding_100,encoding_101,encoding_102,encoding_103,encoding_104,encoding_105,encoding_106,encoding_107,encoding_108,encoding_109,encoding_110,encoding_111,encoding_112,encoding_113,encoding_114,encoding_115,encoding_116,encoding_117,encoding_118,encoding_119,encoding_120,encoding_121,encoding_122,encoding_123,encoding_124,encoding_125,encoding_126,encoding_127) values ('%s','%s','%s',%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g)"%(name,sex,id_card,face_encoding[0][0],face_encoding[0][1],face_encoding[0][2],face_encoding[0][3],face_encoding[0][4],face_encoding[0][5],face_encoding[0][6],face_encoding[0][7],face_encoding[0][8],face_encoding[0][9],face_encoding[0][10],face_encoding[0][11],face_encoding[0][12],face_encoding[0][13],face_encoding[0][14],face_encoding[0][15],face_encoding[0][16],face_encoding[0][17],face_encoding[0][18],face_encoding[0][19],face_encoding[0][20],face_encoding[0][21],face_encoding[0][22],face_encoding[0][23],face_encoding[0][24],face_encoding[0][25],face_encoding[0][26],face_encoding[0][27],face_encoding[0][28],face_encoding[0][29],face_encoding[0][30],face_encoding[0][31],face_encoding[0][32],face_encoding[0][33],face_encoding[0][34],face_encoding[0][35],face_encoding[0][36],face_encoding[0][37],face_encoding[0][38],face_encoding[0][39],face_encoding[0][40],face_encoding[0][41],face_encoding[0][42],face_encoding[0][43],face_encoding[0][44],face_encoding[0][45],face_encoding[0][46],face_encoding[0][47],face_encoding[0][48],face_encoding[0][49],face_encoding[0][50],face_encoding[0][51],face_encoding[0][52],face_encoding[0][53],face_encoding[0][54],face_encoding[0][55],face_encoding[0][56],face_encoding[0][57],face_encoding[0][58],face_encoding[0][59],face_encoding[0][60],face_encoding[0][61],face_encoding[0][62],face_encoding[0][63],face_encoding[0][64],face_encoding[0][65],face_encoding[0][66],face_encoding[0][67],face_encoding[0][68],face_encoding[0][69],face_encoding[0][70],face_encoding[0][71],face_encoding[0][72],face_encoding[0][73],face_encoding[0][74],face_encoding[0][75],face_encoding[0][76],face_encoding[0][77],face_encoding[0][78],face_encoding[0][79],face_encoding[0][80],face_encoding[0][81],face_encoding[0][82],face_encoding[0][83],face_encoding[0][84],face_encoding[0][85],face_encoding[0][86],face_encoding[0][87],face_encoding[0][88],face_encoding[0][89],face_encoding[0][90],face_encoding[0][91],face_encoding[0][92],face_encoding[0][93],face_encoding[0][94],face_encoding[0][95],face_encoding[0][96],face_encoding[0][97],face_encoding[0][98],face_encoding[0][99],face_encoding[0][100],face_encoding[0][101],face_encoding[0][102],face_encoding[0][103],face_encoding[0][104],face_encoding[0][105],face_encoding[0][106],face_encoding[0][107],face_encoding[0][108],face_encoding[0][109],face_encoding[0][110],face_encoding[0][111],face_encoding[0][112],face_encoding[0][113],face_encoding[0][114],face_encoding[0][115],face_encoding[0][116],face_encoding[0][117],face_encoding[0][118],face_encoding[0][119],face_encoding[0][120],face_encoding[0][121],face_encoding[0][122],face_encoding[0][123],face_encoding[0][124],face_encoding[0][125],face_encoding[0][126],face_encoding[0][127])                # print(sql)
                try:
                    
                    # 执行sql语句
                    cursor.execute(sql)
                    # 提交到数据库执行
                    db.commit()
                    QtWidgets.QMessageBox.information(self,"提示","训练完成，已成功加入数据库！") 
                    
                except Exception as e:
                    # 如果发生错误则回滚
                    db.rollback()  
                    print(e)      
                    QtWidgets.QMessageBox.warning(self,"警告","数据库连接失败") 
                    # 关闭数据库连接
                    db.close()
            else:
                QtWidgets.QMessageBox.warning(self,"警告","未能识别人脸，请重新拍照")


        else:
            QtWidgets.QMessageBox.warning(self,"警告","所填内容不能为空！")

class PictureRec(QtWidgets.QWidget,Ui_PictureRec):  
    def __init__(self):
        super(PictureRec,self).__init__()
        self.setupUi(self)
        self.SelectFileButton.clicked.connect(self.selectfile)
        self.PicRecButton.clicked.connect(self.picrec)
        
        Config = configparser.ConfigParser()

        ConfigPath = os.getcwd() + '/Config.ini'
        try:
            Config.read(ConfigPath)
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.warning(self,"警告","请检查配置文件Config.ini！")             
        self.fx = Config.get("add_face", "fx")
        self.fy = Config.get("add_face", "fy")
        self.number_of_times_to_upsample  = Config.get("add_face", "number_of_times_to_upsample")
        modelIndex  = int(Config.get("face_location", "model"))
        if modelIndex == 0:
            self.model = "hog"
        else:
            self.model = "cnn"

        self.num_jitters  = Config.get("add_face", "num_jitters")
        self.tolerance  = Config.get("add_face", "tolerance")

        self.db_host = Config.get("db", "db_host")
        self.db_port = Config.get("db", "db_port")
        self.db_user = Config.get("db", "db_user")
        self.db_pass = Config.get("db", "db_pass")
        self.database = Config.get("db", "database")

    def selectfile(self):
        
        FilePath = QtWidgets.QFileDialog.getOpenFileName(self,"打开文件","/","Images(*.png *.jpg *.ico *.jpeg)")
        self.SelectFile.setScaledContents(True)
        self.SelectFile.setPixmap(QPixmap(FilePath[0]))
        self.FilePathEdit.setText(FilePath[0])

    def picrec(self):
        if len(self.FilePathEdit.text()):
            try:
                image = face_recognition.load_image_file(self.FilePathEdit.text())
                face_locations = face_recognition.face_locations(image,number_of_times_to_upsample=int(self.number_of_times_to_upsample),model= self.model)#这里已经处理好了帧，将其缩小4倍，转为RGB
                self.face_encodings = face_recognition.face_encodings(image,face_locations,num_jitters=int(self.num_jitters))
                
                if len(self.face_encodings):
                    try:
                        self.db = pymysql.connect(host = self.db_host,port = int(self.db_port),user = self.db_user,passwd = self.db_pass,db = self.database,charset="utf8" )
                        self.cursor = self.db.cursor()
                        #self.sql = "SELECT * FROM user ORDER BY SQRT(POW(%g-encoding_0,2)+POW(%g-encoding_1,2)+POW(%g-encoding_2,2)+POW(%g-encoding_3,2)+POW(%g-encoding_4,2)+POW(%g-encoding_5,2)+POW(%g-encoding_6,2)+POW(%g-encoding_7,2)+POW(%g-encoding_8,2)+POW(%g-encoding_9,2)+POW(%g-encoding_10,2)+POW(%g-encoding_11,2)+POW(%g-encoding_12,2)+POW(%g-encoding_13,2)+POW(%g-encoding_14,2)+POW(%g-encoding_15,2)+POW(%g-encoding_16,2)+POW(%g-encoding_17,2)+POW(%g-encoding_18,2)+POW(%g-encoding_19,2)+POW(%g-encoding_20,2)+POW(%g-encoding_21,2)+POW(%g-encoding_22,2)+POW(%g-encoding_23,2)+POW(%g-encoding_24,2)+POW(%g-encoding_25,2)+POW(%g-encoding_26,2)+POW(%g-encoding_27,2)+POW(%g-encoding_28,2)+POW(%g-encoding_29,2)+POW(%g-encoding_30,2)+POW(%g-encoding_31,2)+POW(%g-encoding_32,2)+POW(%g-encoding_33,2)+POW(%g-encoding_34,2)+POW(%g-encoding_35,2)+POW(%g-encoding_36,2)+POW(%g-encoding_37,2)+POW(%g-encoding_38,2)+POW(%g-encoding_39,2)+POW(%g-encoding_40,2)+POW(%g-encoding_41,2)+POW(%g-encoding_42,2)+POW(%g-encoding_43,2)+POW(%g-encoding_44,2)+POW(%g-encoding_45,2)+POW(%g-encoding_46,2)+POW(%g-encoding_47,2)+POW(%g-encoding_48,2)+POW(%g-encoding_49,2)+POW(%g-encoding_50,2)+POW(%g-encoding_51,2)+POW(%g-encoding_52,2)+POW(%g-encoding_53,2)+POW(%g-encoding_54,2)+POW(%g-encoding_55,2)+POW(%g-encoding_56,2)+POW(%g-encoding_57,2)+POW(%g-encoding_58,2)+POW(%g-encoding_59,2)+POW(%g-encoding_60,2)+POW(%g-encoding_61,2)+POW(%g-encoding_62,2)+POW(%g-encoding_63,2)+POW(%g-encoding_64,2)+POW(%g-encoding_65,2)+POW(%g-encoding_66,2)+POW(%g-encoding_67,2)+POW(%g-encoding_68,2)+POW(%g-encoding_69,2)+POW(%g-encoding_70,2)+POW(%g-encoding_71,2)+POW(%g-encoding_72,2)+POW(%g-encoding_73,2)+POW(%g-encoding_74,2)+POW(%g-encoding_75,2)+POW(%g-encoding_76,2)+POW(%g-encoding_77,2)+POW(%g-encoding_78,2)+POW(%g-encoding_79,2)+POW(%g-encoding_80,2)+POW(%g-encoding_81,2)+POW(%g-encoding_82,2)+POW(%g-encoding_83,2)+POW(%g-encoding_84,2)+POW(%g-encoding_85,2)+POW(%g-encoding_86,2)+POW(%g-encoding_87,2)+POW(%g-encoding_88,2)+POW(%g-encoding_89,2)+POW(%g-encoding_90,2)+POW(%g-encoding_91,2)+POW(%g-encoding_92,2)+POW(%g-encoding_93,2)+POW(%g-encoding_94,2)+POW(%g-encoding_95,2)+POW(%g-encoding_96,2)+POW(%g-encoding_97,2)+POW(%g-encoding_98,2)+POW(%g-encoding_99,2)+POW(%g-encoding_100,2)+POW(%g-encoding_101,2)+POW(%g-encoding_102,2)+POW(%g-encoding_103,2)+POW(%g-encoding_104,2)+POW(%g-encoding_105,2)+POW(%g-encoding_106,2)+POW(%g-encoding_107,2)+POW(%g-encoding_108,2)+POW(%g-encoding_109,2)+POW(%g-encoding_110,2)+POW(%g-encoding_111,2)+POW(%g-encoding_112,2)+POW(%g-encoding_113,2)+POW(%g-encoding_114,2)+POW(%g-encoding_115,2)+POW(%g-encoding_116,2)+POW(%g-encoding_117,2)+POW(%g-encoding_118,2)+POW(%g-encoding_119,2)+POW(%g-encoding_120,2)+POW(%g-encoding_121,2)+POW(%g-encoding_122,2)+POW(%g-encoding_123,2)+POW(%g-encoding_124,2)+POW(%g-encoding_125,2)+POW(%g-encoding_126,2)+POW(%g-encoding_127,2)) LIMIT 1"%(face_encodings[0][0],face_encodings[0][1],face_encodings[0][2],face_encodings[0][3],face_encodings[0][4],face_encodings[0][5],face_encodings[0][6],face_encodings[0][7],face_encodings[0][8],face_encodings[0][9],face_encodings[0][10],face_encodings[0][11],face_encodings[0][12],face_encodings[0][13],face_encodings[0][14],face_encodings[0][15],face_encodings[0][16],face_encodings[0][17],face_encodings[0][18],face_encodings[0][19],face_encodings[0][20],face_encodings[0][21],face_encodings[0][22],face_encodings[0][23],face_encodings[0][24],face_encodings[0][25],face_encodings[0][26],face_encodings[0][27],face_encodings[0][28],face_encodings[0][29],face_encodings[0][30],face_encodings[0][31],face_encodings[0][32],face_encodings[0][33],face_encodings[0][34],face_encodings[0][35],face_encodings[0][36],face_encodings[0][37],face_encodings[0][38],face_encodings[0][39],face_encodings[0][40],face_encodings[0][41],face_encodings[0][42],face_encodings[0][43],face_encodings[0][44],face_encodings[0][45],face_encodings[0][46],face_encodings[0][47],face_encodings[0][48],face_encodings[0][49],face_encodings[0][50],face_encodings[0][51],face_encodings[0][52],face_encodings[0][53],face_encodings[0][54],face_encodings[0][55],face_encodings[0][56],face_encodings[0][57],face_encodings[0][58],face_encodings[0][59],face_encodings[0][60],face_encodings[0][61],face_encodings[0][62],face_encodings[0][63],face_encodings[0][64],face_encodings[0][65],face_encodings[0][66],face_encodings[0][67],face_encodings[0][68],face_encodings[0][69],face_encodings[0][70],face_encodings[0][71],face_encodings[0][72],face_encodings[0][73],face_encodings[0][74],face_encodings[0][75],face_encodings[0][76],face_encodings[0][77],face_encodings[0][78],face_encodings[0][79],face_encodings[0][80],face_encodings[0][81],face_encodings[0][82],face_encodings[0][83],face_encodings[0][84],face_encodings[0][85],face_encodings[0][86],face_encodings[0][87],face_encodings[0][88],face_encodings[0][89],face_encodings[0][90],face_encodings[0][91],face_encodings[0][92],face_encodings[0][93],face_encodings[0][94],face_encodings[0][95],face_encodings[0][96],face_encodings[0][97],face_encodings[0][98],face_encodings[0][99],face_encodings[0][100],face_encodings[0][101],face_encodings[0][102],face_encodings[0][103],face_encodings[0][104],face_encodings[0][105],face_encodings[0][106],face_encodings[0][107],face_encodings[0][108],face_encodings[0][109],face_encodings[0][110],face_encodings[0][111],face_encodings[0][112],face_encodings[0][113],face_encodings[0][114],face_encodings[0][115],face_encodings[0][116],face_encodings[0][117],face_encodings[0][118],face_encodings[0][119],face_encodings[0][120],face_encodings[0][121],face_encodings[0][122],face_encodings[0][123],face_encodings[0][124],face_encodings[0][125],face_encodings[0][126],face_encodings[0][127])
                        self.sql = "SELECT *,SQRT(POW(%g-encoding_0,2)+POW(%g-encoding_1,2)+POW(%g-encoding_2,2)+POW(%g-encoding_3,2)+POW(%g-encoding_4,2)+POW(%g-encoding_5,2)+POW(%g-encoding_6,2)+POW(%g-encoding_7,2)+POW(%g-encoding_8,2)+POW(%g-encoding_9,2)+POW(%g-encoding_10,2)+POW(%g-encoding_11,2)+POW(%g-encoding_12,2)+POW(%g-encoding_13,2)+POW(%g-encoding_14,2)+POW(%g-encoding_15,2)+POW(%g-encoding_16,2)+POW(%g-encoding_17,2)+POW(%g-encoding_18,2)+POW(%g-encoding_19,2)+POW(%g-encoding_20,2)+POW(%g-encoding_21,2)+POW(%g-encoding_22,2)+POW(%g-encoding_23,2)+POW(%g-encoding_24,2)+POW(%g-encoding_25,2)+POW(%g-encoding_26,2)+POW(%g-encoding_27,2)+POW(%g-encoding_28,2)+POW(%g-encoding_29,2)+POW(%g-encoding_30,2)+POW(%g-encoding_31,2)+POW(%g-encoding_32,2)+POW(%g-encoding_33,2)+POW(%g-encoding_34,2)+POW(%g-encoding_35,2)+POW(%g-encoding_36,2)+POW(%g-encoding_37,2)+POW(%g-encoding_38,2)+POW(%g-encoding_39,2)+POW(%g-encoding_40,2)+POW(%g-encoding_41,2)+POW(%g-encoding_42,2)+POW(%g-encoding_43,2)+POW(%g-encoding_44,2)+POW(%g-encoding_45,2)+POW(%g-encoding_46,2)+POW(%g-encoding_47,2)+POW(%g-encoding_48,2)+POW(%g-encoding_49,2)+POW(%g-encoding_50,2)+POW(%g-encoding_51,2)+POW(%g-encoding_52,2)+POW(%g-encoding_53,2)+POW(%g-encoding_54,2)+POW(%g-encoding_55,2)+POW(%g-encoding_56,2)+POW(%g-encoding_57,2)+POW(%g-encoding_58,2)+POW(%g-encoding_59,2)+POW(%g-encoding_60,2)+POW(%g-encoding_61,2)+POW(%g-encoding_62,2)+POW(%g-encoding_63,2)+POW(%g-encoding_64,2)+POW(%g-encoding_65,2)+POW(%g-encoding_66,2)+POW(%g-encoding_67,2)+POW(%g-encoding_68,2)+POW(%g-encoding_69,2)+POW(%g-encoding_70,2)+POW(%g-encoding_71,2)+POW(%g-encoding_72,2)+POW(%g-encoding_73,2)+POW(%g-encoding_74,2)+POW(%g-encoding_75,2)+POW(%g-encoding_76,2)+POW(%g-encoding_77,2)+POW(%g-encoding_78,2)+POW(%g-encoding_79,2)+POW(%g-encoding_80,2)+POW(%g-encoding_81,2)+POW(%g-encoding_82,2)+POW(%g-encoding_83,2)+POW(%g-encoding_84,2)+POW(%g-encoding_85,2)+POW(%g-encoding_86,2)+POW(%g-encoding_87,2)+POW(%g-encoding_88,2)+POW(%g-encoding_89,2)+POW(%g-encoding_90,2)+POW(%g-encoding_91,2)+POW(%g-encoding_92,2)+POW(%g-encoding_93,2)+POW(%g-encoding_94,2)+POW(%g-encoding_95,2)+POW(%g-encoding_96,2)+POW(%g-encoding_97,2)+POW(%g-encoding_98,2)+POW(%g-encoding_99,2)+POW(%g-encoding_100,2)+POW(%g-encoding_101,2)+POW(%g-encoding_102,2)+POW(%g-encoding_103,2)+POW(%g-encoding_104,2)+POW(%g-encoding_105,2)+POW(%g-encoding_106,2)+POW(%g-encoding_107,2)+POW(%g-encoding_108,2)+POW(%g-encoding_109,2)+POW(%g-encoding_110,2)+POW(%g-encoding_111,2)+POW(%g-encoding_112,2)+POW(%g-encoding_113,2)+POW(%g-encoding_114,2)+POW(%g-encoding_115,2)+POW(%g-encoding_116,2)+POW(%g-encoding_117,2)+POW(%g-encoding_118,2)+POW(%g-encoding_119,2)+POW(%g-encoding_120,2)+POW(%g-encoding_121,2)+POW(%g-encoding_122,2)+POW(%g-encoding_123,2)+POW(%g-encoding_124,2)+POW(%g-encoding_125,2)+POW(%g-encoding_126,2)+POW(%g-encoding_127,2)) as result from face order by result LIMIT 1"%(self.face_encodings[0][0],self.face_encodings[0][1],self.face_encodings[0][2],self.face_encodings[0][3],self.face_encodings[0][4],self.face_encodings[0][5],self.face_encodings[0][6],self.face_encodings[0][7],self.face_encodings[0][8],self.face_encodings[0][9],self.face_encodings[0][10],self.face_encodings[0][11],self.face_encodings[0][12],self.face_encodings[0][13],self.face_encodings[0][14],self.face_encodings[0][15],self.face_encodings[0][16],self.face_encodings[0][17],self.face_encodings[0][18],self.face_encodings[0][19],self.face_encodings[0][20],self.face_encodings[0][21],self.face_encodings[0][22],self.face_encodings[0][23],self.face_encodings[0][24],self.face_encodings[0][25],self.face_encodings[0][26],self.face_encodings[0][27],self.face_encodings[0][28],self.face_encodings[0][29],self.face_encodings[0][30],self.face_encodings[0][31],self.face_encodings[0][32],self.face_encodings[0][33],self.face_encodings[0][34],self.face_encodings[0][35],self.face_encodings[0][36],self.face_encodings[0][37],self.face_encodings[0][38],self.face_encodings[0][39],self.face_encodings[0][40],self.face_encodings[0][41],self.face_encodings[0][42],self.face_encodings[0][43],self.face_encodings[0][44],self.face_encodings[0][45],self.face_encodings[0][46],self.face_encodings[0][47],self.face_encodings[0][48],self.face_encodings[0][49],self.face_encodings[0][50],self.face_encodings[0][51],self.face_encodings[0][52],self.face_encodings[0][53],self.face_encodings[0][54],self.face_encodings[0][55],self.face_encodings[0][56],self.face_encodings[0][57],self.face_encodings[0][58],self.face_encodings[0][59],self.face_encodings[0][60],self.face_encodings[0][61],self.face_encodings[0][62],self.face_encodings[0][63],self.face_encodings[0][64],self.face_encodings[0][65],self.face_encodings[0][66],self.face_encodings[0][67],self.face_encodings[0][68],self.face_encodings[0][69],self.face_encodings[0][70],self.face_encodings[0][71],self.face_encodings[0][72],self.face_encodings[0][73],self.face_encodings[0][74],self.face_encodings[0][75],self.face_encodings[0][76],self.face_encodings[0][77],self.face_encodings[0][78],self.face_encodings[0][79],self.face_encodings[0][80],self.face_encodings[0][81],self.face_encodings[0][82],self.face_encodings[0][83],self.face_encodings[0][84],self.face_encodings[0][85],self.face_encodings[0][86],self.face_encodings[0][87],self.face_encodings[0][88],self.face_encodings[0][89],self.face_encodings[0][90],self.face_encodings[0][91],self.face_encodings[0][92],self.face_encodings[0][93],self.face_encodings[0][94],self.face_encodings[0][95],self.face_encodings[0][96],self.face_encodings[0][97],self.face_encodings[0][98],self.face_encodings[0][99],self.face_encodings[0][100],self.face_encodings[0][101],self.face_encodings[0][102],self.face_encodings[0][103],self.face_encodings[0][104],self.face_encodings[0][105],self.face_encodings[0][106],self.face_encodings[0][107],self.face_encodings[0][108],self.face_encodings[0][109],self.face_encodings[0][110],self.face_encodings[0][111],self.face_encodings[0][112],self.face_encodings[0][113],self.face_encodings[0][114],self.face_encodings[0][115],self.face_encodings[0][116],self.face_encodings[0][117],self.face_encodings[0][118],self.face_encodings[0][119],self.face_encodings[0][120],self.face_encodings[0][121],self.face_encodings[0][122],self.face_encodings[0][123],self.face_encodings[0][124],self.face_encodings[0][125],self.face_encodings[0][126],self.face_encodings[0][127])
                        
                        try:
                            self.cursor.execute(self.sql)
                            self.data = self.cursor.fetchone()
                            if self.data[132] > float(self.tolerance):
                                QtWidgets.QMessageBox.information(self,"提示","数据库中并无匹配信息！")
                            else:
                                self.NameEdit.setText(self.data[1])
                                self.SexEdit.setText(self.data[2])
                                self.InfoEdit.setText(self.data[3])

                        except Exception as e:
                            print(e)

                    except Exception as e:
                        print(e)
                        QtWidgets.QMessageBox.warning(self,"警告","数据库连接失败")
                        self.close()
                else:
                    QtWidgets.QMessageBox.warning(self,"警告","未能识别到人脸")
                    

            except Exception as e:
                print(e)
                QtWidgets.QMessageBox.warning(self,"警告","文件读取失败！请重试")
        
        else:
            
            QtWidgets.QMessageBox.warning(self,"警告","请选择文件")
            





class Window(QtWidgets.QMainWindow,Ui_MainWindow):

    def __init__(self):
        super(Window,self).__init__()
        self.setupUi(self)
        self.InitConfig()

        self.Video_Thread = VideoThread()#实例化Video线程
        self.Info_Thread = InfoThread()#实例化Info线程

        self.OpenVideoButton.clicked.connect(self.Open_Video_Thread)#点击OpenVideoButton按钮触发Open_Video_Thread函数
        # self.WriteDataConfigButton.clicked.connect(self.Write_Data_Config)
        # self.TestDataButton.clicked.connect(self.Test_Data)

        self.signButton.clicked.connect(self.Sign_Thread)

        self.AboutSysButton.triggered.connect(self.AboutSys)
        self.Setting_Location_Button.triggered.connect(self.Setting_Location)
        self.Setting_Encoding_Button.triggered.connect(self.Setting_Encoding)


        self.AddImageButton.triggered.connect(self.AddImage)
        self.AddCameraButton.triggered.connect(self.AddCamera)

        self.PictureRecButton.triggered.connect(self.picturerec)

        self.Video_Thread.VideoFrame.connect(self.Fresh_Video)#Video_Thread线程开启后捕捉摄像头调用Fresh_Video刷新界面
        self.Video_Thread.OpenVideoFlag.connect(self.Un_Open_Camera) #开启摄像头失败触发Un_Open_Camera函数
        self.Video_Thread.OpenInfoThread.connect(self.Info_Thread.SetData)#Video_Thread线程发出信号触发Info_Thread 线程开启
        self.Info_Thread.Sql_Info_Sin.connect(self.Fresh_info)

    def InitConfig(self):
        sm = QtGui.QStandardItemModel()
        sm.setHorizontalHeaderItem(0, QtGui.QStandardItem("Name"))
        sm.setHorizontalHeaderItem(1, QtGui.QStandardItem("ID_card"))
        sm.setHorizontalHeaderItem(2, QtGui.QStandardItem("Is_Sign"))

        Config = configparser.ConfigParser()
        ConfigPath = os.getcwd() + '/Config.ini'
        
        try:
            Config.read(ConfigPath)
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.warning(self,"警告","请检查配置文件Config.ini！") 
            
        db_host = Config.get("db", "db_host")
        db_port = Config.get("db", "db_port")
        db_user = Config.get("db", "db_user")
        db_pass = Config.get("db", "db_pass")
        database = Config.get("db", "database")

        try:
            db = pymysql.connect(host=db_host, port=int(db_port), user=db_user, passwd=db_pass, db=database,
                                 charset="utf8")
            cursor = db.cursor()
            self.table_sql = "select student_name,id_card,is_sign from user"
            try:
                # 执行sql语句
                cursor.execute(self.table_sql)
                # 提交到数据库执行
                data = cursor.fetchall()
                for index,i in enumerate(data):
                    sm.setItem(index, 0, QtGui.QStandardItem(i[0]))
                    sm.setItem(index, 1, QtGui.QStandardItem(i[1]))
                    sm.setItem(index, 2, QtGui.QStandardItem(i[2]))
                self.studentTable.setModel(sm)

            except Exception as e:
                # 如果发生错误则回滚
                db.rollback()
                print(e)
                QtWidgets.QMessageBox.warning(self, "警告", "签到失败")
                # 关闭数据库连接
                db.close()
            db.close()
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.warning(self, "警告", "数据库链接失败")
        # self.DataAddress.setText(db_host)
        # self.DataAddress.setEnabled(False)
        # self.DataPort.setText(db_port)
        # self.DataPort.setEnabled(False)
        # self.UserName.setText(db_user)
        # self.UserName.setEnabled(False)
        # self.PassWord.setText(db_pass)
        # self.PassWord.setEnabled(False)
        # self.Database.setText(database)
        # self.Database.setEnabled(False)
        
    def Write_Data_Config(self):
        if not self.DataAddress.isEnabled():
            self.DataAddress.setEnabled(True)
            self.DataPort.setEnabled(True)        
            self.UserName.setEnabled(True)        
            self.PassWord.setEnabled(True)        
            self.Database.setEnabled(True)
        else:
            cf = configparser.ConfigParser()

            ConfigPath = os.getcwd() + '/Config.ini'
            try:
                cf.read(ConfigPath)
            except Exception as e:
                print(e)
            QtWidgets.QMessageBox.warning(self,"警告","请检查配置文件Config.ini！") 
                
            # print(cf.sections())
            cf.set("db", "db_host", self.DataAddress.text())
            cf.set("db", "db_port", self.DataPort.text())
            cf.set("db", "db_user", self.UserName.text())
            cf.set("db", "db_pass", self.PassWord.text())
            cf.set("db", "database", self.Database.text())
            try:
                cf.write(open(ConfigPath, "w"))
            except Exception as e:
                print(e)
            
            self.DataAddress.setEnabled(False)
            self.DataPort.setEnabled(False)        
            self.UserName.setEnabled(False)        
            self.PassWord.setEnabled(False)        
            self.Database.setEnabled(False)
          
            QtWidgets.QMessageBox.information(self,"提示","修改成功")
            
    def Test_Data(self):
        Config = configparser.ConfigParser()

        ConfigPath = os.getcwd() + '/Config.ini'
        try:
            Config.read(ConfigPath)
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.warning(self,"警告","请检查配置文件Config.ini！") 
            
        db_host = Config.get("db", "db_host")
        db_port = Config.get("db", "db_port")
        db_user = Config.get("db", "db_user")
        db_pass = Config.get("db", "db_pass")
        database = Config.get("db", "database")
        try:
            db = pymysql.connect(host = db_host,port = int(db_port),user = db_user,passwd = db_pass,db = database,charset="utf8" )
            cursor = db.cursor()
            QtWidgets.QMessageBox.information(self,"提示","连接成功")            
            db.close()
        except Exception as e:
            # 如果发生错误则回滚

            QtWidgets.QMessageBox.warning(self,"警告","链接数据库失败，请检查配置文件或者\n检查数据库端链接设置")
            print(e)
        # 关闭数据库连接
       
    def Sign_Thread(self):
        Config = configparser.ConfigParser()

        ConfigPath = os.getcwd() + '/Config.ini'
        try:
            Config.read(ConfigPath)
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.warning(self, "警告", "请检查配置文件Config.ini！")

        db_host = Config.get("db", "db_host")
        db_port = Config.get("db", "db_port")
        db_user = Config.get("db", "db_user")
        db_pass = Config.get("db", "db_pass")
        database = Config.get("db", "database")

        id_card = self.InfoEdit.text()

        try:
            db = pymysql.connect(host=db_host, port=int(db_port), user=db_user, passwd=db_pass, db=database,
                                 charset="utf8")
            cursor = db.cursor()
            self.sign_sql = "update user set is_sign='1' where id_card = '%s' " %(id_card)
            try:
                # 执行sql语句
                cursor.execute(self.sign_sql)
                # 提交到数据库执行
                db.commit()
                QtWidgets.QMessageBox.information(self, "提示", "签到成功")

            except Exception as e:
                # 如果发生错误则回滚
                db.rollback()
                print(e)
                QtWidgets.QMessageBox.warning(self, "警告", "读取数据表有问题")
                # 关闭数据库连接
                db.close()
            db.close()

        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "警告", "链接数据库失败，请检查配置文件或者\n检查数据库端链接设置")
            print(e)

    def Open_Video_Thread(self):
        Config = configparser.ConfigParser()

        ConfigPath = os.getcwd() + '/Config.ini'
        try:
            Config.read(ConfigPath)
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.warning(self,"警告","请检查配置文件Config.ini！") 
            
        db_host = Config.get("db", "db_host")
        db_port = Config.get("db", "db_port")
        db_user = Config.get("db", "db_user")
        db_pass = Config.get("db", "db_pass")
        database = Config.get("db", "database")

        try:
            db = pymysql.connect(host = db_host,port = int(db_port),user = db_user,passwd = db_pass,db = database,charset="utf8" )
            cursor = db.cursor()
            db.close()
            if not self.Video_Thread.isRunning():
                self.Video_Thread.start()
                self.OpenVideoButton.setText("关闭摄像头")
            else:
                self.Video_Thread.Stop_Video()
                self.VideoLabel.setStyleSheet("border-image: url(:/pic/30.jpg);")
                self.VideoLabel.setText("")
                self.VideoLabel.setPixmap(QtGui.QPixmap(":/pic/Images/30.jpg"))

        except Exception as e:
            QtWidgets.QMessageBox.warning(self,"警告","链接数据库失败，请检查配置文件或者\n检查数据库端链接设置")
            print(e)
        

    def Fresh_Video(self,qImg):
        self.VideoLabel.setPixmap(QPixmap.fromImage(qImg))

    def Un_Open_Camera(self,bool):
        QtWidgets.QMessageBox.warning(self,"警告","打开摄像头失败")
        self.OpenVideoButton.setText("打开摄像头")


    def Fresh_info(self,Info,Face):
        if not self.NameEdit.text() == Info[1]:
            self.NameEdit.setText(Info[1])
            self.SexEdit.setText(Info[2])
            self.InfoEdit.setText(str(Info[3]))

            image = array2qimage(Face)
            self.FaceFrame.setPixmap(QPixmap.fromImage(image))
        else:
            pass

    def AboutSys(self):
        self.about = AboutSys()
        self.about.setModal(True)
        self.about.show()
    
    def Setting_Location(self):
        self.setting = SettingUp()
        self.setting.tabWidget.setCurrentIndex(0)
        self.setting.show()

    def Setting_Encoding(self):
        self.setting = SettingUp()
        self.setting.tabWidget.setCurrentIndex(1)
        self.setting.show()
    def AddImage(self):
        self.addimage = AddData()
        self.addimage.tabWidget.setCurrentIndex(0)
        self.addimage.show()
    def AddCamera(self):
        self.addcamera = AddData()
        self.addcamera.tabWidget.setCurrentIndex(1)
        self.addcamera.show()
    def picturerec(self):
        self.picrec = PictureRec()
        self.picrec.show()



def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
