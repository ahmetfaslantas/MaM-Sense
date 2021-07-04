from BasicUI import BasicUI

class Radio(BasicUI):

	def __init__(self, parent, socket):
		super().__init__("./ui/radio.ui", parent, socket)