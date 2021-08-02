from BasicUI import BasicUI

class Emergency(BasicUI):

	def __init__(self, parent, bluetoothThread, auth):
		super(Emergency, self).__init__("./ui/emergency.ui", parent, bluetoothThread, auth)
		