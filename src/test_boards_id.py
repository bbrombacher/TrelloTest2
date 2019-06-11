from .TrelloAPI import TrelloToken
from .TrelloAPI import TrelloMembers
from .TrelloAPI import TrelloBoards
from .Utility import utils

import pprint

import pytest

class TestBoards(object):
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
        member_board_query_params = {'memberships': 'all'}
        request_boards = trelloMember.requestMembersBoards(member_board_query_params)

        board_ids = request_boards.json()['idBoards']
        board_query_params = {}
        request_board = trelloBoardObject.requestBoard(board_ids[0], board_query_params)
        pprint.pprint(request_board.text)

        assert request_board.status_code == self.expected_status_code