import logging
import asyncio
from .apiBase import APIBase
import requests

log = logging.getLogger(__name__)
class APIPost(APIBase):

	def sendChallenge(self, opponent, limit, increment):
		payload = {
			'clock.limit': limit,
			'clock.increment': increment

		}

		with requests.Session() as s:

			response = s.post(f'https://lichess.org/api/challenge/{opponent}', data=payload, headers=self.authHeader)

			if response.status_code == 200:
				log.debug(f'Challenge Sent to {opponent}')

			log.debug(response.json())
		