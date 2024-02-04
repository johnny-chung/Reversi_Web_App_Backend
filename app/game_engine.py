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


class GameEngine:
    # # deep copy board to game-engine
    # def __init__(self, a_board):
    #     self.board = deep_copy_2d_array( a_board)

    # # update game data in game-engine
    # def set_data(self,  a_board):
    #     self.board = deep_copy_2d_array( a_board)

    # def __deepcopy__(self):
    #     new_instance = self.__class__(self.board)
    #     return new_instance

    # check if a move is valid, return None if invalid
    # return the grid that need to change if the move is valid
    def check_move(self, a_board, grid_x, grid_y, player):
        # return None if the grid is occupied
        if a_board[grid_x][grid_y] is not None and a_board[grid_x][grid_y] != 0:
            return None
        # array to store the grid that need to change
        grid_to_change = []
        # hardcoded direction
        dir_changes = [(1, 0), (-1, 0), (0, 1), (0, -1),
                       (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dir in dir_changes:
            res = []
            self.check_move_r(a_board, grid_x, grid_y,
                              dir[0], dir[1], player, res)
            # print("outer: ", res)
            if res is not None:
                for elem in res:
                    grid_to_change.append(elem)
        if len(grid_to_change) > 0:
            return grid_to_change
        else:
            return None

    # recursively move toward the direction util base conditon reached
    # base condition: 1) out of bound 2) reach an empty grid 3) reach the opposite color
    # return True if move is valid
    # arg: result to store the grids that need to change color if the move is valid
    def check_move_r(self, a_board, cur_x, cur_y, dir_x, dir_y, player, result=[]):

        new_x = cur_x + dir_x
        new_y = cur_y + dir_y

        if new_x < 0 or new_x > BOARD_SIZE - 1 or new_y < 0 or new_y > BOARD_SIZE - 1:
            return None
        elif a_board[new_x][new_y] is None or a_board[new_x][new_y] == 0:
            return None
        elif a_board[new_x][new_y] == player:
            return True
        else:
            # move to next grid
            res = self.check_move_r(
                a_board, new_x, new_y, dir_x, dir_y, player, result)
            if res is True:
                result.append((new_x, new_y))
            return res

    def get_new_board(self, a_board, x, y, player):
        grid_change = self.check_move(a_board, x, y, player)
        if grid_change is not None:
            # if valid, change the corresponding grid
            new_board = deep_copy_2d_array(a_board)
            # print("org: ", new_board)
            new_board[x][y] = player
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
