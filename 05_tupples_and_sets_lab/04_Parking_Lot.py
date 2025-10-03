n = int(input())
parking = set()

for _ in range(n):
    direction, plate = input().split(', ')

    if direction == 'IN':
        parking.add(plate)
    elif direction == 'OUT' and plate in parking:
        parking.remove(plate)

if parking:
    print(*parking, sep='\n')
else:
    print("Parking Lot is Empty")