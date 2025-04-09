class TennisGame2:
    score_names = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

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

    def score(self):
        win_result = self.handle_win()
        if win_result:
            return win_result

        advantage = self.handle_advantage()
        if advantage:
            return advantage

        tie_result = self.handle_tie()
        if tie_result:
            return tie_result

        return self.handle_regular_score()

    def handle_tie(self):
        if self.p1points == self.p2points and self.p1points >= 3:
            return "Deuce"

        if self.p1points == self.p2points:
            return f"{self._get_score_name(self.p1points)}-All"

        return None

    def handle_advantage(self):
        if self.p1points > self.p2points >= 3:
            return "Advantage player1"
        if self.p2points > self.p1points >= 3:
            return "Advantage player2"

        return None

    def handle_win(self):
        if self.p1points >= 4 and self.p1points - self.p2points >= 2:
            return f"Win for {self.player1_name}"
        if self.p2points >= 4 and self.p2points - self.p1points >= 2:
            return f"Win for {self.player2_name}"
        return None

    def handle_regular_score(self):
        return f"{self._get_score_name(self.p1points)}-{self._get_score_name(self.p2points)}"

    def _get_score_name(self, points):
        return self.score_names.get(points, "Unknown")

    def set_p1_score(self, points):
        for _ in range(points):
            self.won_point(self.player1_name)

    def set_p2_score(self, points):
        for _ in range(points):
            self.won_point(self.player2_name)
