import requests
import pprint
from src.TrelloAPI import TrelloAPI
from src.Utility import utils

class TrelloToken(TrelloAPI.TrelloApi):

    tokenInfo = None

    def __init__(self, user_token):
        utils.log()
        super().__init__(user_token)
        self.tokenURL = self.baseURL + '/tokens/' + self.user_token + self.tokenKey


    def requestTokenInfo(self):
        utils.log()
        r = requests.get(self.tokenURL)
        utils.log('Status Code: ' + str(r.status_code))
        pprint.pprint(r.json())
        self.tokenInfo = r
        return r

    def getIDMember(self):
        utils.log()
        i = self.tokenInfo.json()['idMember']
        utils.log(i)
        return i

    def getStatusCode(self):
        utils.log()
        i = self.tokenInfo.status_code
        utils.log(str(i))
        return i