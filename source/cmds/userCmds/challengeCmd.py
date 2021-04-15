from api.apiPost import APIPost
from cmds.baseCmds import BaseUserCmd

class challenge(BaseUserCmd):

	
	def __init__(self, opponent, limit, increment):
		super().__init__()
		self.opponent = opponent
		self.limit = limit
		self.increment = increment


	def run(self):

		apiPost = APIPost()
		apiPost.sendChallenge(self.opponent, int(self.limit)*60, int(self.increment))