sudoku_board = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 0, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]
]


def solve_the_sudoku(board):
    """The solve function is set to return the right solution of the sudoku when in every coordinate of the board
    there is the right number in range from 1 to 9. For that case I check if all the spots are
    occupied and if the number is valid with the help of recursion and the backtracking algorithm. """
    find = find_empty_spot(board)
    if not find:  # If the solution is found the program returns the solution.
        return True
    else:
        row, column = find
    # Here with recursion we are trying to finish the solution by finding the valid number.
    # If all numbers are not valid the value of the number is set to 0
    # and we backtrack to the last element we set because there is a mistake.
    for number in range(1, 9 + 1):
        if cell_is_valid(board, number, (row, column)):
            board[row][column] = number

            if solve_the_sudoku(board):
                return True

            board[row][column] = 0

    return False


def cell_is_valid(board, number, position):  # position = row, column
    """Checking each element in the current row if it is equal to the number we just added in.
    Also checks if the position is the same where we just added in. If it is the same, skip."""
    for column in range(len(board[0])):  # Column == element in the current row.
        if board[position[0]][column] == number and position[1] != column:  # position[0], position[1]
            # = the actual row, column
            return False

    # Checking column.
    for row in range(len(board)):  # position[0], position[1] = the actual row, column
        if board[row][position[1]] == number and position[0] != row:
            return False

    # Checking the boxes.
    box_column_coordinates = position[1] // 3
    box_row_coordinates = position[0] // 3

    for row in range(box_row_coordinates * 3, box_row_coordinates * 3 + 3):
        for column in range(box_column_coordinates * 3, box_column_coordinates * 3 + 3):
            if board[row][column] == number and (row, column) != position:
                return False

    return True


def find_empty_spot(board):
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == 0:
                return row, column

    return None


def print_board(board):
    """
    This function separates each square in 3 x 3 format with the help of nested loops.
    """
    for row in range(len(board)):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - ")

        for column in range(len(board[row])):
            if column % 3 == 0 and column != 0:
                print("|", end="")

            if column == 8:
                print(board[row][column])
            else:
                print(str(board[row][column]) + " ", end="")
                # This statement prints the elements one by one in the correct coordinates.


print_board(sudoku_board)
solve_the_sudoku(sudoku_board)
print("Expected Solution:")
print_board(sudoku_board)
