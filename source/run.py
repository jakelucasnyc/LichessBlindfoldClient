from apiGet import APIGet
import asyncio
import aiohttp
import logging
from cli import CLI

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


async def run():

	with open ('./secrets/lichess.token', 'r') as f:
		token = f.read()
	authHeader = {
		'Authorization': f'Bearer {token}'
	}

	async with aiohttp.ClientSession() as session:

		apiGet = APIGet(authHeader, loop)
		cli = CLI(loop)

		events = loop.create_task(apiGet.handleEvents(session))#listening for events
		# await events

		cli.getInput = loop.create_task(cli.input()) #allowing us to enter a command before we get an event
		try:
			await asyncio.gather(events, cli.getInput)
		except asyncio.CancelledError:
			log.debug('\ninput cancelled outside self.input\n')

		# print(token)







if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	try:
		loop.create_task(run())
		loop.run_forever()
	except Exception as e:
		log.error(e)
	finally:
		loop.run_until_complete(loop.shutdown_asyncgens())
		loop.close()