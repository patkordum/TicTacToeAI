import tictactoe as ttt

X = "X"
O = "O"
EMPTY = None

board =  [  [EMPTY,     X,      O],
            [O,         X,      EMPTY],
            [X,         EMPTY,     O]]


#print(board)
print(ttt.minimax(board))