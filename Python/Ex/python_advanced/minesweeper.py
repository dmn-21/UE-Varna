def is_outside(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size


def calculate_mines(matrix_, row_, col_):
    total_mines = 0
    # row - 1, col
    if not is_outside(row - 1, col, len(matrix_)):
        if matrix_[row - 1][col] == '*':
            total_mines += 1
    # row - 1, col - 1
    if not is_outside(row - 1, col - 1, len(matrix_)):
        if matrix_[row - 1][col - 1] == '*':
            total_mines += 1
    # row - 1, col + 1
    if not is_outside(row - 1, col + 1, len(matrix_)):
        if matrix_[row - 1][col + 1] == '*':
            total_mines += 1
    # row, col - 1
    if not is_outside(row, col - 1, len(matrix_)):
        if matrix_[row][col - 1] == '*':
            total_mines += 1
    # row, col + 1
    if not is_outside(row, col + 1, len(matrix_)):
        if matrix_[row][col + 1] == '*':
            total_mines += 1
    # row + 1, col - 1
    if not is_outside(row + 1, col - 1, len(matrix_)):
        if matrix_[row + 1][col - 1] == '*':
            total_mines += 1
    # row + 1, col
    if not is_outside(row + 1, col, len(matrix_)):
        if matrix_[row + 1][col] == '*':
            total_mines += 1
    # row + 1, col + 1
    if not is_outside(row + 1, col + 1, len(matrix_)):
        if matrix_[row + 1][col + 1] == '*':
            total_mines += 1
    return total_mines


n = int(input())

matrix = [[0 for col in range(n)] for row in range(n)]

commands = int(input())
for _ in range(commands):
    data = input().strip("(").strip(')').split(', ')
    curr_row, curr_col = [int(x) for x in data]
    matrix[curr_row][curr_col] = '*'


for row in range(n):
    for col in range(n):
        if matrix[row][col] == '*':
            continue
        matrix[row][col] = calculate_mines(matrix, row, col)

for row in matrix:
    print(*row, sep=' ')