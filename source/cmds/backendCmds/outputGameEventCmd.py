from cmds.baseCmds import BaseBackendCmd

class outputGameEvent(BaseBackendCmd):

	def __init__(self, dataDict):
		super().__init__()
		self.dataDict = dataDict

	def run(self):

		self.log.info('INCOMING GAME EVENT:')


		if self.dataDict['type'] == 'initial':

			print(f'{self.dataDict["white"]} is white!')
			print(f'{self.dataDict["black"]} is black!')
			print(f'Time control is {self.dataDict["showTimeControl"]}.')
			print(f'Happy Blindfold!')

		elif self.dataDict['type'] == 'update':

			print(f"{self.dataDict['mover']} played {self.dataDict['move']}.")

		elif self.dataDict['type'] == 'gameOver':

			print(f"Game Over! Outcome: {self.dataDict['outcome']}.")
			if self.dataDict['winner'] is not None:
				print(f'Winner: {self.dataDict["winner"]}')

		elif self.dataDict['type'] == 'drawOffer':

			print(f"{self.dataDict['drawer']} offered a draw.")
