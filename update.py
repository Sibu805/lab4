#Комбинация должна содержать противоядие (пункт d).
#Общий размер предметов в комбинации не должен превышать 7 ячеек.
#Каждый включенный предмет добавляет свои очки выживания к общему количеству.
#Каждый исключенный предмет вычитает свои очки выживания из общего количества.
#Комбинация действительна, только если общее количество очков выживания больше нуля.
#Программа генерирует все возможные наборы предметов, чтобы найти допустимые комбинации.
#Отображаются только те комбинации, которые:
#Включают противоядие.
#Укладываются в ограничение в 7 ячеек.
#Дают положительные очки выживания.

from itertools import combinations

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
    ('crossbow', 'c', 2, 20),
    ('antidote', 'd', 1, 10)  # противоядие (пункт d)
]

def combination(items, cell, initial_points):
    possible_combinations = []

    items_set = set(items) 
    for r in range(1, len(items) + 1):
        for combo in combinations(items, r):
            if ('antidote', 'd', 1, 10) not in combo:
                continue  

            size = sum(item[2] for item in combo)
            added_points = sum(item[3] for item in combo)
            subtracted_points = sum(item[3] for item in (items_set - set(combo)))
            result_points = initial_points + added_points - subtracted_points
            if size <= cell and result_points > 0:
                possible_combinations.append((combo, result_points))
    
    return possible_combinations

valid_combos = combination(items, cell=7, initial_points=20)

print(f"Total Valid Combinations: {len(valid_combos)}\n")
for idx, (combo, points) in enumerate(valid_combos, 1):
    print(f"Option {idx}: Survival Points = {points}")
    for item in combo:
        print(f" - {item[1]} ({item[0]}, Size: {item[2]}, Points: {item[3]})")
    print()

if len(valid_combos) == 0: 
    print("Proof of absence of the combimations") 