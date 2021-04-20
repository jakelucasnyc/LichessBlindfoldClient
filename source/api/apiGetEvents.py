import logging
import json
from .apiBase import APIBase
from cmdHandler import CmdHandler
from threading import Thread
import requests
from parse import EventParser
import time
from api.apiGame import APIGame

log = logging.getLogger(__name__)


class APIGetEvents(APIBase, Thread):

	def __init__(self, inputQ):
		APIBase.__init__(self)
		Thread.__init__(self, daemon=True)
		self.inputQ = inputQ


	def _getEvents(self):
		with requests.Session() as s:
			response = s.get('https://lichess.org/api/stream/event', headers=self.authHeader, stream=True)
			if response.status_code == 200:
				log.info('Listening for Incoming Events')

			else:
				log.warning(f'Problem Listening for Incoming Events. Status Code: {response.status_code}')

			for line in response.iter_lines():

				#filtering out keep-alive b"\n" responses
				if line:
					eventJSON = json.loads(line.decode('utf-8'))
					parser = EventParser.fromJSON(eventJSON)
					self.inputQ.put({'type': 'BackendCmd', 
						             'cmdName': 'outputEvent', 
						             'cmdParams': [parser]})

					#if a game has started, start the game play process
					if parser.typeName == 'gameStart':
						self.inputQ.put({
							'type': 'globalObjAdd',
							'cls': APIGame,
							'clsParams': {'gameId': parser.id}
						})

						time.sleep(2)

						self.inputQ.put({
							'type': 'BackendCmd', 
							'cmdName': 'streamGameEvents', 
							'cmdParams': [self.inputQ, parser.id]
						})
						
					elif parser.typeName == 'challenge':
						self.inputQ.put({'type': 'BackendCmd',
										 'cmdName': 'saveChallenge',
										 'cmdParams': [parser]})


					elif parser.typeName == 'challengeCancelled' or parser.typeName == 'challengeDeclined':
						self.inputQ.put({'type': 'BackendCmd',
										 'cmdName': 'deleteChallenge',
										 'cmdParams': [parser.id]})




	def run(self):
		self._getEvents()