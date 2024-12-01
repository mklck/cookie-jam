import time

class Timer:
	def __init__(self):
		self.start = None
	def reset(self):
		self.start = time.time()
	def get(self):
		return time.time() - self.start()
