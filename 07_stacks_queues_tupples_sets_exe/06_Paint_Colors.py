from collections import deque

string = deque(input().split())

colors = {"red", "yellow", "blue"}
subcolors = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"},
}

paints = []

while string:
    first_str = string.popleft()
    last_str = string.pop() if string else ""
    
    for color in (first_str + last_str, last_str + first_str):
        if color in colors or color in subcolors:
            paints.append(color)
            break
    else:
        first_sub = first_str[:-1] if first_str else ""
        last_sub = last_str[:-1] if last_str else ""

        middle = len(string) // 2
        if len(string) % 2:
            middle += 1

        if first_sub:
            string.insert(middle, first_sub)
        if last_sub:
            string.insert(middle, last_sub)

for color in paints:
    if color in subcolors and not subcolors[color].issubset(paints):
        paints.remove(color)

print(paints)