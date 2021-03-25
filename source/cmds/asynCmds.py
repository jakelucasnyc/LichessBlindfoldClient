from . import baseCmd
from apiPost import APIPost

class challenge(baseCmd.BaseCmd):

	asyn = True

	def __init__(self, loop, session, opponent, limit, increment):
		super().__init__(loop, session)
		self.opponent = opponent
		self.limit = limit
		self.increment = increment


	async def run(self):

		apiPost = APIPost(self.session, self.loop)
		await apiPost.sendChallenge(self.opponent, int(self.limit)*60, int(self.increment))

