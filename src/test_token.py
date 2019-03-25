from .TrelloAPI import TrelloToken
import pytest


class TestToken(object):

    expected_top_keys = ['id', 'identifier', 'idMember', 'dateCreated', 'dateExpires', 'permissions']
    expected_permissions_keys = ['idModel', 'modelType', 'read', 'write']

    @pytest.fixture
    def trello(self):
        a = TrelloToken.TrelloToken('1935e1c580f75d052d9e43373518994da776ebd81f43c9763bea3a5509f0dd4a')
        a.requestTokenInfo()
        return a

    def test_statusCode(self, trello):
        trello.log()
        assert trello.getStatusCode() == 200

    def test_verifyTopKeys(self, trello):
        trello.log()
        actual_keys = trello.getActualKeys(trello.tokenInfo.json())
        assert actual_keys == self.expected_top_keys

    def test_verifyPermissionkeys(self, trello):
        trello.log()
        actual_keys = trello.getActualKeys(trello.tokenInfo.json()['permissions'][0])
        assert actual_keys == self.expected_permissions_keys
