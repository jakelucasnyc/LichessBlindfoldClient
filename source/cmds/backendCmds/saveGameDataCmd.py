from cmds.baseCmds import BaseBackendCmd

class saveGameData(BaseBackendCmd):

	objsNeeded = ['APIGameData']

	def __init__(self, gameDataDict, objDict):

		super().__init__()
		self.gameDataDict = gameDataDict
		self.gameData = objDict['APIGameData']

	def run(self):

		self.gameData.saveGame(self.gameDataDict)