import requests
import pprint
import inspect


class TrelloApi(object):
    def __init__(self, user_token):
        # the API Key provided to me from Trello to perform API operations.
        self.apiKey = '84c263c996f3197cae36c9af02352a9d'
        # the token manually created from my own account to perform local testing.
        # in a real application this token will need to be acquired on a per user basis.
        self.user_token = '1935e1c580f75d052d9e43373518994da776ebd81f43c9763bea3a5509f0dd4a'
        self.baseURL = 'https://api.trello.com/1'

        self.user_token = user_token
        self.tokenKey = '?token=' + self.user_token + '&key=' + self.apiKey

        self.tokenURL = None
        self.tokenInfo = None

        self.membersURL = None
        self.memberInfo = None

    def processUser(self):
        self.tokenURL = self.makeTokenURL()
        self.tokenInfo = self.getTokenInfo() #json of available information from the token response

        # move this to members class
        self.membersURL = self.makeMembersURL()
        self.memberInfo = self.getMembersInfo()

# Create URL strings
    def makeTokenURL(self):
        self.log() #print('makeTokenURL')
        url = self.baseURL + '/tokens/' + self.user_token + self.tokenKey#'?token=' + self.user_token + '&key=' + self.apiKey
        self.log(url)
        return url

        # move this to members class
    def makeMembersURL(self):
        self.log() #rint('makeMembersURL')
        url = self.baseURL+'/members/'+self.getIDMember() + self.tokenKey #'?token=' + self.user_token + '&key=' + self.apiKey
        self.log('members url: ' + url)
        return url

# Get methods

    # Token Methods
    def getTokenInfo(self):
        self.log() #print('getTokenInfo')
        r = requests.get(self.tokenURL)
        self.log('Status Code: ' + str(r.status_code))
        pprint.pprint(r.json())
        return r.json()

    def getIDMember(self):
        self.log()  # print('getIDMember')
        i = self.tokenInfo['idMember']
        self.log(i)
        return i

    # move this to members class
    def getMembersInfo(self):
        self.log() #print('getMembersInfo')
        self.log()
        r = requests.get(self.membersURL)
        pprint.pprint(r.json())
        return r.json()

    def getMembersActions(self):
        self.log()  # print('getMemberActions')

    def getMembersBoards(self):
        self.log() #print('getMemberBoards')

    def getMembersBoardBackgrounds(self):
        self.log()  # print('getMemberBoardBackgrounds')

# Post methods

#utility methods
    def log(self, message=None):
        if message is None:
            print(inspect.stack()[1].function)
        else:
            print(inspect.stack()[1].function + ': ' + message)

print(__name__)
if __name__ == '__main__':
    a = TrelloApi('1935e1c580f75d052d9e43373518994da776ebd81f43c9763bea3a5509f0dd4a')
    a.processUser()
