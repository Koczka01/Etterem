#I've become so numb
import read_files
import write_files

table_count = int(input('Adja meg hány asztal van: '))

class table:
    def __init__(self) -> None:
        self.orders = []

tables = [table()]*table_count

action = input('írd be, hogy new_recipe: ')
while action != '':
    if action == 'new_recipe':
        read_files.recipe.append(read_files.Recipe(input('Add meg a nevét a kajának: ')))
        material = input('Adjon meg egy alapanyagot: ')
        while material != '':
            read_files.recipe[-1].material.append(material) 
            read_files.recipe[-1].amount.append(int(input("Kérlek add meg az alapanyag mennyiségét: ")))
            material = input('Adjon meg egy alapanyagot, ha nem szeretne többet, akkor nyomjon entert: ')
    
    write_files.recipe(read_files.recipe[-1].name, read_files.recipe[-1].material, read_files.recipe[-1].amount)

    action = input('Nyomj egy entert: ')

print(read_files.recipe[-1].amount)
