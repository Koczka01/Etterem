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
    recipe[-1].material.append(read[1])
    recipe[-1].amount.append(read[2])
    for i in file:
        i = i.strip().split(';')
        if i[0] != recipe[-1].name:
            recipe.append(Recipe(i[0]))
        
        recipe[-1].material.append(i[1])
        recipe[-1].amount.append(i[2])

with open('raktar.csv', encoding='utf8') as file:
    storage = []
    for i in file:
        storage.append(i.strip().split(';'))

#print(menu)
#print(recipe[1].material)
#print(storage)