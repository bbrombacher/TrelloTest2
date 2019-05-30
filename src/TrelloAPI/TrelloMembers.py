from src.TrelloAPI import TrelloAPI

import requests
import pprint


class TrelloMembers(TrelloAPI.TrelloApi):

    def __init__(self, user_token, member_id):
        self.log()
        super().__init__(user_token)
        self.member_id = member_id


    def requestMember(self):
        #https://developers.trello.com/reference#membersid
        self.log()
        members_url = self.baseURL + '/members/' + self.member_id + self.tokenKey
        self.log(members_url)
        r = requests.get(members_url)
        self.log(str(r.status_code))
        self.log(str(r.json()))
        return r

    def requestMemberField(self, field):
        #https://developers.trello.com/reference#membersidfield
        self.log()
        members_field_url = self.baseURL + '/members/' + self.member_id + '/' + field + self.tokenKey
        r = requests.get(members_field_url)
        self.log(str(r.status_code))
        self.log(str(r.json))
        return r

    def requestMembersActions(self):
        self.log()

    def requestMembersBoards(self):
        self.log()

    def requestMembersBoardBackgrounds(self):
        self.log()
