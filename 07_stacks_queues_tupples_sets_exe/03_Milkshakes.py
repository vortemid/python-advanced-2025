from collections import deque


chocolates = deque(int(x) for x in input().split(', '))
cups_milk = deque(int(x) for x in input().split(', '))
milkshakes = 0

while chocolates and cups_milk and milkshakes < 5:

    if chocolates[-1] <= 0 and cups_milk[0] <= 0:
        chocolates.pop()
        cups_milk.popleft()
        continue
    if chocolates[-1] <= 0:
        chocolates.pop()
        continue
    if cups_milk[0] <= 0:
        cups_milk.popleft()
        continue

    if chocolates[-1] == cups_milk[0]:
        milkshakes += 1
        chocolates.pop()
        cups_milk.popleft()
    else:
        cups_milk.rotate(-1)
        chocolates[-1] -= 5

if milkshakes < 5:
    print("Not enough milkshakes.")
else:
    print("Great! You made all the chocolate milkshakes needed!")

print(f"Chocolate: {', '.join(str(x) for x in chocolates) if chocolates else 'empty'}")
print(f"Milk: {', '.join(str(x) for x in cups_milk) if cups_milk else 'empty'}")