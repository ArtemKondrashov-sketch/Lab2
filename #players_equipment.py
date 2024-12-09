#players_equipment.py.
things = {'key': 3, 'mace': 1, 'gold coin': 24, 'lantern': 1, 'stone': 10}
print("Equipment:")
total = 0
for item, quantity in things.items():
    print(f"{quantity} {item}")
    total+= quantity
    print(f"Total number of things: {total}")