from .TrelloAPI import TrelloToken
from .TrelloAPI import TrelloMembers

import pytest

class TestMembers(object):

    expected_top_keys = ['']
    expected_status_code = 200

    @pytest.fixture
    def trello(self):
        a = TrelloToken.TrelloToken('1935e1c580f75d052d9e43373518994da776ebd81f43c9763bea3a5509f0dd4a')
        a.requestTokenInfo()
        b = TrelloMembers.TrelloMembers('1935e1c580f75d052d9e43373518994da776ebd81f43c9763bea3a5509f0dd4a',
                                        a.getIDMember())
        b.requestMembersInfo()
        return b

    def test_statusCode(self, trello):
        trello.log()
        assert trello.membersInfo.status_code == self.expected_status_code
        assert 0

