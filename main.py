#Wilson! Lo siento!
class Recipe():
    def __init__(self, name):
        self.name = name
        self.material = []
        self.amount = []
    
with open('menu.csv', encoding='utf8') as file:
    menu = []
    for i in file:
        menu.append(i.strip().split(';'))

with open('recept.csv', encoding='utf8') as file:
    read = file.readline()
    read = read.strip().split(';')
    recipe = []
    recipe.append(Recipe(read[0]))
    recipe
    print(recipe[0].name)
    for i in file:
        if i[0] != recipe[-1].name:
            recipe.append(Recipe(i[0]))

with open('raktar.csv', encoding='utf8') as file:
    storage = []
    for i in file:
        storage.append(i.strip().split(';'))

print(menu)
print(recipe)
print(storage)