from collections import deque

materials = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])

presents = {
    'Gemstone': 0,
    'Porcelain Sculpture': 0,
    'Gold': 0,
    'Diamond Jewellery': 0
}
while materials and magic_level:
    current_material = materials.pop()
    current_magic = magic_level.popleft()

    result = current_magic + current_material
    if result < 100:
        if result % 2 == 0:
            result = current_material * 2 + current_magic * 3
        else:
            result *= 2
    elif result >= 500:
        result /= 2

    if 100 <= result < 200:
        presents['Gemstone'] += 1
    elif 200 <= result < 300:
        presents['Porcelain Sculpture'] += 1
    elif 300 <= result < 400:
        presents['Gold'] += 1
    elif 400 <= result < 500:
        presents['Diamond Jewellery'] += 1

if (presents['Gemstone'] > 0 and presents['Porcelain Sculpture'] > 0) or \
        (presents['Gold'] > 0 and presents['Diamond Jewellery'] > 0):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials])}")
if magic_level:
    print(f"Magic left: {', '.join([str(x) for x in magic_level])}")

for key, value in sorted(presents.items()):
    if value > 0:
        print(f"{key}: {value}")
