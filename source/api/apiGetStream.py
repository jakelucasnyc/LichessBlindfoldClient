import logging
import asyncio
import aiohttp
import json
# from play import Play
from .apiBase import APIBase
from cmdHandler import CmdHandler

log = logging.getLogger(__name__)
class APIGetStream(APIBase):

	def __init__(self):
		super().__init__()
		self.timeout = aiohttp.ClientTimeout(total=None)

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
			async for event in self._getEvents():
				eventJSON = json.loads(event)

				log.debug(f'\n\n{eventJSON}\n\n')
				CmdHandler.fromBackend('outputEvent', [eventJSON]).run()
				

				if eventJSON['type'] == 'gameStarted':
					return

		# print(events)
	#GET
	# async def getAccount(self):
	# 	async with self.session.get('https://lichess.org/api/account', headers=self.authHeader) as response:

	# 		log.debug(response.status)
	# 		print(await response.json())
	# #POST

	# async def seek(self, time, increment, rated=False, challenge=True, oppponent=None):



	# def acceptOrDecline(self)


