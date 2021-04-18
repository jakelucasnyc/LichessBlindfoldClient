from cmds.baseCmds import BaseBackendCmd

class saveChallenge(BaseBackendCmd):

	objsNeeded = ['APIChallengeData']

	def __init__(self, eventParser, objDict):
		super().__init__()
		self.eventParser = eventParser
		self.challengeDict = {
			'id': self.eventParser.id,
			'timeControl': self.eventParser.timeControl,
			'challenger': self.eventParser.opponent,
			'destUser': self.eventParser.destUser
		}
		self.objDict = objDict

	def run(self):

		self.objDict['APIChallengeData'].addChallengeEntry(self.challengeDict)