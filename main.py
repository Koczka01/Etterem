#I've become so numb

table_count = int(input('Adja meg hány asztal van: '))

etelek = []

class table: #Asztalok
    def __init__(self) -> None:
        self.orders = []
        self.order_count = []
        self.price = 0
        self.waiter = ""
        self.guest = ""

tables = []
for i in range(table_count): #Asztal tábla feltöltése
    tables.append(table())

import read_files
import write_files
import random
import time

time.sleep(0.2)

def New_recipe(): #Új recept hozzáadása
    name = input('Add meg a nevét a kajának: ') #Kaja neve
    if name != '':
        read_files.recipe.append(read_files.Recipe(name)) 
        material = input('Adjon meg egy alapanyagot: ')
        amount = input("Kérlek add meg az alapanyag mennyiségét: ")
        while material != '':
            if amount.isnumeric() and amount != '': #Mennyiség adat ellenőrzése
                read_files.recipe[-1].material.append(material) 
                read_files.recipe[-1].amount.append(int(amount))
                i = 0
                while i < len(read_files.storage) and read_files.storage[i][0] != material: #Ellenőrizzük, hogy a raktár.csv fileban szerepel-e már az alapanyag
                    i += 1

                if i == len(read_files.storage):
                    write_files.storage(material)
                    read_files.storage.append([material, 0])

            material = input('Adjon meg egy alapanyagot, ha nem szeretne többet, akkor nyomjon entert: ')
            amount = input("Kérlek add meg az alapanyag mennyiségét: ")

        price = input("Kérlek adj meg egy árat: ")
        if price.isnumeric() and price != '':
            write_files.menu(read_files.recipe[-1].name, price)
            read_files.menu.append([name, price])
            write_files.recipe(read_files.recipe[-1].name, read_files.recipe[-1].material, read_files.recipe[-1].amount)
        else:
            read_files.recipe.pop(-1)

def Storage_load():
    i = 0
    m = input("kérem adja meg, hogy mit szeretne feltölteni: ")
    while i < len(read_files.storage) and m != read_files.storage[i][0]: #Megkeressük, hogy hol van a keresett alapanyag
        i += 1 
        
    if i < len(read_files.storage):
        read_files.storage[i][1] += int(input("Kérlek add meg, hogy mennyi szeretnél hozzá adni: "))
    else:
        print("Rossz alapanyagot adtál meg!")
        
    write_files.storage_all(read_files.storage)
        
def Order():
    there_is_a_table = True
    while there_is_a_table:
        which = int(input("Melyik asztalhoz ment a pincér: "))
        if tables[which].waiter == '':
            tables[which].waiter = input("Ki lesz a pincér: ")
            name = ["Aliz", "Anna", "Áron", "Bence", "Benett", "Boglárka", "Boróka", "Botond", "Dániel", "Dominik", "Emma", "Hanna", "Hunor", "Jázmin", "Kamilla", "Lelle", "Léna", "Levente", "Lili", "Luca", "Marcell", "Máté", "Milán", "Mira", "Nimród", "Noel", "Olivér", "Zalán", "Zoé", "Zsófia"]
            tables[which].guest = random.choice(name)
        o = input("Kérem adja meg a rendelését: ")
        o = o.strip()
        while o != "":
            i = 0
            logic = False
            while i < len(read_files.menu): #Megkeressük, hogy van-e ilyen étel
                if o == read_files.menu[i][0]:
                    logic = True

                    k = 0 # Ellenőrizzük, hogy van-e elegendő alapanyag
                    while o != read_files.recipe[k].name: 
                        k += 1
                    for l in range(len(read_files.recipe[k].material)):
                        for m in read_files.storage:
                            if read_files.recipe[k].material[l] == m[0]:
                                if read_files.recipe[k].amount[l] > m[1]:
                                    logic = False

                    if logic: #Ha lehetséges elkészíteni, akkor True
                        j = 0
                        while j < len(tables[which].orders) and o != tables[which].orders[j]:
                            j += 1
                        if j < len(tables[which].orders):
                            tables[which].order_count[j] += 1
                        else:
                            tables[which].orders.append(o)
                            tables[which].order_count.append(1)
                        tables[which].price += int(read_files.menu[i][1])
                        write_files.storage_minus(read_files.storage, o)
                        etelek.append(o)
                    break
                i += 1

            if logic == False:
                print("Bocs haver ilyet nem esszel") #Kedvesen közli, hogy ilyen étellel nem tudunk szolgálni

            write_files.pay(tables, which)

            o = input("Kérem adjon meg még egy új ételt, ha nem szeretne akkor nyomjon egy entert: ") #Megkérdezi a program, hogy szeretné-e a felhasználó több étellel bővíteni a rendelést
            o = o.strip()
        further = input("Szeretnél másik asztaltól is rendelést felvenni? (Y/N): ")
        if further != "Y":
            there_is_a_table = False

def Order_finish():
    which = input('Adja meg melyik asztalnál szeretnének fizetni (Nyomjon entert a megszakításhoz): ')
    while (not(which.isnumeric()) or int(which) > table_count or int(which) < 0) and which != '':
        which = input('Adja meg melyik asztalnál szeretnének fizetni (Nyomjon entert a megszakításhoz): ')
    if which != '': #Ha nincs megszakítva, akkor az asztal paramétereit visszaállítja alapértelmetettre
        write_files.Conludes(tables[int(which)], which) 
        tables[int(which)].orders = []
        tables[int(which)].order_count = []
        tables[int(which)].price = 0
        tables[int(which)].waiter = ""
        tables[int(which)].guest = ""
        write_files.Update_orders(tables)

def Menu_element_delete():
    '''
    i = 0
    delete = input("Kérem adja hogy melyik ételt szeretné törölni a menüből: ")
    while i < len(read_files.menu):
        if delete == read_files.menu[i][0]:
            read_files.menu[i].pop
            read_files.storage[i].pop
            write_files.menu_delete(read_files.menu, delete)
            write_files.storage_delete(read_files.recipe, delete)
        i += 1
    '''
    i = 0
    delete = input("Kérem adja hogy melyik ételt szeretné törölni a menüből: ")
    while i < len(read_files.menu):
            if delete == read_files.menu[i][0]:
                write_files.menu_delete(read_files.menu, delete)
                write_files.recipe_delete(read_files.recipe, delete)
                write_files.storage_delete(read_files.recipe, read_files.storage, delete)
            i += 1
        
    delete = input("Kérem adja hogy melyik más ételt szeretné kitörölni a listából, hanem szeretne, akkor nyomjon egy enter: ")