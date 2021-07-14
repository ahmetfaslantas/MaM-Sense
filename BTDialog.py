from BasicUI import BasicUI
from PyQt5.QtWidgets import QListWidget, QStatusBar, QWidget
from PyQt5 import QtBluetooth, uic
from PyQt5.QtCore import pyqtSlot


class BTDialog(BasicUI):

	def __init__(self, parent, connectedFunc):
		super(BTDialog, self).__init__("./ui/bluetooth.ui", parent, None, None)
		self.connectedFunc = connectedFunc

		self.btDevices = self.findChild(QListWidget, "btList")
		self.btDevices.clicked.connect(self.deviceSelected)
		self.scanDevices()

	def scanDevices(self):
		self.agent = QtBluetooth.QBluetoothDeviceDiscoveryAgent(self)
		self.agent.finished.connect(self.devicesFound)
		self.agent.setLowEnergyDiscoveryTimeout(1000)
		self.agent.start()

	def devicesFound(self):
		for device in self.agent.discoveredDevices():
			self.btDevices.insertItem(0, device.address().toString())

	def initBluetooth(self):
		self.socket = QtBluetooth.QBluetoothSocket(QtBluetooth.QBluetoothServiceInfo.RfcommProtocol)
		self.socket.connected.connect(self.connectedFunc)
		self.socket.disconnected.connect(self.deviceDisconnected)
		self.socket.error.connect(self.bluetoothError)

		self.socket.connectToService(QtBluetooth.QBluetoothAddress(self.address), 1)

	@pyqtSlot()
	def deviceSelected(self):
		self.address = self.btDevices.currentItem().text()
		self.initBluetooth()

	@pyqtSlot()
	def deviceDisconnected(self):
		print("Device disconnected!")

	@pyqtSlot()
	def bluetoothError(self):
		print("Error while connecting: " + self.socket.errorString())


