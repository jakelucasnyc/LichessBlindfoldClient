from api.apiGetEvents import APIGetEvents
from api.apiGetGameEvents import APIGetGameEvents
from api.apiGame import APIGame
from api.apiPost import APIPost
from api.apiChallengeData import APIChallengeData
import asyncio
import logging
from cli import CLI
from cmdHandler import CmdHandler
import threading
from queue import Queue
import time

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


async def main():

	#initializing objects
	inputQ = Queue()
	globalObjs = {
		'APIPost': APIPost(),
		'APIChallengeData': APIChallengeData()
	}
	# outputQ = Queue()
	# apiGetStream = APIGetStream(inputQ)
	# events = asyncio.create_task(apiGetStream.handleEvents())#listening for events
	eventGetter = APIGetEvents(inputQ)
	eventGetter.start()

	time.sleep(1)
	cli = CLI(inputQ)
	cli.start()

	while True:
		
		
		#example return = {'type': 'UserCmd', 'cmdCls': 'cmdCls', 'cmdParams': cmdParams, 'objs': globalObjList}
						# {'type': 'BackendCmd', 'cmdName': 'name', 'cmdParams': cmdParams, 'objs': globalObjList}
						# {'type': 'globalObjAdd', 'cls': cls, 'clsParams': clsParamsDict}
		qEntry = inputQ.get()
		# print('qEntry', qEntry)
		#send the qEntry to the command handler
		objsSent = {}
		cmdResult = ''
		if qEntry['type'] == 'BackendCmd':


			cmdWithParams = CmdHandler.fromBackend(cmdName=qEntry['cmdName'], cmdParams=qEntry['cmdParams'], objDict=objsSent)

			#if there are any objects that the command needs, add them to the dict. If objsNeeded is empty, the dict remains empty
			cmdWithParams.objDict.update({clsName: inst for clsName, inst in globalObjs.items() if clsName in cmdWithParams.cmdCls.objsNeeded})

			cmdResult = cmdWithParams.run()

		elif qEntry['type'] == 'UserCmd':

			#this returns an empty dict if the objsNeeded list is empty or has no clsName in common with the globalObjs dict
			objsSent = {clsName: inst for clsName, inst in globalObjs.items() if clsName in qEntry['cmdCls'].objsNeeded}

			cmdResult = CmdHandler.fromUser(cmdCls=qEntry['cmdCls'], cmdParams=qEntry['cmdParams'], objDict=objsSent).run()

		elif qEntry['type'] == 'globalObjAdd':
			globalObjs.update({qEntry['cls'].__name__: qEntry['cls'](**qEntry['clsParams'])})

		elif qEntry['type'] == 'globalObjDel':
			globalObjs.pop(qEntry['cls'].__name__)


		#example cmdResult = [('CRUD', 'obj', 'key', 'value'), ('CRUD', 'obj', 'key', 'value')]
		if not cmdResult:
			continue

		#figure out what to do with the return values of the command
		elif cmdResult[0] == 'APIPlay':
			pass



	# await asyncio.gather(events)







if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	try:
		loop.run_until_complete(main())

	finally:
		loop.run_until_complete(loop.shutdown_asyncgens())
		loop.close()