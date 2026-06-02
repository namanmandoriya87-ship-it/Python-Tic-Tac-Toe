from IPython.display import clear_output
import random


def display_board(board):
    clear_output(wait=True)

    print("     |   |")
    print(f"  {board[7]}  | {board[8]} | {board[9]}")
    print("_____|___|_____")
    print("     |   |")
    print(f"  {board[4]}  | {board[5]} | {board[6]}")
    print("_____|___|_____")
    print("     |   |")
    print(f"  {board[1]}  | {board[2]} | {board[3]}")
    print("     |   |")


def player_input():
    marker = ""

    while marker not in ["X", "O"]:
        marker = input("Player 1: Do you want to be X or O? ").upper()

    if marker == "X":
        return ("X", "O")
    else:
        return ("O", "X")


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return (
        (board[7] == mark and board[8] == mark and board[9] == mark) or
        (board[4] == mark and board[5] == mark and board[6] == mark) or
        (board[1] == mark and board[2] == mark and board[3] == mark) or
        (board[7] == mark and board[4] == mark and board[1] == mark) or
        (board[8] == mark and board[5] == mark and board[2] == mark) or
        (board[9] == mark and board[6] == mark and board[3] == mark) or
        (board[7] == mark and board[5] == mark and board[3] == mark) or
        (board[1] == mark and board[5] == mark and board[9] == mark)
    )


def choose_first():
    return random.choice(["Player 1", "Player 2"])


def space_check(board, position):
    return board[position] == " "


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0

    while position not in range(1, 10) or not space_check(board, position):
        try:
            position = int(input("Choose your next position (1-9): "))
        except ValueError:
            print("Please enter a valid number.")

    return position


def replay():
    return input("Do you want to play again? (Yes/No): ").lower() == "yes"


print("Welcome to Tic Tac Toe!")

while True:

    the_board = [" "] * 10

    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(f"{turn} will go first.")

    ready = input("Are you ready to play? (y/n): ").lower()

    game_on = ready == "y"

    while game_on:

        if turn == "Player 1":

            display_board(the_board)

            position = player_choice(the_board)

            place_marker(the_board, player1_marker, position)

            if win_check(the_board, player1_marker):
                display_board(the_board)
                print("Congratulations! Player 1 has won!")
                game_on = False

            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("The game is a tie!")
                    break
                else:
                    turn = "Player 2"

        else:

            display_board(the_board)

            position = player_choice(the_board)

            place_marker(the_board, player2_marker, position)

            if win_check(the_board, player2_marker):
                display_board(the_board)
                print("Congratulations! Player 2 has won!")
                game_on = False

            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("The game is a tie!")
                    break
                else:
                    turn = "Player 1"

    if not replay():
        print("Thanks for playing!")
        break