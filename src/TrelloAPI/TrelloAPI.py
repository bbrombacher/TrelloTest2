from src.Utility import utils


class TrelloApi():
    def __init__(self, user_token):
        # the API Key provided to me from Trello to perform API operations.
        self.apiKey = '84c263c996f3197cae36c9af02352a9d'
        # the token manually created from my own account to perform local testing.
        # in a real application this token will need to be acquired on a per user basis.
        self.user_token = user_token #'d162d502aa68a59be4b15279a2fafebeb33b93a4282e2ff0c96e7babf6a16514'
        self.baseURL = 'https://api.trello.com/1'
        self.tokenKey = '?token=' + self.user_token + '&key=' + self.apiKey

