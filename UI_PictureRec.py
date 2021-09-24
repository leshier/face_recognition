# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI_PictureRec.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PictureRec(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.ApplicationModal)
        Form.resize(763, 442)
        Form.setMinimumSize(QtCore.QSize(763, 424))
        Form.setMaximumSize(QtCore.QSize(763, 442))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/Images/ico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 450, 424))
        self.groupBox.setMinimumSize(QtCore.QSize(450, 424))
        self.groupBox.setMaximumSize(QtCore.QSize(450, 380))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem = QtWidgets.QSpacerItem(32, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem, 1, 5, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(31, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem1, 1, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(26, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem2, 0, 6, 1, 1)
        self.PicRecButton = QtWidgets.QPushButton(self.groupBox)
        self.PicRecButton.setObjectName("PicRecButton")
        self.gridLayout_6.addWidget(self.PicRecButton, 1, 4, 1, 1)
        self.SelectFileButton = QtWidgets.QPushButton(self.groupBox)
        self.SelectFileButton.setObjectName("SelectFileButton")
        self.gridLayout_6.addWidget(self.SelectFileButton, 1, 2, 1, 1)
        self.SelectFile = QtWidgets.QLabel(self.groupBox)
        self.SelectFile.setAlignment(QtCore.Qt.AlignCenter)
        self.SelectFile.setObjectName("SelectFile")
        self.gridLayout_6.addWidget(self.SelectFile, 0, 1, 1, 5)
        spacerItem3 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem3, 0, 0, 1, 1)
        self.FilePathEdit = QtWidgets.QLineEdit(self.groupBox)
        self.FilePathEdit.setObjectName("FilePathEdit")
        self.gridLayout_6.addWidget(self.FilePathEdit, 1, 3, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(465, 9, 289, 424))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 0, 0, 1, 2)
        self.NameEdit = QtWidgets.QLabel(self.groupBox_3)
        self.NameEdit.setText("")
        self.NameEdit.setObjectName("NameEdit")
        self.gridLayout_4.addWidget(self.NameEdit, 0, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 1, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 3, 0, 1, 1)
        self.SexEdit = QtWidgets.QLabel(self.groupBox_3)
        self.SexEdit.setText("")
        self.SexEdit.setObjectName("SexEdit")
        self.gridLayout_4.addWidget(self.SexEdit, 1, 2, 1, 1)
        self.InfoEdit = QtWidgets.QTextBrowser(self.groupBox_3)
        self.InfoEdit.setObjectName("InfoEdit")
        self.gridLayout_4.addWidget(self.InfoEdit, 3, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "图片识别"))
        self.groupBox.setTitle(_translate("Form", "选择照片"))
        self.PicRecButton.setText(_translate("Form", "识别"))
        self.SelectFileButton.setText(_translate("Form", "选择文件"))
        self.SelectFile.setText(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'华文琥珀\'; font-size:36pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#cbcbcb;\">照片</span></p></body></html>"))
        self.groupBox_3.setTitle(_translate("Form", "信息"))
        self.label_8.setText(_translate("Form", "姓名："))
        self.label_9.setText(_translate("Form", "性别："))
        self.label.setText(_translate("Form", "信息："))

import Images_rc
