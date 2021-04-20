from .apiBase import APIBase
import chess
import requests
import logging

log = logging.getLogger(__name__)
class APIGame(APIBase):
	
	def __init__(self, gameId):
		super().__init__()
		self.gameId = gameId
		self.board = chess.Board()

		#after a draw offer is sent, it remains for 2 moves and this gets in the way of my logging logic.
		self.alreadyOfferedDraw = False


	def initializeFromParser(self, parser):
		self.white = parser.whiteName
		self.black = parser.blackName
		self.limit = parser.timeLimit
		self.increment = parser.timeIncrement

		moves = parser.moves.split()
		for move in moves:
			self.board.push_uci(move)

		# print('MOVE STACK:', self.board.move_stack)

		returnDict = {
			'type': 'initial',
			'white': self.white,
			'black': self.black,
			'limit': self.limit,
			'increment': self.increment,
			'showTimeControl': f'{int(self.limit/60000)}+{int(self.increment/1000)}',

		}

		return returnDict

	def updateFromParser(self, parser):
		



		self.whiteTime = parser.whiteTime
		self.blackTime = parser.blackTime
		if parser.gameStatus != 'started':
			self.outcome = parser.gameStatus
			self.gameOver = True
			#if the ndjson contains a winner after the game is over
			if hasattr(parser, 'winner'):
				returnDict = {
					'type': 'gameOver',
					'outcome': self.outcome,
					'winner': parser.winner 
				}

			#if the ndjson contains no winner after the game is over
			else:
				returnDict = {
					'type': 'gameOver',
					'outcome': self.outcome,
					'winner': None 
				}


		elif parser.wdraw or parser.bdraw and not self.alreadyOfferedDraw:
			if parser.wdraw:
				drawer = 'White'

			elif parser.bdraw:
				drawer = 'Black'

			self.alreadyOfferedDraw = True
			returnDict = {
				'type': 'drawOffer',
				'drawer': drawer
			}
		else:

			#clause to reset self.alreadyOfferedDraw
			if not parser.wdraw and not parser.bdraw:
				self.alreadyOfferedDraw = False

			#code to update moves when it's a normal gameState Event
			lastMove = self._getLastMove(parser.moves)
			lastMoveSan = self._apiParseUciToSan(lastMove)
			returnDict = {
				'type': 'update',
				'move': lastMoveSan,
				'mover': self._getMover()
			}

		return returnDict

	def _getMover(self):
		if len(self.board.move_stack) % 2 == 1:
			return 'White'
		elif len(self.board.move_stack) % 2 == 0:
			return 'Black'

	def _getLastMove(self, movesStr):

		movesList = movesStr.split()
		return movesList[-1]
		
	def _userParseSanToUci(self, moveStr):
		try:
			moveObj = self.board.parse_san(moveStr)

		except ValueError:
			print('That move is illegal. Please try again.')
			return None

		else:
			return self.board.uci(moveObj)

	def _apiParseUciToSan(self, moveStr):
		moveObj = self.board.parse_uci(moveStr)
		sanStr = self.board.san(moveObj)
		self.board.push(moveObj)
		return sanStr

	def makeMove(self, moveStr):
		"""
		Sending san (turned uci) formatted move to Lichess
		"""
		moveStr = str(moveStr)

		moveUci  = self._userParseSanToUci(moveStr)
		# print(moveUci)

		if moveUci is None:
			return

		response = requests.post(f'https://lichess.org/api/board/game/{self.gameId}/move/{moveUci}', headers=self.authHeader)

		if response.status_code == 200:
			log.debug('Move Successfully Sent')

		else:
			log.warning(f'Move Unsuccessfully Sent. Status Code: {response.status_code}')

	def resign(self):
		response = requests.post(f'https://lichess.org/api/board/game/{self.gameId}/resign', headers=self.authHeader)

		if response.status_code == 200:
			log.debug('Resignation Successfully Sent')

		else:
			log.warning(f'Resignation Unsuccessfully Sent. Status Code: {response.status_code}')


	def offerOrAcceptDraw(self):

		response = requests.post(f'https://lichess.org/api/board/game/{self.gameId}/draw/yes', headers=self.authHeader)

		if response.status_code == 200:
			log.debug('Draw Offer Successfully Sent or Accepted')

		else:
			log.warning(f'Draw Offer Unsuccessfully Sent or Accepted. Status Code: {response.status_code}')


	def declineDraw(self):

		response = requests.post(f'https://lichess.org/api/board/game/{self.gameId}/draw/no', headers=self.authHeader)

		if response.status_code == 200:
			log.debug('Draw Offer Successfully Declined')

		else:
			log.warning(f'Draw Offer Unsuccessfully Declined. Status Code: {response.status_code}')


	def abort(self):

		response = requests.post(f'https://lichess.org/api/board/game/{self.gameId}/abort', headers=self.authHeader)

		if response.status_code == 200:
			log.debug('Game Aborted Successful')

		else:
			log.warning(f'Game Unsuccessfully Aborted. Status Code: {response.status_code}')