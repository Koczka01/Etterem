#I've become so numb
import read_files
import write_files

table_count = int(input('Adja meg hány asztal van: '))

class table:
    def __init__(self) -> None:
        self.orders = []

tables = [table()]*table_count

action = input('írd be, hogy new_recipe vagy Storage_load vagy Order vagy Menu element delete: ')
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
        while i < len(read_files.storage) and m != read_files.storage[i][0]:
            i += 1 
        
        if i < len(read_files.storage):
            read_files.storage[i][1] += int(input("Kérlek add meg, hogy mennyi szeretnél hozzá adni: "))
        else:
            print("Rossz alapanyagot adtál meg!")
        
        write_files.storage_all(read_files.storage)
        
    if action == "Order":
        there_is_a_table = True
        while there_is_a_table:
            which = int(input("Melyik asztalhoz ment a pincér: "))
            o = input("Kérem adja meg a rendelését: ")
            o = o.strip()
            while o != "":
                i = 0
                logic = False
                while i < len(read_files.menu):
                    if o == read_files.menu[i][0]:
                        tables[which].orders.append(o)
                        logic = True
                        break
                    i += 1

                if logic == False:
                    print("Bocs haver ilyet nem esszel")
            
                o = input("Kérem adjon meg még egy új ételt, ha nem szeretne akkor nyomjon egy entert: ")
                o = o.strip()
            further = input("Szeretnél másik asztaltól is rendelést felvenni? (Y/N): ")
            if further != "Y":
                there_is_a_table = False

    if action == "Menu element delete":
        i = 0
        delete = input("Kérem adja hogy melyik ételt szeretné törölni a menüből: ")
        while i < len(read_files.menu):
            if delete == read_files.menu[i][0]:
                read_files.menu[i].pop
                read_files.storage[i].pop
                write_files.menu_delete(read_files.menu, delete)
                write_files.storage_delete(read_files.storage, delete)
            i += 1
        
        delete = input("Kérem adja hogy melyik más ételt szeretné kitörölni a listából, hanem szeretne, akkor nyomjon egy enter: ")

    action = input('Nyomj egy entert: ')