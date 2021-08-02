from Login import Login
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
from dotenv import load_dotenv

class App(BasicUI):

	def __init__(self):
		super(App, self).__init__("./ui/main.ui", None, None, None)

		self.communicationButton.clicked.connect(self.openCommunication)
		self.needsButton.clicked.connect(self.openNeeds)
		self.entertainmentButton.clicked.connect(self.openEntertainment)
		self.manageButton.clicked.connect(self.openManagement)
		self.emergencyButton.clicked.connect(self.openEmergency)
		self.hide()
		self.openLogin()

	def openBluetooth(self):
		self.btWindow = BTDialog(self, self.bluetoothDataCallback, self.bluetoothConnectionEstablished, self.bluetoothError)

	@pyqtSlot()
	def openEmergency(self):
		self.emergencyUI = Emergency(self, self.bluetoothThread, self.auth)

	@pyqtSlot()
	def openCommunication(self):
		self.communicationUI = Communication(self, self.bluetoothThread, self.auth)
	
	@pyqtSlot()
	def openNeeds(self):
		self.needsUI = Needs(self, self.bluetoothThread, self.auth)

	@pyqtSlot()
	def openEntertainment(self):
		self.entertainmentUI = Entertainment(self, self.bluetoothThread, self.auth)
	
	@pyqtSlot()
	def openManagement(self):
		self.managementUI = Management(self, self.bluetoothThread, self.auth)

	@pyqtSlot()
	def openLogin(self):
		self.loginUI = Login(self, self.loginSuccessful)

	def bluetoothConnectionEstablished(self):
		self.bluetoothThread = self.btWindow.bluetoothThread
		self.btWindow.close()
		self.bluetoothThread.changeDataCallback(self.bluetoothDataCallback)
	
	def bluetoothError(self, e):
		print("Error: {}".format(e))
	
	def bluetoothDataCallback(self, data):
		print(data)
	
	@pyqtSlot()
	def loginSuccessful(self):
		self.auth = self.loginUI.auth
		self.loginUI.close()
		self.show()
		self.openBluetooth()

	
	
if __name__ == "__main__":
	load_dotenv()
	app = QApplication(sys.argv)
	app.setStyle("Fusion")
	ex = App()
	sys.exit(app.exec_())
