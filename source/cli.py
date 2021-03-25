from parse import Parser
import logging
import asyncio
from aioconsole import ainput
from cmds.synCmds import *
from cmds.asynCmds import *
from cmds.baseCmd import BaseCmd
from inspect import signature
from secrets import secrets

log = logging.getLogger(__name__)


class CLI:


	def __init__(self, session, loop):
		self.session = session
		self.loop = loop
		self.getInput = None
		self.cmdDict = {cls.__name__: cls for cls in BaseCmd.__subclasses__()}
		self.extraCmdParams = [self.loop, self.session]


	async def outputEvent(self, eventJSON):

		parser = Parser.fromEvent(eventJSON)
		#if I send anything that comes through as if another person did it:
		if parser.opponent['name'] == secrets.USERNAME:
			return
		
		#formatting interaction with command input marker
		if self.getInput is not None:
			self.getInput.cancel()
			
		print('')
		log.info('INCOMING EVENT:')

		if parser.typeName == 'gameStart':
			print(f'Game Started! GameID: {parser.id}')

		elif parser.typeName == 'gameFinish':
			print(f'Game Finished! GameID: {parser.id}')

		elif parser.typeName == 'challenge' and parser.opponent['name'] != secrets.USERNAME:
			
			if parser.timeControl['type'] == 'unlimited':
				print(f'{parser.opponent["name"]} has challenged you to an unlimited time game!')
			if parser.timeControl['type'] == 'clock':
				print(f'{parser.opponent["name"]} has challenged you to a {parser.timeControl["show"]} game!')

		elif parser.typeName == 'challengeCanceled':
			if parser.timeControl['type'] == 'unlimited':
				print(f'{parser.opponent["name"]} has cancelled their challenge for an unlimited time game.')
			if parser.timeControl['type'] == 'clock':
				print(f'{parser.opponent["name"]} has cancelled their challenge for a {parser.timeControl["show"]} game.')

		elif parser.typeName == 'challengeDeclined':
			print(f'{parser.destUser["name"]} has declined your challenge.')

		else:
			log.error('Invalid typeName')


		#calling self.input again to allow the user to input a command after the printed information
		self.getInput = self.loop.create_task(self.input())
		try:
			await self.getInput
		except asyncio.CancelledError:
			log.debug('\ninput cancelled outside self.input\n')

	async def input(self):
		await asyncio.sleep(0.01)#delay to make sure the input line is always last
		cmd = ainput("> ")
		try:
			cmdList = await asyncio.gather(cmd)
		except asyncio.CancelledError:
			log.debug('\ninput cancelled inside self.input\n')
		else:

			cmdText = str(cmdList[0].strip())#list with one element stripped of surrounding whitespace
			cmdWords = cmdText.split()

			
			
			cmdWord = cmdWords[0]
			cmdParams = cmdWords[1:]
			#inserting extra command parameters in reverse order so that they end up in the correct order within the list
			for param in reversed(self.extraCmdParams):
				cmdParams.insert(0, param) 
			#if the first word in the command is a valid command:
			if cmdWord in self.cmdDict.keys():

				cmdCls = self.cmdDict[cmdWord]
				#if the number of words in the command - 1 (the initial command) == the number of parameters for the __init__ method of the command class: 
				if len(cmdParams) == len(signature(cmdCls).parameters):
					#instantiate the class and fill in the parameters using the rest of the words in the command input
					if not cmdCls.asyn:
						cmdCls(*cmdParams).run()
					elif cmdCls.asyn:
						await cmdCls(*cmdParams).run()
					# print(signature(cmdCls).parameters)
			else:
				print('Invalid command. Please try again. Type "help" to get a list of valid commands')

			# print('COMMAND: '+cmdText)

			#recalling the input function to be able to input another command after the output
			self.getInput = self.loop.create_task(self.input())
			try:
				await self.getInput
			except asyncio.CancelledError:
				log.debug('\ninput cancelled outside self.input\n')









