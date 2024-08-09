

class Item():
    '''
    Valid Item Types:
        consumable
        health
        magic
        damage
        fire
        ice
        lightening
        defense
    '''

    def __init__(self, value, name, desc, item_type = []):
        self.value = value
        self.name = name
        self.desc = desc
        self.item_type = item_type


# potion = Item(15, "Minor Health Potion", "Heals a character for a small amoutn of HP", item_type=['health', 'consumable'])

class Potion(Item):
    '''
    Rarity Options:
        minor
        common
        rare
        exotic
        legendary
        mythic
    '''

    effects = {
        'heal_hp' : 0,
        'attk_boost' : 0,
        'def_boost' : 0,
        'heal_mana' : 0
    }

    def __init__(self, value, name, desc, item_type, rarity):
        super().__init__(value, name, desc, item_type)
        self.rarity = rarity
        self.effect = self.effects # how is this structured and dealth with? 
        


healingpotion = Potion(15, "Minor Healing Potion", "Heals a character for a small amoutn of HP", item_type=['health', 'consumable'], )