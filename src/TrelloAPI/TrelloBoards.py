from src.TrelloAPI import TrelloAPI
from src.Utility import utils
import requests
import pprint

class TrelloBoards(TrelloAPI.TrelloApi):


    def __init__(self, user_token):
        utils.log()
        super().__init__(user_token)

    def requestBoard(self, board_id, query_params):
        #https://developers.trello.com/reference#boardsboardid-1
        utils.log()
        boards_url = self.baseURL + '/boards/' + board_id + self.tokenKey
        utils.log(boards_url)
        r = requests.get(boards_url, params=query_params)
        utils.log(r.text)
        return r

    def putBoardId(self, board_id, query_params):
        #https://developers.trello.com/reference#idnext
        utils.log()
        update_board_url = self.baseURL + '/boards/' + board_id + self.tokenKey
        utils.log(update_board_url)
        r = requests.put(update_board_url, params=query_params)
        utils.log(r.text)
        return r
