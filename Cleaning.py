from BasicUI import BasicUI

class Cleaning(BasicUI):

    def __init__(self, parent, bluetoothThread, auth):
        super(Cleaning, self).__init__("./ui/cleaning.ui", parent, bluetoothThread, auth)