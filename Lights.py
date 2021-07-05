from BasicUI import BasicUI

class Lights(BasicUI):

    def __init__(self, parent, socket):
        super(Lights, self).__init__("./ui/lights.ui", parent, socket)