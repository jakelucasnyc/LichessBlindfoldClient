from cmds.baseCmds import BaseUserCmd
from api.apiPost import APIPost

class acceptChallenge(BaseUserCmd):

	objsNeeded = ['APIPost', 'APIChallengeData']

	def __init__(self, challengeId, objDict):
		super().__init__()
		self.challengeId = challengeId
		self.objDict = objDict


	def run(self):

		self.objDict['APIPost'].acceptChallenge(self.challengeId)

	@staticmethod
	def showHelp():
		print('acceptChallenge -> challenge_ID')