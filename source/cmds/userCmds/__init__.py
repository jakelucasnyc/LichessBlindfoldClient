from ..baseCmds import BaseUserCmd
from .timeCmd import time
from .challengeCmd import challenge
from .acceptChallengeCmd import acceptChallenge
from .declineChallengeCmd import declineChallenge
from .moveCmd import move
from .resignCmd import resign
from .drawCmd import draw
from .declineDrawCmd import declineDraw
from .abortCmd import abort

class help(BaseUserCmd):

	def __init__(self):
		super().__init__()
		self.cmdList = [cmd for cmd in BaseUserCmd.__subclasses__()]

	def run(self):


		print('\nCOMMAND DOCUMENTATION FORMAT:')
		print('command_word -> parameter_1 + parameter_2 + parameter_3\n')
		print('HOW TO TYPE IT:')
		print('command_word parameter_1 parameter_2 parameter_3\n')
		print('COMMAND LIST:\n\n')
		for cmd in self.cmdList:

			if hasattr(cmd, 'showHelp'):

				cmd.showHelp()
