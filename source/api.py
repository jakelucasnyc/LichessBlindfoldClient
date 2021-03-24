import logging
import aiohttp
import asyncio
# from play import Play
# from parser import Parser
# from cli import CLI

log = logging.getLogger(__name__)
class API:

	def __init__(self, authHeader):
		self.authHeader = authHeader

	async def test(self):
		print('helloworld')

	async def _getEvents(self, session, loop):
		async with session.get('https://lichess.org/api/stream/event', headers=self.authHeader) as response:
			log.debug('Event Status:' + str(response.status))
			log.info('Listening For Events')
			await loop.create_task(self.test())

			
			async for line in response.content:
				if line != b'\n':
					yield line.decode('utf-8')
				# print(line)


	async def handleEvents(self, session, loop):
		while True:
			events = []
			async for event in self._getEvents(session, loop):
				print('\nhandled event\n')

		# print(events)

	async def getAccount(self, session, loop):
		async with session.get('https://lichess.org/api/account', headers=self.authHeader) as response:

			log.debug(response.status)
			print(await response.json())



	# async def seek(self, time, increment, rated=False, challenge=True, oppponent=None):



	# def acceptOrDecline(self)
