from constant import BOARD_SIZE

# deep copy 2d array


def deep_copy_2d_array(array):
    new_array = []
    if array is not None:
        row = len(array)
    for i in range(row):
        a_row = []
        for elem in array[i]:
            a_row.append(elem)
        new_array.append(a_row)
    return new_array


class GameHelper:
    

    # check if a move is valid, return None if invalid
    # return the grid that need to change if the move is valid
    def check_move(self, a_board, row, col, player):
        # return None if the grid is occupied
        if a_board[row][col] is not None and a_board[row][col] != 0:
            return None
        # array to store the grid that need to change
        grid_to_change = []
        # hardcoded direction
        dir_changes = [(1, 0), (-1, 0), (0, 1), (0, -1),
                       (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dir in dir_changes:
            res = []
            self.check_move_r(a_board, row, col,
                              dir[0], dir[1], player, res)
            #print("loop res: ", res)
            if res is not None:
                for elem in res:
                    grid_to_change.append(elem)
        #print(grid_to_change)
        if len(grid_to_change) > 0:
            #print(grid_to_change)
            return grid_to_change
        else:
            return None

    # recursively move toward the direction util base conditon reached
    # base condition: 1) out of bound 2) reach an empty grid 3) reach the opposite color
    # return True if move is valid
    # arg: result to store the grids that need to change color if the move is valid
    def check_move_r(self, a_board, cur_row, cur_col, dir_row, dir_col, player, result=[]):

        new_row = cur_row + dir_row
        new_col = cur_col + dir_col

        if new_row < 0 or new_row > BOARD_SIZE - 1 or new_col < 0 or new_col > BOARD_SIZE - 1:
            return None
        elif a_board[new_row][new_col] is None or a_board[new_row][new_col] == 0:
            return None
        elif a_board[new_row][new_col] == player:
            return True
        else:
            # move to next grid
            res = self.check_move_r(
                a_board, new_row, new_col, dir_row, dir_col, player, result)
            if res is True:
                result.append((new_row, new_col))
            return res

    def get_new_board(self, a_board, row, col, player):
        grid_change = self.check_move(a_board, row, col, player)
        if grid_change is not None:
            # if valid, change the corresponding grid
            new_board = deep_copy_2d_array(a_board)
            # print("org: ", new_board)
            new_board[row][col] = player
            # print(x, y, new_board)
            for elem in grid_change:
                new_board[elem[0]][elem[1]] = player

            return new_board
        else:
            return None

    # check if there are any valid move on the board for the given player
    def check_moves_exist(self, a_board, player):
        row = 0
        moves_exist = False
        while not moves_exist and row < BOARD_SIZE:
            col = 0
            while not moves_exist and col < BOARD_SIZE:
                res = self.check_move(a_board, row, col, player)
                if res is not None:
                    moves_exist = True
                else:
                    col += 1
            row += 1

        return moves_exist

    # return None if game is to be continue
    # return 1 if player 1 (repsented by 1 in array) win, 
    # return -1 when player 2 (represented by -1 in array) win, 
    # return 0 when tie
    def check_win(self, a_board):
        if self.check_moves_exist(a_board, 1) or self.check_moves_exist(a_board, -1):
            return None

        player1_score, player2_score = 0, 0
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if a_board[row][col] > 0:
                    player1_score += 1
                elif a_board[row][col] < 0:
                    player2_score += 1
        
        if player1_score > player2_score:
            return 1
        elif player2_score > player1_score:
            return -1
        else:
            return 0
