from colorama import Fore, Style # pip install colorama
import random
from tools.helper import d, fancy, clear, bar
from .HealthBar import HealthBar
from .ExpBar import ExpBar


class Character():

    def __init__(self, name, defense = 50, exp = 0, lvl = 1, hp = 100):
        self.name = name
        self.hp = hp
        # self.max_hp = hp # Potentially needed
        self.defense = defense # !!!!?!!?!????!
        self.exp = exp
        self.lvl = lvl
        self.base_damage = 15
        self.health_bar = HealthBar(self, color = 'green')
        self.exp_bar = ExpBar(self, color= 'cyan')
        # create a magic bar as well!
        self.stamina = 100 # do something with this?!?!
        self.inventory = []
        self.runes = 0

    # implement block functionality !!!!
    def block(self):
        '''30% chance to block'''
        return random.random() < .30
    
    # implement parry functionality !!!!


    # get character info
    def get_info(self):
        '''Displays character information and updates health and exp bars.'''
        self.health_bar.update()
        self.exp_bar.update()
        print(f'''
~~~~~CHARACTER STATS~~~~~
{self.name}'s current level: {self.lvl}
''')
        self.health_bar.draw()
        self.exp_bar.draw()
    
    def level_check(self): # might need to add a parameter for the character we're checking for
        if self.exp >= 100: # leveling up might need to be a function for better useability
                self.lvl += 1
                self.exp -= 100
                print(f"{self.name} just gained a level!!")
                self.get_info()

    def attack(self, target):
        if target.hp <= 0:
            print(f"{target.name} is already dead!!!")
            return
        
        print(f"{Fore.MAGENTA}{self.name}{Fore.RESET} is attacking {Fore.RED}{target.name}{Style.RESET_ALL}!! ")
        # initialize an attack sequence, determine damage value
        damage = self.calculate_damage()
        if self.block():
            print(f"{Fore.RED}{target.name}{Fore.RESET} blocked {Fore.MAGENTA}{self.name}{Fore.RESET}'s attack!!")
            return
        target.hp -= damage
        # target.health_bar.change_color('red') ### Depending on who we're attacking, this color may already be set
        target.health_bar.update()
        if target.hp <= 0:
            print(f"{self.name} has defeated {Fore.RED}{target.name}{Fore.RESET}!!! {Fore.RED}****FATALITY****{Style.RESET_ALL}")
            self.exp += 20
            self.level_check() # level up??

        else:
            print(f"{Fore.MAGENTA}{self.name}{Fore.RESET} inflicted {Fore.YELLOW}{damage}{Fore.RESET} damage!!")
            print(f"{Fore.RED}{target.name}{Fore.RESET}'s remaining HP: {target.hp}") #### make this into a health bar type of thing
            fancy()
            # self.get_info()
            self.health_bar.draw()
            target.health_bar.draw()
            d()

    def calculate_damage(self):
        '''Randomize damage based on base damage and consider critical hit'''
        # randomize damage based off of base damage
        damage = random.randint(self.base_damage - 5, self.base_damage + 5)
        if self.critical_hit():
            damage *= 2
            print(f"{self.name} made a {Fore.RED} critical hit!!! {Style.RESET_ALL}")
            return damage
        return damage


    def critical_hit(self):
        # 15% chance for a critical hit
        return random.random() < .15




if __name__ == '__main__':

    rogue = Character('Aragorn')
    warrior = Character('Zelda')

    # rogue.attack(warrior)
    # rogue.attack(warrior)
    # rogue.attack(warrior)
    # rogue.attack(warrior)
    # rogue.attack(warrior)
    # rogue.attack(warrior)
    # rogue.attack(warrior)
    # rogue.attack(warrior)
    # rogue.attack(warrior)


    # print("|███████████████_________|")

    flag = True
    while flag:
        ans = input("Continue or quit?")
        if ans == 'quit':
            break
        elif ans == 'i':
            rogue.get_info()
        else:
            clear()
            rogue.attack(warrior)