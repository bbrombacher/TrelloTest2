from .TrelloAPI import TrelloAPI
from .TrelloAPI import TrelloMembers

class TestToken(object):
    a = TrelloAPI.TrelloApi('1935e1c580f75d052d9e43373518994da776ebd81f43c9763bea3a5509f0dd4a')
    b = TrelloMembers

    def test_statusCode(self):
        print('test_statusCode')
        self.a.processUser()
        assert 1==1

    def test_members(self):
        print('test_members')
        self.b.TrelloMembers().method1()
        assert 1==1

