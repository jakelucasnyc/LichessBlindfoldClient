from cmds.baseCmds import BaseBackendCmd
from api.apiGetGameEvents import APIGetGameEvents

class streamGameEvents(BaseBackendCmd):

	objsNeeded = ['APIGame']

	def __init__(self, inputQ, gameId, objDict):
		super().__init__()
		self.inputQ = inputQ
		self.gameId = gameId
		self.objDict = objDict
		self.game = objDict['APIGame']

	def run(self):

		APIGetGameEvents(self.inputQ, self.gameId, self.game).start()

