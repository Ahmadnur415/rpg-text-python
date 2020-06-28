from .enemy import *
import random


def firstName():  # Memasukan Nama Awal Secara Random Kepada Musuh
    name = random.choice(
        [
            'Steve', 'Archer', 'Alex', 'Kero', 'Kahuna', 'Shaol', 'Khine', 'Aggressive', 'Axe', 'Deef', 'Yang', 'Khan',
            'Shadow', 'Black', 'Creed', 'Death', 'Core', 'Titan', 'Limit', 'legion', 'Chi', 'Dara', 'John', 'Timid ',
            'average Duck', 'Jiff', 'Iconic', 'Hanzell', 'Hell', 'Gritz', 'Frost', 'Felix', 'Elder', 'Exotic', 'lelion'
        ]
    )
    return name


def lastName():  # Memasukan Nama Terakhir Secara Random
    name = random.choice(
        [
            'Naked', 'Cry', 'One', 'Fast', 'Jax', 'Heavy', 'Dast', 'Izzy', 'Halder', 'Harry', 'Hell', 'heat',
            'Flux', "Flint", 'Eco', 'G', 'F', 'Z', 'W', 'P', 'M4n', 'Hart', 'Shot', 'Fire', 'Abs', '123', '415', '435'
        ]
    )
    return name


def gen_hp(player):  # Untuk Meyeimbangkan Health Musuh dan Player
    hp_min = player.healthMax / 2
    hp_max = player.healthMax
    hp = random.randint(hp_min, hp_max)
    return hp


def Enemy(hero):
    from ..setup import typeHero
    hpEnemyMin = round(hero.healthMax - (hero.healthMax * 50 / 100))
    hpEnemyMax = round(hero.healthMax + (hero.healthMax * 10 / 100))

    defEnemyMin = round(hero.armor - (hero.armor * 40 / 100))
    defEnemyMax = round(hero.armor - (hero.armor * 15 / 100))

    critEnemyMin = round(hero.crit - (hero.crit * 10 / 100))
    critEnemyMax = round(hero.crit + (hero.crit * 20 / 100))

    if hero.type_hero == typeHero.Mage:
        atkEnemyMin = round(hero.magic - (hero.magic * 40 / 100))
        atkEnemyMax = round(hero.magic - (hero.magic * 5 / 100))
    else:
        atkEnemyMin = round(hero.attpower - (hero.attpower * 40 / 100))
        atkEnemyMax = round(hero.attpower - (hero.attpower * 5 / 100))

    enemyArena = enemy(
        name=firstName(),
        lastName=lastName(),
        hpMaxE=random.randint(hpEnemyMin, hpEnemyMax),
        atkE=random.randint(atkEnemyMin, atkEnemyMax),
        dfnE=random.randint(defEnemyMin, defEnemyMax),
        crit=random.randint(critEnemyMin, critEnemyMax),
        clss=hero.enemy_change
    )

    return enemyArena


# TODO: easy
pangolin = boss('Pamgolin', atkE=10, hpE=30, hpMaxE=30, dfnE=5, crit=15, clss="easy")

goblin = monster_easy("Goblin")
m_orc = monster_easy("Mini Orc")
ark = monster_easy("Ark")
worm = monster_easy("Mini Worm")


# TODO: medium
hydra = boss('Hydra', atkE=15, hpE=50, hpMaxE=50, dfnE=10, crit=20, clss="medium")


# TODO: hard
orc = boss('Orc', atkE=10, hpE=100, hpMaxE=100, dfnE=10, crit=15, clss="hard")


# TODO: hardcore
dragon = boss('Dragon', atkE=20, hpE=150, hpMaxE=150, dfnE=20, crit=5, clss="Hardcore")
