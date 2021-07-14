import os
import requests

class AuthUtil(object):


	def loginWithEmailPassword(self, email, password):
		query = {"email": email, "password": password, "returnSecureToken": True}
		reqRes = requests.post(url = "http://192.168.1.60:9199/identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=" + os.getenv("APIKEY"),
					json = query,
					headers = {"Content-Type": "application/json"})
		res = reqRes.json()
		if ("error" in res):
			# TODO:  Print some error thing here.
			return
		self.localId = res["localId"]
		self.idToken = res["idToken"]
		self.displayName = res["displayName"]

	def refreshToken(self, refreshToken):
		query = {"grant_type": "refresh_token", "refresh_token": refreshToken}
		reqRes = requests.post(url = "http://192.168.1.60:9199/securetoken.googleapis.com/v1/token?key=" + os.getenv("APIKEY"), 
					json = query,
					headers = {"Content-Type": "application/json"})
		res = reqRes.json()
		if ("error" in res):
			# TODO:  Print some error thing here.
			return
		self.idToken = res["idToken"]