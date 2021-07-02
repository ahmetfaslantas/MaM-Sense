from FocusUtil import Direction, FocusUtil
from PyQt5.QtWidgets import QGridLayout, QWidget
from PyQt5 import uic

class Emergency(QWidget):

	def __init__(self, socket):
		super(Emergency, self).__init__()
		self.socket = socket
		uic.loadUi("./ui/emergency.ui", self)

		self.setStyleSheet(open("./ui/buttonFocus.css").read())
		self.needsGroup = self.findChild(QGridLayout, "gridLayout")
		self.focusUtil = FocusUtil(self.needsGroup)
		self.show()