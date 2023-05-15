from enum import Enum 
from copy import deepcopy


class Result(Enum):
    WIN = 1
    LOSS = 2
    DRAW = 3
    IN_PROGRESS = 4

def change_player(player):
    if(player == 'X'):
        return 'O'
    elif(player == 'O'):
        return 'X'
    else:
        print("Invalid player")
        return -1

def make_move(board, move_index, player):
    if(board[move_index] != ' '):
        print("Invalid move, place is already taken")
        return -1
    board[move_index] = player
    return 0

def print_board(arr):
    if(len(arr) != 9):
        print("Array length is not 9")
        return -1
    
    print(f"""-------------
| {arr[0]} | {arr[1]} | {arr[2]} |
-------------
| {arr[3]} | {arr[4]} | {arr[5]} |
-------------
| {arr[6]} | {arr[7]} | {arr[8]} |
-------------""")
    return 0

def check_win(arr):
    #check rows
    for i in range(0,3):
        if(arr[3*i] == arr[3*i+1] == arr[3*i+2] != ' '):
            return arr[3*i]
    #check columns
    for i in range(0,3):
        if(arr[i] == arr[i+3] == arr[i+6] != ' '):
            return arr[i]
    #check diagonals
    if(arr[0] == arr[4] == arr[8] != ' '):
        return arr[0]
    if(arr[2] == arr[4] == arr[6] != ' '):
        return arr[2]
    #check if draw 
    if(all(arr[i] != ' ' for i in range(0,9))):
        return Result.DRAW
    return Result.IN_PROGRESS

def evaluate_board(arr, pc_player):
    result = check_win(arr)
    if(result == ' '):
        return 0
    elif(result == pc_player):
        return 1
    elif(result == Result.DRAW):
        return -1
    else:
        return -2
    
def generate_possible_moves(arr):
    moves = []
    for i in range(0,9):
        if(arr[i] == ' '):
            moves.append(i)
    return moves

def evaluate_possible_moves(board_state, pc_player):
    possible_moves = generate_possible_moves(board_state)
    scores = {}
    for move in possible_moves:
        checked_board_state = deepcopy(board_state)
        checked_board_state[move] = pc_player
        scores[move] = evaluate_board(checked_board_state, pc_player)
    return scores

number_board = [1,2,3,4,5,6,7,8,9]
start_board_state = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
current_board_state = start_board_state.copy()
while True:
    player = input("Please select a player (X or O): ")
    if(player == 'X' or player == 'O'):
        current_player = player
        break

while True:
    print_board(number_board)
    print(f"{current_player}'s turn\nTo exit the game type any letter")

    move_index = input("Please select a field number: ")
    if(not move_index.isdigit()):
        print("Exiting the game...")
        break
    else:
        move_index = int(move_index) - 1
        if(move_index < 0 or move_index > 8):
            print("Invalid move")
            continue
        else:
            if(make_move(current_board_state, move_index, current_player) == -1):
                continue
            else:
                current_player = change_player(current_player)
                if(current_player == -1):
                    break
        print_board(current_board_state)

        winner = check_win(current_board_state)
        if(winner == 'X' or winner == 'O'):
            print(f"{winner} won!")
            break
        elif(winner == Result.DRAW):
            print("Draw!")
            break
        elif(winner == Result.IN_PROGRESS):
            continue