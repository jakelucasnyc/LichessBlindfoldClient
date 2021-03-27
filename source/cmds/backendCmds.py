from .baseCmds import BaseBackendCmd
from parse import Parser
from threading import Thread
from secrets import secrets


class outputEvent(BaseBackendCmd, Thread):

	joinable = True

	def __init__(self, eventJSON):
		BaseBackendCmd.__init__(self)
		Thread.__init__(self)
		self.eventJSON = eventJSON

	def run(self):

		parser = Parser.fromEvent(self.eventJSON)
		#if I send anything that comes through as if another person did it:
		if parser.opponent['name'] == secrets.USERNAME:
			return

		self.log.info('INCOMING EVENT:')

		if parser.typeName == 'gameStart':
			print(f'Game Started! GameID: {parser.id}')

		elif parser.typeName == 'gameFinish':
			print(f'Game Finished! GameID: {parser.id}')

		elif parser.typeName == 'challenge' and parser.opponent['name'] != secrets.USERNAME:
			
			if parser.timeControl['type'] == 'unlimited':
				print(f'{parser.opponent["name"]} has challenged you to an unlimited time game!')
			if parser.timeControl['type'] == 'clock':
				print(f'{parser.opponent["name"]} has challenged you to a {parser.timeControl["show"]} game!')

		elif parser.typeName == 'challengeCanceled':
			if parser.timeControl['type'] == 'unlimited':
				print(f'{parser.opponent["name"]} has cancelled their challenge for an unlimited time game.')
			if parser.timeControl['type'] == 'clock':
				print(f'{parser.opponent["name"]} has cancelled their challenge for a {parser.timeControl["show"]} game.')

		elif parser.typeName == 'challengeDeclined':
			print(f'{parser.destUser["name"]} has declined your challenge.')

		else:
			self.log.error('Invalid typeName')

