rows = int(input())

matrix = []

for row in range(rows):
    matrix.append([x for x in input().split()])
    for col in range(rows):
        if matrix[row][col] == "B":
            bunny_start = [row, col]

max_eggs = float("-inf")
max_direction = ""
max_eggs_matrix = []

possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

for direction, move in possible_moves.items():
    eggs = 0
    curr_egg_matrix = []
    row = bunny_start[0] + move[0]
    col = bunny_start[1] + move[1]
    while 0 <= row < rows and 0 <= col < rows:
        if matrix[row][col] == 'X':
            break

        curr_egg_matrix.append([row, col])
        eggs += int(matrix[row][col])
        row += move[0]
        col += move[1]
    
    if eggs > max_eggs and curr_egg_matrix:
        max_eggs = eggs
        max_eggs_matrix = curr_egg_matrix
        max_direction = direction

print(max_direction)
print(*max_eggs_matrix, sep='\n')
print(max_eggs)
