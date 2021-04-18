from threading import Thread
from .apiBase import APIBase
import requests
import logging
import json
from parse import GameEventParser


log = logging.getLogger(__name__)

class APIGetGameEvents(APIBase, Thread):

	def __init__(self, inputQ, gameId):
		APIBase.__init__(self)
		Thread.__init__(self)
		self.inputQ = inputQ
		self.gameId = gameId

	def _getGameEvents(self):
		with requests.Session() as s:
			response = s.get(f'https://lichess.org/api/board/game/stream/{self.gameId}', headers=self.authHeader, stream=True)
			if response.status_code == 200:
				log.info('Listening for Incoming Game Events')

			else:

				log.warning(f'Problem Listening for Incoming Game Events. Status Code: {response.status_code}')

			for line in response.iter_lines():
				#filtering out keep-alive b"\n" responses
				if line:
					eventJSON = json.loads(line.decode('utf-8'))
					print(eventJSON)
					# self.inputQ.put(['BackendCmd', 'outputEvent', [eventJSON]])

	def run(self):
		self._getGameEvents()