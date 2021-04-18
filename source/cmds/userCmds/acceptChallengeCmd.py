from cmds.baseCmds import BaseUserCmd
from api.apiPost import APIPost

class acceptChallenge(BaseUserCmd):

	def __init__(self, challengeId):
		super().__init__()
		self.challengeId = challengeId


	def run(self):

		APIPost().acceptChallenge(self.challengeId)