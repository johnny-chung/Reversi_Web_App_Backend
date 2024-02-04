from game_helper import GameHelper, deep_copy_2d_array
from own_heap import OwnHeap
from constant import BOARD_SIZE, MAX_SCORE
from rule import RULE

# game_helper/ helper function
game_helper = GameHelper()
rule = RULE()


class GameTree:
    class Node:
        def __init__(self, move_row, move_col, player, depth, score=0):
            self.move_row = move_row
            self.move_col = move_col
            self.player = player
            self.depth = depth
            self.score = score
            self.children = OwnHeap()

        # custom operator overload for comparison in heap
        def __lt__(self, other):
            return self.score < other.score

        def __gt__(self, other):
            return self.score > other.score

        def __le__(self, other):
            return self.score <= other.score

        def __ge__(self, other):
            return self.score >= other.score

        def __eq__(self, other):
            return self.score == other.score

        def __ne__(self, other):
            return self.score != other.score

    def __init__(self, a_board, player, tree_height=4):
        self.board = deep_copy_2d_array(a_board)
        self.player = player
        self.tree_height = tree_height

        self.root = GameTree.Node(-1, -1, player, 0)

        self.create_children(self.root, self.board, player)

    def create_children(self, sub_tree, a_board, player):
        # layer 0 (root) and 1 are both the same player, 
        # player will be reversed in recursive function
        # thus in root create childern funtion player need to reverse
        self.recur_create_children(sub_tree, a_board, -1 * player, 0)

    def recur_create_children(self, parent_node, parent_board, parent_player, parent_depth):
        
        child_depth = parent_depth + 1
        child_player = parent_player * -1

        if child_depth >= self.tree_height:
            #print("depth: ", cur_depth, "player: ", cur_player)
            parent_node.score = rule.cal_score(parent_board, parent_player)
            return None

        elif game_helper.check_win(parent_board) == parent_player:
            score_sign = parent_depth % 2
            if score_sign == 0:
                score_sign = -1
            parent_node.score = MAX_SCORE * score_sign
            return None

        else:
            for row in range(BOARD_SIZE):
                for col in range(BOARD_SIZE):
                    child_board = game_helper.get_new_board(
                        parent_board, row, col, child_player)

                    if child_board is not None:
                        # print(x, y, "| ", child_board)
                        # print("----------")
                        new_child = GameTree.Node(
                            row, col, child_player, child_depth)
                        
                        #print("new_child depth: ", new_child.depth, "player ", new_child.player)

                        self.recur_create_children(
                            new_child, child_board, child_player, child_depth)

                        parent_node.children.ins(new_child)

            if len(parent_node.children.arr) > 0:
                if parent_depth % 2 == 0:
                    parent_node.children.heapify_max()
                else:
                    parent_node.children.heapify_min()                  


                parent_node.score = parent_node.children.arr[0].score

    def get_best_move(self):
        # if game_helper.check_win(self.board, self.player) == 0:
        #     return (self.root.children.arr[0].move_row, self.root.children.arr[0].move_col)
        # else:
        #     return None
        if len(self.root.children) > 0:
            return (self.root.children.arr[0].move_row, self.root.children.arr[0].move_col)
        else:
            return None


    def print(self):
        self.print_r(self.root)

    def print_r(self, subtree):        
        if subtree.children is not None:
            for elem in subtree.children.arr:
                self.print_r(elem)
        print(f"depth: {subtree.depth}, player: {subtree.player}, move: {subtree.move_row} {subtree.move_col}, score: {subtree.score}")
        
    def print_target_depth(self, target_d):
        self.print_td_r(self.root, target_d)

    
    def print_td_r(self, subtree, target_d):
        if subtree.children is not None:
            for elem in subtree.children.arr:
                self.print_td_r(elem, target_d)
        if subtree.depth == target_d:
            print(f"depth: {subtree.depth}, player: {subtree.player}, move: {subtree.move_row} {subtree.move_col}, score: {subtree.score}")
        
   
