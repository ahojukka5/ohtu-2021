from datetime import datetime

from player_reader import PlayerReader
from player_stats import PlayerStats


def main(verbose=False):
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    nationality = "FIN"
    now = datetime.now()
    print(f"Players from {nationality} {now}")
    players = stats.top_scorers_by_nationality(nationality)
    for player in players:
        print(player)


if __name__ == "__main__":
    main()
