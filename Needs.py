from BasicUI import BasicUI


class Needs(BasicUI):

	def __init__(self, parent, socket):
		super(Needs, self).__init__("./ui/needs.ui", parent, socket)

	def readData(self):
		return super().readData()
