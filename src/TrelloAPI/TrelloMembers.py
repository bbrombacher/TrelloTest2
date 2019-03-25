import sys
from .TrelloAPI import TrelloApi

import requests
import pprint
import inspect

class TrelloMembers(object):

    def __init__(self):
        self.user = TrelloApi('1935e1c580f75d052d9e43373518994da776ebd81f43c9763bea3a5509f0dd4a')

    def getMembersInfo(self):
        self.log()
        self.log()
        r = requests.get(self.membersURL)
        pprint.pprint(r.json())
        return r.json()

    def getMembersActions(self):
        self.log()

    def getMembersBoards(self):
        self.log()

    def getMembersBoardBackgrounds(self):
        self.log()