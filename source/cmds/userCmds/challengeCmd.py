from api.apiPost import APIPost
from cmds.baseCmds import BaseUserCmd

class challenge(BaseUserCmd):

	objsNeeded = ['APIPost']
	
	def __init__(self, opponent, limit, increment, objDict):
		super().__init__()
		self.opponent = opponent
		self.limit = limit
		self.increment = increment
		self.objDict = objDict


	def run(self):

		self.objDict['APIPost'].sendChallenge(self.opponent, int(self.limit)*60, int(self.increment))