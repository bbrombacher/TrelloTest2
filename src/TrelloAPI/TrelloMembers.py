from src.TrelloAPI import TrelloAPI
from src.Utility import utils

import requests
import pprint


class TrelloMembers(TrelloAPI.TrelloApi):

    def __init__(self, user_token, member_id):
        utils.log()
        super().__init__(user_token)
        self.member_id = member_id


    def requestMember(self):
        #https://developers.trello.com/reference#membersid
        utils.log()
        members_url = self.baseURL + '/members/' + self.member_id + self.tokenKey
        utils.log(members_url)
        r = requests.get(members_url)
        utils.log(r.text)
        return r

    def requestMemberField(self, field):
        #https://developers.trello.com/reference#membersidfield
        utils.log()
        members_field_url = self.baseURL + '/members/' + self.member_id + '/' + field + self.tokenKey
        utils.log(members_field_url)
        r = requests.get(members_field_url)
        utils.log(r.text)
        return r

    def requestMembersBoards(self, query_params):
        #https://developers.trello.com/reference#membersidboards
        utils.log()
        members_boards_url = self.baseURL + '/members/' + self.member_id + self.tokenKey
        utils.log(members_boards_url)
        r = requests.get(members_boards_url, params=query_params)
        utils.log(r.text)
        return r

