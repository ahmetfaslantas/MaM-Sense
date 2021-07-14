from Radio import Radio
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QPushButton
from BasicUI import BasicUI

class Entertainment(BasicUI):
	
	def __init__(self, parent, socket, auth):
		super().__init__("./ui/entertainment.ui", parent, socket, auth)

		self.radioButton = self.findChild(QPushButton, "radioButton")
		self.radioButton.clicked.connect(self.openRadio)

	@pyqtSlot()
	def openRadio(self):
		self.radioUI = Radio(self, self.socket)

	def readData(self):
		return super().readData()