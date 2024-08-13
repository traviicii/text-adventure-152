from colorama import Fore, Style

class HealthBar():

    symbol_remaining = "█"
    symbol_lost = "_"
    barrier = "|"

    colors = {
        'red': Fore.RED,
        'purple': Fore.MAGENTA,
        'green': Fore.GREEN,
        'blue': Fore.BLUE,
        'yellow': Fore.YELLOW,
        'cyan': Fore.CYAN,
        'default': Fore.RESET
    }

    def __init__(self, character, length = 20, color = colors['default']):
        self.character = character
        self.length = length
        self.max_value = 100
        self.current_hp = character.hp
        self.color = self.colors.get(color, self.colors['default'])

    def change_color(self, color):
        self.color = self.colors.get(color, self.colors['default'])

    def update(self):
        self.current_hp = self.character.hp

    def draw(self): #               50        /     100 = .5 * 20 = 10 bars of health left
        remaining_bars = round((self.current_hp / self.max_value) * self.length)
        lost_bars = self.length - remaining_bars
        if remaining_bars <= 5:
            self.color = self.colors['red']
        print(f"{self.character.name}'s HEALTH: {self.character.hp}/{self.max_value}")
        print(f"{self.barrier}{self.color}{self.symbol_remaining * remaining_bars}{self.symbol_lost * lost_bars}{self.colors["default"]}{self.barrier}")

