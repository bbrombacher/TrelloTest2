from .TrelloAPI import TrelloToken
from .TrelloAPI import TrelloMembers
from .Utility import utils

import pprint

import pytest

class TestMembers(object):
    #actual values
    member_info = ''
    actual_status_code = 0

    actual_keys_top = []
    actual_keys_limits = []
    actual_keys_limits_boards = []
    actual_keys_limits_boards_totalPerMember = []
    actual_keys_limits_orgs = []
    actual_keys_limits_orgs_totalPerMember = []

    #expected values
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

    user_token = 'd162d502aa68a59be4b15279a2fafebeb33b93a4282e2ff0c96e7babf6a16514'

    @pytest.fixture
    def trelloMember(self):
        a = TrelloToken.TrelloToken(self.user_token)
        r = a.requestTokenInfo()
        b = TrelloMembers.TrelloMembers(self.user_token,
                                        r.json()['idMember'])

        rr = b.requestMember()

        #actual status code
        self.actual_status_code = rr.status_code

        #actual keys
        self.actual_keys_top = utils.getActualKeys(rr.json())
        self.actual_keys_limits = utils.getActualKeys(rr.json()['limits'])
        self.actual_keys_limits_boards = utils.getActualKeys(rr.json()['limits']['boards'])
        self.actual_keys_limits_boards_totalPerMember = utils.getActualKeys(rr.json()['limits']['boards']['totalPerMember'])
        self.actual_keys_limits_orgs = utils.getActualKeys(rr.json()['limits']['orgs'])
        self.actual_keys_limits_orgs_totalPerMember = utils.getActualKeys(rr.json()['limits']['orgs']['totalPerMember'])

        return b

    def test_statusCode(self, trelloMember):
        utils.log()
        assert self.actual_status_code == self.expected_status_code

    def test_verifyKeysTop(self, trelloMember):
        utils.log()
        assert self.actual_keys_top.sort() == self.expected_top_keys.sort()

    def test_verifyKeysLimits(self, trelloMember):
        utils.log()
        assert self.actual_keys_limits.sort() == self.expected_keys_limits.sort()
        assert self.actual_keys_limits_boards.sort() == self.expected_keys_limits_boards.sort()
        assert self.actual_keys_limits_boards_totalPerMember.sort() == self.expected_keys_limits_boards_totalPerMember.sort()
        assert self.actual_keys_limits_orgs.sort() == self.expected_keys_limits_orgs.sort()
        assert self.actual_keys_limits_orgs_totalPerMember.sort() == self.expected_keys_limits_orgs_totalPerMember.sort()



