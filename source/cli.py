from parse import Parser
import logging
import asyncio
from aioconsole import ainput

log = logging.getLogger(__name__)


class CLI:



	def __init__(self, loop):
		self.loop = loop
		self.getInput = None
		commands = {
			'quit': self.loop.stop
		}

	async def outputEvent(self, eventJSON):
		parser = Parser.fromEvent(eventJSON)

		if parser.typeName == 'gameStart':
			print(f'Game Started! GameID: {parser.id}')

		elif parser.typeName == 'gameFinish':
			print(f'Game Finished! GameID: {parser.id}')

		elif parser.typeName == 'challenge':
			if parser.timeControl['type'] == 'unlimited':
				print(f'{parser.opponent["name"]} has challenged you to an unlimited time game!')
			if parser.timeControl['type'] == 'clock':
				print(f'{parser.opponent["name"]} has challenged you to a {parser.timeControl["show"]} game!')

		elif parser.typeName == 'challengeCanceled':
			if parser.timeControl['type'] == 'unlimited':
				print(f'{parser.opponent["name"]} has cancelled their challenge for an unlimited time game!')
			if parser.timeControl['type'] == 'clock':
				print(f'{parser.opponent["name"]} has cancelled their challenge for a {parser.timeControl["show"]} game!')

		elif parser.typeName == 'challengeDeclined':
			print(f'{parser.destUser["name"]} has declined your challenge!')

		else:
			log.error('Invalid typeName')


		if self.getInput is not None:
			self.getInput.cancel()
		self.getInput = self.loop.create_task(self.input())
		try:
			await self.getInput
		except asyncio.CancelledError:
			log.debug('\ninput cancelled outside self.input\n')

	async def input(self):
		await asyncio.sleep(0.01)#delay to make sure the input line is always last
		cmd = ainput("> ")
		try:
			cmdList = await asyncio.gather(cmd)
		except asyncio.CancelledError:
			log.debug('\ninput cancelled inside self.input\n')
		else:

			cmdText = str(cmdList[0].strip())#list with one element stripped of surrounding whitespace

			print('COMMAND: '+cmdText)

			#recalling the input function to be able to input another command after the output
			self.getInput = self.loop.create_task(self.input())
			try:
				await self.getInput
			except asyncio.CancelledError:
				log.debug('\ninput cancelled outside self.input\n')









