from math import floor


def take_next_steps(row_, col_, action_):
    if action_ == "up":
        return row_ - 1, col_
    elif action_ == "down":
        return row_ + 1, col_
    elif action_ == "left":
        return row_, col_ - 1
    elif action_ == "right":
        return row_, col_ + 1


n = int(input())
matrix = []
player_row = 0
player_col = 0
game_over = False
path = []

for row in range(n):
    data = input().split()
    matrix.append(data)

    for col in range(n):
        if data[col] == 'P':
            player_row = row
            player_col = col
            path.append([row, col])
            matrix[row][col] = '-'
            break

current_row = player_row
current_col = player_col
collected_coins = 0


while True:
    command = input()

    current_row, current_col = take_next_steps(current_row, current_col, command)

    if current_row < 0:
        current_row = n - 1
    elif current_row >= n:
        current_row = 0

    if current_col < 0:
        current_col = n - 1
    elif current_col >= n:
        current_col = 0

    path.append([current_row, current_col])

    if matrix[current_row][current_col] == 'X':
        collected_coins /= 2
        game_over = True
        break
    if matrix[current_row][current_col].isdigit():
        collected_coins += int(matrix[current_row][current_col])
        matrix[current_row][current_col] = '-'

    if collected_coins >= 100:
        break


if collected_coins >= 100:
    print(f"You won! You've collected {collected_coins} coins.")
elif game_over:
    print(f"Game over! You've collected {floor(collected_coins)} coins.")

print("Your path:")
for curr in path:
    print(curr)