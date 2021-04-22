from cmds.baseCmds import BaseUserCmd
from threading import Thread
import requests
import time

class seek(BaseUserCmd, Thread):

	objsNeeded = ['APIPost', 'inputQ']

	def __init__(self, time, increment, objDict=None):
		Thread.__init__(self)
		BaseUserCmd.__init__(self)
		self.time = time
		self.increment = increment

		self.authHeader = objDict['APIPost'].authHeader
		self.inputQ = objDict['inputQ']

		self.maxSeekDuration = 300



	def run(self):

		payload = {
			'time': self.time,
			'increment': self.increment
		}


		start = time.time()

		response = requests.post('https://lichess.org/api/board/seek', headers=self.authHeader, data=payload, stream=True)

		if response.status_code == 200:
			self.log.debug('Seek Successfully Created.')
			self.inputQ.put({
				'type': 'BackendCmd',
				'cmdName': 'outputSeek',
				'cmdParams': [True, self.time, self.increment]
			})

		else:
			self.log.warning(f'Seek Unsuccessfully Created. Status Code: {response.status_code}.')

		for line in response.iter_lines():

			if time.time() - start >= self.maxSeekDuration:
				self.inputQ.put({
					'type': 'BackendCmd',
					'cmdName': 'outputSeek',
					'cmdParams': [False, self.time, self.increment]
				})
				response.close()
				break



