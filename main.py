# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ENVui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import serial, serial.tools.list_ports
from numpy import mean
from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from PyQt5.QtCore import pyqtSignal, QThread
import sip

class Ui_EnvDevice(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self) #Setup UI Stuff

        self.back = Backend()
        self.back._enviroval.connect(self.dispval)
        self.back.start()

    # display values to UI
    def dispval(self,data):
        self.Value1.setText(str(data[0])) # eCO2 (ppm)
        self.Value2.setText(str(data[1])) # eCH2O (ug/m3)
        self.Value3.setText(str(data[2])) # TVOC (ug/m3)
        self.Value4.setText(str(data[3])) # PM2.5 (ug/m3)
        self.Value5.setText(str(data[4])) # PM10 (ug/m3)
        self.Value6.setText(str(data[5])) # Temp (C)
        self.Value7.setText(str(data[6])) # Humid (%RH)

    #Setup UI Stuff
    def setupUi(self, EnvDevice):
        EnvDevice.setObjectName("EnvDevice")
        EnvDevice.resize(300, 280)
        self.centralwidget = QtWidgets.QWidget(EnvDevice)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(300, 280))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        #Setup Labels
        font = QtGui.QFont()
        font.setPointSize(12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)

        self.Label1 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy.setHeightForWidth(self.Label1.sizePolicy().hasHeightForWidth())
        self.Label1.setSizePolicy(sizePolicy)
        self.Label1.setMinimumSize(QtCore.QSize(150, 0))
        self.Label1.setFont(font)
        self.Label1.setScaledContents(True)
        self.Label1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Label1.setObjectName("Label1")
        self.gridLayout.addWidget(self.Label1, 0, 0, 1, 1)

        self.Label2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy.setHeightForWidth(self.Label2.sizePolicy().hasHeightForWidth())
        self.Label2.setSizePolicy(sizePolicy)
        self.Label2.setMinimumSize(QtCore.QSize(150, 0))
        self.Label2.setFont(font)
        self.Label2.setScaledContents(True)
        self.Label2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Label2.setObjectName("Label2")
        self.gridLayout.addWidget(self.Label2, 1, 0, 1, 1)

        self.Label3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy.setHeightForWidth(self.Label3.sizePolicy().hasHeightForWidth())
        self.Label3.setSizePolicy(sizePolicy)
        self.Label3.setMinimumSize(QtCore.QSize(150, 0))
        self.Label3.setFont(font)
        self.Label3.setScaledContents(True)
        self.Label3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Label3.setObjectName("Label3")
        self.gridLayout.addWidget(self.Label3, 2, 0, 1, 1)

        self.Label4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy.setHeightForWidth(self.Label4.sizePolicy().hasHeightForWidth())
        self.Label4.setSizePolicy(sizePolicy)
        self.Label4.setMinimumSize(QtCore.QSize(150, 0))
        self.Label4.setFont(font)
        self.Label4.setScaledContents(True)
        self.Label4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Label4.setObjectName("Label4")
        self.gridLayout.addWidget(self.Label4, 3, 0, 1, 1)

        self.Label5 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy.setHeightForWidth(self.Label5.sizePolicy().hasHeightForWidth())
        self.Label5.setSizePolicy(sizePolicy)
        self.Label5.setMinimumSize(QtCore.QSize(150, 0))
        self.Label5.setFont(font)
        self.Label5.setTextFormat(QtCore.Qt.AutoText)
        self.Label5.setScaledContents(True)
        self.Label5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Label5.setObjectName("Label5")
        self.gridLayout.addWidget(self.Label5, 4, 0, 1, 1)

        self.Label6 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy.setHeightForWidth(self.Label6.sizePolicy().hasHeightForWidth())
        self.Label6.setSizePolicy(sizePolicy)
        self.Label6.setMinimumSize(QtCore.QSize(150, 0))
        self.Label6.setFont(font)
        self.Label6.setScaledContents(True)
        self.Label6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Label6.setObjectName("Label6")
        self.gridLayout.addWidget(self.Label6, 5, 0, 1, 1)

        self.Label7 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy.setHeightForWidth(self.Label7.sizePolicy().hasHeightForWidth())
        self.Label7.setSizePolicy(sizePolicy)
        self.Label7.setMinimumSize(QtCore.QSize(150, 0))
        self.Label7.setFont(font)
        self.Label7.setScaledContents(True)
        self.Label7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Label7.setObjectName("Label7")
        self.gridLayout.addWidget(self.Label7, 6, 0, 1, 1)

        # Setup Values
        self.Value1 = QtWidgets.QLabel(self.centralwidget)
        self.Value1.setFont(font)
        self.Value1.setAlignment(QtCore.Qt.AlignCenter)
        self.Value1.setObjectName("Value1")
        self.gridLayout.addWidget(self.Value1, 0, 1, 1, 1)

        self.Value2 = QtWidgets.QLabel(self.centralwidget)
        self.Value2.setFont(font)
        self.Value2.setAlignment(QtCore.Qt.AlignCenter)
        self.Value2.setObjectName("Value2")
        self.gridLayout.addWidget(self.Value2, 1, 1, 1, 1)

        self.Value3 = QtWidgets.QLabel(self.centralwidget)
        self.Value3.setFont(font)
        self.Value3.setAlignment(QtCore.Qt.AlignCenter)
        self.Value3.setObjectName("Value3")
        self.gridLayout.addWidget(self.Value3, 2, 1, 1, 1)

        self.Value4 = QtWidgets.QLabel(self.centralwidget)
        self.Value4.setFont(font)
        self.Value4.setAlignment(QtCore.Qt.AlignCenter)
        self.Value4.setObjectName("Value4")
        self.gridLayout.addWidget(self.Value4, 3, 1, 1, 1)

        self.Value5 = QtWidgets.QLabel(self.centralwidget)
        self.Value5.setFont(font)
        self.Value5.setAlignment(QtCore.Qt.AlignCenter)
        self.Value5.setObjectName("Value5")
        self.gridLayout.addWidget(self.Value5, 4, 1, 1, 1)

        self.Value6 = QtWidgets.QLabel(self.centralwidget)
        self.Value6.setFont(font)
        self.Value6.setAlignment(QtCore.Qt.AlignCenter)
        self.Value6.setObjectName("Value6")
        self.gridLayout.addWidget(self.Value6, 5, 1, 1, 1)

        self.Value7 = QtWidgets.QLabel(self.centralwidget)
        self.Value7.setFont(font)
        self.Value7.setAlignment(QtCore.Qt.AlignCenter)
        self.Value7.setObjectName("Value7")
        self.gridLayout.addWidget(self.Value7, 6, 1, 1, 1)

        EnvDevice.setCentralWidget(self.centralwidget)

        self.retranslateUi(EnvDevice)
        QtCore.QMetaObject.connectSlotsByName(EnvDevice)

    # Set Default Text
    def retranslateUi(self, EnvDevice):
        _translate = QtCore.QCoreApplication.translate
        EnvDevice.setWindowTitle(_translate("EnvDevice", "EnviroSense Viewer"))
        
        self.Label1.setText(_translate("EnvDevice", "eCO2 (ppm) :"))
        self.Label2.setText(_translate("EnvDevice", "eCH2O (ug/m3) :"))
        self.Label3.setText(_translate("EnvDevice", "TVOC (ug/m3) :"))
        self.Label4.setText(_translate("EnvDevice", "PM2.5 (ug/m3) :"))
        self.Label5.setText(_translate("EnvDevice", "PM10 (ug/m3) :"))
        self.Label6.setText(_translate("EnvDevice", "Temp (C) :"))
        self.Label7.setText(_translate("EnvDevice", "Humid (%RH) :"))

        self.Value1.setText("Value1")
        self.Value2.setText("Value2")
        self.Value3.setText("Value3")
        self.Value4.setText("Value4")
        self.Value5.setText("Value5")
        self.Value6.setText("Value6")
        self.Value7.setText("Value7")

class Backend(QtCore.QThread):
    _enviroval = QtCore.pyqtSignal(list)

    def __init__(self):
        self.encfound = True
        try:
            self.enc = serial.Serial(port='COM5',baudrate=38400,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,rtscts=True) #Optical Encoder config E1090BK25 chang chun hua te guang dian   
        except:
            self.encfound = False

'''
        ports = list(serial.tools.list_ports.comports()) #find all coms
        for comnum, comname, comadd in ports:  #find comport of seeeduino nano
            if "Silicon Labs CP210x USB to UART Bridge" in comname:
                self.com = serial.Serial(port=comnum,baudrate=38400,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,rtscts=True)

'''
    @property
    def readval(self):
        if self.encfound == True:
            self.enc.flushInput()
            self.encraw=self.enc.readline(5) # read 5 btyes of data {1: 0xff, 2: 0x81, 3: 2bits high [4pos], 4: 8bits low [255pos]}
            self.enc.flushInput()
                
            self.enchigh = int.from_bytes(self.encraw[2:3], byteorder='big')
            self.enclow = int.from_bytes(self.encraw[3:4], byteorder='big')
            self.encdeg = (self.enchigh*90) + round((self.enclow*90/256),1)
        else:
            self.encdeg = 0

        return self.encdeg

    def run(self): #QThread run
        while True:
            # self.vals = self.readval()
            self._enviroval.emit([1,2,3,4,5,5,6])

            QtTest.QTest.qWait(1000)

if __name__ == "__main__":
    ## Run GUI + Backend ##
    import sys
    app = QtWidgets.QApplication(sys.argv)

    ui = Ui_EnvDevice()
    ui.show()

    sys.exit(app.exec_())

    ## Run Backend only ##
    # ard = Backend()
    # ard.findport()
    # ard.run()