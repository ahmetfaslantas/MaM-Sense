from BasicUI import BasicUI

class BedControl(BasicUI):

	def __init__(self, socket):
		super(BedControl, self).__init__("./ui/bedcontrol.ui", socket)

	def readData(self):
		return super().readData()