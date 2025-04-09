class TennisGame1:
    score_names = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
    winning_threshold = 4

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.p1points += 1
        elif player_name == self.player2_name:
            self.p2points += 1

    def get_score_name(self, points):
        return self.score_names.get(points, "Deuce")

    def score(self):
        if self.p1points == self.p2points:
            return self.handle_tie(self.p1points)

        if self.p1points >= self.winning_threshold or self.p2points >= self.winning_threshold:
            return self.handle_win_or_advantage()

        return self.handle_regular_score()

    def handle_win_or_advantage(self):
        score_difference = self.p1points - self.p2points
        if score_difference == 1:
            return f"Advantage {self.player1_name}"
        elif score_difference == -1:
            return f"Advantage {self.player2_name}"
        elif score_difference >= 2:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"

    def handle_tie(self, points):
        if points >= 3:
           return "Deuce"
        return f"{self.get_score_name(points)}-All"

    def handle_regular_score(self):
        p1_score = self.get_score_name(self.p1points)
        p2_score = self.get_score_name(self.p2points)
        return f"{p1_score}-{p2_score}"
