# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI_SettingUp.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SettingUp(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.ApplicationModal)
        Form.resize(460, 350)
        Form.setMinimumSize(QtCore.QSize(460, 350))
        Form.setMaximumSize(QtCore.QSize(478, 368))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/Images/ico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.Fx = QtWidgets.QLineEdit(self.groupBox)
        self.Fx.setObjectName("Fx")
        self.horizontalLayout.addWidget(self.Fx)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.Fy = QtWidgets.QLineEdit(self.groupBox)
        self.Fy.setObjectName("Fy")
        self.horizontalLayout.addWidget(self.Fy)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.Num_of_times_to_upsample = QtWidgets.QLineEdit(self.groupBox)
        self.Num_of_times_to_upsample.setMinimumSize(QtCore.QSize(110, 0))
        self.Num_of_times_to_upsample.setMaximumSize(QtCore.QSize(110, 16777215))
        self.Num_of_times_to_upsample.setObjectName("Num_of_times_to_upsample")
        self.horizontalLayout_2.addWidget(self.Num_of_times_to_upsample)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.Model_comboBox = QtWidgets.QComboBox(self.groupBox)
        self.Model_comboBox.setObjectName("Model_comboBox")
        self.Model_comboBox.addItem("")
        self.Model_comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.Model_comboBox)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(163, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 1, 0, 1, 1)
        self.FaceLocationsButton = QtWidgets.QPushButton(self.tab)
        self.FaceLocationsButton.setMinimumSize(QtCore.QSize(75, 23))
        self.FaceLocationsButton.setMaximumSize(QtCore.QSize(75, 23))
        self.FaceLocationsButton.setObjectName("FaceLocationsButton")
        self.gridLayout_3.addWidget(self.FaceLocationsButton, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(163, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 1, 2, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 0, 0, 1, 1)
        self.Num_jitters = QtWidgets.QLineEdit(self.groupBox_2)
        self.Num_jitters.setObjectName("Num_jitters")
        self.gridLayout_5.addWidget(self.Num_jitters, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 0, 2, 1, 1)
        self.Tolerance = QtWidgets.QLineEdit(self.groupBox_2)
        self.Tolerance.setObjectName("Tolerance")
        self.gridLayout_5.addWidget(self.Tolerance, 0, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_5.addWidget(self.label_8, 1, 0, 1, 4)
        self.gridLayout_4.addWidget(self.groupBox_2, 0, 0, 1, 3)
        spacerItem3 = QtWidgets.QSpacerItem(163, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 1, 0, 1, 1)
        self.FaceEncodingButton = QtWidgets.QPushButton(self.tab_2)
        self.FaceEncodingButton.setObjectName("FaceEncodingButton")
        self.gridLayout_4.addWidget(self.FaceEncodingButton, 1, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(162, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem4, 1, 2, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "????????????"))
        self.groupBox.setTitle(_translate("Form", "Face_Locations"))
        self.label.setText(_translate("Form", "fx:"))
        self.label_2.setText(_translate("Form", "fy:"))
        self.label_4.setText(_translate("Form", "number_of_times_to_upsample:"))
        self.label_5.setText(_translate("Form", "model:"))
        self.Model_comboBox.setItemText(0, _translate("Form", "HOG"))
        self.Model_comboBox.setItemText(1, _translate("Form", "CNN"))
        self.label_3.setText(_translate("Form", "Tips:fx???fy??????????????????????????????Face_Location????????????resize????????????\n"
"???????????????Face_Location?????????????????????????????????????????????(????????????1)???\n"
"number_of_times_to_upsample?????????????????????????????????????????????????????????\n"
"????????????????????????????????????????????????1??????\n"
"model:???????????????????????????????????????HOG??????cpu???????????????????????????????????????\n"
"???CNN???????????????????????????????????????????????????gpu/cuda?????????????????????????????????\n"
"??????????????????HOG??????"))
        self.FaceLocationsButton.setText(_translate("Form", "??????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "??????????????????"))
        self.groupBox_2.setTitle(_translate("Form", "Face_Encoding"))
        self.label_6.setText(_translate("Form", "num_jitters:"))
        self.label_7.setText(_translate("Form", "tolerance:"))
        self.label_8.setText(_translate("Form", "Tips:num_jitters:????????????????????????????????????????????????????????????????????????\n"
"?????????????????????1??????\n"
"tolerance:???????????????????????????????????????????????????????????????0.6????????????\n"
"???????????????"))
        self.FaceEncodingButton.setText(_translate("Form", "??????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "??????????????????"))

import Images_rc
