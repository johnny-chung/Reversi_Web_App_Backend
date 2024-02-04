from nn_ai import REVERSI_AI
from game_tree import GameTree
from game_helper import GameHelper



def prediction(gameData, player): 
    reversi_ai = REVERSI_AI()
    move = reversi_ai.get_move(gameData, player)
    print("ai move", move)
    if move is None:
            print("ai fail")
            game_tree = GameTree(gameData, player)             
            move = game_tree.get_best_move()   
    
    game_helper = GameHelper()
    return {
            'move': move,         
            'new_game_data': game_helper.get_new_board(gameData, move[0], move[1], player)
          }
    
