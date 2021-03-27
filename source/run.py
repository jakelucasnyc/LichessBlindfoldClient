from api.apiGetStream import APIGetStream
import asyncio
import aiohttp
import logging
from cli import CLI
from cmdHandler import CmdHandler

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


async def run():

	
	apiGetStream = APIGetStream()

	events = asyncio.create_task(apiGetStream.handleEvents())#listening for events
	cli = CLI()
	cli.start()
	print(cli.name)

	while True:
		await asyncio.gather(events)

	# print(token)







if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	try:
		loop.run_until_complete(run())
	except Exception as e:
		log.error(e)
	finally:
		loop.run_until_complete(loop.shutdown_asyncgens())
		loop.close()