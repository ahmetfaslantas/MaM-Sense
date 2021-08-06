import os
import requests

LOGINURL = "http://192.168.1.60:9199/identitytoolkit.googleapis.com/v1"
REFRESHURL = "http://192.168.1.60:9199/securetoken.googleapis.com/v1"

class ErrorCodes:
	WRONGCREDENTIALS = 1
	CONNECTIONERROR = 2
	UNKNOWNERROR = 3
	

class AuthUtil(object):


	def loginWithEmailPassword(self, email, password):
		try:
			query = {"email": email, "password": password, "returnSecureToken": True}
			reqRes = requests.post(url = LOGINURL + "/accounts:signInWithPassword?key=" + os.getenv("APIKEY"),
						json = query,
						headers = {"Content-Type": "application/json"})
			res = reqRes.json()
			if ("error" in res):
				# TODO:  Print some error thing here.
				return False, ErrorCodes.WRONGCREDENTIALS
			
			self.localId = res["localId"]
			self.idToken = res["idToken"]
			self.displayName = res["displayName"]
			return True, None
		except requests.exceptions.ConnectionError as errc:
			return False, ErrorCodes.CONNECTIONERROR

	def refreshToken(self, refreshToken):
		try:
			query = {"grant_type": "refresh_token", "refresh_token": refreshToken}
			reqRes = requests.post(url = REFRESHURL + "/token?key=" + os.getenv("APIKEY"), 
						json = query,
						headers = {"Content-Type": "application/json"})
			res = reqRes.json()
			if ("error" in res):
				# TODO:  Print some error thing here.
				return False, ErrorCodes.UNKNOWNERROR
			self.idToken = res["idToken"]
			return True, None
		except requests.exceptions.ConnectionError as errc:
			return False, ErrorCodes.CONNECTIONERROR