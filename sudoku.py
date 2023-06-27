import random
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageFont

class SudokuApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku App")

        # Sudoku board initialization
        self.board = [[0] * 9 for _ in range(9)]
        self.generate_sudoku()

        # Create widgets
        self.frame = Frame(self.master)
        self.frame.pack()

        self.buttons = []
        for i in range(9):
            row = []
            for j in range(9):
                button = Button(self.frame, width=2, font=('Arial', 14, 'bold'),
                                command=lambda x=i, y=j: self.number_button_click(x, y))
                button.grid(row=i, column=j, padx=1, pady=1)
                row.append(button)
            self.buttons.append(row)

        check_button = Button(self.master, text="Check", command=self.check_solution)
        check_button.pack(pady=5)

        solve_button = Button(self.master, text="Solve", command=self.solve_and_show_solution)
        solve_button.pack(pady=5)

        save_button = Button(self.master, text="Save as PNG", command=self.save_as_image)
        save_button.pack(pady=5)

        # Display the board
        self.update_board()

    def generate_sudoku(self):
        # Sudoku generation algorithm
        # You can implement a different generation algorithm if desired

        # Fill the board with empty values
        self.board = [[0] * 9 for _ in range(9)]

        # Fill the diagonal 3x3 with unique numbers
        for i in range(3):
            nums = random.sample(range(1, 10), 9)
            for j in range(3):
                self.board[i * 3 + j][i * 3 + j] = nums[i * 3 + j]

        # Solve the board
        self.solve_sudoku()

        # Remove a random number from each cell
        for _ in range(45):
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            self.board[row][col] = 0

    def update_board(self):
        # Update the displayed state of the board
        for i in range(9):
            for j in range(9):
                value = self.board[i][j]
                if value != 0:
                    self.buttons[i][j].config(text=str(value), state=DISABLED)
                else:
                    self.buttons[i][j].config(text="", state=NORMAL)

    def number_button_click(self, row, col):
        # Handle number button click
        value = self.buttons[row][col].cget("text")
        if value != "":
            messagebox.showinfo("Error", "This cell is already filled.")
            return

        # Dialog window to enter a value
        dialog = Toplevel(self.master)
        dialog.title("Enter a value")

        entry = Entry(dialog, font=('Arial', 14, 'bold'), justify=CENTER)
        entry.pack(padx=10, pady=10)

        submit_button = Button(dialog, text="OK", command=lambda: self.set_cell_value(row, col, entry.get(), dialog))
        submit_button.pack(pady=5)

    def set_cell_value(self, row, col, value, dialog):
        # Set the value in the cell
        if not value.isdigit() or int(value) not in range(1, 10):
            messagebox.showinfo("Error", "Enter a number from 1 to 9.")
        else:
            self.board[row][col] = int(value)
            self.update_board()
            dialog.destroy()

    def check_solution(self):
        # Check the correctness of the solution
        solution = [[self.board[i][j] for j in range(9)] for i in range(9)]
        if self.solve_sudoku(solution):
            if solution == self.board:
                messagebox.showinfo("Correct", "The solution is correct!")
            else:
                messagebox.showinfo("Incorrect", "The solution is incorrect.")
        else:
            messagebox.showinfo("Incorrect", "Cannot solve the sudoku.")

    def solve_sudoku(self, board=None):
        # Solve the sudoku (backtracking algorithm)
        if board is None:
            board = self.board

        empty_cell = self.find_empty_cell(board)
        if not empty_cell:
            return True

        row, col = empty_cell
        for num in range(1, 10):
            if self.is_valid_move(board, row, col, num):
                board[row][col] = num
                if self.solve_sudoku(board):
                    return True
                board[row][col] = 0

        return False

    def solve_and_show_solution(self):
        # Solve the sudoku and display the solution
        solution = [[self.board[i][j] for j in range(9)] for i in range(9)]
        if self.solve_sudoku(solution):
            self.board = solution
            self.update_board()
        else:
            messagebox.showinfo("Incorrect", "Cannot solve the sudoku.")

    def find_empty_cell(self, board):
        # Find an empty cell in the board
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return (i, j)
        return None

    def is_valid_move(self, board, row, col, num):
        # Check if a number can be placed in a cell
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False

        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return False

        return True

    def save_as_image(self):
        # Save the board as a PNG image
        image_size = 400
        cell_size = image_size // 9
        image = Image.new("RGB", (image_size, image_size), "white")
        draw = ImageDraw.Draw(image)

        for i in range(10):
            line_width = 1 if i % 3 != 0 else 2
            draw.line([(i * cell_size, 0), (i * cell_size, image_size)], fill="black", width=line_width)
            draw.line([(0, i * cell_size), (image_size, i * cell_size)], fill="black", width=line_width)

        for i in range(9):
            for j in range(9):
                value = str(self.board[i][j]) if self.board[i][j] != 0 else ""
                text_bbox = draw.textbbox((j * cell_size, i * cell_size),
                                           value, font=ImageFont.truetype("arial.ttf", 30))
                text_position = ((text_bbox[0] + text_bbox[2]) // 2,
                                 (text_bbox[1] + text_bbox[3]) // 2)
                draw.text(text_position, value, font=ImageFont.truetype("arial.ttf", 30), fill="black")

        image.save("sudoku.png")
        messagebox.showinfo("Saved", "Board saved as sudoku.png.")

# Initialize the application
root = Tk()
sudoku_app = SudokuApp(root)
root.mainloop()
