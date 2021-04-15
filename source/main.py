from api.apiGetStream import APIGetStream, APIGetEvents
import asyncio
import aiohttp
import logging
from cli import CLI
from cmdHandler import CmdHandler
import threading
from queue import Queue
import time

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


async def main():

	#initializing commands
	inputQ = Queue()
	# outputQ = Queue()
	# apiGetStream = APIGetStream(inputQ)
	# events = asyncio.create_task(apiGetStream.handleEvents())#listening for events
	eventGetter = APIGetEvents(inputQ)
	eventGetter.start()

	time.sleep(1)
	cli = CLI(inputQ)
	cli.start()

	while True:
		
		# print('in loop')
		# #if no events are coming in from lichess or the cli
		# if inputQ.empty():
		# 	continue
		# #if there are events coming
		# elif not inputQ.empty():

		#example return = ['UserCmd', cmdCls, cmdParams] or ['BackendCmd', 'cmdCls', cmdParams]
		# await asyncio.gather(events)
		# print('past await')
		qEntry = inputQ.get()
		# print('qEntry', qEntry)
		#send the qEntry to the command handler
		if qEntry[0] == 'BackendCmd':
			cmdResult = CmdHandler.fromBackend(qEntry[1], qEntry[2]).run()

		elif qEntry[0] == 'UserCmd':
			cmdResult = CmdHandler.fromUser(qEntry[1], qEntry[2]).run()

		if not cmdResult:
			continue

		#figure out what to do with the return values of the command
		else:
			pass



	# await asyncio.gather(events)







if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	try:
		loop.run_until_complete(main())
	except Exception as e:
		log.error(e)
	finally:
		loop.run_until_complete(loop.shutdown_asyncgens())
		loop.close()