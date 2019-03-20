import sys
from .TrelloAPI import TrelloApi

import requests
import pprint
import inspect

class TrelloMembers(object):
    varry = 'method 1'

    def __init__(self):
        self.user = TrelloApi('1935e1c580f75d052d9e43373518994da776ebd81f43c9763bea3a5509f0dd4a')

    def method1(self):
        print('method1')
        self.user.processUser()


