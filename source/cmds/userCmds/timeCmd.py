import datetime
from cmds.baseCmds import BaseUserCmd

class time(BaseUserCmd):
	
	def __init__(self):
		super().__init__()
		self.time = datetime.datetime.now()

	def run(self):

		print('CURRENT TIME: '+str(self.time))