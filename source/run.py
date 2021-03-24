from api import API
import asyncio
import aiohttp
import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


async def run():

	with open ('./secrets/lichess.token', 'r') as f:
		token = f.read()
	authHeader = {
		'Authorization': f'Bearer {token}'
	}

	async with aiohttp.ClientSession() as session:

		api = API(authHeader)
		# print(token)
		events = loop.create_task(api.handleEvents(session, loop))
		await events






if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	try:
		loop.create_task(run())
		loop.run_forever()
	except Exception as e:
		log.error(e)
	finally:
		loop.close()