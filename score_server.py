import socket

def msg_recv(score):
    """Parse the message from client."""
    winner, versus = score.split()
    return winner, versus

def msg_print(win, vs):
    """Return string representing the winner of the game against an AI or Player."""
    return f"\nWinner: {win}\nPlaying against {vs}"

def msg_send(x_wins, o_wins, draws):
    """Return string of the each player's wins and the number of draws in a game which will be sent to client."""
    return f"player x wins {x_wins} player o win {o_wins} and draws {draws}"
    

if __name__ == '__main__':
    # Create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")

    s.bind((socket.gethostname(), 12340))

    s.listen(5)
    print("Socket is listening")

    clients = 0

    games = {}

    while True:
        clientsocket, address = s.accept()

        if address not in games:
            games[address] = {
                'X_wins_with_players': 0,
                'O_wins_with_players': 0,
                'draws_with_players': 0,
                'game_num_with_players': 0,
                'X_wins_with_ai': 0,
                'O_wins_with_ai': 0,
                'draws_with_ai': 0,
                'game_num_with_ai': 0
            }
        print(f"Connection from {address} has been established")

        clientsocket.send(bytes("Successfully Connected!", "utf-8"))

        while True:
            try:
                winner, versus = msg_recv(clientsocket.recv(1024).decode("utf-8"))
                print(msg_print(winner, versus))

                # Record wins and draws for games against Player
                if versus == "Player":
                    games[address]['game_num_with_players'] += 1
                    if winner == "X":
                        games[address]['X_wins_with_players'] += 1
                    elif winner == "O":
                        games[address]['O_wins_with_players'] += 1
                    elif winner == "Draw":
                            games[address]['draws_with_players'] += 1

                # Record wins and draws for games against AI
                elif versus == "AI":
                    games[address]['game_num_with_ai'] += 1
                    if winner == "X":
                        games[address]['X_wins_with_ai'] += 1
                    elif winner == "O":
                        games[address]['O_wins_with_ai'] += 1
                    elif winner == "Draw":
                        games[address]['draws_with_ai'] += 1

                # Count the number of human games
                human_games = 0
                for game in games:
                    human_games += games[game]['game_num_with_players']

                # Count the number of AI games
                ai_games = 0
                for game in games:
                    ai_games += games[game]['game_num_with_ai']
                        
                print(f"\n{human_games} human games and {ai_games} AI games reported from {len(games)} client(s)")

                # Count the number of X wins for all games
                client_x_wins = 0
                client_x_wins += games[address]['X_wins_with_players']
                client_x_wins += games[address]['X_wins_with_ai']

                # Count the number of O wins for all games
                client_o_wins = 0
                client_o_wins += games[address]['O_wins_with_players']
                client_o_wins += games[address]['O_wins_with_ai']

                # Count the number of draws for all games
                client_draws = 0
                client_draws += games[address]['draws_with_players']
                client_draws += games[address]['draws_with_ai']

                # Send client game score summary       
                clientsocket.send(bytes(msg_send(client_x_wins, client_o_wins, client_draws), "utf-8"))

            except Exception as e:
                print(e)
                break
                

        clientsocket.close()
        print("Client socket closed.")

