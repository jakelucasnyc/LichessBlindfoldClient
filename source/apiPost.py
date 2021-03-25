import logging
import asyncio

log = logging.getLogger(__name__)
class APIPost:

	def __init__(self, session, loop):

		with open ('./secrets/lichess.token', 'r') as f:
			token = f.read()
		self.authHeader = {
		'Authorization': f'Bearer {token}'
		}

		self.session = session
		self.loop = loop


	async def sendChallenge(self, opponent, limit, increment):
		payload = {
			'clock.limit': limit,
			'clock.increment': increment

		}

		async with self.session.post(f'https://lichess.org/api/challenge/{opponent}', json=payload, headers=self.authHeader)as response:
			if response.status == 200:
				log.info(f'Challenge Sent to {opponent}')

			log.debug(await response.json())
		