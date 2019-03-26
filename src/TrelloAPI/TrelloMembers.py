from src.TrelloAPI import TrelloAPI
import requests
import pprint


class TrelloMembers(TrelloAPI.TrelloApi):
    membersInfo = None

    def __init__(self, user_token, id_member):
        self.log()
        super().__init__(user_token)
        self.tokenKey = '?token=' + self.user_token + '&key=' + self.apiKey
        self.log(self.tokenKey)
        self.membersURL = self.baseURL + '/members/' + id_member + self.tokenKey
        self.log(self.membersURL)

    def requestMembersInfo(self):
        self.log()
        r = requests.get(self.membersURL)
        self.membersInfo = r
        self.log(str(self.membersInfo.status_code))
        self.log(str(r.json()))
        return r

    def getMembersActions(self):
        self.log()

    def getMembersBoards(self):
        self.log()

    def getMembersBoardBackgrounds(self):
        self.log()