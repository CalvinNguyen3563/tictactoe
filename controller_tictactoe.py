"""
Full Name: Calvin Nguyen
UCINetID: Calvihn3
ID Number: 11863209

Program: A controller for indirect communication between the model
         and the view. This separates the model and the view layer and
         enables the concepts of MVC to be applies. The controller handles
         events in the GUI and queries the data to be used in the view as
         well as update the model data when needed.
"""
import tkinter as tk
from tkinter import messagebox
from view_tictactoe import View as view
from model_tictactoe import Board as model


class Controller:
    """Enable indirect communication between model and view. Handle events."""
    def __init__(self):
        """Instantiate Controller instance and connect controller with model and view."""
        self.model = model(self)
        self.view = view(self)

        # starts interactive GUI
        self.view.window.mainloop()


    # getter
    def get_marker(self):
        """Contact the model for the marker to be used."""
        marker = ' X ' if (self.model.turns % 2) == 0 else ' O ' 
        return marker


    def get_numGames(self):
        """Contact the model for the number of games played."""
        return self.model.numGames


    def get_Xwin(self):
        """Contact the model for the number of X wins."""
        return self.model.Xwin


    def get_Owin(self):
        """Contact the model for the number of Y wins."""
        return self.model.Owin


    # event handlers
    def isWinner(self):
        """Check if the game is won and then increment winner score by 1."""
        if self.model.is_winner():
            marker = self.get_marker()
            messagebox.showinfo(title='Tic-Tac-Toe', message=f"Player{marker}has won")
            if marker == ' X ':
                self.model.Xwin += 1
                self.view.Xwin_txt.set(self.model.Xwin)
                self.model.numGames += 1
                self.view.numGames_txt.set(self.model.numGames)
                self.playAgain()
            elif marker == ' O ':
                self.model.Owin += 1
                self.view.Owin_txt.set(self.model.Owin)
                self.model.numGames += 1
                self.view.numGames_txt.set(self.model.numGames)
                self.playAgain()
            return True
        else:
            return False

            
    def isTie(self):
        """Check if the game is tie. If not, then increment the turns by 1."""
        if self.model.is_tie():
            messagebox.showinfo(title='Tic-Tac-Toe', message="It's a tie game!")
            self.model.numGames += 1
            self.view.numGames_txt.set(self.model.numGames)
            self.playAgain()
        else:
            self.model.turns += 1

        
    def makeMove(self, cell_no):
        """Contact model to update cell."""
        try:
            self.model.update_cell(cell_no)
        except ValueError as e:
            print(e)
            messagebox.showinfo(title='Tic-Tac-Toe', message="Button already Clicked!")
            return False
        else:
            return True
 

    def playAgain(self):
        """Reset the model data and the GUI board."""
        self.model.reset()
        self.view.auto_reset()



if __name__ == '__main__':
    control = Controller()
