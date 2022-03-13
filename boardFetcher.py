import requests

from screens.game_over import game_over


def retrieveRandomBoard(difficulty):  # This method retrieve random board from an api with the request difficulty level
    url = "https://sugoku.herokuapp.com/board?difficulty=" + difficulty

    try:
        res = requests.request("GET", url)
        response = res.json()
    except:
        return None

    return response['board']
