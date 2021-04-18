from .apiBase import APIBase

class APIPlay(APIBase):
	
	def __init__(self, gameId):
		self.gameId = gameId

	def makeMove(self, move):
		pass