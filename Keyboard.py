from BasicUI import BasicUI
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic
from PyQt5.QtWidgets import QLineEdit


class Keyboard(BasicUI):
    def __init__(self, parent, socket):
        super(Keyboard, self).__init__("./ui/keyboard.ui", parent, socket)

        self.textOutput = self.findChild(QLineEdit, "textOutput")
        for i in range(self.gridLayout.count()):
            self.gridLayout.itemAt(i).widget().clicked.connect(self.keyboardInput)

    @pyqtSlot()
    def keyboardInput(self):
        button = self.sender()
        if (len(button.text()) == 1):
            self.textOutput.setText(self.textOutput.text() + button.text())
        else:
            if (button.objectName() == "space"):
                self.textOutput.setText(self.textOutput.text() + " ")
            elif (button.objectName() == "delete" or button.objectName() == "deleteAlt"):
                self.textOutput.setText(self.textOutput.text()[:-1])
            elif (button.objectName() == "deleteAll"):
                self.textOutput.setText("")
