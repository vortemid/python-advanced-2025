rows, cols = [int(x) for x in input().split()]

matrix = [[x for x in input().split()] for _ in range(rows)]

command = input()
while command != 'END':
    cmd = command.split()
    if cmd[0] == 'swap' and len(cmd) == 5:
        first_el_row, first_el_col, second_el_row, second_el_col = [int(x) for x in cmd[1:]]
        if 0 < first_el_row > rows or 0 < second_el_row > rows or 0 < first_el_col > cols or 0 < second_el_col > cols:
            print("Invalid input!")
        else:
            first_swap = matrix[first_el_row][first_el_col]
            second_swap = matrix[second_el_row][second_el_col]
            matrix[first_el_row][first_el_col] = second_swap
            matrix[second_el_row][second_el_col] = first_swap
            for row in matrix:
                print(' '.join(row))
    else:
        print("Invalid input!")
    command = input()
