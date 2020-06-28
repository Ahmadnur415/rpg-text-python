from .create_item import *


def get_item():

    """
    :return:
        pass
    :argument
        :Perolehan item
            25% Zonk / tidak dapat Item
            60% Item Biasa seperti : stick, stone, mana, health, dll
            17% item Langka seperti : Gold, Iron , Diamond, Dll
            2,5% Item senjata kualitas Biasa / common / uncommon
            0.5 Item senjata Kualitas rare / Epic / Special
    """
    # import random
    global items
    changeItem = round(random.uniform(1, 100), 1)

    if changeItem >= 99.5:
        items = random.choice([seblak, ruby])
    elif changeItem >= 98.0:
        items = random.choice([diamond, candy, health])
    elif changeItem >= 81.0:
        items = random.choice([gold, iron, leather])
    elif changeItem >= 25.0:
        items = random.choice([twigs, stone, mana, health, leaf, leather])
    elif changeItem >= 0.0:
        items = "[== tidak Menemukan Item ==]"

    """if 0.0 <= changeItem <= 25.0:
        items = "[== tidak Menemukan Item ==]"
    elif 25.0 <= changeItem <= 80.0:
        items = random.choice([twigs, stone, mana, health, leaf, leather])
    elif 81.0 <= changeItem <= 97.0:
        items = random.choice([gold, iron, leather])
    elif 98.0 <= changeItem <= 99.4:
        items = random.choice([diamond, candy, health])
    elif 99.5 <= changeItem <= 100.0:
        items = random.choice([seblak, ruby])"""
    return items


def boxRare(hero):
    from ..setup import typeHero
    global box
    get = round(random.uniform(1, 100), 1)
    if 1.0 <= get <= 25.0:
        box = getFragmen('Kupon', random.randint(1, 20))
    elif 26.0 <= get <= 80.0:
        box = random.choice([mana, health])
    elif 81.0 <= get <= 97.0:
        box = random.choice([gold, iron, leather])
    elif 98.0 <= get <= 99.4:
        box = random.choice([diamond, candy, health])
    elif 99.5 <= get <= 100.0:
        if hero.type_hero == typeHero.Mage:
            box = None
        elif hero.type_hero == typeHero.Warrior:
            box = None
        elif hero.type_hero == typeHero.Archer:
            box = None
    return box
