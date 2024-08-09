
from helper import bar, clear
from character_classes.Character import Character
from storyline.chapter1 import intro

def new_character():
    name = input("Please enter your character's name: ")
    new_character = Character(name)
    return new_character


# -text-adventure
#     -storyline
#         -chapter1.py
#     -character_classes
#         -Chatacter.py
#         -Wizard.py
#     -inventory
#         -Item.py
#         -Weapon.py
#     -helper.py
#     -main.py

def main():
    current_character = None
    running = True
    while running:
        clear()
        if current_character:
            current_character.exp = 60
            current_character.exp_bar.update()
            bar()
            current_character.get_info()
        bar()
        print('''
    1.) New Character
    2.) Load Character
    3.) Save Progress
    4.) Start Game
    5.) Help
    6.) Quit''')
        bar()
        ans = input("\n> ")

        if ans == '1':
            current_character = new_character()
        elif ans == '2':
            pass
        elif ans == '3':
            pass
        elif ans == '4':
            intro()
        elif ans == '5':
            running = False

main()