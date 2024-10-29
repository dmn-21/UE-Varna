from collections import deque

def perfect_show(fireworks_):
    perfect = False
    for bomb, value in fireworks_.items():
        if value >= 3:
            perfect = True
        else:
            perfect = False
            break
    return perfect


firework_effects = deque([int(x) for x in input().split(', ')])
explosive_power = [int(x) for x in input().split(', ')]

fireworks = {
    'Palm Fireworks': 0,
    'Willow Fireworks': 0,
    'Crossette Fireworks': 0
}

while firework_effects and explosive_power:
    current_effect = firework_effects.popleft()

    if current_effect <= 0:
        continue

    current_power = explosive_power.pop()

    if current_power <= 0:
        firework_effects.appendleft(current_effect)
        continue

    total = current_power + current_effect

    if total % 3 == 0 and total % 5 != 0:
        fireworks['Palm Fireworks'] += 1
    elif total % 5 == 0 and total % 3 != 0:
        fireworks['Willow Fireworks'] += 1
    elif total % 5 == 0 and total % 3 == 0:
        fireworks['Crossette Fireworks'] += 1
    else:
        firework_effects.append(current_effect - 1)
        explosive_power.append(current_power)

    if perfect_show(fireworks):
        break

if perfect_show(fireworks):
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join([str(x) for x in firework_effects])}")
if explosive_power:
    print(f"Explosive Power left: {', '.join([str(x) for x in explosive_power])}")

for key, value in fireworks.items():
    print(f"{key}: {value}")