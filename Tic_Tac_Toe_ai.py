import random

board = [" " for _ in range(9)]

def print_board():
    print()
    for i in range(3):
        print(" " + board[i * 3] + " | " + board[i * 3 + 1] + " | " + board[i * 3 + 2])
        if i < 2:
            print("---|---|---")
    print()

def check_winner(player):
    win_patterns = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for pattern in win_patterns:
        if all(board[pos] == player for pos in pattern):
            return True
    return False

def board_full():
    return " " not in board

def human_move():
    while True:
        try:
            move = int(input("Enter position (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == " ":
                board[move] = "X"
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Enter a number between 1 and 9.")

def ai_move():
    empty_positions = [i for i in range(9) if board[i] == " "]
    move = random.choice(empty_positions)
    board[move] = "O"

print("Tic-Tac-Toe AI")
print("You are X, AI is O")

while True:
    print_board()

    human_move()

    if check_winner("X"):
        print_board()
        print("You Win!")
        break

    if board_full():
        print_board()
        print("It's a Draw!")
        break

    ai_move()

    if check_winner("O"):
        print_board()
        print("AI Wins!")
        break

    if board_full():
        print_board()
        print("It's a Draw!")
        break
