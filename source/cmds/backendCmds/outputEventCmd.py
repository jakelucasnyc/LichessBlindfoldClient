from cmds.baseCmds import BaseBackendCmd
from parse import Parser
from threading import Thread
from secrets import secrets

class outputEvent(BaseBackendCmd, Thread):

	joinable = True

	def __init__(self, eventJSON):
		BaseBackendCmd.__init__(self)
		Thread.__init__(self)
		self.eventJSON = eventJSON
		self.parser = Parser.fromEvent(self.eventJSON)
		
		#if the event is being sent from me
		# if self.parser.opponent['name'] == secrets.USERNAME:
		# 	outputEvent.visible = False
		# else:
		# 	outputEvent.visible = True

	def run(self):
		#if I send anything that comes through as if another person did it:

		# if parser.opponent['name'] == secrets.USERNAME:
		# 	#this is used so that another ">" isn't printed after this is over
		# 	outputEvent.visible = False

		self.log.info('INCOMING EVENT:')

		if self.parser.typeName == 'gameStart':
			print(f'Game Started! GameID: {self.parser.id}')

		elif self.parser.typeName == 'gameFinish':
			print(f'Game Finished! GameID: {self.parser.id}')

		#if a challenge was sent or received
		elif self.parser.typeName == 'challenge':

			#if the user sent the challenge
			if self.parser.opponent['name'] == secrets.USERNAME:

				if self.parser.timeControl['type'] == 'unlimited':
					print(f'Challenge for an unlimited time game was successfully sent to {self.parser.destUser["name"]}!')
				elif self.parser.timeControl['type'] == 'clock':
					print(f'Challenge for a {self.parser.timeControl["show"]} game was successfully sent to {self.parser.destUser["name"]}!')

			#if the challenge was sent to the user
			else:

				if self.parser.timeControl['type'] == 'unlimited':
					print(f'{self.parser.opponent["name"]} has challenged you to an unlimited time game!')
				elif self.parser.timeControl['type'] == 'clock':
					print(f'{self.parser.opponent["name"]} has challenged you to a {self.parser.timeControl["show"]} game!')

		elif self.parser.typeName == 'challengeCanceled':
			if self.parser.timeControl['type'] == 'unlimited':
				print(f'{self.parser.opponent["name"]} has cancelled their challenge for an unlimited time game.')
			if self.parser.timeControl['type'] == 'clock':
				print(f'{self.parser.opponent["name"]} has cancelled their challenge for a {self.parser.timeControl["show"]} game.')

		elif parser.typeName == 'challengeDeclined':
			print(f'{self.parser.destUser["name"]} has declined your challenge.')

		else:
			self.log.error('Invalid typeName')