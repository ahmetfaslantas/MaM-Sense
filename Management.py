from PyQt5.QtCore import pyqtSlot
from BasicUI import BasicUI
from Lights import Lights
from BedControl import BedControl

class Management(BasicUI):

    def __init__(self, parent, bluetoothThread, auth):
        super(Management, self).__init__("./ui/management.ui", parent, bluetoothThread, auth)

        self.lightsButton.clicked.connect(self.openLightControl)
        self.bedButton.clicked.connect(self.openBedControl)

    @pyqtSlot()
    def openLightControl(self):
        self.lightsUI = Lights(self, self.bluetoothThread)

    @pyqtSlot()
    def openBedControl(self):
        self.bedUI = BedControl(self, self.bluetoothThread)
