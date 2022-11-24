""""""""
## Function solver - use to solve the board
## Takes in the game board (2d array)
## Returns the solution
""""""""

def solver(board):
    
    if not find_empty(board):
        return True
    else:
        row, column = find_empty(board)

    for x in range(1, 10):
        if check_num(board, x, (row, column)):
            board[row][column] = x
        
            if solver(board):
                return True
        
        board[row][column] = 0

    return False

""""""""
## Function find_empty
## Takes in the game board (2d array)
## Returns either 
""""""""

def find_empty(board):
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == 0:
                return (row, column)
    
    return None

""""""""    
## Function check_num - used to check if a number would be valid in a row, column, and square
## Takes in the game board (2d array), an integer (will be the number a square needs), and a position (a place in the game where a check is happening)
## Returns a boolean - true if a number would work, false if it wouldn't
""""""""

def check_num(board, number, position):
    # Check Row
    for column in range(0, len(board)):
        if board[position[0]][column] == number and position[1] != column:
            return False

    # Check Column
    for row in range(0, len(board)):
        if board[row][position[1]] == number and position[1] != row:
            return False

    # Check Square
    xb = position[1] // 3
    yb = position[0] // 3

    for i in range (yb * 3, yb * 3 + 3):
        for j in range (xb * 3, xb * 3 + 3):
            if board[i][j] == number and (i, j) != position:
                return False

    return True
    
"""""""""""" 
## Function print_game - prints the full 9x9 board
## Takes in the game board (2d array)
## Returns nothing
""""""""""""

def print_game(board):

    for row in range(len(board)):
        if row % 3 == 0 and row != 0:
            print('- - - - - - - - - - - -')

        for column in range(len(board)):
            if column % 3 == 0 and column != 0:
                print(" | ", end = "")
            
            if column == 8:
                print(board[row][column])
            else:
                print(str(board[row][column]) + (" " ), end = "")


game_board = [
    [0, 0, 6, 9, 0, 3, 0, 0, 4],
    [0, 3, 0, 0, 8, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 0, 0, 9, 0],
    [0, 0, 4, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 3, 0, 0, 0, 0],
    [0, 6, 0, 5, 0, 7, 0, 8, 0],
    [5, 0, 0, 0, 0, 0, 0, 0, 8],
    [6, 0, 0, 2, 0, 0, 0, 0, 0],
    [0, 7, 0, 6, 0, 9, 0, 5, 0]
]

solver(game_board)
print_game(game_board)