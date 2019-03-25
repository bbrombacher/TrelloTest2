from .TrelloAPI import TrelloToken
import pytest


class TestToken(object):

    @pytest.fixture
    def trello(self):
        return TrelloToken.TrelloToken('1935e1c580f75d052d9e43373518994da776ebd81f43c9763bea3a5509f0dd4a')

    def test_statusCode(self, trello):
        trello.log()
        trello.requestTokenInfo()
        trello.getIDMember()

        assert 0


