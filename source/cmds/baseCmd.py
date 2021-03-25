import logging

class BaseCmd:

	asyn = False


	def __init__(self, loop, session):
		self.loop = loop
		self.session = session
		self.log = logging.getLogger('commandHandler')


