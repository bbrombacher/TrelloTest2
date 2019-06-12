from .TrelloAPI import TrelloToken
from .TrelloAPI import TrelloMembers
from .TrelloAPI import TrelloBoards
from .Utility import utils
import datetime

import pytest

class TestBoards(object):
    #https://developers.trello.com/reference#boardsboardid-1
    user_token = 'd162d502aa68a59be4b15279a2fafebeb33b93a4282e2ff0c96e7babf6a16514'

    #expected values
    expected_status_code = 200

    #actual values
    board_membership = ''
    board_ids = []


    #key variables
    board_description_key = 'desc'
    members_board_id_key = 'idBoards'

    #query variables
    members_all_boards_query = {'memberships': 'all'}

    @pytest.fixture
    def trelloMember(self):
        a = TrelloToken.TrelloToken(self.user_token)
        r = a.requestTokenInfo()
        b = TrelloMembers.TrelloMembers(self.user_token,
                                        r.json()['idMember'])

        self.board_membership = self.getBoardMembership(b)
        self.board_ids = self.getBoardIdsWithBoardMembership(self.board_membership)

        utils.log('board_membership: ' + self.board_membership.text)
        utils.log('board_ids: ' + str(self.board_ids))

        return b

    @pytest.fixture
    def trelloBoardObject(self):
        b = TrelloBoards.TrelloBoards(self.user_token)

        utils.log('board_zero: ' + str(self.board_zero))
        return b

    def test_statusCode(self, trelloMember, trelloBoardObject):
        utils.log()
        board = self.getBoard(self.board_ids[0], trelloBoardObject)
        assert board.status_code == self.expected_status_code

    def test_updateBoardDescription(self, trelloMember, trelloBoardObject):
        utils.log()
        current_datetime = datetime.datetime.now()
        new_desc = current_datetime
        query_params = {self.board_description_key: new_desc}

        r = trelloBoardObject.putBoardId(self.board_ids[0], query_params)
        assert str(new_desc) == r.json()[self.board_description_key]


    ## Get Methods
    def getBoardMembership(self, trelloMember):
        utils.log()
        request_boards = trelloMember.requestMembersBoards(self.members_all_boards_query)
        utils.log(request_boards.text)
        return request_boards

    def getBoardIdsWithBoardMembership(self, board_membership):
        utils.log()
        boards = board_membership.json()[self.members_board_id_key]
        utils.log(str(boards))
        return boards

    def getBoard(self, board_id, trelloBoardObject):
        utils.log()
        board_query_params = {}
        request_board = trelloBoardObject.requestBoard(board_id, board_query_params)
        utils.log(request_board.text)
        return request_board

