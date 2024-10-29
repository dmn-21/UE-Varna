from collections import deque


def pouch_filled(pouch):
    pouch_is_filled = False
    for bomb, value in pouch.items():
        if value >= 3:
            pouch_is_filled = True
        else:
            pouch_is_filled = False
            break
    return pouch_is_filled


bomb_effects = deque([int(x) for x in input().split(', ')])
bomb_casings = [int(x) for x in input().split(', ')]

bombs = {
    'Datura Bombs': 0,
    'Cherry Bombs': 0,
    'Smoke Decoy Bombs': 0
}

while bomb_effects and bomb_casings:
    current_effect = bomb_effects.popleft()
    current_casing = bomb_casings.pop()

    result = current_effect + current_casing
    if result == 40:
        bombs['Datura Bombs'] += 1
    elif result == 60:
        bombs['Cherry Bombs'] += 1
    elif result == 120:
        bombs['Smoke Decoy Bombs'] += 1
    else:
        bomb_effects.appendleft(current_effect)
        bomb_casings.append(current_casing - 5)

    if pouch_filled(bombs):
        break

if pouch_filled(bombs):
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effects])}")
else:
    print("Bomb Effects: empty")

if bomb_casings:
    print(f"Bomb Casings: {', '.join([str(x) for x in bomb_casings])}")
else:
    print("Bomb Casings: empty")

for key, value in sorted(bombs.items()):
    print(f"{key}: {value}")