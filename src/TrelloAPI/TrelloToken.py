import requests
import pprint
from src.TrelloAPI import TrelloAPI

class TrelloToken(TrelloAPI.TrelloApi):

    tokenInfo = None

    def __init__(self, user_token):
        self.log()
        super().__init__(user_token)
        self.tokenURL = self.baseURL + '/tokens/' + self.user_token + self.tokenKey


    def requestTokenInfo(self):
        self.log()
        r = requests.get(self.tokenURL)
        self.log('Status Code: ' + str(r.status_code))
        pprint.pprint(r.json())
        self.tokenInfo = r
        return r

    def getIDMember(self):
        self.log()
        i = self.tokenInfo.json()['idMember']
        self.log(i)
        return i

    def getStatusCode(self):
        self.log()
        i = self.tokenInfo.status_code
        self.log(str(i))
        return i