import torch
import random
from CNN import MyCNN
from game_helper import GameHelper, deep_copy_2d_array
from constant import BOARD_SIZE

random.seed()

game_helper = GameHelper()

def flip_board(array):
    new_board = deep_copy_2d_array(array)
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if new_board[i][j] != 0:
                new_board[i][j] *= -1
    return new_board


class REVERSI_AI:
    def __init__(self):
        self.model = MyCNN()
        self.model.load_state_dict(torch.load('./trained_reversi_model.pth'))
        self.model.eval()

    def get_move(self, a_board, player):

        input_board = None
        output = None
        if player == -1:
            input_board = flip_board(a_board)
        else:
            input_board = deep_copy_2d_array(a_board)

        input_data = torch.tensor(input_board, dtype=torch.float32)

        # Reshape the input to match the expected shape (batch_size, channels, height, width)
        input_data = input_data.unsqueeze(0).unsqueeze(0)  # Assuming the model expects a single-channel input

        # Make predictions
        with torch.no_grad():
            output = self.model(input_data)

        print("model output: ", output)
        # print(output[0][0])
        # print(output[0][1])
        move_x = round(output[0][0].item())
        move_y = round(output[0][1].item())

        random_x, random_y = 0, 0

        move_not_valid = True  
        count = 0     
        while move_not_valid and count < 15:
            temp_move_x = move_x + random_x
            temp_move_y = move_y + random_y
            if  temp_move_x >= 0 and temp_move_x <= 7 and temp_move_y >= 0 and temp_move_y <= 7 and game_helper.check_move(a_board, temp_move_x, temp_move_y, player) is not None:
                move_not_valid = False
            else:                
                random_x = random.randint(-1, 1)
                random_y = random.randint(-1, 1)
                count += 1
        
        if count >= 15:
            return None

        return (move_x + random_x, move_y + random_y)
    
