from cmds.baseCmds import BaseUserCmd
import webbrowser
from secrets import secrets

class analyze(BaseUserCmd):

	objsNeeded = ['APIGameData']

	def __init__(self, objDict=None):
		super().__init__()
		self.gameData = objDict['APIGameData']

	def run(self):
		if self.gameData.gameList:
			lastGame = self.gameData.gameList[-1]

			lastId = lastGame['gameId']

			if lastGame['white'].lower() == secrets.USERNAME.lower():
				userSide = 'white'
			elif lastGame['black'].lower() == secrets.USERNAME.lower():
				userSide = 'black'

			else:
				userSide = 'white'

			browser = webbrowser.get()
			browser.open(f'https://lichess.org/{lastId}/{userSide}', new=2)