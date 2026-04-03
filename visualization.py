import os
from pynput import keyboard
from termcolor import colored
import read_files
import write_files
import msvcrt
import time
import main

def on_key_release(key): #Billentyű figyelő
    global selected, options, doit, enter
    if key == keyboard.Key.down and selected < len(options)-1:
        selected += 1
        return False
    elif key == keyboard.Key.up and selected > 0:
        selected -= 1
        return False
    elif selected == len(options)-1 and key == keyboard.Key.enter:
        enter = True
        doit = True
        return False
    elif key == keyboard.Key.enter:
        doit = True
        return False

options = ['main.Order()', 'main.Order_finish()', 'main.Storage_load()', 'main.New_recipe()', 'main.Menu_element_delete()', 'exit()'] #Menü elemei
optionsshow = ['Rendelés hozzáadása', 'Fizetés', 'Raktár töltése', 'Új étel hozzáadása', 'Étel törlése', 'Bezárás'] #Menü elemek megjelenített szövege
longest = len(optionsshow[0])
for i in optionsshow:
    if len(i) > longest:
        longest = len(i)
selected = 0
longest += 8

enter = False
doit = False

while not(enter): #Design
    os.system('cls')
    print(' ' + '_'*longest)
    print('|' + ' '*longest + '|')
    for i in range(len(optionsshow)):
        space = (longest-len(optionsshow[i]))/2 + 0.1
        if i != selected: print('|' + ' '*int(space) + str(optionsshow[i]) + ' '*round(space) + '|')
        else: print('|' + ' '*int(space) + colored(optionsshow[i], 'green') + ' '*round(space) + '|')
    print('|' + '_'*longest + '|')

    with keyboard.Listener(on_release=on_key_release) as listener: #Billentyűfigyelő meghívása
        listener.join()
    os.system('cls')

    if doit: #Törli az eltárolt billentyűleütéseket
        while msvcrt.kbhit():
            msvcrt.getch()

        eval(options[selected]) #Lefuttatja a menü kiválasztott programjáz
        doit = False
        time.sleep(0.2) #Hibák elkerülése végett vár mielőtt megjeleníti a menüt újra