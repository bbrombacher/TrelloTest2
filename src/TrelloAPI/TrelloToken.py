import requests
from src.TrelloAPI import TrelloAPI
from src.Utility import utils

class TrelloToken(TrelloAPI.TrelloApi):

    tokenInfo = None

    def __init__(self, user_token):
        utils.log()
        super().__init__(user_token)
        self.tokenURL = self.baseURL + '/tokens/' + self.user_token + self.tokenKey


    def requestTokenInfo(self):
        #https://developers.trello.com/reference#tokens
        utils.log()
        utils.log(self.tokenURL)
        r = requests.get(self.tokenURL)
        utils.log(r.text)
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
