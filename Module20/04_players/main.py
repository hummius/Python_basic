players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

new_list= list()

for key, value in players.items():
    temp = list()
    temp.extend(list(key))
    temp.extend(list(value))
    new_list.append(tuple(temp))

print(new_list)