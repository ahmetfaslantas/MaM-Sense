from BasicUI import BasicUI

class Radio(BasicUI):

	def __init__(self, parent, bluetoothThread):
		super().__init__("./ui/radio.ui", parent, bluetoothThread)