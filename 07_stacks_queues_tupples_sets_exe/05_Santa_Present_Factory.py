from collections import deque

materials = deque(int(x) for x in input().split())
magic_level = deque(int(x) for x in input().split())

presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

created_presents = {}

while materials and magic_level:
    last_material = materials[-1]
    first_magic = magic_level[0]

    if last_material == 0 and first_magic == 0:
        materials.pop()
        magic_level.popleft()
        continue
    if last_material == 0:
        materials.pop()
        continue
    if first_magic == 0:
        magic_level.popleft()
        continue

    magic = last_material * first_magic

    if magic in presents:
        materials.pop()
        magic_level.popleft()
        created_present = presents[magic]
        created_presents[created_present] = created_presents.get(created_present, 0) + 1
    elif magic < 0:
        materials.pop()
        magic_level.popleft()
        materials.append(last_material + first_magic)
    elif magic > 0:
        magic_level.popleft()
        materials[-1] += 15

christmas = (
        ("Doll" in created_presents and "Wooden train" in created_presents) or 
        ("Teddy bear" in created_presents and "Bicycle" in created_presents)
    )

if christmas:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print("Materials left:", ', '.join(str(x) for x in reversed(materials)))

if magic_level:
    print("Magic left:", ', '.join(str(x) for x in magic_level))

for k, v in sorted(created_presents.items()):
    print(f"{k}: {v}")