from BasicUI import BasicUI

class BlockMessage(BasicUI):

	def __init__(self, parent, socket):
		super(BlockMessage, self).__init__("./ui/blockmessage.ui", parent, socket)
