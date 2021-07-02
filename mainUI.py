from Emergency import Emergency
from BlockMessage import BlockMessage
from Needs import Needs
from FocusUtil import Direction, FocusUtil
from Keyboard import Keyboard
from BTDialog import BTDialog
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QCloseEvent
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QGridLayout, QMainWindow, QPushButton

class App(QMainWindow):
	def __init__(self):
		super(App, self).__init__()
		uic.loadUi("./ui/main.ui", self)
		self.setStyleSheet(open("./ui/buttonFocus.css").read())

		self.actionGroup = self.findChild(QGridLayout, "gridLayout")
		self.focusUtil = FocusUtil(self.actionGroup)

		self.keyboardButton = self.findChild(QPushButton, "keyboard")
		self.keyboardButton.clicked.connect(self.openKeyboard)

		self.needsButton = self.findChild(QPushButton, "needs")
		self.needsButton.clicked.connect(self.openNeeds)
		self.a = Emergency(None)
		self.show()
		self.initBluetooth()

	def initBluetooth(self):
		self.btWindow = BTDialog(self.connectionEstablished)

	def keyPressEvent(self, event):
		if (event.key() == 87):
			self.focusUtil.moveFocusUpdate(Direction.UP)
		elif (event.key() == 65):
			self.focusUtil.moveFocusUpdate(Direction.LEFT)
		elif (event.key() == 83):
			self.focusUtil.moveFocusUpdate(Direction.DOWN)
		elif (event.key() == 68):
			self.focusUtil.moveFocusUpdate(Direction.RIGHT)

	@pyqtSlot()
	def openKeyboard(self):
		self.keyboardUI = Keyboard(None) # TODO: We need to pass the bluetooth socket object here.
	
	@pyqtSlot()
	def openNeeds(self):
		self.needsUI = Needs(None) # TODO: We need to pass the bluetooth socket object here.

	@pyqtSlot()
	def connectionEstablished(self):
		self.socket = self.btWindow.socket
		self.btWindow = None
		self.socket.readyRead.connect(self.readData)

	@pyqtSlot()
	def readData(self):
		while self.socket.canReadLine():
			data = self.socket.readLine()
			print(str(data, "utf-8"))
	
	def closeEvent(self, a0: QCloseEvent) -> None:
		self.btWindow = None
		self.keyboardUI = None
		self.needsUI = None
		return super().closeEvent(a0)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	app.setStyle("Fusion")
	ex = App()
	sys.exit(app.exec_())