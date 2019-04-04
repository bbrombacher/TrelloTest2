from .TrelloAPI import TrelloToken
from .TrelloAPI import TrelloMembers
import pprint

import pytest

class TestMembers(object):
    expected_status_code = 200
    expected_top_keys = ['id', 'avatarHash', 'avatarUrl', 'bio', 'bioData', 'confirmed', 'fullName',
                         'idEnterprise', 'idEnterprisesDeactivated', 'idMemberReferrer', 'idPremOrgsAdmin',
                         'initials', 'memberType', 'nonPublic', 'nonPublicAvailable', 'products', 'status', 'url',
                         'username', 'aaEmail', 'aaId', 'avatarSource', 'email', 'gravatarHash', 'idBoards',
                         'idOrganizations', 'idEnterprisesAdmin', 'limits', 'loginTypes', 'marketingOptIn',
                         'messagesDismissed', 'oneTimeMessagesDismissed', 'prefs', 'trophies', 'uploadedAvatarHash',
                         'uploadedAvatarUrl', 'premiumFeatures', 'isAaMastered', 'idBoardsPinned']

    expected_keys_limits = ['boards', 'orgs']
    expected_keys_limits_boards = ['totalPerMember']
    expected_keys_limits_boards_totalPerMember = ['status', 'disableAt', 'warnAt']
    expected_keys_limits_orgs = ['totalPerMember']
    expected_keys_limits_orgs_totalPerMember = ['status', 'disableAt', 'warnAt']

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

    def test_verifyKeysTop(self, trello):
        trello.log()
        actual_keys = trello.getActualKeys(trello.membersInfo.json())
        assert actual_keys.sort() == self.expected_top_keys.sort()

    def test_verifyKeysLimits(self, trello):
        trello.log()
        actual_keys_limits = trello.getActualKeys(trello.membersInfo.json()['limits'])
        actual_keys_limits_boards = trello.getActualKeys(trello.membersInfo.json()['limits']['boards'])
        actual_keys_limits_boards_totalPerMember = trello.getActualKeys(trello.membersInfo.json()['limits']['boards']['totalPerMember'])
        actual_keys_limits_orgs = trello.getActualKeys(trello.membersInfo.json()['limits']['orgs'])
        actual_keys_limits_orgs_totalPerMember = trello.getActualKeys(trello.membersInfo.json()['limits']['orgs']['totalPerMember'])

        assert actual_keys_limits.sort() == self.expected_keys_limits.sort()
        assert actual_keys_limits_boards.sort() == self.expected_keys_limits_boards.sort()
        assert actual_keys_limits_boards_totalPerMember.sort() == self.expected_keys_limits_boards_totalPerMember.sort()
        assert actual_keys_limits_orgs.sort() == self.expected_keys_limits_orgs.sort()
        assert actual_keys_limits_orgs_totalPerMember.sort() == self.expected_keys_limits_orgs_totalPerMember.sort()

    def test_verifyKeysPrefs(self, trello):
        trello.log()

