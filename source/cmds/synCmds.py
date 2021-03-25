from . import baseCmd
import sys


class quit(baseCmd.BaseCmd):

	def run(self):

		self.log.info('Quitting Application')
		try:
			self.loop.stop()
			self.loop.run_until_complete(self.loop.shutdown_asyncgens())
			self.loop.close()
			sys.exit()
		except RuntimeError as e:
			print('exception')