# Sudoku App

The Sudoku App is a simple GUI-based application that allows you to play Sudoku puzzles, generate new puzzles, check your solution, and even save the current Sudoku board as an image.

## How to Use

1. Run the program, and the Sudoku App window will appear.
2. A Sudoku board with some pre-filled cells will be displayed.
3. The board consists of a 9x9 grid with 3x3 sub-grids. The goal is to fill in the empty cells with digits from 1 to 9, following these rules:
   - Each row must contain all digits from 1 to 9, without repetition.
   - Each column must contain all digits from 1 to 9, without repetition.
   - Each 3x3 sub-grid must contain all digits from 1 to 9, without repetition.
4. You can click on any empty cell and enter a number from 1 to 9 using a pop-up dialog.
   - If you try to fill a cell with an invalid number, you will receive an error message.
   - If you try to fill a cell that already contains a value, you will receive an error message.
5. Use the "Check" button to check your current solution. If your solution is correct, a message will confirm it. Otherwise, an incorrect solution will be indicated.
6. The "Solve" button will attempt to solve the Sudoku puzzle and display the solution on the board. If the puzzle is solvable, the solved board will be shown; otherwise, an error message will be displayed.
7. The "Save as PNG" button will save the current Sudoku board as an image named "sudoku.png" in the same directory as the code. A confirmation message will be shown after saving the image.

## Code Overview

The code uses the `tkinter` library for creating the GUI, the `random` module for puzzle generation, and the `PIL` library (`Pillow` package) for saving the Sudoku board as an image.

The main class `SudokuApp` contains methods for initializing the GUI, handling number button clicks, checking the solution, solving the puzzle, saving the board as an image, and other helper functions for Sudoku operations.

## Customization

You can customize the Sudoku board by adjusting the following:

- The initial number of pre-filled cells by modifying the value in the `generate_sudoku()` function.
- The font style and size for the Sudoku board and dialog box by changing the font parameters in the code.

## Have Fun!

Run the code and enjoy playing Sudoku with the Sudoku App! Have fun solving puzzles and testing your skills!
