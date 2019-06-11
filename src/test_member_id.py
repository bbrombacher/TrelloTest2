from .TrelloAPI import TrelloToken
from .TrelloAPI import TrelloMembers
from .Utility import utils

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
        a = TrelloToken.TrelloToken('d162d502aa68a59be4b15279a2fafebeb33b93a4282e2ff0c96e7babf6a16514')
        a.requestTokenInfo()

        b = TrelloMembers.TrelloMembers('d162d502aa68a59be4b15279a2fafebeb33b93a4282e2ff0c96e7babf6a16514',
                                        a.getIDMember())
        r = b.requestMember()
        self.member_info = r.json()
        self.actual_status_code = r.status_code
        return b

    def test_statusCode(self, trelloMember):
        utils.log()
        assert self.actual_status_code == self.expected_status_code

    def test_verifyKeysTop(self, trelloMember):
        utils.log()
        actual_keys = utils.getActualKeys(self.member_info)
        assert actual_keys.sort() == self.expected_top_keys.sort()

    def test_verifyKeysLimits(self, trelloMember):
        utils.log()
        actual_keys_limits = utils.getActualKeys(self.member_info['limits'])
        actual_keys_limits_boards = utils.getActualKeys(self.member_info['limits']['boards'])
        actual_keys_limits_boards_totalPerMember = utils.getActualKeys(self.member_info['limits']['boards']['totalPerMember'])
        actual_keys_limits_orgs = utils.getActualKeys(self.member_info['limits']['orgs'])
        actual_keys_limits_orgs_totalPerMember = utils.getActualKeys(self.member_info['limits']['orgs']['totalPerMember'])

        assert actual_keys_limits.sort() == self.expected_keys_limits.sort()
        assert actual_keys_limits_boards.sort() == self.expected_keys_limits_boards.sort()
        assert actual_keys_limits_boards_totalPerMember.sort() == self.expected_keys_limits_boards_totalPerMember.sort()
        assert actual_keys_limits_orgs.sort() == self.expected_keys_limits_orgs.sort()
        assert actual_keys_limits_orgs_totalPerMember.sort() == self.expected_keys_limits_orgs_totalPerMember.sort()

    def test_verifyKeysPrefs(self, trelloMember):
        utils.log()

