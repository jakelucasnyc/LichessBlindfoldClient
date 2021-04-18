from cmds.baseCmds import BaseUserCmd
from api.apiPost import APIPost

class declineChallenge(BaseUserCmd):

	objsNeeded = ['APIPost']

	def __init__(self, challengeId, objDict):
		super().__init__()
		self.challengeId = challengeId
		self.objDict = objDict

	def run(self):

		self.objDict['APIPost'].declineChallenge(self.challengeId)