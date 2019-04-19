# sudokusolver
*Mini Python project to understand backtracking with classic Sudoku puzzle.*

## **Intro**
Credits to [Tech with Tim](https://www.youtube.com/channel/UC4JX40jDee_tINbkjycV4Sg/featured).

*Simple, fast way to learn about backtracking. After watching Tim's tutorials, it was very straightforward. Clearly explained concepts.*

*Tool used to generate sample sudoku board and check the final answer: [Sudoku Bencher](http://sudoku.becher-sundstroem.de/)*

## **Body**
***NOTE: This project only solves 9x9 sudoku puzzles. Other types of puzzles won't work.***

Sudoku puzzles are implemented as a 2D-array. ~~There is already one stored in variable "board"~~. Empty cells are represented by 0
There are 4 functions total:

  ·print_board(puzzle): takes the 2D-array sudoku as input and prints the board as string representations.
  
  ·get_empty_cells(puzzle): looks for empty cells in the sudoku board. Returns the (x, y) position of empty cells. Returns none if full.
  
  ·is_valid(puzzle, num, pos): takes 3 parameters, the sudoku board, the number that the program wants to test and the (x, y) position that    it wants to test the number in. Checks for number in x column, y row and corresponding 3x3 box.
  
  ·solve_sudoku(puzzle): solves sudoku puzzle. Checks if there are any empty cells calling get_empty_cells(puzzle). If there are empty        cells, test a digit from 1 to 9 in an empty cell, (x, y) position given by get_empty_cells(puzzle). Then check validness of digit with      is_valid(puzzle, digit, (row,col)). If valid, add number to (x, y) cell. After, recursively call solve_sudoku(puzzle) with new digits in    board. If it encounters an invalid digit, it resets the corresponding cell and starts again, until every cell is valid and non-empty.
  
 ***19/04/19 UPDATE***: Users can now input rows of sudoku puzzle without needing to separate with commas or other separators. Empty cells are still represented by a 0.
  
  


