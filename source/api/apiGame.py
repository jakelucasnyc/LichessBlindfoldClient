from .apiBase import APIBase

class APIGame(APIBase):
	
	def __init__(self, gameId):
		self.gameId = gameId

	def makeMove(self, move):
		pass