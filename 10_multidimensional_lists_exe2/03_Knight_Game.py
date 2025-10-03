rows = int(input())

matrix = []
knights = []

for row in range(rows):
    matrix.append([x for x in input()])
    for col in range(rows):
        if matrix[row][col] == "K":
            knights.append([row, col])

removed_knights = 0
possible_moves = [[1, 2], [2, 1], [-1, 2], [1, -2], [2, -1], [-2, 1], [-1, -2], [-2, -1]]

while True:
    max_hits = 0
    max_knight = [0, 0]
    for k_row, k_col in knights:
        hits = 0
        for move in possible_moves:
            next_row = move[0] + k_row
            next_col = move[1] + k_col
            if 0 <= next_row < rows and 0 <= next_col < rows:
                if matrix[next_row][next_col] == 'K':
                    hits += 1
        if hits > max_hits:
            max_hits = hits 
            max_knight = [k_row, k_col]
    
    if max_hits == 0:
        break

    knights.remove(max_knight)
    matrix[max_knight[0]][max_knight[1]] = '0'
    removed_knights += 1

print(removed_knights)
