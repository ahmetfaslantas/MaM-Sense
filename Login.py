from AuthUtil import AuthUtil
from PyQt5.QtCore import pyqtSlot
from BasicUI import BasicUI

class Login(BasicUI):

	def __init__(self, parent, loginFunc):
		super(Login, self).__init__("./ui/login.ui", parent, None, None)
		self.loginFunc = loginFunc
		self.loginButton.clicked.connect(self.login)

	@pyqtSlot()
	def login(self):
		email = self.email.text()
		password = self.password.text()
		auth = AuthUtil()
		auth.loginWithEmailPassword(email, password)
		
		self.auth = auth
		self.loginFunc()
