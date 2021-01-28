class Player:
    def __init__(self, name, nationality, assists, goals, penalties, team, games):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games

    @property
    def points(self):
        return self.goals + self.assists

    def __str__(self):
        return f"{self.name} team {self.team} goals {self.goals} assists {self.assists}"
