# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Wed Apr 22 22:01:41 2015
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
from database import database
import register_new

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

class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)

    def click(self):
        if len(self.lineEdit.text()) == 0 or len(self.lineEdit_2.text()) == 0 or len(self.lineEdit_3.text()) == 0:
            msgBox = QtGui.QMessageBox()
            msgBox.setText("Some fields have not been filled out!")
            msgBox.exec_()
        elif (str(self.lineEdit_3.text()).isdigit()):
            msgBox = QtGui.QMessageBox()
            msgBox.setText("Numbers not allowed in passphrase!")
            msgBox.exec_()
        else:
            r = register_new.Register(str(self.lineEdit.text()), str(self.lineEdit_2.text()), str(self.lineEdit_3.text()), self.comboBox.currentText(), self.comboBox_2.currentText())
            r.folderCheck()
            r.capImg()
            msgBox = QtGui.QMessageBox()
            msgBox.setText("Successfully registered user.")
            msgBox.exec_()

    def setupUi(self, MainWindow):
        db = database()
        roomid,rooms = db.get_rooms()
        groupid,groups = db.get_groups()
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        print groupid
        print groups
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 330, 94, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.click)
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(260, 260, 83, 25))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        print rooms
        print roomid
        self.comboBox.addItem("Room",0)
        for i in range(len(roomid)):
            self.comboBox.addItem(rooms[i],roomid[i])
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 90, 113, 29))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 60, 81, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 220, 81, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 140, 81, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 170, 113, 29))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(50, 260, 113, 29))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.comboBox_2 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(260, 170, 83, 25))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem("Group",0)
        for i in range(len(groupid)):
            self.comboBox_2.addItem(groups[i],groupid[i])
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(260, 140, 81, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(260, 220, 81, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "Submit", None))
        self.label.setText(_translate("MainWindow", "First Name", None))
        self.label_2.setText(_translate("MainWindow", "Passphrase", None))
        self.label_3.setText(_translate("MainWindow", "Last Name", None))
        self.label_4.setText(_translate("MainWindow", "Groups", None))
        self.label_5.setText(_translate("MainWindow", "Rooms", None))

if __name__ == '__main__':
        app = QtGui.QApplication(sys.argv)
        ex = Ui_MainWindow()
        ex.show()
        sys.exit(app.exec_())

