from Character import Character


class Wizard(Character):

    def __init__(self, name, defense, exp, lvl, hp, mana):
        super().__init__(name, defense, exp, lvl, hp)
        self.mana = mana

    def cast_fireball(self):
        pass

    def cast_lightening(self):
        pass

    def grand_heal(self):
        pass