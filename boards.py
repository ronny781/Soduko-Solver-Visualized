
import requests


def retrieveRandomBoard(difficulty):  # This method retrieve random board from an api with the request difficulty level
    url = "https://sugoku.herokuapp.com/board?difficulty=" + difficulty

    res = requests.request("GET", url)

    response = res.json()

    return response['board']

