# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt.ui'
#
# Created: Sun Feb 15 16:26:54 2015
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import cv2 as cv

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(806, 772)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setContentsMargins(-1, -1, -1, 600)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.verticalLayout.addLayout(self.formLayout)
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        #self.lineEdit_2.setToolTipDuration(-1)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.lineEdit_2)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.lineEdit_3)
        self.lineEdit_4 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_4)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.FieldRole, self.pushButton)
        self.verticalLayout.addLayout(self.formLayout_3)
        #MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 806, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        #MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        #MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.ImageFromCam(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        MainWindow.setAccessibleName(_translate("MainWindow", "First name", None))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "First name", None))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Surname", None))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Permitted rooms", None))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Usergroups", None))
        self.pushButton.setText(_translate("MainWindow", "Register", None))

        self.pushButton.clicked.connect(self.Register)

    def ImageFromCam(self, MainWindow):
        cap = cv.VideoCapture(0)
        cap.set(1, 20.0)
        cap.set(3,640)  
        cap.set(4,480) 

         
        Face_Cascade = cv.CascadeClassifier('../cv/haarcascade_frontalface_default.xml')
        #Eye_Cascade = cv.CascadeClassifier('./cv/haarcascade_eye.xml') # Later may add eyes.


        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()

            Gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

            Faces = Face_Cascade.detectMultiScale(Gray, scaleFactor = 1.1, minNeighbors = 5, minSize = (30, 30), flags = cv.cv.CV_HAAR_SCALE_IMAGE)

            # Draw a rectangle around the faces
            for (x, y, w, h) in Faces: # To draw rectangle for face
                cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # Display the resulting frame
            cv.imshow('Webcam - Active (Press Q to finish)', frame)
            
            key = cv.waitKey(99)
            if key == 99:
                cv.imwrite('../img/face.jpg', frame)
                break
            # if cv.waitKey(1) & 0xFF == ord('c'):
            #     cv.imwrite('../img/face.jpg', frame)
            #     print "captured"


        # When everything is done, release the capture
        cap.release()
        cv.destroyAllWindows()

    def Register(self):
        print "Hi"


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_MainWindow()
    ex.show()
    sys.exit(app.exec_())

