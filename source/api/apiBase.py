import os

class APIBase:

	def __init__(self):


		path = 'secrets/lichess.token'
		start = os.getcwd()

		relPath = os.path.relpath(path, start)

		with open (relPath, 'r') as f:
			token = f.read()
		self.authHeader = {
		'Authorization': f'Bearer {token}'
		}
