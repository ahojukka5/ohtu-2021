class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        p = list(filter(lambda p: p.nationality == nationality, self.reader.players))
        p.sort(key=lambda p: p.points, reverse=True)
        return p
