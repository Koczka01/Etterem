import read_files #importáljuk a read_files python filet

def recipe(name, material, amount):
    file = open("recept.csv", 'a', encoding="utf8") #megnyitjuk a recept.csv filet
    
    for i in range(len(material)):
        file.write(f"\n{name};{material[i]};{amount[i]}") # a filebe beleírjuk a name, a material i-dik elemét és a mennyiség i-dik elemét
    file.close()
  
def storage(name):
    file = open('raktar.csv', 'a', encoding='utf8') #megnyitjuk a raktar.csv filet.
    file.write(f'\n{name};0')# a file-be beleírjuk a name-t és utána egy 0-át
    file.close()

def storage_all(white_monster):
    file = open('raktar.csv', 'w', encoding='utf8')#megnyitjuk a raktar.csv filet
    for i in white_monster:
        file.write(f'{i[0]};{i[1]}\n') #a filebe beleírjuk az i első és második elemét
    file.close()

def menu(menu, price):
    file = open("menu.csv", 'a', encoding= 'utf8')# megnyitjuk a menu.csv filet.
    file.write(f'\n{menu};{price}')# a file-be beleírjuk a menu-t és a price-t
    file.close()

def menu_delete(menu_list, target_name):
    new_menu = []
    for item in menu_list:
        if item[0] != target_name: #ha az item első eleme nem egyenlő a target_name-val akkor hozzá adjuk a new_menuhoz az itemet
            new_menu.append(item)
    with open("menu.csv", 'w', encoding='utf8') as file:
        for item in new_menu:
            file.write(f'{item[0]};{item[1]}\n')# a file-be beleírjuk az item első és második elemét
    return new_menu # a new_menu tömböt visszaküldjük 

def recipe_delete(recipe_list, name):
    new_recipe = []
    for item in recipe_list:
        if item.name != name: # Ha az item name része nem egyenlő a name (a deletével), akkor hozzá adjuk a new_recipe-hez az itemet
            new_recipe.append(item)
    
    with open("recept.csv", 'w', encoding='utf8') as file: #megnyitjuk a recept.csv filet
        for item in new_recipe:
            for j in range(len(item.material)):
                file.write(f'{item.name};{item.material[j]};{item.amount[j]}\n')# a filebe beleírjuk az item name részét, az item material részét és az item amount részét.
    return new_recipe

def storage_delete(recipe_list, storage_list, name):
    delete_element = []
    for item in recipe_list: 
        if item.name == name: #ha az item name részével egyenlő a name
            for anyag in item.material:
                delete_element.append(anyag) #delete_element tömbhöz hozzá adjuk az anyagot

    there_is_another_recipe = []
    for item in recipe_list:
        if item.name != name: #ha az item name részével nem lesz egyenlő a name-val
            for anyag in item.material:
                there_is_another_recipe.append(anyag) #there_is_another_recipe tömbhöz hozzá adja az anyagot

    new_storage = []
    for item in storage_list:
        benne_van_masban = False
        benne_van_toroltban = False

        for anyag in there_is_another_recipe:
            if item[0] == anyag:
                benne_van_masban = True

        for anyag in delete_element:
            if item[0] == anyag:
                benne_van_toroltban = True

        if benne_van_masban or not benne_van_toroltban:
            new_storage.append(item)

    with open("raktar.csv", "w", encoding="utf8") as file:
        for item in new_storage:
            file.write(f"{item[0]};{item[1]}\n")# a file-hez hozzá adjuk az item első elemét és a második elemét
    
    return new_storage

def storage_minus(storage, amount):
    hozzavalok = []
    with open("recept.csv", "r", encoding="utf8") as f:
        for sor in f:
            stripped = sor.strip() # a sort lestripeljük
            if stripped:
                adat = stripped.split(";")
                if adat[0] == amount:# Ha az adat első elemét egyenlő az amounttal akkor a hozzavalok tömbhöz hozzá adja az adat második és a harmadik elemét amit int-é alakít
                    hozzavalok.append([adat[1], int(adat[2])])

    raktar_sorok = []
    with open("raktar.csv", "r", encoding="utf8") as f:
        for sor in f:
            stripped = sor.strip() # a sort lestrippeled
            if stripped:
                raktar_sorok.append(stripped.split(";"))# a raktar_sorok hozzá adja a stripped-et lesplitelve 

    for recept_elem in hozzavalok:
        nev = recept_elem[0]
        mennyiseg = recept_elem[1]
        for i in range(len(raktar_sorok)):
            if raktar_sorok[i][0] == nev:# ha a raktar_sorok i-dik elemének első eleme egyenlő a névvel, akkor a raktar_sorok i-dik eleme egyenlő lesz a raktar_sorok i-dik elemének második elméből a mennyiséggel.
                raktar_sorok[i][1] = str(int(raktar_sorok[i][1]) - mennyiseg)

    with open("raktar.csv", "w", encoding="utf8") as f:
        for sor in raktar_sorok:
            f.write(f'{sor[0]};{sor[1]}\n')# az f-hez hozzá adjuk a sor első és a második elemét

    read_files.storage.clear()
    for sor in raktar_sorok:
        read_files.storage.append([sor[0], int(sor[1])])# a read_files storage részéhez hozzá adjuk a sor első elemét és a második elemét int-é alakítva

    return storage

def pay(tables, which):
    try:
        with open("vasarlasok.csv", "r", encoding="utf8") as file:
            sorok = file.readlines()
    except FileNotFoundError:
        sorok = []# ha nincs vasarlasok.csv akkor létre hozza a sorok tömböt

    uj_sor = f"{which};{tables[which].guest};{tables[which].waiter};"
    for j in range(len(tables[which].orders)):
        uj_sor += f"{tables[which].order_count[j]};{tables[which].orders[j]};"#az uj_sorhoz hozzá írja a tables valahanyadik elemének az order_count j.dik elemét, majd a tables valahanydik elemének az order részének a j.dik elemét
    uj_sor += f"{ tables[which].price}\n" # az uj_sorhoz hozzá adjuk a tables valahanyadik elemének price részét.

    talalt = False
    for i in range(len(sorok)):
        if sorok[i].split(";")[0] == str(which):
            sorok[i] = uj_sor
            talalt = True
            break
    
    if talalt == False:
        sorok.append(uj_sor)# a sorokhoz hozzá adjuk az uj_sort

    with open("vasarlasok.csv", "w", encoding="utf8") as file:
        file.writelines(sorok)

def Update_orders(tables):
    file = open('vasarlasok.csv', 'w', encoding='utf8')
    for i in range(len(tables)):
        if tables[i].orders != []:
            uj_sor = f"{i};{tables[i].guest};{tables[i].waiter};"#az uj_sorhoz hozzá adjuk az i-t, a tables i-dik elemének guest részét, a tables i-dik elemének waiter részét
            for j in range(len(tables[i].orders)):
                uj_sor += f"{tables[i].order_count[j]};{tables[i].orders[j]};" # az uj_sor hozzá adjuk a tables i-dik elem order_count j-dik részét, tables i-dik elem orders részének j elemét
            uj_sor += f"{ tables[i].price}\n"
            file.write(uj_sor)
    file.close()

def Conludes(table, which):
    with open("lezart_rendeles.csv", "a", encoding="utf8") as file:
        if len(table.orders) > 0:
            rendeles = ""
            for i in range(len(table.orders)):
                rendeles += f"{table.order_count[i]}db {table.orders[i]}, " # a rendeleshez hozzá adjuk a table order_count részének i-dik elemét és a table orders i-dik elemét
            file.write(f"A {which} számú asztal vendége: {table.guest}, felszolgálója: {table.waiter}. Rendelés: {rendeles}végösszeg: {table.price}\n")#kiirajtuk őket.