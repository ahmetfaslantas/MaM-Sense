from AuthUtil import AuthUtil, ErrorCodes
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
		success, code = auth.loginWithEmailPassword(email, password)
		
		if (success):
			self.auth = auth
			self.loginFunc()
		elif (code == ErrorCodes.WRONGCREDENTIALS):
			print("Wrong username/password") # TODO: Replace with UI changes.
		elif (code == ErrorCodes.CONNECTIONERROR):
			print("Cannot connect to the server") # TODO: Replace with UI changes.
			
