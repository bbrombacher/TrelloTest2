from .TrelloAPI import TrelloToken
import pytest


class TestToken(object):
    token_info = ''
    actual_status_code = 0

    expected_top_keys = ['id', 'identifier', 'idMember', 'dateCreated', 'dateExpires', 'permissions']
    expected_permissions_keys = ['idModel', 'modelType', 'read', 'write']
    expected_status_code = 200

    @pytest.fixture
    def trelloToken(self):
        a = TrelloToken.TrelloToken('1935e1c580f75d052d9e43373518994da776ebd81f43c9763bea3a5509f0dd4a')
        r = a.requestTokenInfo()
        self.token_info = r.json()
        self.actual_status_code = r.status_code
        return a

    def test_statusCode(self, trelloToken):
        trelloToken.log()
        assert self.actual_status_code == self.expected_status_code

    def test_verifyKeysTop(self, trelloToken):
        trelloToken.log()
        actual_keys = trelloToken.getActualKeys(self.token_info)
        assert actual_keys == self.expected_top_keys

    def test_verifyKeysPermissions(self, trelloToken):
        trelloToken.log()
        actual_keys = trelloToken.getActualKeys(self.token_info['permissions'][0])
        assert actual_keys == self.expected_permissions_keys
