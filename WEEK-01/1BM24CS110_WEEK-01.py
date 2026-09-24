
import random
def print_board(board):
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def check_winner(board, player):
    win_states = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for condition in win_states:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def play_tic_tac_toe():
    board = [" "] * 9
    current_player = "X"
    print("\n--- Tic-Tac-Toe Game Starting ---")
    print("Positions match grid cells 1 to 9:")
    print(" 1 | 2 | 3 \n---|---|---\n 4 | 5 | 6 \n---|---|---\n 7 | 8 | 9 ")

    for turn in range(9):
        print_board(board)
        print(f"Player {current_player}'s turn.")
        
        while True:
            try:
                move = int(input("Enter position (1-9): ")) - 1
                if 0 <= move <= 8 and board[move] == " ":
                    board[move] = current_player
                    break
                else:
                    print("Invalid move or slot taken. Try again.")
            except ValueError:
                print("Please enter a valid integer between 1 and 9.")

        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            return
        
        current_player = "O" if current_player == "X" else "X"
        
    print_board(board)
    print("🤝 It's a draw!")


if __name__ == "__main__":
    while True:
        print("\n==============================")
        print("     AI LAB - WEEK 1 MENU     ")
        print("==============================")
        print("1. Run Tic-Tac-Toe Game")
        print("2. Exit Program")
        
        choice = input("Select an option (1/2): ").strip()
        if choice == "1":
            play_tic_tac_toe()
        elif choice == "2":
            print("Exiting lab program. Submitted by 1BM24CS110-Harsh Langote")
            break
        else:
            print("Invalid choice, please select 1 or 2.")
