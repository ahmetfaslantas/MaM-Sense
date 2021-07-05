from BasicUI import BasicUI

class Cleaning(BasicUI):

    def __init__(self, parent, socket):
        super(Cleaning, self).__init__("./ui/cleaning.ui", parent, socket)