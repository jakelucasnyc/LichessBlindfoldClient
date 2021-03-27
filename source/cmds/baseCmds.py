import logging

class BaseCmd:

	asyn = False
	joinable = False
	visible = True

	def __init__(self):
		pass

class BaseUserCmd(BaseCmd):

	def __init__(self):

		self.log = logging.getLogger('UserCommandHandler')

class BaseBackendCmd(BaseCmd):

	def __init__(self):
		self.log = logging.getLogger('BackendCommandHandler')

