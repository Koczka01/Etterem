#Wilson! Lo siento!

import main

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
    recipe[-1].amount.append(int(read[2]))
    for i in file:
        i = i.strip().split(';')
        if i[0] != recipe[-1].name:
            recipe.append(Recipe(i[0]))
        
        recipe[-1].material.append(i[1])
        recipe[-1].amount.append(int(i[2]))

with open('raktar.csv', encoding='utf8') as file:
    storage = []
    for i in file:
        i = i.strip().split(';')
        i[1] = int(i[1])
        storage.append(i)

with open("vasarlasok.csv", encoding="utf-8") as file:
    for i in file:
        i = i.strip().split(';')
        for j in range(3, len(i)-1, 2):
            main.tables[int(i[0])].orders = [i[j+1]]
            main.tables[int(i[0])].order_count = [int(i[j])]
        main.tables[int(i[0])].price = int(i[-1])
        main.tables[int(i[0])].waiter = i[1]
        main.tables[int(i[0])].guest = i[2]