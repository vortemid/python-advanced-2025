n = int(input())

matrix = []

for row in range(n):
    matrix.append([x for x in input().split()])
    for col in range(n):
        if matrix[row][col] == 'A':
            alice = [row, col]
        elif matrix[row][col] == 'R':
            rabbithole = [row, col]

possible_directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

tea = 0
matrix[alice[0]][alice[1]] = '*'

while tea < 10:
    direction = input()
    move = possible_directions[direction]
    row = alice[0] + move[0]
    col = alice[1] + move[1]

    if row < 0 or row >= n or col < 0 or col >= n:
        break

    if matrix[row][col] == 'R':
        matrix[row][col] = "*"
        break

    if matrix[row][col] not in '.*':
        tea += int(matrix[row][col])
    
    matrix[row][col] = "*"
    alice = [row, col]
    
if tea >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

[print(*row) for row in matrix]