from BasicUI import BasicUI

class BedControl(BasicUI):

	def __init__(self, parent, socket):
		super(BedControl, self).__init__("./ui/bedcontrol.ui", parent, socket)

	def readData(self):
		return super().readData()