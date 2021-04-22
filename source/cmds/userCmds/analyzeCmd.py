from cmds.baseCmds import BaseUserCmd

class analyze(BaseUserCmd):

	objsNeeded = ['APIGame']

	def __init__(self, objDict=None):
		super().__init__()
		self.game = objDict['APIGame']

	def run(self):
		pass