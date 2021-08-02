from BasicUI import BasicUI

class Lights(BasicUI):

    def __init__(self, parent, bluetoothThread):
        super(Lights, self).__init__("./ui/lights.ui", parent, bluetoothThread, None)