from collections import deque

bees = deque(int(x) for x in input().split())
nectars = deque(int(x) for x in input().split())
symbols = deque(input().split())
total_nectar = 0

operators = {
    "+": lambda a, b: abs(a + b),
    "-": lambda a, b: abs(a - b),
    "*": lambda a, b: abs(a * b),
    "/": lambda a, b: abs(a / b) if b != 0 else 0,
}

while bees and nectars:
    if nectars[-1] < bees[0]:
        nectars.pop()
        continue

    if nectars[-1] >= bees[0]:
        bee = bees.popleft()
        nectar = nectars.pop()
        symbol = symbols.popleft()

        total_nectar += operators[symbol](bee, nectar)

print("Total honey made:", total_nectar)
if bees:
    print("Bees left:", ', '.join(str(x) for x in bees))
if nectars:
    print("Nectar left:", ', '.join(str(x) for x in nectars))
