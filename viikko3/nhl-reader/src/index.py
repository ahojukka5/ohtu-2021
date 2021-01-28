from datetime import datetime
import requests

from player import Player


def main(verbose=False):
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    if verbose:
        print("JSON-muotoinen vastaus:")
        print(response)

    players = []

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

    nationality = "FIN"
    now = datetime.now()
    print(f"Players from {nationality} {now}")

    for player in filter(lambda p: p.nationality == nationality, players):
        print(player)


if __name__ == "__main__":
    main()
