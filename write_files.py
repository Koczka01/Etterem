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
    new_menu = [item for item in menu_list if item[0] != target_name]
    with open("menu.csv", 'w', encoding='UTF-8') as file:
        for item in new_menu:
            file.write(f'{item[0]};{item[1]}\n')
    return new_menu

def storage_delete(storage_list, name):
    new_storage = [item for item in storage_list if item[0] != name]
    with open("recept.csv", 'w', encoding= 'utf-8') as file:
        for item in new_storage:
            file.write(f'{item[0]};{item[1]}\n')
    return new_storage
