from Cleaning import Cleaning
from PyQt5.QtCore import pyqtSlot
from BasicUI import BasicUI


class Needs(BasicUI):

	def __init__(self, parent, socket, auth):
		super(Needs, self).__init__("./ui/needs.ui", parent, socket, auth)

		self.needWater.clicked.connect(self.transmitWaterNeed)
		self.needFood.clicked.connect(self.transmitFoodNeed)
		self.needExercise.clicked.connect(self.transmitExerciseNeed)
		self.requestCleaning.clicked.connect(self.transmitCleaningNeed)


	@pyqtSlot()
	def transmitWaterNeed(self):
		self.writeData("Need Water")

	@pyqtSlot()
	def transmitFoodNeed(self):
		self.writeData("Need Food")

	@pyqtSlot()
	def transmitExerciseNeed(self):
		self.writeData("Need Exercise")

	@pyqtSlot()
	def transmitCleaningNeed(self):
		self.cleaningUI = Cleaning(self, self.socket, self.auth)

	def readData(self):
		return super().readData()
