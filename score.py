class Score:
    @staticmethod
    def add_score(name: str, score: int):
        with open('scores.txt', 'r') as top_score:
            score_board = [line for line in top_score]
        with open('scores.txt', 'w') as top_score:
            score_board.append(name + ' ' + str(score))
            for place in score_board:
                top_score.write(place + '\n')
