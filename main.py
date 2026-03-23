#I've become so numb
import read_files
import write_files

table_count = int(input('Adja meg hány asztal van: '))

class table:
    def __init__(self) -> None:
        self.orders = []

tables = [table()]*table_count

action = input('írd be, hogy new_recipe vagy Storage_load: ')
while action != '':
    if action == 'new_recipe':
        read_files.recipe.append(read_files.Recipe(input('Add meg a nevét a kajának: ')))
        material = input('Adjon meg egy alapanyagot: ')
        while material != '':
            read_files.recipe[-1].material.append(material) 
            read_files.recipe[-1].amount.append(int(input("Kérlek add meg az alapanyag mennyiségét: ")))
            i = 0
            while i < len(read_files.storage) and read_files.storage[i][0] != material:
                i += 1

            if i == len(read_files.storage):
                write_files.storage(material)

            material = input('Adjon meg egy alapanyagot, ha nem szeretne többet, akkor nyomjon entert: ')

        write_files.menu(read_files.recipe[-1].name)

        write_files.recipe(read_files.recipe[-1].name, read_files.recipe[-1].material, read_files.recipe[-1].amount)

    if action == "Storage_load":
        i = 0
        m = input("kérem adja meg, hogy mit szeretne feltölteni: ")
        while i < len(read_files.storage) and m == read_files.storage[i][0]:
            read_files.storage.append(read_files.Recipe(input("Kérlek add meg, hogy mennyi szeretnél hozzá adni: ")))
            i += 1

    action = input('Nyomj egy entert: ')    

print(read_files.recipe[-1].amount)
