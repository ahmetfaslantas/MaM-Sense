from Radio import Radio
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QPushButton
from BasicUI import BasicUI

class Entertainment(BasicUI):
	
	def __init__(self, parent, bluetoothThread, auth):
		super().__init__("./ui/entertainment.ui", parent, bluetoothThread, auth)

		self.radioButton = self.findChild(QPushButton, "radioButton")
		self.radioButton.clicked.connect(self.openRadio)

	@pyqtSlot()
	def openRadio(self):
		self.radioUI = Radio(self, self.bluetoothThread)

	def bluetoothDataCallback(self, data):
		return super().bluetoothDataCallback(data)
