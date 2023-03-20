
board = list(range(0,9))
cells = 3
dashes = 13
spaces = 14
counter = 0
is_win = False
tictoken = ''


def check_win():
    win_coords = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coords:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def make_step(count):
    if count % 2 == 0:
        token = take_input('X')
    else:
        token = take_input('0')
    return token


def draw_board():
    for i in range(cells):
       print(' ' * spaces, end="")
       print('-' * dashes)
       print(' ' * spaces, end="")
       print(f'! {board[0 + i * 3]} ! {board[1 + i * 3]} ! {board[2 + i * 3]} !')
       print(' ' * spaces, end="")
       print("-" * dashes)

def take_input(player_token):
    player_answer = input(f'Where we put a {player_token}?: ')
    if player_answer == "":
        return 1
    elif int(player_answer) >= len(board):
        print("this area is not available")
        return 1
    player_answer = int(player_answer)
    if str(board[player_answer]) not in 'XO':
        board[player_answer] = player_token
    else:
        print("This cell is already taken!")
        return 1
    return player_token

def main():
    counter = 0
    is_win = False

    while not is_win:
        draw_board()

        tictoken = make_step(counter)

        counter+=1

        if counter > 4:
            winner = check_win()
            if winner:
                is_win = True
                print(f'{tictoken} is win!')
            elif counter == 9:
                print("Draw! You're amazing!")
                return 1
    draw_board()
    input('Press enter to exit.')

main()



