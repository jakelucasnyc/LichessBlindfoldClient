from .baseCmds import BaseUserCmd
from threading import Thread
import datetime
from api.apiPost import APIPost

class challenge(BaseUserCmd):

	
	def __init__(self, opponent, limit, increment):
		super().__init__()
		self.opponent = opponent
		self.limit = limit
		self.increment = increment


	def run(self):

		apiPost = APIPost()
		apiPost.sendChallenge(self.opponent, int(self.limit)*60, int(self.increment))


class time(BaseUserCmd):
	
	def __init__(self):
		super().__init__()
		self.time = datetime.datetime.now()

	def run(self):

		print('CURRENT TIME: '+str(self.time))

