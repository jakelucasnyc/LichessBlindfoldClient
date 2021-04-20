import chess

class GameFullParser:

	def __init__(self, eventJSON):

		self.whiteName = eventJSON['white']['name']
		self.blackName = eventJSON['black']['name']
		self.timeLimit = eventJSON['clock']['initial']
		self.timeIncrement = eventJSON['clock']['increment']
		self.moves = eventJSON['state']['moves']

		

class GameStateParser:

	def __init__(self, eventJSON):

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

