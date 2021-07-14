from BasicUI import BasicUI

class Emergency(BasicUI):

	def __init__(self, parent, socket, auth):
		super(Emergency, self).__init__("./ui/emergency.ui", parent, socket, auth)
		