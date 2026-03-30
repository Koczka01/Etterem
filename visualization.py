import os
from pynput import keyboard
from pynput.keyboard import Key
from termcolor import colored
import read_files
import write_files


def on_key_release(key):
    global selected
    global options
    if key == keyboard.Key.down and selected < len(options)-1:
        selected += 1
    elif key == keyboard.Key.up and selected > 0:
        selected -= 1
    elif selected == len(options)-1 and key == keyboard.Key.enter:
        global enter
        enter = True
    elif key == keyboard.Key.enter:
        eval(options[selected])
    exit()

def new_recipe():
    os.system('cls')
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


def Storage_load():
    pass

def Finish_run():
    pass

options = ['new_recipe()', 'storage_load()', 'finish_run()']
optionsshow = ['Új étel hozzáadása', 'Raktár töltése', 'Bezárás']
longest = len(optionsshow[0])
for i in optionsshow:
    if len(i) > longest:
        longest = len(i)
selected = 0
longest += 8

enter = False

while not(enter):
    os.system('cls')
    print(' ' + '_'*longest)
    print('|' + ' '*longest + '|')
    for i in range(len(optionsshow)):
        space = (longest-len(optionsshow[i]))/2 + 0.1
        if i != selected: print('|' + ' '*int(space) + str(optionsshow[i]) + ' '*round(space) + '|')
        else: print('|' + ' '*int(space) + colored(optionsshow[i], 'green') + ' '*round(space) + '|')
    print('|' + '_'*longest + '|')

    with keyboard.Listener(on_release=on_key_release) as listener:
        listener.join()
    os.system('cls')