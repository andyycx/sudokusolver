"""
Created on 18 Apr 2019
Last modified on 18 Apr 2019

@author: Andy
"""

board = [
    [0, 0, 0, 4, 0, 3, 0, 7, 0],
    [0, 4, 7, 9, 0, 1, 0, 6, 8],
    [0, 0, 0, 0, 0, 2, 4, 0, 0],
    [4, 0, 1, 0, 3, 0, 9, 0, 7],
    [0, 7, 0, 0, 9, 0, 1, 5, 0],
    [0, 6, 0, 5, 0, 7, 0, 0, 0],
    [0, 1, 4, 3, 0, 8, 0, 9, 5],
    [6, 0, 5, 0, 0, 0, 0, 4, 2],
    [0, 3, 2, 0, 4, 5, 7, 0, 0]
]

def print_board(puzzle):
    #2D array to string representation
    box_lines = "+-----------" * 3 + "+"
    grid_lines = "|-----------" * 3 + "|"
    
    for count in range(9):
        if count == 0 or count == 3 or count == 6:  #Only corners of 3x3 boxes will have + sign to distinguis boxes
            print(box_lines)
        else:
            print(grid_lines)
        for row in puzzle:
            print("| {} | {} | {} | {} | {} | {} | {} | {} | {} |".format(*puzzle[count]))
            break
    print(box_lines)

def get_empty_cells(puzzle):
    #Find empty cell's (x, y) position
    for row in range(len(puzzle)):
        for col in range(len(puzzle[row])):
            if puzzle[row][col] == 0:
                return (row, col)
            
    return None
    
def is_valid(puzzle, num, pos):
    #Check if introduced number is valid in the row
    for col in range(9):
        if puzzle[pos[0]][col] == num and pos[1] != col:    #Checks if number is already in row, no need checking the position just added.
            return False

    #Check if introduced number is valid in the col
    for row in range(9):
        if puzzle[row][pos[1]] == num and pos[0] != row:    #Checks if number is already in col, no need checking the position just added. 
            return False

    #Check if introduced number is valid in the box
    box_col = pos[1] // 3    #Determines box number in x-axis. 0: boxcol1 / 1: boxcol2 / 2: boxcol3
    box_row = pos[0] // 3    #Determines box number in y-axis. 0: boxrow1 / 1: boxrow2 / 2: boxrow3

    for row in range(box_row*3, box_row*3 + 3):                 #Determine box row boundaries
        for col in range(box_col * 3, box_col * 3 + 3):         #Determine box col boundaries
            if puzzle[row][col] == num and (row, col) != pos:   #Check if any other element in the box is == number, no need checking the position just added.
                return False

    return True     #Valid

def solve_sudoku(puzzle):
    #Solve sudoku
    empty = get_empty_cells(puzzle)
    
    if not empty:           #Solved state, no empty cells
        return True

    else:
        row, col = empty    #Empty cells

    for digit in range(1,10):
        if is_valid(puzzle, digit, (row,col)):
            puzzle[row][col] = digit    #Add digit to board in (row,col) if valid

            if solve_sudoku(puzzle):    #Recursive call with new digit in board
                return True

            puzzle[row][col] = 0    #Backtracking

    return False

input("Enter any key to start sudoku...\n")
print_board(board)
print("This is your unsolved sudoku board...\n")
input("Enter any key to solve sudoku...\n")
solve_sudoku(board)
print_board(board)
    



