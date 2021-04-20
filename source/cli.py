import logging
from cmds.userCmds import *
from cmds.baseCmds import BaseUserCmd
from inspect import signature
from secrets import secrets
import re
from threading import Thread
from cmdHandler import CmdHandler
import time

log = logging.getLogger(__name__)


class CLI(Thread):


	def __init__(self, inputQ):
		
		Thread.__init__(self, name='CLI')
		self.cmdDict = {cls.__name__: cls for cls in BaseUserCmd.__subclasses__()}
		self._return = None
		self.inputQ = inputQ
		# self.extraCmdParams = [self.loop, self.session]
		# self.cmdExtraDelims = ['+']
		# self.eventActing = False
		# self.gameEventActing = False

	def run(self):
		while True:
			time.sleep(0.001)
			inputText = str(input('> '))
			if not inputText:
				continue
			valid, cmdCls, cmdParams, objsNeeded = self.verifyCommand(inputText)
			if valid:
				# self._return = [cmdCls, cmdParams]
				self.inputQ.put({
					'type': 'UserCmd', 
					'cmdCls': cmdCls, 
					'cmdParams': cmdParams, 
					'objs': objsNeeded
				})

			else:
				continue

	# def join(self, *args):
	# 	Thread.join(self, *args)
	# 	return self._return
				

	def verifyCommand(self, cmdText):
		#separating words with possible delimiters
		cmdWords = re.split('[\s+]', cmdText.strip())
			
		cmdWord = cmdWords[0]
		cmdParams = cmdWords[1:]

		if cmdWord in self.cmdDict.keys():

			cmdCls = self.cmdDict[cmdWord]
			#if the number of words in the command - 1 (the initial command) == the number of parameters for the __init__ method of the command class: 
			classParams = signature(cmdCls).parameters

			if (len(cmdParams) == len(classParams) and not 'objDict' in classParams) or (len(cmdParams) == len(classParams)-1 and 'objDict' in classParams) :

				if 'objDict' in classParams:
					return True, cmdCls, cmdParams, cmdCls.objsNeeded #bool, class, list, list
				else:
					return True, cmdCls, cmdParams, []
			else:
				print('Invalid Parameters. Type "help" to see the parameters for each command')
				return False, None, None, None
		else:
			print('Invalid Command. Type "help" to see the possible commands')
			return False, None, None, None

	











