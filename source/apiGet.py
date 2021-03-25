import logging
import aiohttp
import asyncio
import json
# from play import Play
from cli import CLI

log = logging.getLogger(__name__)
class APIGet:

	def __init__(self, session, loop):

		with open ('./secrets/lichess.token', 'r') as f:
			token = f.read()
		self.authHeader = {
		'Authorization': f'Bearer {token}'
		}

		self.session = session
		self.loop = loop
		self.cli = CLI(self.session, self.loop)

	async def _getEvents(self):
		log.info('Listening For Incoming Events')
		async with self.session.get('https://lichess.org/api/stream/event', headers=self.authHeader) as response:
			log.debug('Event Status:' + str(response.status))
			

			
			async for line in response.content:
				if line != b'\n':
					yield line.decode('utf-8')
				# print(line)


	async def handleEvents(self):
		while True:
			async for event in self._getEvents():
				eventJSON = json.loads(event)

				# log.info('INCOMING EVENT:')
				log.debug(f'\n\n{eventJSON}\n\n')
				self.loop.create_task(self.cli.outputEvent(eventJSON))

		# print(events)
	#GET
	async def getAccount(self):
		async with self.session.get('https://lichess.org/api/account', headers=self.authHeader) as response:

			log.debug(response.status)
			print(await response.json())
	#POST

	# async def seek(self, time, increment, rated=False, challenge=True, oppponent=None):



	# def acceptOrDecline(self)


