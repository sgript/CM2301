from PySide.QtCore import *
from PySide.QtGui import *
import sip
import cv2
import sys
 
class MainApp(QWidget):
	 
	def __init__(self):
		QWidget.__init__(self)
		self.video_size = QSize(320, 240)
		self.setup_ui()
		self.setup_camera()
                self.im = 0
	 
	def setup_ui(self):
		"""Initialize widgets.
		"""
#		self.image_label = QLabel()
#		self.image_label.setFixedSize(self.video_size)

                self.firstName = QLineEdit()
                self.firstName.setPlaceholderText("First Name")
                self.lastName = QLineEdit()
                self.lastName.setPlaceholderText("Last Name")
                #self.group = QComboBox()

                ### SQL TO GET GROUPS ###
                self.identify = QLineEdit()
                self.identify.setPlaceholderText("ID")

                self.quit_button = QPushButton("Quit")
		self.quit_button.clicked.connect(self.close)
                
                self.continue_button = QPushButton("Continue")
                self.continue_button.clicked.connect(self.continue_process)
                
		self.main_layout = QVBoxLayout()
#		self.main_layout.addWidget(self.image_label)
                self.main_layout.addWidget(self.firstName)
                self.main_layout.addWidget(self.lastName)
                #self.main_layout.addWidget(self.group)
		self.main_layout.addWidget(self.quit_button)
		self.main_layout.addWidget(self.continue_button)
                self.main_layout.addWidget(self.identify)
                
		self.setLayout(self.main_layout)

        def continue_process(self):
                if not (self.identify.text()) or not (self.firstName.text()) or not (self.lastName.text()) or not(self.group.itemText()) :
                        self.alert()
                else:
                        self.main_layout.removeWidget(self.firstName)
                        sip.delete(self.firstName)
                        self.firstName = None
                        self.main_layout.removeWidget(self.lastName)
                        sip.delete(self.lastName)
                        self.lastName = None
                       # self.main_layout.removeWidget(self.group)
                        #sip.delete(self.group)
                        #self.group = None
                        self.main_layout.removeWidget(self.continue_button)
                        sip.delete(self.continue_button)
                        self.continue_button = None
                        self.main_layout.removeWidget(self.identify)
                        sip.delete(self.identify)
                        self.identify = None

                
        def capturePic(self):
                if self.id.text():
                        cv2.imwrite(self.id.text() + "_" + str(self.im) + ".jpg", self.capture.read)
                else:
                        self.alert()
                #cv.imwrite(
                print "LOL"

        def alert(self):
                self.alert = QMessageBox()
                self.alert.setText("Some fields have not been filled out. Please enter correct information and try again.")
                self.alert.exec_()
                
	def setup_camera(self):
		"""Initialize camera.
		"""
		self.capture = cv2.VideoCapture(0)
		self.capture.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, self.video_size.width())
		self.capture.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, self.video_size.height())
		 
		self.timer = QTimer()
		self.timer.timeout.connect(self.display_video_stream)
		self.timer.start(30)
	 
	def display_video_stream(self):
		"""Read frame from camera and repaint QLabel widget.
		"""
		_, frame = self.capture.read()
		frame = cv2.cvtColor(frame, cv2.cv.CV_BGR2RGB)
		frame = cv2.flip(frame, 1)
		image = QImage(frame, frame.shape[1], frame.shape[0],
		frame.strides[0], QImage.Format_RGB888)
		self.image_label.setPixmap(QPixmap.fromImage(image))
	 
if __name__ == "__main__":
	app = QApplication(sys.argv)
	win = MainApp()
	win.show()
	sys.exit(app.exec_()) 
