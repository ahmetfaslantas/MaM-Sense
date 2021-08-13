from PyQt5.QtGui import QCloseEvent
from FocusUtil import Direction, FocusUtil
from PyQt5.QtWidgets import QApplication, QGridLayout, QWidget
from PyQt5 import uic, QtCore

class BasicUI(QWidget):

	def __init__(self, uipath, parent, bluetoothThread, auth):
		super(BasicUI, self).__init__()

		self.bluetoothThread = bluetoothThread
		self.parent = parent
		self.auth = auth

		uic.loadUi(uipath, self)
		self.installEventFilter(self)

		self.setFixedSize(self.geometry().width(), self.geometry().height())
		self.setStyleSheet(open("./ui/buttonFocus.css").read())

		self.gridLayout = self.findChild(QGridLayout, "gridLayout")

		if (self.bluetoothThread != None):
			self.bluetoothThread.changeDataCallback(self.bluetoothDataCallback)

		if (self.gridLayout != None):
			self.focusUtil = FocusUtil(self.gridLayout)
		else:
			self.focusUtil = None
		self.show()

	def closeEvent(self, a0: QCloseEvent) -> None:
		widgets = QApplication.topLevelWidgets()
		for widget in widgets:
			if (widget.parent == self):
				widget.close()
		return super().closeEvent(a0)

	def eventFilter(self, object, event):
		if (event.type() == QtCore.QEvent.WindowActivate):
			if (self.bluetoothThread != None):
				self.bluetoothThread.changeDataCallback(self.bluetoothDataCallback)
		return False

	def keyPressEvent(self, event):
		if (self.focusUtil == None):
			return
		
		if (event.key() == 87):
			self.focusUtil.moveFocusUpdate(Direction.UP)
		elif (event.key() == 65):
			self.focusUtil.moveFocusUpdate(Direction.LEFT)
		elif (event.key() == 83):
			self.focusUtil.moveFocusUpdate(Direction.DOWN)
		elif (event.key() == 68):
			self.focusUtil.moveFocusUpdate(Direction.RIGHT)

	def bluetoothDataCallback(self, data):
		raise NotImplementedError("This function is not yet implemented.")

	def bluetoothWriteData(self, data):
		if (self.bluetoothThread != None):
			self.bluetoothThread.write(data.encode())
		else:
			raise Exception("Bluetooth bluetoothThread not initialized yet!")
