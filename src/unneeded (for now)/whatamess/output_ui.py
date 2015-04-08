'''
@worzel666

Need to add capturing screen to the GUI.

Added an empty function called Register, this is for the register button on the GUI
Once clicked, it should retrieve the information entered on the four forms.
'''

from PyQt4 import QtCore, QtGui, Qt
import sys
import cv2 as cv
import Register as Reg
#from qt.ui import Ui_MainWindow

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

class Gui(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        #self.ui = Ui_MainWindow()
        self.setupUi(self)
        self.video = Reg.Cam(cv.VideoCapture(0))
        self._timer = QtCore.QTimer(self)
        self._timer.timeout.connect(self.fromCam)
        self._timer.start(27)
        self.update()

    def fromCam(self):
        try:
            self.video.captureNextFrame()
            self.videoFrame.setPixmap(self.video.toQtFrame())
            self.videoFrame.setScaledContents(True)
        except TypeError:
            print "No frame!"

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(806, 772)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.videoFrame = QtGui.QLabel(self.centralwidget)
        self.videoFrame.setGeometry(QtCore.QRect(40, 32, 721, 521))
        self.videoFrame.setObjectName(_fromUtf8("videoFrame"))
       # self.verticalLayout.addLayout(self.)
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
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
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 806, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))


        self.retranslateUi(MainWindow)
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

    def Register(self):
        print "Action for Register goes here"

#    def main():
 #      app = QtGui.QApplication(sys.argv)
  #     ex = Gui()
       
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Gui()
    ex.show()
    sys.exit(app.exec_())

