from Cleaning import Cleaning
from PyQt5.QtCore import pyqtSlot
from BasicUI import BasicUI
from FirestoreUtil import FirestoreUtil


class Needs(BasicUI):

	def __init__(self, parent, bluetoothThread, auth):
		super(Needs, self).__init__("./ui/needs.ui", parent, bluetoothThread, auth)

		self.needWater.clicked.connect(self.transmitWaterNeed)
		self.needFood.clicked.connect(self.transmitFoodNeed)
		self.needExercise.clicked.connect(self.transmitExerciseNeed)
		self.requestCleaning.clicked.connect(self.transmitCleaningNeed)


	@pyqtSlot()
	def transmitWaterNeed(self):
		data = FirestoreUtil.formatData({"needType": "water"})
		FirestoreUtil.writeDocument("/users/{}/needs".format(self.auth.localId), data, self.auth.idToken)

	@pyqtSlot()
	def transmitFoodNeed(self):
		data = FirestoreUtil.formatData({"needType": "food"})
		FirestoreUtil.writeDocument("/users/{}/needs".format(self.auth.localId), data, self.auth.idToken)

	@pyqtSlot()
	def transmitExerciseNeed(self):
		data = FirestoreUtil.formatData({"needType": "exercise"})
		FirestoreUtil.writeDocument("/users/{}/needs".format(self.auth.localId), data, self.auth.idToken)

	@pyqtSlot()
	def transmitCleaningNeed(self):
		self.cleaningUI = Cleaning(self, self.bluetoothThread, self.auth)

	def bluetoothDataCallback(self, data):
		return super().readData()
