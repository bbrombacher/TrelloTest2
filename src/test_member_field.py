from .TrelloAPI import TrelloToken
from .TrelloAPI import TrelloMembers
from .Utility import utils
import pytest

class TestMemberId(object):
    #expected value
    expected_positive_status_code = 200
    expected_negative_status_code = 404
    expected_avatar_hash_response_keys = ['_value']
    expected_email_response_keys = ['_value']

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




    user_token = 'd162d502aa68a59be4b15279a2fafebeb33b93a4282e2ff0c96e7babf6a16514'

    @pytest.fixture
    def trelloMemberField(self):
        a = TrelloToken.TrelloToken(self.user_token)
        r = a.requestTokenInfo()
        b = TrelloMembers.TrelloMembers(self.user_token,
                                        r.json()['idMember'])

        return b

    def test_positiveStatusCode(self, trelloMemberField):
        utils.log()
        r = trelloMemberField.requestMemberField(self.email_field)
        assert r.status_code == self.expected_positive_status_code

    def test_negativeStatusCode(self, trelloMemberField):
        utils.log()
        r = trelloMemberField.requestMemberField(self.nonexistant_field)
        assert r.status_code == self.expected_negative_status_code

    def test_verifyEmailField(self, trelloMemberField):
        utils.log()
        r = trelloMemberField.requestMemberField(self.email_field)
        utils.log(r.text)
        actual_keys = utils.getActualKeys(r.json())
        assert actual_keys == self.expected_email_response_keys

    def test_verifyAvatarHash(self, trelloMemberField):
        utils.log()
        r = trelloMemberField.requestMemberField(self.avatarHash_field)
        utils.log(r.text)
        actual_keys = utils.getActualKeys(r.json())
        assert actual_keys == self.expected_avatar_hash_response_keys



