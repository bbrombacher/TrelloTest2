import requests
from src.TrelloAPI import TrelloAPI
from src.Utility import utils

class TrelloToken(TrelloAPI.TrelloApi):


    def __init__(self, user_token):
        utils.log()
        super().__init__(user_token)


    def requestTokenInfo(self):
        #https://developers.trello.com/reference#tokens
        utils.log()
        token_url = self.baseURL + '/tokens/' + self.user_token + self.tokenKey
        utils.log(token_url)
        r = requests.get(token_url)
        utils.log(r.text)
        return r


#should be able to remove the code below
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
