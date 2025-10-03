from collections import deque

quantity_water = int(input())
command = input()
queue = deque([])

while command != 'Start':
    queue.append(command)
    command = input()

command = input()

while command != 'End':

    if command.isdigit():
        litters = int(command)
        if quantity_water >= litters:
            quantity_water -= litters
            print(f"{queue.popleft()} got water")
        else:
            print(f"{queue.popleft()} must wait")
    elif command.split(" ")[0] == 'refill':
        quantity_water += int(command.split(" ")[-1])

    command = input()

print(f"{quantity_water} liters left")
