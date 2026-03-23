def recipe(name, material, amount):
    file = open("recept.csv", 'a', encoding="UTF-8")
    
    for i in range(len(material)):
        file.write(f"\n{name};{material[i]};{amount[i]}")
    file.close()
  
def storage(name):
        file = open('raktar.csv', 'a', encoding='utf8')
        print(name)
        file.write(f'\n{name};0')
        file.close()