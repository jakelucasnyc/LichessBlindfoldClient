import logging
import json
from .apiBase import APIBase
from cmdHandler import CmdHandler
from threading import Thread
import requests
from parse import EventParser
import time

log = logging.getLogger(__name__)


class APIGetEvents(APIBase, Thread):

	def __init__(self, inputQ):
		APIBase.__init__(self)
		Thread.__init__(self)
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
					self.inputQ.put({'type': 'BackendCmd', 'cmdName': 'outputEvent', 'cmdParams': [parser]})

					#if a game has started, start the game play process
					if parser.typeName == 'gameStart':
						time.sleep(2)
						self.inputQ.put({'type': 'BackendCmd', 'cmdName': 'streamGameEvents', 'cmdParams': [self.inputQ, parser.id]})
						# return




	def run(self):
		self._getEvents()