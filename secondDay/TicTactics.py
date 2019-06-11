import os


def display(board):
    print(board['tl'] + '|' + board['tm'] + '|' + board['tr'])
    print(board['ml'] + '|' + board['mm'] + '|' + board['mr'])
    print(board['bl'] + '|' + board['bm'] + '|' + board['br'])
    pass


def main():
    init_board = {
        'tl': ' ',
        'tm': ' ',
        'tr': ' ',
        'ml': ' ',
        'mm': ' ',
        'mr': ' ',
        'bl': ' ',
        'bm': ' ',
        'br': ' '
    }
    curr_board = init_board
    count = 0
    display(init_board)
    turn = 'x'
    while (count < 9):
        #os.system('clear')
        #display(curr_board)
        pos = input("it is time for %s to play" % turn)
        if curr_board[pos] == ' ':
            curr_board[pos] = turn
            if turn == 'x':
                turn = 'o'
            else:
                turn = 'x'
            os.system('clear')
            display(curr_board)
            count += 1
    pass


if __name__ == "__main__":
    main()
    pass