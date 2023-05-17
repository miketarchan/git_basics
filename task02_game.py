#!/usr/bin/env python3
"""Tic-tac-toe game.
User can play with an algorithm by placing his mark by simply adding coordinate like 'x y'
"""
BOARD_SIZE = 3

board = []

def fill_board():
    """Fill the board"""
    for i in range(BOARD_SIZE):
        row = []
        for j in range(BOARD_SIZE):
            row.append('-')
        board.append(row)

def get_played_lines():
    """Collect the played lines by rows, columns and diagonals"""
    lines = []

    #fill by row
    for i in range(BOARD_SIZE):
        line = []
        for j in range(BOARD_SIZE):
            line.append({'x': i, 'y': j, 'player': board[i][j]})
        
        # print(line)
        lines.append(line)
    
    #fill by column
    for i in range(BOARD_SIZE):
        line = []
        for j in range(BOARD_SIZE):
            line.append({'x': j, 'y': i, 'player': board[j][i]})
        # print(line)
        lines.append(line)

    #fill by diagonal
    # from top left to bottom right
    line = []
    for i in range(BOARD_SIZE):
       line.append({'x': i, 'y': i, 'player': board[i][i]})
    lines.append(line)
    
    line = []
    # from top right to bottom left
    win = True
    for i in range(BOARD_SIZE):
        j = BOARD_SIZE - i -1
        line.append({'x': i, 'y': j, 'player': board[i][j]})
    lines.append(line)
    return lines
                

def is_player_win(player):
    """Detect if player winner"""

    played_lines = get_played_lines()
    for items in played_lines:
        win = True
        for item in items:
            if item['player'] != player:
                win = False
                break
        if win:
            print(f"Player '{player}' win. Congrants!!!")
            return True
    
    return False


def draw_board():
    for row in board:
        for item in row:
            print(item, end=' ')
        print()

def markSpot(x, y, player):
    if x < 0 or x > BOARD_SIZE -1 :
        print("Invalid 'x' value")
        return False
    
    if y < 0 or y > BOARD_SIZE - 1:
        print("Invalid 'y' value")
        return False

    if board[x][y] != '-':
        print("The spot already in use")
        return False
    
    board[x][y] = player
    return True

def switch_player(player):
    return 'x' if player == 'o' else 'o'

def detect_best_position_for_player(player):
    played_lines = get_played_lines()

    def sort_lines(items):
        i = 0
        for item in items:
            if(item['player']==player):
                i += 1
    
        return i
    
    sorted_items = sorted(played_lines, key=sort_lines)
    items = sorted_items[0]
    for item in items:
        if item['player']=='-':
            return [item['x'], item['y']]

def main():
    print("Hi there, I'm a simple tic-tac-toe game. ")
    fill_board()
    current_player = 'x'
    while True:
        draw_board()
        print(f"Player '{current_player}' turn")

        if current_player == 'x':
            list_tmp=list(
                map(int, input("Enter row and column numbers to fix spot: ").split()))
            if len(list_tmp) != 2:
                print('Wrong Parameters')
                continue

            x, y = list_tmp
            if markSpot(x,y,current_player):
                if is_player_win(current_player):
                    draw_board()
                    break
                else:
                    current_player = switch_player(current_player)
                    continue
        else:
            x, y = detect_best_position_for_player(current_player)
            markSpot(x,y,current_player)
            if is_player_win(current_player):
                draw_board()
                break
            else:
                current_player = switch_player(current_player)




if __name__ == '__main__':
    import random
    main()

# fill_board()
# markSpot(0,0,'x')
# markSpot(0,1,'o')
# draw_board()
# detect_best_position_for_player('x')