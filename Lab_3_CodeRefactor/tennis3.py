class TennisGame3:
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1_score = 0
        self.p2_score = 0

    def won_point(self, player):
        if player == self.player1_name:
            self.p1_score += 1
        elif player == self.player2_name:
            self.p2_score += 1

    def score(self):
        if self._is_standard_score():
            return self._standard_score()
        else:
            return self._advantage_or_winner()

    def _is_standard_score(self):
        return self.p1_score < 4 and self.p2_score < 4 and (self.p1_score + self.p2_score < 6)

    def _standard_score(self):
        if self.p1_score == self.p2_score:
            return f"{self.SCORE_NAMES[self.p1_score]}-All"
        else:
            return f"{self.SCORE_NAMES[self.p1_score]}-{self.SCORE_NAMES[self.p2_score]}"

    def _advantage_or_winner(self):
        if self.p1_score == self.p2_score:
            return "Deuce"

        leading_player = self.player1_name if self.p1_score > self.p2_score else self.player2_name
        score_diff = self.p1_score - self.p2_score

        if abs(score_diff) == 1:
            return f"Advantage {leading_player}"
        else:
            return f"Win for {leading_player}"
