import random
import numpy as np

class TicTacToe:
    def __init__(self):
        self.board = np.zeros((3, 3))
        self.current_player = 1
    
    def reset(self):
        self.board = np.zeros((3, 3))
        self.current_player = 1
        return self.get_state()
    
    def get_state(self):
        return tuple(tuple(row) for row in self.board)
    
    def is_valid_move(self, x, y):
        return self.board[x, y] == 0
    
    def sample(self):
        return random.randint(0, 8)
    
    def step(self, action):
        x, y = divmod(action, 3)
        
        if self.is_valid_move(x, y):
            self.board[x, y] = self.current_player
            
            if self.current_player == 1:
                self.current_player = 2
            else:
                self.current_player = 1
            
            winner = self.check_winner()
            if winner is not None:
                if winner == 1:
                    reward = 1
                elif winner == 2:
                    reward = -1
                else:
                    reward = 0
                done = True
            elif np.count_nonzero(self.board) == 9:
                reward = 0
                done = True
            else:
                reward = 0
                done = False
            
            return self.get_state(), reward, done
        else:
            raise ValueError("Invalid action")
    
    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] != 0:
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] != 0:
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != 0:
            return self.board
    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] != 0:
                return self.board[i][0]
        if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] != 0:
            return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != 0:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != 0:
            return self.board[0][2]
            return 0