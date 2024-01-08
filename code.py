def draw_board(board_state):
    print("Current State Of Board : \n\n")
    for i in range(0, 9):
        if ((i > 0) and (i % 3) == 0):
            print("\n")
        if (board_state[i] == 0):
            print("- ", end=" ")
        if (board_state[i] == 1):
            print("O ", end=" ")
        if (board_state[i] == -1):
            print("X ", end=" ")
    print("\n\n")


def user_input(board_state):
    position = input("al3ab  X khayar men [1...9]: ")
    position = int(position)
    if board_state[position - 1] != 0:
        print("Wrong Move!!!")
        exit(0)
    board_state[position - 1] = -1


def minimax_algorithm(board_state, player):
    result = analyze_board(board_state)
    if result != 0:
        return result * player

    move_position = -1
    best_value = -2
    for i in range(0, 9):
        if board_state[i] == 0:
            board_state[i] = player
            score = -minimax_algorithm(board_state, (player * -1))
            if score > best_value:
                best_value = score
                move_position = i
            board_state[i] = 0

    if move_position == -1:
        return 0
    return best_value


def computer_move(board_state):
    move_position = -1
    best_value = -2
    for i in range(0, 9):
        if board_state[i] == 0:
            board_state[i] = 1
            score = -minimax_algorithm(board_state, -1)
            board_state[i] = 0
            if score > best_value:
                best_value = score
                move_position = i

    board_state[move_position] = 1


def analyze_board(board_state):
    combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for combo in combinations:
        if (board_state[combo[0]] != 0 and
                board_state[combo[0]] == board_state[combo[1]] and
                board_state[combo[0]] == board_state[combo[2]]):
            return board_state[combo[2]]
    return 0


def main():
    print("Computer : O Vs. You : X")
    current_player = 1
    current_board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(0, 9):
        if analyze_board(current_board) != 0:
            break
        if (i + current_player) % 2 == 0:
            computer_move(current_board)
        else:
            draw_board(current_board)
            user_input(current_board)

    result = analyze_board(current_board)
    if result == 0:
        draw_board(current_board)
        print("slaktalha!!!")
    elif result == -1:
        draw_board(current_board)
        print("GG well played !!!")
    elif result == 1:
        draw_board(current_board)
        print("5sart vs computer aktol ro7ak")


main()
