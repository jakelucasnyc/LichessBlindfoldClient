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

		#print aftr the input line
		if self.cmdCls.visible and issubclass(self.cmdCls, BaseBackendCmd):
			print('')

		if not self.cmdCls.asyn:
			if issubclass(self.cmdCls, Thread):
				t = self.cmdCls(*self.cmdParams)
				t.start()
				log.debug('Cmd Thread Started')
				if self.cmdCls.joinable:
					t.join()
					log.debug('Cmd Joined')

		if self.cmdCls.asyn:
			asyncio.run_coroutinue_threadsafe(self.cmdCls(*self.cmdParams).run())
			log.debug('Cmd Coroutine Ran')

		#give the illusion that the input function has been called again
		if self.cmdCls.visible and issubclass(self.cmdCls, BaseBackendCmd):
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



