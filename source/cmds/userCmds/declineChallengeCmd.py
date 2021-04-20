from cmds.baseCmds import BaseUserCmd
from api.apiPost import APIPost

class declineChallenge(BaseUserCmd):

	objsNeeded = ['APIPost', 'APIChallengeData']

	def __init__(self, challengeId, objDict):
		super().__init__()
		self.objDict = objDict

		if challengeId is None:

			challengeList = self.objDict['APIChallengeData'].challengeList
			if challengeList:
				self.challengeId = self.objDict['APIChallengeData'].challengeList[-1]['id']

		elif challengeId is not None:

			self.challengeId = challengeId


	def run(self):

		self.objDict['APIPost'].declineChallenge(self.challengeId)