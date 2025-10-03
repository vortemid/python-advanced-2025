n = int(input())
reservations = set()

for _ in range(n):
    reservation = input()
    reservations.add(reservation)

reservation = input()
while reservation != 'END':
    reservations.remove(reservation)
    reservation = input()

print(len(reservations))
print(*sorted(reservations), sep='\n')