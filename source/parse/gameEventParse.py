import chess

class GameFullParser:

	def __init__(self, eventJSON):
		self.typeName = eventJSON['type']
		self.whiteName = eventJSON['white']['name']
		self.blackName = eventJSON['black']['name']
		self.gameId = eventJSON['id']
		self.timeLimit = eventJSON['clock']['initial']
		self.timeIncrement = eventJSON['clock']['increment']

		

class GameStateParser:

	def __init__(self, eventJSON):
		self.typeName = eventJSON['type']
		self.moves = eventJSON['moves']
		self.whiteTime = eventJSON['wtime']
		self.blackTime = eventJSON['btime']
		self.gameStatus = eventJSON['status']
		self.winner = None
		if 'winner' in eventJSON.keys():
			self.winner = eventJSON['winner']



class ChatLineParser:

	def __init__(self, eventJSON):
		self.typeName = eventJSON['type']
		self.username = eventJSON['username']
		self.message = eventJSON['text']
		self.room = eventJSON['room']

