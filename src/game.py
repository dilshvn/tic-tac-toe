class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] #single list is used to represent 3x3 board
        self.current_winner = None #keep track of winner

    def print_board(self): #to see board
        #getting rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod #don't need to pass in self
    def print_board_nums():
        # 0 | 1 | 2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        #to list the available moves
        return [i for i, spot in enumerate(self.board) if spot == ' '] #list comprehensions, enumerate creates a list

    def empty_squares(self):
        #to check if any empty squares
        return ' ' in self.board

    def num_empty_squares(self):
        #to count empty squares
        return self.board.count(' ')

    def make_move(self, square, letter):
        #if valid move -> make the move (assign square to letter), then return True
        #if invalid -> return False
        if self.board[square] == ' ':
            self.board[square] = letter
            return True
        return False #only occurs at else

def play(game, x_player, o_player, print_game = True):
    if print_game:
        game.print_board_nums()
    
    letter = 'X' #starting letter

    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        #defining a func to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('') #just empty line
                