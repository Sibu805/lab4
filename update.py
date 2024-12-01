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

# Function to evaluate combinations
def evaluate_combinations(items, max_cells, initial_points):
    valid_combinations = []

    all_items_set = set(items)  # All items as a set for exclusion calculation

    # Generate all combinations of items
    for r in range(1, len(items) + 1):
        for combo in combinations(items, r):
            # Ensure the combo includes the antidote
            if ('antidote', 'd', 1, 10) not in combo:
                continue  # Skip combinations without the antidote

            # Calculate the total size of included items
            total_size = sum(item[2] for item in combo)

            # Calculate survival points: Add included, subtract excluded
            included_points = sum(item[3] for item in combo)
            excluded_points = sum(item[3] for item in (all_items_set - set(combo)))
            net_points = initial_points + included_points - excluded_points

            # Check if the total size does not exceed available cells and survival points are positive
            if total_size <= max_cells and net_points > 0:
                valid_combinations.append((combo, net_points))
    
    return valid_combinations

# Evaluate all valid combinations
valid_combos = evaluate_combinations(items, max_cells=7, initial_points=20)

# Display results
print(f"Total Valid Combinations: {len(valid_combos)}\n")
for idx, (combo, points) in enumerate(valid_combos, 1):
    print(f"Option {idx}: Survival Points = {points}")
    for item in combo:
        print(f" - {item[1]} ({item[0]}, Size: {item[2]}, Points: {item[3]})")
    print()

if len(valid_combos) == 0: 
    print(" proof of absence of the combimations") 