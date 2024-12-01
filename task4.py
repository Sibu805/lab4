items = [
    ('rifle', 'r', 3, 25),
    ('pistol', 'p', 2, 15),
    ('ammo', 'a', 2, 15),
    ('medkit', 'm', 2, 20),
    ('knife', 'k', 1, 15),
    ('axe', 'x', 3, 20),
    ('talisman', 't', 1, 25),
    ('flask', 'f', 1, 15),
    ('supplies', 's', 2, 20),
    ('crossbow', 'c', 2, 20)
]

rukzak = [['' for _ in range(4)] for _ in range(2)]  
ochki = 20  
yachenki = 8 

nuzhnik = [('antidote', 'd', 1, 10)]

for n_item in nuzhnik:
    items.append(n_item)

items.sort(key=lambda x: x[3] / x[2], reverse=True)

final_list = []
for item in items:
    name, abbr, size, points = item
    if yachenki >= size:
        final_list.extend([abbr] * size)  
        ochki += points
        yachenki -= size
    else:
        ochki -= points

inventry_order = final_list[:8]  
for i in range(2):
    for j in range(4):
        if i * 4 + j < len(inventry_order):
            rukzak[i][j] = inventry_order[i * 4 + j]

for row in rukzak:
    print(row)
print(f"Final Survival Points: {ochki}")
