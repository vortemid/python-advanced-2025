from collections import deque

number_pumps = int(input())
pumps = deque()

for _ in range(number_pumps):
    petrol_amount, distance = map(int, input().split())
    pumps.append((petrol_amount, distance))

starting_position = 0
stops = 0

while stops < number_pumps:
    tank_fuel = 0
    for petrol_amount, distance in pumps:
        tank_fuel += petrol_amount
        if tank_fuel < petrol_amount:
            pumps.rotate(-1)
            starting_position += 1
            stops = 0
            break
        stops += 1
        tank_fuel -= distance

print(starting_position)
