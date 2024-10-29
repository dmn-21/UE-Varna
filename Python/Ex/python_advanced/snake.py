def take_next_steps(row_, col_, action_):
    if action_ == "up":
        return row_ - 1, col_
    elif action_ == "down":
        return row_ + 1, col_
    elif action_ == "left":
        return row_, col_ - 1
    elif action_ == "right":
        return row_, col_ + 1


def is_outside(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size


n = int(input())
food_quantity = 0
matrix = []
snake_row = 0
snake_col = 0
burrows = []

for row in range(n):
    data = list(input())
    matrix.append(data)
    for col in range(n):
        if data[col] == 'S':
            snake_row = row
            snake_col = col
            matrix[row][col] = '.'
        elif data[col] == 'B':
            burrows.append([row, col])

game_won = False
game_lost = False
current_row = snake_row
current_col = snake_col

while True:
    action = input()
    matrix[current_row][current_col] = '.'

    current_row, current_col = take_next_steps(current_row, current_col, action)

    if is_outside(current_row, current_col, n):
        game_lost = True
        break

    if matrix[current_row][current_col] == '*':
        food_quantity += 1

    matrix[current_row][current_col] = 'S'
    if food_quantity >= 10:
        game_won = True
        break

    if burrows:
        if current_row == burrows[0][0] and current_col == burrows[0][1]:
            matrix[current_row][current_col] = '.'
            current_row = burrows[1][0]
            current_col = burrows[1][1]
            burrows.clear()
        elif current_row == burrows[1][0] and current_col == burrows[1][1]:
            matrix[current_row][current_col] = '.'
            current_row = burrows[0][0]
            current_col = burrows[0][1]
            burrows.clear()


if game_lost:
    print("Game over!")
elif game_won:
    print("You won! You fed the snake.")

print(f"Food eaten: {food_quantity}")
for row in matrix:
    print(*row, sep='')