NAMES = {
    0: "Love",
    1: "Fifteen",
    2: "Thirty",
    3: "Forty"}


def score_to_string(score):
    return NAMES[score]


def get_draw_score(score):
    assert score >= 0
    if score < 4:
        return score_to_string(score) + "-All"
    else:
        return "Deuce"


def get_winning_score(player1_name, player1_score, player2_name, player2_score):
    assert player1_score >= 4 or player2_score >= 4
    diff = player1_score - player2_score
    if diff == 1:
        return f"Advantage {player1_name}"
    if diff == -1:
        return f"Advantage {player2_name}"
    if diff >= 2:
        return f"Win for {player1_name}"
    else:
        return f"Win for {player2_name}"


def scores_to_string(p1_name, p1_points, p2_name, p2_points):
    if p1_points == p2_points:
        return get_draw_score(p1_points)
    if p1_points >= 4 or p2_points >= 4:
        return get_winning_score(p1_name, p1_points, p2_name, p2_points)
    return score_to_string(p1_points) + "-" + score_to_string(p2_points)


class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.p1_name = player1_name
        self.p2_name = player2_name
        self.p1_points = 0
        self.p2_points = 0

    def won_point(self, player_name):
        assert player_name in (self.p1_name, self.p2_name)
        if player_name == self.p1_name:
            self.p1_points = self.p1_points + 1
        else:
            self.p2_points = self.p2_points + 1

    def get_score(self):
        return scores_to_string(self.p1_name, self.p1_points,
                                self.p2_name, self.p2_points)
