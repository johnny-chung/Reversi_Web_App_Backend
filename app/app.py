
from flask import Flask, request, jsonify
from flask_cors import CORS

from game_helper import GameHelper
from prediction import prediction


game_helper = GameHelper()

app = Flask(__name__)

# Load your PyTorch model
# Adjust the path to your saved PyTorch model file


@app.route('/api/predict/', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        board = data['board']
        player = data['player']
        print("prediction for: ", board, player)
        result = prediction(board, player)        
        print(result['move'])
        
        return jsonify(result)
    except Exception as err:
        print('Error:', err)
        return jsonify({'error': err}), 500

@app.route('/api/check_move/', methods=['POST'])
def check_move():
    try:
        data = request.get_json()
        board = data['board']
        move_row = data['row']
        move_col = data['col']
        player = data['player']
        # print(board, move_row, move_col, player)
        result = {}
        new_board = game_helper.get_new_board(board, move_row, move_col, player)
        if new_board is None:
            result = { 'move_valid' : False }
        else:
            result = { 'move_valid' : True,
                       'new_game_data': new_board
                      }
        return jsonify(result)
    
    except Exception as err:
        print('Error:', err)
        return jsonify({'error': err}), 500

@app.route('/api/check_move_exists/', methods=['POST'])
def check_move_exists():    
    try:
        data = request.get_json()
        board = data['board']
        player = data['player']
        result = game_helper.check_moves_exist(board, player)
        return jsonify(result)
    
    except Exception as err:
        print('Error:', err)
        return jsonify({'error': err}), 500



@app.route('/api/check_win/', methods=['POST'])
def check_win():    
    try:
        data = request.get_json()
        board = data['board']
        result = game_helper.check_win(board)
        return jsonify(result)
    
    except Exception as err:
        print('Error:', err)
        return jsonify({'error': err}), 500


CORS(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
