from BasicUI import BasicUI

class BedControl(BasicUI):

	def __init__(self, parent, bluetoothThread):
		super(BedControl, self).__init__("./ui/bedcontrol.ui", parent, bluetoothThread, None)

	def bluetoothDataCallback(self, data):
		return super().bluetoothDataCallback(data)
