import read_files


def recipe(name, material, amount):
    file = open("recept.csv", 'a', encoding="UTF-8")
    
    for i in range(len(material)):
        file.write(f"\n{name};{material[i]};{amount[i]}")
    file.close()
  
def storage(name):
        file = open('raktar.csv', 'a', encoding='utf8')
        file.write(f'\n{name};0')
        file.close()

def storage_all(white_monster):
    file = open('raktar.csv', 'w', encoding='utf8')
    for i in white_monster:
        file.write(f'{i[0]};{i[1]}\n')

def menu(menu):
    file = open("menu.csv", 'a', encoding= 'UTF-8')
    file.write(f'\n{menu};{input("Kérlek adj meg egy árat: ")}')
    file.close

def menu_delete(menu_list, target_name):
    new_menu = []
    for item in menu_list:
        if item[0] != target_name:
            new_menu.append(item)
    with open("menu.csv", 'w', encoding='UTF-8') as file:
        for item in new_menu:
            file.write(f'{item[0]};{item[1]}\n')
    return new_menu

def recipe_delete(recipe_list, name):
    new_recipe = []
    for item in recipe_list:
        if item.name != name:
            new_recipe.append(item)
    
    with open("recept.csv", 'w', encoding='utf-8') as file:
        for item in new_recipe:
            for j in range(len(item.material)):
                file.write(f'{item.name};{item.material[j]};{item.amount[j]}\n')
    return new_recipe

def storage_delete(recipe_list, storage_list, name):
    delete_element = []
    for item in recipe_list:
        if item.name == name:
            for anyag in item.material:
                delete_element.append(anyag)

    there_is_another_recipe = []
    for item in recipe_list:
        if item.name != name:
            for anyag in item.material:
                there_is_another_recipe.append(anyag)

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

    with open("raktar.csv", "w", encoding="UTF-8") as file:
        for item in new_storage:
            file.write(f"{item[0]};{item[1]}\n")
    
    return new_storage

def storage_minus(storage, amount):
    hozzavalok = []
    with open("recept.csv", "r", encoding="UTF-8") as f:
        for sor in f:
            adat = sor.strip().split(";")
            if adat[0] == amount:
                hozzavalok.append([adat[1], int(adat[2])])

    raktar_sorok = []
    with open("raktar.csv", "r", encoding="UTF-8") as f:
        for sor in f:
            raktar_sorok.append(sor.strip().split(";"))

    for recept_elem in hozzavalok:
        nev = recept_elem[0]
        mennyiseg = recept_elem[1]

        for i in range(len(raktar_sorok)):
            if raktar_sorok[i][0] == nev:
                aktualis_keszlet = int(raktar_sorok[i][1])
                uj_keszlet = aktualis_keszlet - mennyiseg
                raktar_sorok[i][1] = str(uj_keszlet)
    
    with open("raktar.csv", "w", encoding= "UTF-8") as f:
        for sor in raktar_sorok:
            f.write(f'{sor[0]};{sor[1]}\n')

    return storage

def pay(tables, which, price):
    try:
        with open("vasarlasok.csv", "r", encoding="UTF-8") as file:
            sorok = file.readlines()
    except FileNotFoundError:
        sorok = []

    uj_sor = f"{which};"
    for j in range(len(tables[which].orders)):
        uj_sor += f"{tables[which].order_count[j]};{tables[which].orders[j]}"
    uj_sor += f"{ tables[which].price}\n"

    talalt = False
    for i in range(len(sorok)):
        if sorok[i].split(";")[0] == str(which):
            sorok[i] = uj_sor
            talalt = True
            break
    
    if talalt == False:
        sorok.append(uj_sor)

    with open("vasarlasok.csv", "w", encoding="UTF-8") as file:
        file.writelines(sorok)
    

def Conludes(tables):
    with open("lezart_rendeles.csv", "a", encoding="UTF-8") as file:
        for which in range(len(tables)):
            if len(tables[which].orders) > 0:
                rendeles = ""
                for i in range(len(tables[which].orders)):
                    rendeles += f"{tables[which].order_count[i]}db {tables[which].orders[i]}, "
                file.write(f"A {which} számú asztal vendége: {tables[which].guest}, felszolgálója: {tables[which].waiter}. Rendelés(ek): {rendeles}végösszeg: {tables[which].price}\n")