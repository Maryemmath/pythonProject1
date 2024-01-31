def board_full(board):
    for i in board:
        for j in i:
            if j == " ":
                return False
    return True


def check_winner(board, current_player):
    if (board[0][0] == board[0][1] == board[0][2] == current_player) or (
            board[0][0] == board[1][1] == board[2][2] == current_player) or (
            board[0][0] == board[1][0] == board[2][0] == current_player):
        print('{current_player} wins!')
        return True
    return False


def play(board, current_player):
    prev_player = current_player
    while True:
        print_board(board)
        if check_winner(board, prev_player):
            print(current_player)
            break
        elif board_full(board):
            print('Tie')
            break
        decision = input("Make your move, enter (x,y) coordinates separated by space ")
        coordinates = decision.split()
        x = int(coordinates[0])
        y = int(coordinates[1])
        if current_player == "X":
            if board[x][y] == " ":
                board[x][y] = "X"
                current_player = "O"
            else:
                print("unavailable coordinates, try again")
                play(board, current_player)
        elif current_player == "O":
            if board[x][y] == " ":
                board[x][y] = "O"
                current_player = "X"
            else:
                print("unavailable coordinates, try again")
                play(board, current_player)


def print_board(board):
    for i in board:
        print(" | ".join(i))
        print("-" * 9)


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    play(board, current_player)


if __name__ == "__main__":
    tic_tac_toe()
