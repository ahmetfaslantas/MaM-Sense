from Entertainment import Entertainment
from Communication import Communication
from BasicUI import BasicUI
from Needs import Needs
from BTDialog import BTDialog
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QPushButton

class App(BasicUI):

	def __init__(self):
		super(App, self).__init__("./ui/main.ui", None, None)

		self.communicationButton = self.findChild(QPushButton, "communication")
		self.communicationButton.clicked.connect(self.openCommunication)

		self.needsButton = self.findChild(QPushButton, "needs")
		self.needsButton.clicked.connect(self.openNeeds)

		self.entertainmentButton = self.findChild(QPushButton, "entertainmentButton")
		self.entertainmentButton.clicked.connect(self.openEntertainment)

		self.initBluetooth()

	def initBluetooth(self):
		self.btWindow = BTDialog(self, self.connectionEstablished)

	@pyqtSlot()
	def openCommunication(self):
		self.communicationUI = Communication(self, None) # TODO: We need to pass the bluetooth socket object here.
	
	@pyqtSlot()
	def openNeeds(self):
		self.needsUI = Needs(self, None) # TODO: We need to pass the bluetooth socket object here.

	@pyqtSlot()
	def openEntertainment(self):
		self.needsUI = Entertainment(self, None) # TODO: We need to pass the bluetooth socket object here.

	@pyqtSlot()
	def connectionEstablished(self):
		self.socket = self.btWindow.socket
		self.btWindow.close()
		self.socket.readyRead.connect(self.readData)

	@pyqtSlot()
	def readData(self):
		while self.socket.canReadLine():
			data = self.socket.readLine()
			print(str(data, "utf-8"))
	
if __name__ == "__main__":
	app = QApplication(sys.argv)
	app.setStyle("Fusion")
	ex = App()
	sys.exit(app.exec_())