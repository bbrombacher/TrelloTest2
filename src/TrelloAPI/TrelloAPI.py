import requests
import pprint
import inspect


class TrelloApi():
    def __init__(self, user_token):
        # the API Key provided to me from Trello to perform API operations.
        self.apiKey = '84c263c996f3197cae36c9af02352a9d'
        # the token manually created from my own account to perform local testing.
        # in a real application this token will need to be acquired on a per user basis.
        self.user_token = '1935e1c580f75d052d9e43373518994da776ebd81f43c9763bea3a5509f0dd4a'
        self.baseURL = 'https://api.trello.com/1'


#utility methods

    def log(self, message=None):
        # str(inspect.stack()[1].filename
        if message is None:
            print(str(inspect.getmodulename(inspect.stack()[1].filename)) + ': ' +
                  inspect.stack()[1].function)
        else:
            print(str(inspect.getmodulename(inspect.stack()[1].filename)) + ': ' +
                  inspect.stack()[1].function + ': ' + message)

    def getActualKeys(self, json):
        self.log()
        actualkeys = []
        for x in json:
            actualkeys.append(x)
        self.log('actual keys: ' + str(actualkeys))
        self.log('actual keys length: ' + str(len(actualkeys)))

        return actualkeys