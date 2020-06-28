import random
from .items import *
from ..setup import typeHero


# TODO: ==== item Material ====
def getFragmen(name, index):
    global items
    if name == 'kupon':
        items = item("Kupon", coin=0, amount=index, type="Fragmen")
    elif name == 'silver':
        items = item("silver", coin=0, amount=index, type="Fragmen")
    return items


twigs = item("Twigs", coin=1, amount=random.randint(1, 10), type="Item")
leaf = item("Leaf", coin=1, amount=random.randint(1, 10), type="Item")
leather = item("leather", coin=2, amount=random.randint(1, 10), type="Item")
stone = item("Stone", coin=3, amount=random.randint(1, 7), type="Item")

iron = item("Iron Ingot", coin=10, amount=random.randint(1, 4), type="Mineral")
gold = item("Gold Ingot", coin=15, amount=random.randint(1, 3), type="Mineral")
diamond = item("Diamond", coin=25, amount=random.randint(1, 2), type="Mineral")
emerald = item("Emerald", coin=50, amount=1, type="Mineral")
ruby = item("Ruby", coin=100, amount=1, type="Mineral")


# TODO: ==== item Potion ====
mana = potion('Potion Mana', coin=5, amount=1, UpHealth=0, UpMana=25, use_hero=typeHero.Mage)
health = potion('Potion Health',  coin=5, amount=1, UpHealth=20, UpMana=0, use_hero='all')


# TODO: ==== item Food ====
kripik = food('kripik', coin=5, amount=1, Up_hp=5, Up_mana=10, Updmg=2)
candy = food('Candy', coin=10, amount=1, Up_hp=12, Up_mana=10, Updmg=5)
seblak = food('Seblak', coin=100, amount=1, Up_hp=100, Up_mana=100, Updmg=25)


test = food('Seblak', coin=100, amount=100, Up_hp=100, Up_mana=100, Updmg=25)


# TODO: ==== Weapons ====
def weapons_warrior(index):
    global weapon
    if index == 0:
        weapon = weapons('Wood', coin=0, power=5, crit=3, qualty='Broken', shape='Sword', equip=False)
    elif index == 1:
        weapon = weapons('Robber', coin=10, power=10, crit=5, qualty="common", shape="Sword", equip=False)
    elif index == 2:
        weapon = weapons('Hunter', coin=50, power=20, crit=7, qualty="Uncommon", shape="Sword", equip=False)
    elif index == 3:
        weapon = weapons('Atlas', coin=100, power=50, crit=10, qualty="Rare", shape="Sword", equip=False)
    elif index == 4:
        weapon = weapons('knight', coin=250, power=100, crit=12, qualty="Epic", shape="Sword", equip=False)
    elif index == 5:
        weapon = weapons('Mega', coin=500, power=250, crit=15, qualty="legendary", shape="Sword", equip=False)
    elif index == 6:
        weapon = weapons('Kujang', coin=1000, power=500, crit=17, qualty="Special", shape="Sword", equip=False)
    else:
        pass
    return weapon


def weapons_mage(index):
    global weapon
    if index == 0:
        weapon = magic_wand('Wood', coin=0, power=5, crit=3, qualty='Broken', shape='Wand', equip=False)
    elif index == 1:
        weapon = magic_wand("Aloha", coin=10, power=10, crit=5, qualty="Common", shape="Wand", equip=False)
    elif index == 2:
        weapon = magic_wand("Flash", coin=50, power=50, crit=10, qualty="Uncommon", shape="Wand", equip=False)
    elif index == 3:
        weapon = magic_wand("Paladin", coin=100, power=100, crit=15, qualty="Rare", shape="Wand", equip=False)
    elif index == 4:
        weapon = magic_wand("Moon", coin=250, power=200, crit=25, qualty="Epic", shape="Wand", equip=False)
    elif index == 5:
        weapon = magic_wand("Silisk", coin=500, power=400, crit=40, qualty="Legendary", shape="Wand", equip=False)
    else:
        pass
    return weapon


def weapons_archer(index):
    global weapon
    if index == 0:
        weapon = weapons('Wood', coin=0, power=5, crit=3, qualty='Broken', shape='Bow', equip=False)
    elif index == 1:
        weapon = bow('Oak', coin=10, power=10, crit=5, qualty='Common', shape='Bow', equip=False)
    elif index == 2:
        weapon = bow('Iron', coin=50, power=50, crit=7, qualty='Uncommon', shape='Bow', equip=False)
    elif index == 3:
        weapon = bow('Gold', coin=100, power=120, crit=10, qualty='Rare', shape='Bow', equip=False)
    elif index == 4:
        weapon = bow('Diamond', coin=250, power=260, crit=15, qualty='Epic', shape='Bow', equip=False)
    elif index == 5:
        weapon = bow('Elf', coin=500, power=510, crit=20, qualty='Legendary', shape='Bow', equip=False)
    else:
        pass
    return weapon


# TODO: ==== Armor ====
def createArmor(index):
    global armor
    if index == 0:
        armor = Armor('Cloth', qualty='Broken', health=5, defn=2, coin=0, equip=False)
    if index == 1:
        armor = Armor("Leather", qualty="Common", health=10, defn=5, coin=10, equip=False)
    elif index == 2:
        armor = Armor("iron", qualty="Uncommon", health=10, defn=15, coin=50, equip=False)
    elif index == 3:
        armor = Armor("Metal", qualty="Rare", health=10, defn=35, coin=100, equip=False)
    elif index == 4:
        armor = Armor("Reaper", qualty="Epic", health=10, defn=70, coin=250, equip=False)
    elif index == 5:
        armor = Armor("gladiator", qualty="Legendary", defn=105, health=500, coin=10, equip=False)
    else:
        pass
    return armor

"""  
finder = Armor(name="Armor Finder", Up_armor=2, Up_healthMax=10, maxArmor=1, coin=10, value=1)
gladiator = Armor(name="Armor gladiator", Up_armor=5, Up_healthMax=20, maxArmor=1, coin=50, value=1)
reaper = Armor(name="Armor reaper", Up_armor=9, Up_healthMax=35, maxArmor=1, coin=100, value=1)
frost = Armor(name="Armor frost", Up_armor=14, Up_healthMax=50, maxArmor=1, coin=150, value=1)
"""
