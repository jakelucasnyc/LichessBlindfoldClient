from cmds.baseCmds import BaseUserCmd

class resign(BaseUserCmd):

	objsNeeded = ['APIGame']

	def __init__(self, objDict):
		super().__init__()
		self.game = objDict['APIGame']

	def run(self):
		self.game.resign()