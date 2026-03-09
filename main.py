#Wilson! Lo siento!

with open('menu.csv', encoding='utf8') as file:
    menu = []
    for i in file:
        menu.append(i.strip().split(';'))

with open('recept.csv', encoding='utf8') as file:
    recipe = []
    for i in file:
        recipe.append(i.strip().split(';'))

with open('raktar.csv', encoding='utf8') as file:
    storage = []
    for i in file:
        storage.append(i.strip().split(';'))

print(menu)
print(recipe)
print(storage)