import logging
import asyncio
from .apiBase import APIBase

log = logging.getLogger(__name__)
class APIPost(APIBase):

	async def sendChallenge(self, opponent, limit, increment):
		payload = {
			'clock.limit': limit,
			'clock.increment': increment

		}

		async with self.session.post(f'https://lichess.org/api/challenge/{opponent}', json=payload, headers=self.authHeader)as response:
			if response.status == 200:
				log.info(f'Challenge Sent to {opponent}')

			log.debug(await response.json())
		