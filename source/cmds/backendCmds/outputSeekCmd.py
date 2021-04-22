from cmds.baseCmds import BaseBackendCmd

class outputSeek(BaseBackendCmd):


	def __init__(self, running, time, increment):

		super().__init__()

		self.time = time
		self.increment = increment
		self.running = running

	def run(self):

		if self.running:
			print(f'Seeking for {self.time}+{self.increment} game.')

		elif not self.running:

			print(f'Seek for {self.time}+{self.increment} game has timed out.')