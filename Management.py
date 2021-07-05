from PyQt5.QtCore import pyqtSlot
from BasicUI import BasicUI
from Lights import Lights

class Management(BasicUI):

    def __init__(self, parent, socket):
        super(Management, self).__init__("./ui/management.ui", parent, socket)

        self.lightsButton.clicked.connect(self.openLights)

    @pyqtSlot()
    def openLights(self):
        self.lightsUI = Lights(self, self.socket)
