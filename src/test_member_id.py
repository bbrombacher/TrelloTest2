from .TrelloAPI import TrelloToken
from .TrelloAPI import TrelloMembers
import pprint

import pytest

class TestMembers(object):
    member_info = ''
    actual_status_code = 0
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
    def trelloMember(self):
        a = TrelloToken.TrelloToken('1935e1c580f75d052d9e43373518994da776ebd81f43c9763bea3a5509f0dd4a')
        a.requestTokenInfo()

        b = TrelloMembers.TrelloMembers('1935e1c580f75d052d9e43373518994da776ebd81f43c9763bea3a5509f0dd4a',
                                        a.getIDMember())
        r = b.requestMember()
        self.member_info = r.json()
        self.actual_status_code = r.status_code
        return b

    def test_statusCode(self, trelloMember):
        trelloMember.log()
        assert self.actual_status_code == self.expected_status_code

    def test_verifyKeysTop(self, trelloMember):
        trelloMember.log()
        actual_keys = trelloMember.getActualKeys(self.member_info)
        assert actual_keys.sort() == self.expected_top_keys.sort()

    def test_verifyKeysLimits(self, trelloMember):
        trelloMember.log()
        actual_keys_limits = trelloMember.getActualKeys(self.member_info['limits'])
        actual_keys_limits_boards = trelloMember.getActualKeys(self.member_info['limits']['boards'])
        actual_keys_limits_boards_totalPerMember = trelloMember.getActualKeys(self.member_info['limits']['boards']['totalPerMember'])
        actual_keys_limits_orgs = trelloMember.getActualKeys(self.member_info['limits']['orgs'])
        actual_keys_limits_orgs_totalPerMember = trelloMember.getActualKeys(self.member_info['limits']['orgs']['totalPerMember'])

        assert actual_keys_limits.sort() == self.expected_keys_limits.sort()
        assert actual_keys_limits_boards.sort() == self.expected_keys_limits_boards.sort()
        assert actual_keys_limits_boards_totalPerMember.sort() == self.expected_keys_limits_boards_totalPerMember.sort()
        assert actual_keys_limits_orgs.sort() == self.expected_keys_limits_orgs.sort()
        assert actual_keys_limits_orgs_totalPerMember.sort() == self.expected_keys_limits_orgs_totalPerMember.sort()

    def test_verifyKeysPrefs(self, trelloMember):
        trelloMember.log()

