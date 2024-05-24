"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    flattened_board = [item for row in board for item in row]

    # Count Xs and Os
    num_x = flattened_board.count("X")
    num_o = flattened_board.count("O")

    if num_x == 0 and num_o == 0:
        return "X"
    elif num_x > num_o:
        return "O"
    else:
        return "X"

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == None:
                actions.add((i,j))

    return actions          

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    result_board = copy.deepcopy(board)

    if action not in actions(board):
        raise Exception(f"{action} not valid, possible actions are: {actions(board)}")
    else:
        result_board[action[0]][action[1]] = player(board)

    return result_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for i in range(len(board)):
            if board[i][0] == board[i][1] == board[i][2] and board[i][0] != None:
                return board[i][0]
            
    # Check columns
    for j in range(len(board)):
            if board[0][j] == board[1][j] == board[2][j] and board[0][j] != None:
                return board[0][j] 
                
    # Check diagonal 
    if board[0][0]==board[1][1]==board[2][2] and board[0][0] != None:
        return board[0][0]
    elif board[0][2]==board[1][1]==board[2][0] and board[0][2] != None:
        return board[0][2]
    
    # If none of the above return a value, there is no winner 
    return None 
    
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    else:
        if None not in board[0] and None not in board[1] and None not in board[2]:
                return True
    # if none of the avoe return a value, game is not terminated
    return False    

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None  # If the game is over, no move is possible
   
    current_player = player(board)

    if current_player == X:
        return max_value(board)[1]
    else:
        return min_value(board)[1]

def min_value(board):
        if terminal(board):
            return utility(board), None
        v = math.inf
        best_action = None
        for action in actions(board):
            value, _ = max_value(result(board, action))
            if value < v:
                v = value
                best_action = action
        return v, best_action

def max_value(board):
        if terminal(board):
            return utility(board), None
        v = -math.inf
        best_action = None
        for action in actions(board):
            value, _ = min_value(result(board, action))
            if value > v:
                v = value
                best_action = action
        return v, best_action
             
