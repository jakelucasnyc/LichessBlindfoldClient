from cmds.baseCmds import BaseUserCmd
from time import gmtime, strftime

class time(BaseUserCmd):

	objsNeeded = ['APIGame']
	
	def __init__(self, objDict):
		self.game = objDict['APIGame']

	def run(self):
		whiteSeconds, blackSeconds = self.game.getTime()

		whiteTime = strftime("%H:%M:%S", gmtime(whiteSeconds))
		blackTime = strftime("%H:%M:%S", gmtime(blackSeconds))

		print(f'White has {whiteTime} remaining.')
		print(f'Black has {blackTime} remaining.')



		