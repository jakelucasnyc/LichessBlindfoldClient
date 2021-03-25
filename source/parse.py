class Parser:

	def __init__(self, typeName, details, timeControl=None, opponent=None, destUser=None):
		self.typeName = typeName
		self.details = details
		self.opponent = opponent
		self.timeControl = timeControl
		self.id = details['id']


	@classmethod
	def fromEvent(cls, eventJSON):
		typeName = eventJSON['type']
		if typeName == 'gameStart' or typeName == 'gameFinish':
			details = eventJSON['game']
		elif typeName == 'challenge' or typeName == 'challengeCanceled' or typeName == 'challengeDeclined':
			details = eventJSON['challenge']
			opponent = details['challenger']
			timeControl = details['timeControl']
			destUser = details['destUser']
		else:
			log.error('No Details in Event')

		return cls(typeName=typeName, details=details, timeControl=timeControl, opponent=opponent, destUser=destUser)

