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


		response = requests.post(f'https://lichess.org/api/challenge/{opponent}', data=payload, headers=self.authHeader)

		if response.status_code == 200:
			log.debug(f'Challenge Sent to {opponent}')
		
		else:
			log.warning(f'Challenge Unsuccessfully Sent. Status Code: {response.status_code}\n')
			print(response.headers)

	def acceptChallenge(self, challengeId):

		response = requests.post(f'https://lichess.org/api/challenge/{challengeId}/accept', headers=self.authHeader)

		if response.status_code == 200:
			log.debug(f'Challenge Accepted. ID: {challengeId}')

		else:

			log.warning(f'Challenge Unsuccessfully Accepted. Status Code: {response.status_code}\n')

	def declineChallenge(self, challengeId):

		response = requests.post(f'https://lichess.org/api/challenge/{challengeId}/decline', headers=self.authHeader)

		if response.status_code == 200:
			log.debug(f'Challenge Declined. ID: {challengeId}')

		else:

			log.warning(f'Challenge Unsuccessfully Declined. Status Code: {response.status_code}\n')
		