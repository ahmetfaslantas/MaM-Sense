from FocusUtil import Direction, FocusUtil
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic
from PyQt5.QtWidgets import QGridLayout, QWidget, QLineEdit

class Keyboard(QWidget):
	def __init__(self, socket):
		super(Keyboard, self).__init__()
		self.socket = socket
		uic.loadUi("./ui/keyboard.ui", self)
		self.setFixedSize(1030, 460)
		self.setStyleSheet(open("./ui/buttonFocus.css").read())
		
		self.keyboardGroup = self.findChild(QGridLayout, "keyboardLayout")
		self.textOutput = self.findChild(QLineEdit, "textOutput")
		for i in range(self.keyboardGroup.count()):
			self.keyboardGroup.itemAt(i).widget().clicked.connect(self.keyboardInput)
		
		self.focusUtil = FocusUtil(self.keyboardGroup)
		self.show()

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
	def keyboardInput(self):
		button = self.sender()
		if (len(button.text()) == 1):
			self.textOutput.setText(self.textOutput.text() + button.text())
		else:
			if (button.objectName() == "space"):
				self.textOutput.setText(self.textOutput.text() + " ")
			elif (button.objectName() == "delete" or button.objectName() == "deleteAlt"):
				self.textOutput.setText(self.textOutput.text()[:-1])
			elif (button.objectName() == "deleteAll"):
				self.textOutput.setText("")