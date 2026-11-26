class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def even_score_is_true(self):
        return self.m_score1 == self.m_score2

    def even_score(self):
        if self.m_score1 == 0:
            return "Love-All"
        elif self.m_score1 == 1:
            return "Fifteen-All"
        elif self.m_score1 == 2:
            return "Thirty-All"
        else:
            return "Deuce"

    def leading_score_is_true(self):
        return self.m_score1 >= 4 or self.m_score2 >= 4

    def leading_score(self):
        minus_result = self.m_score1 - self. m_score2
        
        if minus_result == 1:
            return "Advantage player1"
        elif minus_result == -1:
            return "Advantage player2"
        elif minus_result >= 2:
            return "Win for player1"
        else:
            return "Win for player2"

    def regular_scores(self):
        score = ""
        points = 0

        for i in range(1, 3):
            if i == 1:
                points = self.m_score1
            else:
                score = score + "-"
                points = self.m_score2

            if points == 0:
                score = score + "Love"
            elif points == 1:
                score = score + "Fifteen"
            elif points == 2:
                score = score + "Thirty"
            elif points == 3:
                score = score + "Forty"
        return score

    def get_score(self):
        
        if self.even_score_is_true():
            return self.even_score()
        elif self.leading_score_is_true():
            return self.leading_score()
        else:
            return self.regular_scores()