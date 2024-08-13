from helper import d, clear
from Character import Character
from ascii_magic import AsciiArt, Back
from PIL import ImageEnhance, Image, ImageFilter
import random

'''
-- Used ChatGTP to initate a story
https://chatgpt.com/share/2814f17c-17a5-421b-8f63-918cbe3bbe11

Character starts with memory loss. Story begins below, they will eventurally have to remember their name which is when we will create the Character object and then they eventually come accross 3 weapons that will decide what character class they are

'''
player = None



def continue_check():
    '''Waits for the user to choose to continue onto the next part of whatever we're doing at the moment
    prints the following in this order:
    divider
    input pause
    clear
    divider
    '''
    d()
    input("> ") # wait for them to press any key before moving on

    clear()
    d()


def chapter1():
    intro()

def intro():
    clear()

    # with Image.open('image.png') as im:
    #     im.filter(ImageFilter.DETAIL)
        # ImageEnhance.Color(im).enhance(1.3)

    # my_art = AsciiArt.from_image('image.png')
    # # enh = ImageEnhance.Color(my_art).enhance(1.3)
    # # my_art.image = ImageEnhance.Brightness(my_art.image).enhance(0.2)
    # my_art.to_terminal(columns=170)

    # img = Image.open('image.png')
    # something = ImageEnhance.Color(img)
    # my_art = AsciiArt.from_image("a_tree.jpg")
    # my_art = AsciiArt.from_pillow_image(img)
    # my_art.to_terminal()

    d()
    print('''
You awaken with a start, your breath ragged and cold as it billows into the misty air. The ground beneath you is damp, covered in a thick carpet of decaying leaves, their once vibrant colors long since faded to a lifeless brown. Tall, twisted trees loom above, their gnarled branches clawing at the murky sky like skeletal hands reaching for salvation. A faint glow filters through the dense canopy, casting eerie shadows that dance and flicker as if alive.
''')
    continue_check()

    print('''
Your heart pounds in your chest, a frantic rhythm that matches the creeping dread curling around your spine. You try to recall how you ended up in this foreboding forest, but your mind is a blank slate, a void where memories should be. The only thing you can grasp is a name— your name —echoing faintly in the recesses of your thoughts. But even that feels uncertain, as if it might slip away at any moment.
''')
    d()
    print("Try to remember your name...\n")
    name = input("> ")

    player = Character(name)

    clear()
    d()
    print('''
A shiver runs through you, but not just from the cold. There is something about this place, an unnatural stillness that presses down on you, suffocating in its intensity. The woods are silent— too silent. No chirping of birds, no rustling of small creatures in the underbrush. Just the oppressive quiet, broken only by the occasional creak of ancient wood swaying in the unseen breeze.''')
    
    continue_check()

    print('''
As you stand, your legs unsteady beneath you, the mist clings to your skin, leaving a damp chill that seeps into your bones. You glance around, trying to get your bearings, but every direction looks the same— an endless maze of trees and shadows.
''')
    
    continue_check()

    print('''
Suddenly, a whisper—barely audible—brushes past your ear, carried on the wind. You turn sharply, but there’s nothing there. Just the shadows, thick and heavy, watching, waiting. You have the sense that you’re not alone, that something is lurking just beyond your sight, hidden in the gloom.''')
    
    continue_check()

    print('''
A narrow path, almost invisible beneath the layers of fallen leaves, stretches out before you, winding deeper into the heart of the forest. It’s the only sign of direction in this disorienting world. With no memory, no past to anchor you, the path seems like the only option. But as you take your first hesitant step forward, a thought strikes you— what if this path was meant to be forgotten, just like everything else?''')
    d()
    
    print("\nContinue down this spooOOOooOoOoky path or Investigate the whisper?")
    print("\n(Continue or Investigate?)")

    choice = input("> ").lower()

    if choice == 'continue':
        pass
    elif choice == 'investigate':
        enemy = Character("Demon")
        enemy.base_damage = 30
        clear()
        d()
        print('''
The shadow that brushed past you emerges and you see a horrifying grotesque demon in the pale moonlight, with piercing black eyes yellow pupils that seem to glow faintly. It's claws gleam at you for a split second before it madly rushes towards you.
''')
        # continue_check()
        d()

        print('''
\nDo you attempt to run down the path you saw (away from danger) or do you try to block the demon attacking you?
''')
        d()

        print("\n(Run or Block)\n")
        choice = input("> ").lower()
        print("\n")
        d()
        print("\n")

        if choice == 'run':
            pass
        elif choice == 'block':
            clear()
            roll = random.randrange(1,21) #roll 20 sided dice for block chance
            if roll > 15: # checking to see if the character successfully blocks
                # character escape
                pass
            else:
                d()
                enemy.attack(player)
                print('''
The demon's claws tear into your arm, pain searing through you as you stumble backward. Desperation fuels your next move—you kick up a cloud of dirt and leaves, momentarily blinding the creature. Seizing the chance, you wrench free and dash down the path, blood pounding in your ears as the forest closes in around you. The demon's enraged screech echoes behind you, but you push forward, the path your only hope of survival.
''')
                continue_check()


if __name__ == "__main__":

    intro()