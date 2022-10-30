import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter #letter is X or O

    def get_move(self, game):
        pass

class RandomComputerPlayer(Player): #inheritance
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        #get a random valid spot for next move
        square = random.choice(game.avaiable_moves()) #from game.py

class HumanPlayer(Player): #inheritance
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + "'s turn. Input move (0-9): ")
            #exception handling
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again')
        return val
