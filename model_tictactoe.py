"""
Full Name: Calvin Nguyen
UCINetID: Calvihn3
ID Number: 11863209

Program: A Tic-Tac-Toe game where two users can play.
         Users can place their markers until they win or tie.
         Once the game is decide, if they choose to play another game,
         the board resets and the game can be played once again.
"""
import os
import random


class Board:
    """
    Create a Tic-Tac-Toe board that in which 2 players can compete 
    against each other by placing 3 markers in a row, resulting in a
    win (horizontal, vertical, diagonal) or a tie.
    
    """
    player_X = ' X '
    player_O = ' O '

    # Constructor should initiliaze the board to a blank state
    def __init__(self, vc):
        """Initialize an empty board using vertical and horizontal lines."""
        self.vc = vc

        self.turns = 0

        self.numGames = 0
        self.Xwin = 0
        self.Owin = 0
        
        vertical_1 = [' - ', '|', ' - ', '|', ' - ']
        vertical_2 = [' - ', '|', ' - ', '|', ' - ']
        vertical_3 = [' - ', '|', ' - ', '|', ' - ']
        horizontal = ['------------']

        self.board = [vertical_1,
                      horizontal,
                      vertical_2,
                      horizontal,
                      vertical_3]
                      
    # Should print out the board
    def display(self):
        """Print out the current state of the board."""
        for row in self.board:
            index = 0
            for square in row:
                if len(row) == 5:
                    if index != 4:
                        print(square, end='')
                    else:
                        print(square)
                else:
                    print(square)

                index += 1


    # Method that updates a cell on the board based off the player
    def update_cell(self, cell_no: str):
        """Fill in an empty cell in the board, given the cell number and the player."""
        def enter_position(cell, symbol, row_num):
            """Fill in a specific cell, given the player's symbol and the row number."""
            error_message = "Invalid Input."
            if cell == 0:
                if row_num[4] != ' - ':
                    raise ValueError(error_message)
                row_num[4] = symbol
            elif cell == 1:
                if row_num[0] != ' - ':
                    raise ValueError(error_message)
                row_num[0] = symbol
            elif cell == 2:
                if row_num[2] != ' - ':
                    raise ValueError(error_message)
                row_num[2] = symbol
                
                            
        marker = ' X ' if (self.turns % 2) == 0 else ' O '
        cell_int = int(cell_no)
        position = cell_int % 3

        if 1 <= cell_int <= 3:
            row = self.board[0]
        elif 4 <= cell_int <= 6:
            row = self.board[2]
        else:
            row = self.board[4]

        enter_position(position, marker, row)
             
    # Checks if the game has been won
    def is_winner(self):
        """
        Check to see if the given player has won the game by getting 3 markers
        in a row vertically, horizontally, or diagonally.

        """
        marker = ' X ' if (self.turns % 2) == 0 else ' O '

        rowsOnly = [self.board[rows] for rows in range(len(self.board)) if rows % 2 == 0]

        column1 = 0
        column2 = 0
        column3 = 0

        for row in rowsOnly:  # vertical win
            if marker in row[0]:
                column1 += 1
            if marker in row[2]:
                column2 += 1
            if marker in row[4]:
                column3 += 1

            if (column1 == 3) | (column2 == 3) | (column3 == 3):
                return True

        for row in rowsOnly:  # horizontal win
            if row.count(marker) == 3:
                return True
 
        if rowsOnly[1][2] == marker:  # diagonal win
            if (marker in rowsOnly[0][0]) & (marker in rowsOnly[2][-1]):
                return True
            elif (marker in rowsOnly[0][-1]) & (marker in rowsOnly[2][0]):
                return True

        return False
            
    # Checks if the game has been tied
    def is_tie(self):
        """Check to see if there are any empty cells in the board left."""
        rowsOnly = [self.board[rows] for rows in range(len(self.board)) if rows % 2 == 0]
        
        for row in rowsOnly:
            for cell in row:
                if cell == ' - ':
                    return False
            
        return True
            
    # resets the game board for another round
    def reset(self):
        """Overwrite the current board with an empty board."""
        vertical_1 = [' - ', '|', ' - ', '|', ' - ']
        vertical_2 = [' - ', '|', ' - ', '|', ' - ']
        vertical_3 = [' - ', '|', ' - ', '|', ' - ']
        horizontal = ['------------']

        self.board = [vertical_1,
                      horizontal,
                      vertical_2,
                      horizontal,
                      vertical_3]
        
        self.turns = 0

    #Partial AI moves (Bonus Challenge(Optional))   
    def ai_move(self, player, available_moves):
        random_move = random.choice(available_moves)
        self.update_cell(random_move, player)
        return random_move

