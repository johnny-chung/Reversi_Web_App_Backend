from game_helper import GameHelper
from constant import BOARD_SIZE, MAX_SCORE

game_helper = GameHelper()


class RULE:
    def check_grid_score(self, row, col, a_board, player):
        score = 6

        if row == 0 or row == 7:
            score += 1
            if col == 0 or col == 7:
                score += 20
        elif row == 1 or row == 6:
            score -= 20
            if col == 1 or col == 6:
                score -= 120
        elif row == 2 or row == 5:
            score += 3

        if col == 0 or col == 7:
            score += 1            
        elif col == 1 or col == 6:
            score -= 20
        elif col == 2 or col == 5:
            score += 3

        if row == 3 or row == 4:
            if col == 0 or col == 7:
                if a_board[row-1][col] == -player:
                    score -= 25
                if a_board[row+1][col] == -player:
                    score -= 25

        if col == 3 or col == 4:
            if row == 0 or row == 7:
                if a_board[row][col-1] == -player:
                    score -= 25
                if a_board[row][col+1] == -player:
                    score -= 25

        return score

    def cal_score(self, a_board, player):
        if game_helper.check_win(a_board) == player:
            return MAX_SCORE

        player_1_score, player_2_score = 0, 0
        zero_score = 0

        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if a_board[row][col] > 0:
                    player_1_score += self.check_grid_score(row, col, a_board, 1)
                elif a_board[row][col] < 0:
                    player_2_score += self.check_grid_score(row, col, a_board, -1)
                else:
                    zero_score += 5

        if player > 0:
            return player_1_score - player_2_score + zero_score
        else:
            return player_2_score - player_1_score + zero_score
