from cmds.baseCmds import BaseUserCmd

class move(BaseUserCmd):

	objsNeeded = ['APIGame']

	def __init__(self, moveStr, objDict):

		self.moveStr = moveStr
		self.objDict = objDict
		self.game = objDict['APIGame']

	def run(self):

		self.game.makeMove(self.moveStr)