from cmds.baseCmds import BaseBackendCmd
from secrets import secrets

class outputEvent(BaseBackendCmd):

	def __init__(self, parser):
		BaseBackendCmd.__init__(self)
		self.parser = parser
		
		

	def run(self):
		

		

		if self.parser.typeName == 'gameStart':
			pass

		elif self.parser.typeName == 'gameFinish':
			pass

		#if a challenge was sent or received
		elif self.parser.typeName == 'challenge':
			self.log.info('INCOMING EVENT:')

			#if the user sent the challenge
			if self.parser.opponent['id'] == secrets.USERNAME.lower():

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
					print(f'Challenge ID: {self.parser.id}')

		elif self.parser.typeName == 'challengeCanceled':

			self.log.info('INCOMING EVENT:')

			if self.parser.timeControl['type'] == 'unlimited':
				print(f'{self.parser.opponent["name"]} has cancelled their challenge for an unlimited time game.')
			if self.parser.timeControl['type'] == 'clock':
				print(f'{self.parser.opponent["name"]} has cancelled their challenge for a {self.parser.timeControl["show"]} game.')

		elif self.parser.typeName == 'challengeDeclined':

			self.log.info('INCOMING EVENT:')

			if self.parser.destUser['id']  == secrets.USERNAME.lower():
				print(f'Challenge (ID: {self.parser.id}) was successfully declined.')

			else:
				print(f'{self.parser.destUser["name"]} has declined your challenge.')

		else:
			self.log.info('INCOMING EVENT:')
			self.log.error('Invalid typeName')