#Wilson! Lo siento!

import main #importáljuk a main python file-t

class Recipe(): #Létrehozzúk a Recipe osztályt
    def __init__(self, name): #iniciáljuk a beérkező adatokat
        self.name = name
        self.material = []
        self.amount = []
    
with open('menu.csv', encoding='utf8') as file: #Megnyitjuk a menu.csv filet
    menu = []
    for i in file: #a menu tömbhözz hozzá adjuk a lestripelt és splitelt i-t.
        menu.append(i.strip().split(';'))

with open('recept.csv', encoding='utf8') as file: #megnyitjuk a recept.csv filet
    read = file.readline() 
    read = read.strip().split(';')
    recipe = []
    recipe.append(Recipe(read[0])) #a recipe tömbhöz hozzá adjuk a read első elemét és elmentjük a Recipe classba
    recipe[-1].material.append(read[1]) # a recipe tömb utolsó eleme materiel részéhez hozzá adjuk a read második elemét
    recipe[-1].amount.append(int(read[2]))# a recipe tömb utolsó elemének amount részéhez hozzá adjuk a read harmadik elemét, melyet int típusá alakítunk
    for i in file:
        i = i.strip().split(';') #az i-t lestripeljük és lespliteljük
        if i[0] != recipe[-1].name: #akkor teljesül a feltétel ha az i első eleme nem lesz egyenlő a recipe tömb utolsó elemének name részével.
            recipe.append(Recipe(i[0]))# hozzá adjuk a recipe tömbhöz az i-dik elem első elemét és a Recipe class eltárolja
        
        recipe[-1].material.append(i[1])# a recipe tömb utolsó elemének material részéhez hozzá adjuk az i második elemét.
        recipe[-1].amount.append(int(i[2]))#a recipe tömb utolsó elemének material részéhez hozzá adjuk az i harmadik elemét és int típusá alakítjuk.

with open('raktar.csv', encoding='utf8') as file: #a raktar.csv filet megnyitjuk.
    storage = []
    for i in file:
        i = i.strip().split(';') # az i-t stripeltük és spliteltük.
        i[1] = int(i[1]) # az i második elemét int típusóvá alakítottuk.
        storage.append(i)

with open("vasarlasok.csv", encoding="utf-8") as file: # vasarlasok.csv filet megnyitjuk.
    for i in file:
        i = i.strip().split(';') 
        for j in range(3, len(i)-1, 2): # a ciklus 3-tól az i-dik elem hoszából egyig tart és kettesével lépked.
            main.tables[int(i[0])].orders = [i[j+1]]# a main python fileből a tables tömb i első eleme számá alakítva annak az orders része egyenlő az i j+1-dik elemével.
            main.tables[int(i[0])].order_count = [int(i[j])]# a main python fileből a tables tömb i első eleme számá alakítva annak az orders_count része egyenlő az i j-dik elemével.
        main.tables[int(i[0])].price = int(i[-1]) # a main python fileből a tables tömb i első eleme számá alakítva annak a price része egyenlő az i utolsó elemével ami int típusóra át lett alakítva
        main.tables[int(i[0])].waiter = i[1]# a main python fileből a tables tömb i első eleme számá alakítva annak a waiter része egyenlő az i második elemével
        main.tables[int(i[0])].guest = i[2]# a main python fileből a tables tömb i első eleme számá alakítva annak az guest része egyenlő az i harmadik elemével.