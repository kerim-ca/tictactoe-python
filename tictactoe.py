# a game of Tic-tac-toe in python
class Tictactoe:
    def __init__(self):
        self.current_player = "X"
        self.board = ["-","-","-","-","-","-","-","-","-"]
        self.is_tie = False
        self.is_win = False
    
        
        
    #checks if a move is a valid move/position
    def is_valid_position(self, position):
        try:
            if self.board[position] == "-" and (position > -1 and position < 9):
                return True
            return False
        except:
            return False
        
    #checks for a horizontal win
    def check_horizontal(self, marker):
        if (self.board[0] == self.board[1] == self.board[2] == marker) or (self.board[3] == self.board[4] == self.board[5] == marker) or (self.board[6] == self.board[7] == self.board[8] == marker):
            return True
        return False
    #checks for a vertical win
    def check_vertical(self, marker):
        if (self.board[0] == self.board[3] == self.board[6] == marker) or (self.board[1] == self.board[4] == self.board[7] == marker) or (self.board[2] == self.board[5] == self.board[8] == marker):
            return True
        return False
    
    #checks for a diagonal win
    def check_diagonal(self, marker):
        if (self.board[0] == self.board[4] == self.board[8] == marker) or (self.board[2] == self.board[4] == self.board[6] == marker):
            return True
        return False
    
    #checks for a win
    def check_win(self):
        if self.check_horizontal(self.current_player) or self.check_vertical(self.current_player) or self.check_diagonal(self.current_player):
            self.is_win = True
            
    
    #checks for a tie
    def check_tie(self):
        if ("-" not in self.board) and (not self.is_win):
            self.is_tie = True
            
            
    #checks if game is over
    def check_game_over(self):
        return(self.is_tie or self.is_win)
    
    #switches player
    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        elif self.current_player == "O":
            self.current_player = "X"
          
    #makes move  
    def make_move(self, position=1000000):
        while not self.is_valid_position(position):
            position = int(input("enter a number between 0-8: \n"))
        
        self.board[position] = self.current_player
    
    
    #prints the board
    def print_board(self):
        print(self.board[:3])
        print()
        print(self.board[3:6])
        print()
        print(self.board[6:9])
        
    #controls game logic
    def game_controller(self):
        
        while True:
            self.make_move()
            self.check_win()
            self.check_tie()
            if self.check_game_over():
                break
            self.switch_player()
            self.print_board()
        self.print_board()
        if self.is_win:
            print(f"winner is {self.current_player}")
        elif self.is_tie:
            print("it's a tie")
        
    


new_ttc = Tictactoe()

print("Tic-tac-toe!")
new_ttc.print_board()
new_ttc.game_controller()
