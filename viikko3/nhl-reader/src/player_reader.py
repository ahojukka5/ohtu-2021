import requests

from player import Player


class PlayerReader:
    def __init__(self, url, verbose=False):

        response = requests.get(url).json()

        if verbose:
            print("JSON-muotoinen vastaus:")
            print(response)

        self.players = players = []

        for player_dict in response:
            player = Player(
                player_dict["name"],
                player_dict["nationality"],
                player_dict["assists"],
                player_dict["goals"],
                player_dict["penalties"],
                player_dict["team"],
                player_dict["games"],
            )

            players.append(player)
