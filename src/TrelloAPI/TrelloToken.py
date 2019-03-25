import requests
import pprint
from src.TrelloAPI import TrelloAPI

class TrelloToken(TrelloAPI.TrelloApi):

    tokenInfo = None

    def __init__(self, user_token):
        self.log()
        super().__init__(user_token)
        self.tokenKey = '?token=' + self.user_token + '&key=' + self.apiKey
        self.log(self.tokenKey)
        self.tokenURL = self.baseURL + '/tokens/' + self.user_token + self.tokenKey
        self.log(self.tokenURL)


    def requestTokenInfo(self):
        self.log()
        r = requests.get(self.tokenURL)
        self.log('Status Code: ' + str(r.status_code))
        pprint.pprint(r.json())
        self.tokenInfo = r.json()
        return r.json()


    def getIDMember(self):
        self.log()
        i = self.tokenInfo['idMember']
        self.log(i)
        return i
