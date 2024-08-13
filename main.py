
from helper import bar, clear
from Character import Character
from chapter1 import intro, chapter1

def new_character():
    name = input("Please enter your character's name: ")
    new_character = Character(name)
    return new_character

def player_actions(): # a menu that can be called on by the player with actions they can take any time throughout the game
    '''
    take [item]
    examine [object]
    move [north, south, east, west]
    continue
    investigate
    attack
    defend
    flee

    '''
    pass


def main():
    current_character = None
    running = True
    while running:
        clear()
        if current_character: # if there is a Character object stored in current_character
            current_character.exp = 60
            current_character.exp_bar.update()
            bar()
            current_character.get_info()
        bar()
        print('''
    1.) New Game
    2.) Load Game
    3.) Save Progress
    4.) Help
    5.) Quit''')
        bar()
        ans = input("\n> ")

        if ans == '1':
            chapter1()
        elif ans == '2':
            pass
        elif ans == '3':
            pass
        elif ans == '4':
            pass # something for help, maybe show main menu or a list of commands/actions they can take
        elif ans == '5':
            running = False

main()