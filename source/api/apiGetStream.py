import logging
import asyncio
import aiohttp
import json
# from play import Play
from .apiBase import APIBase
from cmdHandler import CmdHandler
from threading import Thread
import requests

log = logging.getLogger(__name__)
class APIGetStream(APIBase):

	def __init__(self, inputQ):
		super().__init__()
		self.timeout = aiohttp.ClientTimeout(total=None)
		self.inputQ = inputQ

	async def _getEvents(self):
		log.info('Listening For Incoming Events')
		async with aiohttp.ClientSession() as session:
			async with session.get('https://lichess.org/api/stream/event', headers=self.authHeader) as response:
				log.debug('Event Status:' + str(response.status))
				

				
				async for line in response.content:
					if line != b'\n':
						yield line.decode('utf-8')
					# print(line)


	async def handleEvents(self):
		while True:
			print('in handleEvents')
			async for event in self._getEvents():
				eventJSON = json.loads(event)

				log.debug(f'\n\n{eventJSON}\n\n')
				
				self.inputQ.put(['BackendCmd', 'outputEvent', [eventJSON]])
		# print(events)
	#GET
	# async def getAccount(self):
	# 	async with self.session.get('https://lichess.org/api/account', headers=self.authHeader) as response:

	# 		log.debug(response.status)
	# 		print(await response.json())
	# #POST

	# async def seek(self, time, increment, rated=False, challenge=True, oppponent=None):



	# def acceptOrDecline(self)


class APIGetEvents(APIBase, Thread):

	def __init__(self, inputQ):
		APIBase.__init__(self)
		Thread.__init__(self)
		self.timeout = aiohttp.ClientTimeout(total=None)
		self.inputQ = inputQ


	def _getEvents(self):
		with requests.Session() as s:
			response = s.get('https://lichess.org/api/stream/event', headers=self.authHeader, stream=True)
			log.info('Listening for Incoming Events')
			for line in response.iter_lines():

				#filtering out keep-alive b"\n" responses
				if line:
					eventJSON = json.loads(line.decode('utf-8'))
					self.inputQ.put(['BackendCmd', 'outputEvent', [eventJSON]])



	def run(self):
		self._getEvents()
