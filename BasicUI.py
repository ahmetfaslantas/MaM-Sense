from PyQt5.QtGui import QCloseEvent
from FocusUtil import Direction, FocusUtil
from PyQt5.QtWidgets import QApplication, QGridLayout, QWidget
from PyQt5 import uic

class BasicUI(QWidget):

	def __init__(self, uipath, parent, socket):
		super(BasicUI, self).__init__()
		
		self.socket = socket
		self.parent = parent

		uic.loadUi(uipath, self)
		self.setFixedSize(self.geometry().width(), self.geometry().height())
		self.setStyleSheet(open("./ui/buttonFocus.css").read())

		self.gridLayout = self.findChild(QGridLayout, "gridLayout")

		if (self.socket != None):
			self.socket.readyRead.connect(self.readData)

		if (self.gridLayout != None):
			self.focusUtil = FocusUtil(self.gridLayout)
		self.show()

	def closeEvent(self, a0: QCloseEvent) -> None:
		widgets = QApplication.topLevelWidgets()
		for widget in widgets:
			if (widget.parent == self):
				widget.close()
		return super().closeEvent(a0)

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

	def readData(self):
		pass