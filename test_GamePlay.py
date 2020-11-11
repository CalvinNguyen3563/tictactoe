"""
Full Name: Calvin Nguyen
UCINetID: Calvihn3
ID Number: 11863209

Program: Run the game TicTacToe and interacts with a server to keep score.
         There is anoption given to either play with an AI or with another
         Player.
"""

#TicTacToe Gameplay Module 
#Includes functions that would normally be included in another file at the top
#While loop is how the game play happens

import os
import test_tic_tac_toe as TicTacToe
import socket

#functions required to run the game
def print_header():
    print("Welcome to Tic Tac Toe\n")

#function that refreshes the screen and prints the header
def refresh_screen():
    #Clear the screen 
    os.system("clear")

    #Print the Header
    print_header()

    #Show the Board
    board.display()

#Function that shows a message after the board object has determined if there is
# a winner, or it is a tie
def show_win(player:str):
    if player == "Tie":
        print("\nTie Game!\n")
    else:
        print("\nPlayer {} wins!\n".format(player))

def num_players(player_or_ai):
    """Determine if the user input is valid and then returns an int of the input"""
    if player_or_ai not in ['1', '2']:
        raise ValueError("Invalid Input.\n")
    return int(player_or_ai)

def x_choice_func(num):
    """Determine if the user input is valid to update cell for X."""
    if num not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        raise ValueError("Invalid Input.\n")
    return int(num)

def o_choice_func(num):
    """Determine if the user input is valid to update cell for O."""
    if num not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        raise ValueError("Invalid Input.\n")
    return int(num)

def play_again_func(ans):
    """Determine if the user input is valid to reset the board or not."""
    if ans not in ["Y", "N", "y", "n"]:
        raise ValueError("Invalid Input.\n")
    return ans.upper()

    
if __name__ == '__main__':
    #Creating socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((socket.gethostname(), 12340))
    msg = s.recv(1024).decode("utf-8")
    print(msg)

    # Creating Board Instance  
    board = TicTacToe.Board()

    # Used to keep track of which cells are empty or not
    available_cells = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Choose whether to play against Player or AI
    while True:
        try:
            versus = num_players(input("\nHow many players?"))
        except ValueError as e:
            print(e)
        else:
            break
            
    enemy = "Player" if versus == 2 else "AI"

    #Gameplay starts from here
    while True:  
        refresh_screen()

        while True:          
            try:
                #Get X input
                x_choice = x_choice_func(input("\nX) Please choose 1 - 9 >"))

                #Update board
                board.update_cell(x_choice, "X")
            except ValueError as e:
                print(e)
                print("These are the only possible inputs that the program can accept.")
                print(available_cells)
            else:
                available_cells.remove(x_choice)
                break

        #refresh screen
        refresh_screen()

        #check for x win
        if board.is_winner("X"):
            show_win("X")

            # Sending message to server for X win
            s.send(bytes(f"X {enemy}", "utf-8"))

            # Receiving message from server about total score
            msg = s.recv(1024).decode("utf-8")
            print(msg)

            # Ask user if they want to reset the game and play again or not
            while True:
                try:
                    play_again = play_again_func(input("would you like to play again? Y/N").upper())
                except ValueError as e:
                    print(e)
                else:
                    break

            # Reset the board   
            if play_again == "Y":
                board.reset()

                while True:
                    try:
                        versus = num_players(input("\nHow many players?"))
                    except ValueError as e:
                        print(e)
                    else:
                        break
                    
                enemy = "Player" if versus == 2 else "AI"
                    
                available_cells = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                continue
            
            else:
                break
            
        #check for Tie
        if board.is_tie():
            show_win("Tie")
            s.send(bytes(f"Draw {enemy}", "utf-8"))
            msg = s.recv(1024).decode("utf-8")
            print(msg)
            
            while True:
                try:
                    play_again = play_again_func(input("would you like to play again? Y/N").upper())
                except ValueError as e:
                    print(e)
                else:
                    break
                
            if play_again == "Y":
                board.reset()
                
                while True:
                    try:
                        versus = num_players(input("\nHow many players?"))
                    except ValueError as e:
                        print(e)
                    else:
                        break
                    
                enemy = "Player" if versus == 2 else "AI"

                    
                available_cells = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                continue
            else:
                break

        if versus == 2:
            while True:
                try:
                    #Get O input
                    o_choice = o_choice_func(input("\nO) Please choose 1 - 9 >"))

                    #Update board
                    board.update_cell(o_choice, "O")
                except Exception as e:
                    print(e)
                    print("These are the only possible inputs that the program can accept.")
                    print(available_cells)
                    
                else:
                    available_cells.remove(o_choice)
                    break
        else:
            o_choice = board.ai_move("O", available_cells)
            available_cells.remove(o_choice)

        refresh_screen()

        #check for o win
        if board.is_winner("O"):
            show_win("O")
            s.send(bytes(f"O {enemy}", "utf-8"))
            msg = s.recv(1024).decode("utf-8")
            print(msg)
            
            while True:
                try:
                    play_again = play_again_func(input("would you like to play again? Y/N"))
                except ValueError as e:
                    print(e)
                else:
                    break
                    
            if play_again == "Y":
                board.reset()

                while True:
                    try:
                        versus = num_players(input("\nHow many players?"))
                    except ValueError as e:
                        print(e)
                    else:
                        break
                    
                enemy = "Player" if versus == 2 else "AI"
                    
                available_cells = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                continue
            else:
                break


