rows = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

def valid_coordinates(r1, c1):
    return 0 <= r1 < rows and 0 <= c1 < len(matrix[r1])

line = input()

while line != 'END':
    command = line.split()
    row1, col1, value = [int(x) for x in command[1:]]

    if valid_coordinates(row1, col1):
        if command[0] == 'Add':
            matrix[row1][col1] += value
        elif command[0] == 'Subtract':
            matrix[row1][col1] -= value
    else:
        print("Invalid coordinates")

    line = input()

[[print(*row, sep=' ')] for row in matrix]