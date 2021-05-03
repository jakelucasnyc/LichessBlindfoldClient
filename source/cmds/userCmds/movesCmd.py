from cmds.baseCmds import BaseUserCmd

class moves(BaseUserCmd):

	objsNeeded = ['APIGame']

	def __init__(self, objDict=None):
		super().__init__()
		self.game = objDict['APIGame']

	def run(self):
		for idx, move in enumerate(self.game.sanMoveList):
			if idx % 2 == 0:
				print(f'{int(idx/2+1)}.', end=' ')
				print(move, end=' ')

			elif idx % 2 == 1:
				print(move)

		print('')