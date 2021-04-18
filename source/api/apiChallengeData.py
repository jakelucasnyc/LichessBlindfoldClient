import logging
from api.apiBase import APIBase


log = logging.getLogger(__name__)
class APIChallengeData(APIBase):

	def __init__(self):
		super().__init__()
		self.challengeList = []

	def addChallengeEntry(self, dataDict):

		self.challengeList.append(dataDict)
		print(self.challengeList)

	def deleteChallengeEntry(self, challengeId):

		for entry in self.challengeList:
			if entry['id'] == challengeId:

				self.challengeList.remove(entry)
				# print(self.challengeList)
				return

		else:
			log.error('Challenge ID Not Found. Aborting Deletion')

		
