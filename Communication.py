from BlockMessage import BlockMessage
from Keyboard import Keyboard
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QPushButton
from BasicUI import BasicUI

class Communication(BasicUI):
	def __init__(self, parent, bluetoothThread, auth):
		super().__init__("./ui/communication.ui", parent, bluetoothThread, auth)


		self.keyboardButton = self.findChild(QPushButton, "keyboardButton")
		self.keyboardButton.clicked.connect(self.openKeyboard)

		self.blockButton = self.findChild(QPushButton, "blockButton")
		self.blockButton.clicked.connect(self.openBlockMessage)

	def bluetoothDataCallback(self, data):
		return super().readData()

	@pyqtSlot()
	def openKeyboard(self):
		self.keyboardUI = Keyboard(self, self.bluetoothThread, self.auth)

	@pyqtSlot()
	def openBlockMessage(self):
		self.blockMessageUI = BlockMessage(self, self.bluetoothThread, self.auth)