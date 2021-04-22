from cmds.baseCmds import BaseUserCmd
import datetime

class test(BaseUserCmd):

	def __init__(self):
		super().__init__()
		self.time = datetime.datetime.now()

	def run(self):

		print(f'Test Command @ Time: {str(self.time)}')