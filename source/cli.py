from parse import Parser
import logging
import asyncio
from cmds.userCmds import *
from cmds.baseCmds import BaseUserCmd
from inspect import signature
from secrets import secrets
import re
import threading
from cmdHandler import CmdHandler
import time

log = logging.getLogger(__name__)


class CLI(threading.Thread):


	def __init__(self):
		
		Thread.__init__(self, name='CLI')
		self.cmdDict = {cls.__name__: cls for cls in BaseUserCmd.__subclasses__()}
		# self.extraCmdParams = [self.loop, self.session]
		# self.cmdExtraDelims = ['+']
		# self.eventActing = False
		# self.gameEventActing = False

	def run(self):
		while True:
			time.sleep(1)
			inputText = str(input('> '))
			if not inputText:
				continue
			valid, cmdCls, cmdParams = self.verifyCommand(inputText)
			if valid:
				CmdHandler.fromUser(cmdCls, cmdParams).run()
				

	def verifyCommand(self, cmdText):
		#separating words with possible delimiters
		cmdWords = re.split('[\s+]', cmdText.strip())
			
		cmdWord = cmdWords[0]
		cmdParams = cmdWords[1:]
			#inserting extra command parameters in reverse order so that they end up in the correct order within the list
		# for param in reversed(self.extraCmdParams):
		# 	cmdParams.insert(0, param) 
		#if the first word in the command is a valid command:
		if cmdWord in self.cmdDict.keys():

			cmdCls = self.cmdDict[cmdWord]
			#if the number of words in the command - 1 (the initial command) == the number of parameters for the __init__ method of the command class: 
			if len(cmdParams) == len(signature(cmdCls).parameters):
				return True, cmdCls, cmdParams
			else:
				print('Invalid Parameters. Type "help" to see the parameters for each command')
				self.run()
				return False
		else:
			print('Invalid Command. Type "help" to see the possible commands')
			return False

	











