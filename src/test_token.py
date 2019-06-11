from .TrelloAPI import TrelloToken
from .Utility import utils
import pytest


class TestToken(object):
    token_info = ''
    actual_status_code = 0

    expected_top_keys = ['id', 'identifier', 'idMember', 'dateCreated', 'dateExpires', 'permissions']
    expected_permissions_keys = ['idModel', 'modelType', 'read', 'write']
    expected_status_code = 200

    user_token = 'd162d502aa68a59be4b15279a2fafebeb33b93a4282e2ff0c96e7babf6a16514'

    @pytest.fixture
    def trelloToken(self):
        a = TrelloToken.TrelloToken(self.user_token)
        r = a.requestTokenInfo()
        self.token_info = r.json()
        self.actual_status_code = r.status_code
        return a

    def test_statusCode(self, trelloToken):
        utils.log()
        assert self.actual_status_code == self.expected_status_code

    def test_verifyKeysTop(self, trelloToken):
        utils.log()
        actual_keys = utils.getActualKeys(self.token_info)
        assert actual_keys == self.expected_top_keys

    def test_verifyKeysPermissions(self, trelloToken):
        utils.log()
        actual_keys = utils.getActualKeys(self.token_info['permissions'][0])
        assert actual_keys == self.expected_permissions_keys
