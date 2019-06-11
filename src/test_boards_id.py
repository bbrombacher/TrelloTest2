from .TrelloAPI import TrelloToken
from .TrelloAPI import TrelloMembers
from .TrelloAPI import TrelloBoards
from .Utility import utils
import datetime

import pprint

import pytest

class TestBoards(object):
    #https://developers.trello.com/reference#boardsboardid-1
    user_token = 'd162d502aa68a59be4b15279a2fafebeb33b93a4282e2ff0c96e7babf6a16514'

    expected_status_code = 200

    @pytest.fixture
    def trelloMember(self):
        a = TrelloToken.TrelloToken(self.user_token)
        a.requestTokenInfo()
        b = TrelloMembers.TrelloMembers(self.user_token,
                                        a.getIDMember())
        return b

    @pytest.fixture
    def trelloBoardObject(self):
        b = TrelloBoards.TrelloBoards(self.user_token)
        return b

    def test_statusCode(self, trelloMember, trelloBoardObject):
        utils.log()
        board_membership = self.getBoardMembership(trelloMember)
        board_ids = self.getBoardIds(board_membership)
        board = self.getBoard(board_ids[0], trelloBoardObject)
        assert board.status_code == self.expected_status_code

    def test_updateBoardDescription(self,trelloMember, trelloBoardObject):
        utils.log()
        board_membership = self.getBoardMembership(trelloMember)
        board_ids = self.getBoardIds(board_membership)
        current_datetime = datetime.datetime.now()
        new_desc = current_datetime
        r = trelloBoardObject.putBoardId(board_ids[0], query_params={'desc': new_desc})
        assert str(new_desc) == r.json()['desc']

    ## Get Methods
    def getBoardMembership(self, trelloMember):
        utils.log()
        member_board_query_params = {'memberships': 'all'}
        request_boards = trelloMember.requestMembersBoards(member_board_query_params)
        return request_boards

    def getBoardIds(self, board_membership):
        utils.log()
        return board_membership.json()['idBoards']

    def getBoard(self, board_id, trelloBoardObject):
        utils.log()
        board_query_params = {}
        request_board = trelloBoardObject.requestBoard(board_id, board_query_params)
        return request_board
