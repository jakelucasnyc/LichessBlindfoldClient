import logging

log = logging.getLogger(__name__)
class APIGameData:

	def __init__(self):
		self.gameList = []

	def saveGame(self, gameDict):

		self.gameList.append(gameDict)
		# print(self.gameList)
