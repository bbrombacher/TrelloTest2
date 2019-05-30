from .TrelloAPI import TrelloToken
from .TrelloAPI import TrelloMembers
from .Utility import utils
import pytest

class TestMemberId(object):
    #status codes
    positive_expected_status_code = 200
    negative_expected_status_code = 404

    #field variables
    nonexistant_field = 'wrongfield'
    id_field = 'id'
    avatarHash_field = 'avatarHash'
    avatarURL_field = 'avatarURL'
    bio_field = 'bio'
    bioData_field = 'bioData'
    confirmed_field = 'confirmed'
    email_field = 'email'
    fullName_field = 'fullName'
    gravatarHash_field = 'gravatarHash'
    idBoards_field = 'idBoards'
    idBoardsPinned_field = 'idBoardsPinned'
    idOrganizations_field = 'idOrganizations'
    idEnterprisesAdmin_field = 'idEnterprisesAdmin'
    idPremOrgsAdmin_field = 'idPremOrgsAdmin'
    initials_field = 'initials'
    longTypes_field = 'loginTypes'
    memberType_field = 'memberType'
    oneTimeMessagesDismissed_field = 'oneTimeMessagesDismissed'
    prefs_field = 'prefs'
    premiumFeatures_field = 'premiumFeatures'
    products_field = 'products'
    status_field = 'status'
    trophies_field = 'trophies'
    uploadedAvatarHash_field = 'uploadedAvatarHash'
    uploadedAvatarURL_field = 'uploadedAvatarURL'
    url_field = 'url'
    username_field = 'username'


    #expected field responses
    expected_email_response_keys = ['_value']



    @pytest.fixture
    def trelloMemberField(self):
        a = TrelloToken.TrelloToken('1935e1c580f75d052d9e43373518994da776ebd81f43c9763bea3a5509f0dd4a')
        a.requestTokenInfo()
        b = TrelloMembers.TrelloMembers('1935e1c580f75d052d9e43373518994da776ebd81f43c9763bea3a5509f0dd4a',
                                        a.getIDMember())
        return b

    def test_positiveStatusCode(self, trelloMemberField):
        utils.log()
        r = trelloMemberField.requestMemberField(self.email_field)
        assert r.status_code == self.positive_expected_status_code

    def test_negativeStatusCode(self, trelloMemberField):
        utils.log()
        r = trelloMemberField.requestMemberField(self.nonexistant_field)
        assert r.status_code == self.negative_expected_status_code

    def test_verifyEmailField(self, trelloMemberField):
        utils.log()
        r = trelloMemberField.requestMemberField(self.email_field)
        utils.log(str(r.json()))
        actual_keys = utils.getActualKeys(r.json())
        assert actual_keys == self.expected_email_response_keys



