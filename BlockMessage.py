from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QPushButton
from BasicUI import BasicUI

class BlockMessage(BasicUI):

	def __init__(self, parent, socket):
		super(BlockMessage, self).__init__("./ui/blockmessage.ui", parent, socket)

		for i in range(self.gridLayout.count()):
			widget = self.gridLayout.itemAt(i).widget()
			if (isinstance(widget, QPushButton)):
				widget.clicked.connect(self.sendBlockMessage)

	@pyqtSlot()
	def sendBlockMessage(self):
		button = self.sender()
		location = self.focusUtil.getButtonLocation(button)
		text = self.focusUtil.getItem(location[0], location[1] - 1).text()
		self.writeData(text)
#denemegitpush