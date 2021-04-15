from cmds.baseCmds import *
from cmds.userCmds import *
from cmds.backendCmds import *
from inspect import signature
from threading import Thread
import asyncio
import logging

log = logging.getLogger(__name__)
class CmdHandler:

	def __init__(self, cmdCls, cmdParams):
		self.cmdCls = cmdCls
		self.cmdParams = cmdParams

	def run(self):

		cmdWithParams = self.cmdCls(*self.cmdParams)
		#print aftr the input line
		if cmdWithParams.visible and issubclass(self.cmdCls, BaseBackendCmd):
			# print('backendcmd?')
			print('')

		if not cmdWithParams.asyn:

			#if the command is a thread
			if issubclass(self.cmdCls, Thread):
				cmdWithParams.start()
				log.debug('Cmd Thread Started')
				if cmdWithParams.joinable:
					cmdWithParams.join()
					log.debug('Cmd Joined')

			#if the command isn't a thread.
			else:
				cmdWithParams.run()

		if cmdWithParams.asyn:
			asyncio.run_coroutine_threadsafe(cmdWithParams.run())
			log.debug('Cmd Coroutine Run')

		#give the illusion that the input function has been called again
		if cmdWithParams.visible and issubclass(self.cmdCls, BaseBackendCmd):
			print('> ', end='', flush=True)

	@staticmethod
	def findCommand(clsDict, cmdName, cmdParams):
		if cmdName in clsDict.keys():
			cmdCls = clsDict[cmdName]
			if len(cmdParams) != len(signature(cmdCls).parameters):
				raise Exception(f"Command '{cmdName}' was given incorrect paramters: {cmdParams}")
			return True, cmdCls, cmdParams
		else:
			raise Exception(f"Command '{cmdName}' doesn't exist")
		

	@classmethod
	def fromUser(cls, cmdCls, cmdParams):
		return cls(cmdCls, cmdParams)

	@classmethod
	def fromBackend(cls, cmdName, cmdParams):
		clsDict = {c.__name__: c for c in BaseBackendCmd.__subclasses__()}
		clsDict.update({c.__name__: c for c in BaseUserCmd.__subclasses__()})
		# print("Keys: "+str(clsDict))
		valid, cmdCls, cmdParams = CmdHandler.findCommand(clsDict, cmdName, cmdParams)
		if valid:
			log.debug('Valid Backend Command')
			return cls(cmdCls, cmdParams)
		else:
			raise Exception('Invalid Backend Command')



