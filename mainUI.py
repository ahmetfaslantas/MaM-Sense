from Emergency import Emergency
from Management import Management
from Entertainment import Entertainment
from Communication import Communication
from BasicUI import BasicUI
from Needs import Needs
from BTDialog import BTDialog
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication

class App(BasicUI):

	def __init__(self):
		super(App, self).__init__("./ui/main.ui", None, None)

		self.communicationButton.clicked.connect(self.openCommunication)
		self.needsButton.clicked.connect(self.openNeeds)
		self.entertainmentButton.clicked.connect(self.openEntertainment)
		self.manageButton.clicked.connect(self.openManagement)
		self.emergencyButton.clicked.connect(self.openEmergency)

		self.initBluetooth()

	def initBluetooth(self):
		self.btWindow = BTDialog(self, self.connectionEstablished)

	@pyqtSlot()
	def openEmergency(self):
		self.emergencyUI = Emergency(self, self.socket)

	@pyqtSlot()
	def openCommunication(self):
		self.communicationUI = Communication(self, self.socket)
	
	@pyqtSlot()
	def openNeeds(self):
		self.needsUI = Needs(self, self.socket)

	@pyqtSlot()
	def openEntertainment(self):
		self.entertainmentUI = Entertainment(self, self.socket)
	
	@pyqtSlot()
	def openManagement(self):
		self.managementUI = Management(self, self.socket)

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