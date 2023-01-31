board = [' ' for x in range(10)]


def insert_letter(letter, pos):
    board[pos] = letter


def space_is_free(pos):
    return board[pos] == ' '


def print_board(bo):
    print('   |   |')
    print(' ' + bo[1] + ' | ' + bo[2] + ' | ' + bo[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + bo[4] + ' | ' + bo[5] + ' | ' + bo[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + bo[7] + ' | ' + bo[8] + ' | ' + bo[9])
    print('   |   |')


def check_winner(bo, letter):
    return (bo[1] == letter and bo[2] == letter and bo[3] == letter) or \
           (bo[4] == letter and bo[5] == letter and bo[6] == letter) or \
           (bo[7] == letter and bo[8] == letter and bo[9] == letter) or \
           (bo[1] == letter and bo[4] == letter and bo[7] == letter) or \
           (bo[2] == letter and bo[5] == letter and bo[8] == letter) or \
           (bo[3] == letter and bo[6] == letter and bo[9] == letter) or \
           (bo[1] == letter and bo[5] == letter and bo[9] == letter) or \
           (bo[3] == letter and bo[5] == letter and bo[7] == letter)


def player1_input():
    run = True
    while run:
        move = input('Please select a position to place an X (1-9): ')
        try:
            move = int(move)
            if 0 < move < 10:
                if space_is_free(move):
                    insert_letter("X", move)
                    run = False
                else:
                    print("That space is occupied")
            else:
                print("Please pick a number within the given range")
        except:
            print("Please type a number")


def player2_input():
    run = True
    while run:
        move = input('Please select a position to place an O (1-9): ')
        try:
            move = int(move)
            if 0 < move < 10:
                if space_is_free(move):
                    insert_letter("O", move)
                    run = False
                else:
                    print("That space is occupied")
            else:
                print("Please pick a number within the given range")
        except:
            print("Please type a number")


def is_board_full(bo):
    if bo.count(' ') > 1:
        return False
    else:
        print_board(board)
        return True


def main():
    print("Welcome to Tic Tac Toe")
    print_board(board)

    while not (is_board_full(board)):

        if not (check_winner(board, "O")):
            if is_board_full(board):
                print("Game is a Tie")
                break
            player1_input()
            print_board(board)
        else:
            print("O is the winner")
            break

        if not (check_winner(board, "X")):
            if is_board_full(board):
                print("Game is a Tie")
                break
            player2_input()
            print_board(board)
        else:
            print("X is the winner")
            break

main()
while True:
    answer = input("Do you want to play again? Y/N: ")
    if answer.lower() == 'y':
        board = [' ' for x in range(10)]
        print('--------------------------------------')
        main()
    else:
        break