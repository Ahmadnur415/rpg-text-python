import random
import time
from ..setup import typeHero


def critical_hit(attacker):
    critical_change = random.randint(1, 100)
    try:
        if critical_change <= attacker.crit:
            return True
        else:
            return False
    except AttributeError:
        if critical_change <= attacker.crit:
            return True
        else:
            return False


def playerAttack(skill, defenders, attacker):
    global atk_hero, text_dmg, magic_atk, atk_enemy
    crit = critical_hit(attacker)

    # trun attacker
    if attacker.type_hero == typeHero.Mage:
        if attacker.mana >= attacker.cost_mana:
            if crit:
                min_crit = (attacker.magic * 2) - defenders.dfnE
                max_crit = (attacker.magic * 2)

                if skill:
                    magic_atk = random.randint(attacker.magic, max_crit)
                elif not skill:
                    magic_atk = random.randint(min_crit, max_crit)

                text_dmg = "Crit"
                defenders.hpE -= magic_atk
            elif not crit:
                min_atk = attacker.magic - defenders.dfnE
                if min_atk <= 0:
                    min_atk = 0

                if skill:
                    magic_atk = attacker.magic
                elif not skill:
                    magic_atk = random.randint(min_atk, attacker.magic)

                text_dmg = ""
                defenders.hpE -= magic_atk
            attacker.mana -= attacker.cost_mana
            print(attacker.name + " Meyerang " + defenders.name + " {} {}".format(magic_atk, text_dmg))
        else:
            print("Mana Anda Kurang")
    else:
        if crit:
            min_crit = (attacker.attpower * 2) - defenders.dfnE
            max_crit = (attacker.attpower * 2)

            if skill:
                atk_hero = random.randint(attacker.attpower, max_crit)
            elif not skill:
                atk_hero = random.randint(min_crit, max_crit)

            text_dmg = "Crit"
            defenders.hpE -= atk_hero
        elif not crit:
            min_atk = attacker.attpower - defenders.dfnE
            if min_atk <= 0:
                min_atk = 0

            if skill:
                atk_hero = attacker.attpower
            elif not skill:
                atk_hero = random.randint(min_atk, attacker.attpower)
            text_dmg = ""

            defenders.hpE -= atk_hero
        print(attacker.name + " Meyerang " + defenders.name + " {} {}".format(atk_hero, text_dmg))
    time.sleep(1)


def enemyAttack(enemy, defenders):
    global atk_enemy, text_dmg
    crit = critical_hit(enemy)
    if crit:
        min_crit = round(enemy.atkE * 0.5 + enemy.atkE) - defenders.armor
        max_cri = round(enemy.atkE * 0.5 + enemy.atkE)
        if min_crit <= 0:
            min_crit = 1
        if max_cri <= 0:
            max_cri = enemy.atkE
        atk_enemy = random.randint(min_crit, max_cri)
        text_dmg = "Crit"
    elif not crit:
        min_dmg = enemy.atkE - defenders.armor
        if min_dmg <= 0:
            min_dmg = 1
        atk_enemy = random.randint(min_dmg, enemy.atkE)
        text_dmg = ""
        defenders.health -= atk_enemy
    print(enemy.name + " Meyerang " + defenders.name + " {} {}".format(atk_enemy, text_dmg))
    time.sleep(1)
