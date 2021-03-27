from .baseCmds import BaseUserCmd
from threading import Thread
import datetime

class challenge(BaseUserCmd):

	asyn = True

	def __init__(self, opponent, limit, increment):
		super().__init__()
		self.opponent = opponent
		self.limit = limit
		self.increment = increment


	async def run(self):

		apiPost = APIPost()
		await apiPost.sendChallenge(self.opponent, int(self.limit)*60, int(self.increment))


class time(BaseUserCmd, Thread):

	joinable = True
	
	def __init__(self):
		Thread.__init__(self)
		BaseUserCmd.__init__(self)
		self.time = datetime.datetime.now()

	def run(self):

		print('CURRENT TIME: '+str(self.time))

