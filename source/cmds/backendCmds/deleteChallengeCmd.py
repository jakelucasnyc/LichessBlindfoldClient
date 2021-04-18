from cmds.baseCmds import BaseBackendCmd

class deleteChallenge(BaseBackendCmd):

	objsNeeded = ['APIChallengeData']

	def __init__(self, challengeId, objDict):
		super().__init__()
		self.challengeId = challengeId
		self.objDict = objDict

	def run(self):

		self.objDict['APIChallengeData'].deleteChallengeEntry(self.challengeId)
