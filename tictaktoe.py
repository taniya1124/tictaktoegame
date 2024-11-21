def print_board(board):
    """Print the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_winner(board, player):
    """Check if a player has won."""
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    """Check if the game is a draw."""
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def play_game():
    """Main function to play the game."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        print(f"Player {players[current_player]}'s turn.")
        try:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter column (0, 1, 2): "))
            if board[row][col] == " ":
                board[row][col] = players[current_player]
                print_board(board)
                if is_winner(board, players[current_player]):
                    print(f"Player {players[current_player]} wins!")
                    break
                if is_draw(board):
                    print("It's a draw!")
                    break
                current_player = 1 - current_player
            else:
                print("Cell is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter numbers between 0 and 2.")

# Start the game
if __name__ == "__main__":
    play_game()
