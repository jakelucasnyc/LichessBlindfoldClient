from cmds.baseCmds import BaseBackendCmd
from api.apiGetGameEvents import APIGetGameEvents

class streamGameEvents(BaseBackendCmd):

	def __init__(self, inputQ, gameId):
		super().__init__()
		self.inputQ = inputQ
		self.gameId = gameId

	def run(self):

		APIGetGameEvents(self.inputQ, self.gameId).start()

