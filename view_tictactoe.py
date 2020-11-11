"""
Full Name: Calvin Nguyen
UCINetID: Calvihn3
ID Number: 11863209

Program: A Tic-Tac-Toe GUI that allows buttons to be pressed to make
         a move or restart the game. Score will be displayed above the game
         as well as the number of games played.
"""
import tkinter as tk
from tkinter import messagebox


class View:
    """Use tkinter to create a Tic-Tac-Toe GUI that updates when interacted."""
    def __init__(self, vc):
        """Instantiate View instance, connects it with a controller and loads the view."""
        self.vc = vc
        
        # create window
        self.window = tk.Tk()
        self.window.title('Tic Tac Toe')
        self.window.geometry("500x550")
        self.window.minsize(500, 550)

        # create adpative scores
        self.numGames_txt = tk.StringVar() 
        self.Xwin_txt = tk.StringVar() 
        self.Owin_txt = tk.StringVar() 

        self.numGames_txt.set(str(self.vc.get_numGames()))
        self.Xwin_txt.set(str(self.vc.get_Xwin()))
        self.Owin_txt.set(str(self.vc.get_Owin()))

        # loads the GUI        
        self.load_view()

    def load_view(self):
        """Creates the GUI using frames, labels, and buttons."""
        # create main frame
        self.frame = tk.Frame(self.window)

        # create secondary frames
        self.top_frame = tk.Frame(self.frame)
        self.middle_frame = tk.Frame(self.frame)

        # create labels and buttons
        self.labels = self.labels()
        self.buttons = self.buttons()

        # pack frames in window
        self.top_frame.pack()
        self.middle_frame.pack()
        self.frame.pack()
        

    # button commands
    def update_button(self, btn, num):
        """Contact the controller to update the model and then updates the button clicked on the GUI."""
        valid = self.vc.makeMove(num)              
        if valid:
            marker = self.vc.get_marker()
            btn['text'] = marker
            winner = self.vc.isWinner()
            if not winner:
                self.vc.isTie()
    
    def reset(self):  # use for manual reset when New Game button is clicked
        """Contact the controller to reset the model and resets the GUI board."""
        self.vc.playAgain()
        

    def auto_reset(self):  # use for automatic reset when the game is over
        """Resets the GUI board."""
        for button in self.btnlst:
            button['text'] = ' - '

    # User Interface
    def labels(self):
        """Create games and score label for the GUI."""
        # create labels
        games_lbl = tk.Label(self.top_frame, text='Number of games played: ', font=('Arial 15 bold'))
        playerX_lbl = tk.Label(self.top_frame, text='Number of wins for Player X: ', font=('Arial 15 bold'))
        playerO_lbl = tk.Label(self.top_frame, text='Number of wins for Player O: ', font=('Arial 15 bold'))        

        # create score labels
        num_games_lbl = tk.Label(self.top_frame, textvariable=self.numGames_txt, font=('Arial 15'))
        winX_lbl = tk.Label(self.top_frame, textvariable=self.Xwin_txt, font=('Arial 15'))
        winO_lbl = tk.Label(self.top_frame, textvariable=self.Owin_txt, font=('Arial 15'))   

        # position labels
        games_lbl.grid(row=0, column=0)
        playerX_lbl.grid(row=1, column=0)
        playerO_lbl.grid(row=2, column=0)
        num_games_lbl.grid(row=0, column=1)
        winX_lbl.grid(row=1, column=1)
        winO_lbl.grid(row=2, column=1)



    def buttons(self):
        """Create interactive buttons for the GUI."""
        # create in-game buttons
        btn1 = tk.Button(self.middle_frame, text=' - ', font=('Arial 30 bold'), foreground='blue', height=2, width=5, command=lambda: self.update_button(btn1, '1'))
        btn2 = tk.Button(self.middle_frame, text=' - ', font=('Arial 30 bold'), foreground='blue', height=2, width=5, command=lambda: self.update_button(btn2, '2'))
        btn3 = tk.Button(self.middle_frame, text=' - ', font=('Arial 30 bold'), foreground='blue', height=2, width=5, command=lambda: self.update_button(btn3, '3'))
        btn4 = tk.Button(self.middle_frame, text=' - ', font=('Arial 30 bold'), foreground='blue', height=2, width=5, command=lambda: self.update_button(btn4, '4'))
        btn5 = tk.Button(self.middle_frame, text=' - ', font=('Arial 30 bold'), foreground='blue', height=2, width=5, command=lambda: self.update_button(btn5, '5'))
        btn6 = tk.Button(self.middle_frame, text=' - ', font=('Arial 30 bold'), foreground='blue', height=2, width=5, command=lambda: self.update_button(btn6, '6'))
        btn7 = tk.Button(self.middle_frame, text=' - ', font=('Arial 30 bold'), foreground='blue', height=2, width=5, command=lambda: self.update_button(btn7, '7'))
        btn8 = tk.Button(self.middle_frame, text=' - ', font=('Arial 30 bold'), foreground='blue', height=2, width=5, command=lambda: self.update_button(btn8, '8'))
        btn9 = tk.Button(self.middle_frame, text=' - ', font=('Arial 30 bold'), foreground='blue', height=2, width=5, command=lambda: self.update_button(btn9, '9'))

        # position in-game buttons
        btn1.grid(row=0, column=0)
        btn2.grid(row=0, column=1)
        btn3.grid(row=0, column=2)
        btn4.grid(row=1, column=0)
        btn5.grid(row=1, column=1)
        btn6.grid(row=1, column=2)
        btn7.grid(row=2, column=0)
        btn8.grid(row=2, column=1)
        btn9.grid(row=2, column=2)

        # create New Game button
        self.btnlst = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]
        newGamebtn = tk.Button(self.middle_frame, text='New Game', font=('Arial 25 bold'), command=lambda: self.reset())
                                                                                                                    

        # position New Game button
        newGamebtn.grid(row=3, column=0, columnspan=3)


    


