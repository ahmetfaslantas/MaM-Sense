import bluetooth
from threading import Thread

class BTThread(Thread):
	
	def __init__(self, address, dataCallback, connectedCallback, errorCallback):
		Thread.__init__(self)
		self.dataCallback = dataCallback
		self.errorCallback = errorCallback
		self.connectedCallback = connectedCallback
		self.address = address
		
		
	def init(self):	
		self.sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
		
		
		try:
			self.sock.connect((self.address, 1))
			self.connectedCallback()
		except Exception as e:
			self.errorCallback(e)
		self.start()
		
		
	def changeDataCallback(self, newCallback):
		self.dataCallback = newCallback
		
		
	def run(self):
		while (1):
			data = ""
			while (len(data) == 0 or data[-1] != "\n"):
				try:
					temp = self.sock.recv(1)
					data = data + temp.decode("utf-8")
				except Exception as e:
					self.errorCallback(e)
			self.dataCallback(data[:-1])
	
	def write(self, data):
		self.sock.send(data)
