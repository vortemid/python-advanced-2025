from collections import deque


rows, cols = [int(x) for x in input().split()]

snake = deque(input())
matrix = []

for r in range(rows):
    matrix.append([""] * cols)
    for c in range(cols):
        if r % 2 == 0:
            matrix[r][c] = snake[0]
        else:
            matrix[r][-1 - c] = snake[0]
        snake.rotate(-1)
    

[print(*row, sep="") for row in matrix]