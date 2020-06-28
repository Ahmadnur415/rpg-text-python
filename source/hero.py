from source.setup.text import line, bcolors, typeHero
from .skill import *
from .setup import enter_select
import random


class Hero:

    def __init__(self, type_hero):
        self.name = 'player'
        # attack
        self.attpower = 0
        self.crit = 0
        # Magic power
        self.magic = 0
        # health
        self.healthMax = 0
        self.hp_rgn = 3
        self.health = self.healthMax
        # Mana
        self.manaMax = 0
        self.mana = self.manaMax
        self.cost_mana = 10
        self.mana_rgn = 2
        # armor
        self.armor = 0
        # coin
        self.__coin = 1000
        self.coin = self.__coin
        # level
        self.level = 1
        # Exp
        self.exp = 0
        self.exp_max = 25
        # Training
        self.UpHp = 5
        self.UpMp = 10
        self.UpPower = 5
        self.UpCrit = 1

        self.reqCoinHp = 5
        self.reqCoinMp = 7
        self.reqCoinPower = 10
        self.reqCoinCrit = 15

        # item / inventory
        self.inventory = []
        self.use_weapons = []
        self.use_armor = []
        self.skill = []
        # type Hero
        self.type_hero = type_hero
        self.enemy_change = "easy"
        self.class_hero()
        self.Class()

    def class_hero(self):
        if self.type_hero == typeHero.Warrior:
            # Atck power
            self.attpower += random.randint(10, 15)
            self.crit += 5
            # health
            self.healthMax += 120
            self.health = self.healthMax
            # armor
            self.armor += 20

            Skill_1 = blackAnger()
            Skill_2 = riseUp()
            self.skill.append(Skill_1)
            self.skill.append(Skill_2)

        elif self.type_hero == typeHero.Mage:
            # Magic Power
            self.magic += 15
            self.crit += 5
            # health
            self.healthMax += 100
            self.health = self.healthMax
            # Mana
            self.manaMax += 150
            self.mana = self.manaMax
            # armor
            self.armor += 7
            Skill_1 = fireBall()
            Skill_2 = healing()
            self.skill.append(Skill_1)
            self.skill.append(Skill_2)

        elif self.type_hero == typeHero.Archer:
            self.attpower += 20
            self.crit += 10
            # health
            self.healthMax += 90
            self.health += self.healthMax
            # armor
            self.armor += 5
            Skill_1 = doubleArrow()
            Skill_2 = avoidAttack()
            self.skill.append(Skill_1)
            self.skill.append(Skill_2)

    def Class(self):
        from .setup import level
        # Menemtukan Enemy dalam Pertarungn menggunakan system health Max Hero
        if self.healthMax >= 7500:
            self.enemy_change = level.hardcore
        elif self.healthMax >= 2500:
            self.enemy_change = level.hard
        elif self.healthMax >= 250:
            self.enemy_change = level.medium
        elif self.healthMax >= 100:
            self.enemy_change = level.easy

    # TODO : Menampilkan Stats Hero Yang Telah Ditentukan
    def info(self):
        print("Nama : {}".format(self.name))
        bar = round((100 / self.exp_max) * self.exp)

        if self.type_hero == typeHero.Mage:
            print(
                "\tmagic  : {}   ".format(
                    self.magic
                )
            )
        else:
            print(
                "\tAttck  : {}   ".format(
                    self.attpower
                )
            )
        print(
            "\tCrit   : {}%  \n"
            "\tHealth : {}/{}\n"
            "\tMana   : {}/{}\n"
            "\tDefn   : {}   \n"
            "\tlevel  : {}   \n"
            "\tCoin   : {}   \n"
            "\tExp    : {}/{}  {}%\n"
            "\tHero   : {}".format(
                self.crit, self.health, self.healthMax, self.mana, self.manaMax, self.armor, self.level,
                self.coin, self.exp, self.exp_max, bar, self.type_hero
            )
        )

    @property
    def info_lite(self):
        if self.health < 0:
            self.health = 0
        if self.health > self.healthMax:
            self.health = self.healthMax

        if self.type_hero == typeHero.Mage:
            if self.mana < 0:
                self.mana = 0
            if self.mana > self.manaMax:
                self.mana = self.manaMax
            return "{} :\n\tmagic: {} \n\tDefn : {}\n\tHp   : {} / {} \n\tMana : {}/{}".format(
                self.name, self.magic, self.armor, self.health, self.healthMax, self.mana, self.manaMax)
        else:
            return "{} :\n\tAtk : {} \n\tDefn : {}\n\tHp   : {} / {}".format(
                self.name, self.attpower, self.armor, self.health, self.healthMax)

    # TODO : Print Stats Hero
    def stats_warrior(self):
        print("Stats Hero Warrior")
        print("\tAtttck : ", self.attpower)
        print("\tCrit   : ", self.crit, "%")
        print("\tDefn   : ", self.armor)
        print("\tHealth : ", self.health, "/", self.healthMax)

    def stats_mage(self):
        print("Stats Hero Mage")
        print("\tMagic  : ", self.magic)
        print("\tCrit   : ", self.crit, "%")
        print("\tDefn   : ", self.armor)
        print("\tHealth : ", self.health, "/", self.healthMax)
        print("\tMana   : ", self.mana, "/", self.manaMax)

    def stats_archer(self):
        print("Stats Hero Archer")
        print("\tAtttck : ", self.attpower)
        print("\tCrit   : ", self.crit, "%")
        print("\tDefn   : ", self.armor)
        print("\tHealth : ", self.health, "/", self.healthMax)

    def print_bar_fight(self):
        # Menampilkan bar HP Dan Mp (hanya hero mage) di dalam Pertarungan
        print(self.info_lite)
        self.bar_hp()
        if self.type_hero == typeHero.Mage:
            self.regenMana = self.mana_rgn
            self.bar_mana()

    # TODO: ======  Exp / Coin ======
    @property
    def gainCoin(self):
        pass

    @gainCoin.setter
    def gainCoin(self, coinUp):
        self.__coin += coinUp
        centerprint("+ {} coin".format(coinUp))
        self.coin = self.__coin

    # ================

    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self, expUp):
        self.exp += expUp
        centerprint("+ {} exp".format(expUp))
        self.levelUp()

    def levelUp(self):
        while self.exp >= self.exp_max:
            print("==============================")
            centerprint("{} level up".format(self.name))
            line()
            self.exp -= self.exp_max
            self.level += 1

            # Menentukan coin , dfn , hp Dan crit ketikan hero levelup
            coinLvl = round(5 + (self.level / 0.3))
            dfnLvl = round(0.2 + (self.level / 0.9))
            hpLvl = round(50 + (self.level / 0.5))
            critLvl = round(0.5 * self.level)

            # Memasulkn coin , dfn , hp Dan crit ketikan hero levelup
            self.__coin += coinLvl
            self.armor += dfnLvl
            self.healthMax += hpLvl
            self.crit += critLvl
            self.exp_max = round((self.exp_max * self.level) / 2 + 20)

            self.health = self.healthMax
            self.coin = self.__coin

            # Print Level Up
            print("Coin + {}\n"
                  "Defn + {}\n"
                  "hp + {}\n"
                  "crit + {} ".format(coinLvl, dfnLvl, hpLvl, critLvl))

            if self.type_hero == typeHero.Mage:
                # Menambahkan power Ke pada Hero type Mage
                mgcLvl = round(4 + (self.level / 0.6))
                mpLvl = round(10 + (self.level / 0.45))
                self.magic += mgcLvl
                self.manaMax += mpLvl

                self.mana = self.manaMax
                print("Magic + {}\n"
                      "Mp + {}".format(mgcLvl, mpLvl))
            else:
                atkLvl = round((self.attpower / 3) + (self.level / 0.6))
                self.attpower += atkLvl
                print("Atk + {}".format(atkLvl))

            # Skill level Up
            self.skill[0].Skill_LevelUp()
            self.skill[1].Skill_LevelUp()

            self.Class()
            line()
            centerprint("{} Level {}".format(self.name, self.level))

    def show_exp(self):
        bar_exp = ""
        bar = round((25 / self.exp_max) * self.exp)
        while bar > 0:
            bar_exp += "█"
            bar -= 1
        while len(bar_exp) < 25:
            bar_exp += " "
        print("Exp|" + bcolors.OKYELLOW + bar_exp + bcolors.ENDC + "|")

    # TODO : ====== darah hero ======

    @property
    def heal(self):
        pass

    @heal.setter
    def heal(self, heal):
        self.health += heal
        self.hp_limit()

    def hp_limit(self):
        if self.health > self.healthMax:
            self.health = self.healthMax

    def bar_hp(self):
        # Menampilkan Bar Hp
        bar_health = ""
        bar = round((25 / self.healthMax) * self.health)
        # health
        while bar > 0:
            bar_health += "█"
            bar -= 1
        while len(bar_health) < 25:
            bar_health += " "
        print("Hp |" + bcolors.OKGREEN + bar_health + bcolors.ENDC + "|")

    # TODO: ========= mana =========
    def bar_mana(self):
        # Menampilkan Bar Mp
        bar_mana = ""
        bar_mn = round((23 / self.manaMax) * self.mana)        # mana
        while bar_mn > 0:
            bar_mana += "█"
            bar_mn -= 1
        while len(bar_mana) < 23:
            bar_mana += " "
        print("Mana |" + bcolors.OKBLUE + bar_mana + bcolors.ENDC + "|")

    @property
    def regenMana(self):
        pass

    @regenMana.setter
    def regenMana(self, mana_regen):
        # regen Mp Ke Hero
        self.mana += mana_regen
        if self.mana > self.manaMax:
            self.mana = self.manaMax

    # TODO: ========= Attack ========

    def lose_attack(self, enemy):
        # Lose
        line()
        centerprint("== Lose ==")
        enter_select()
        gift = round((10 + self.level / 0.25) / 2)
        self.gainExp = gift
        self.gainCoin = gift
        enter_select()
        self.health = 0
        heal_hp = self.healthMax / 2
        self.health += round(heal_hp)
        enemy.run()

    def draw_attack(self, enemy):
        line()
        centerprint("== Draw ==")
        enter_select()
        gift = round((10 + self.level / 0.25) / 2)
        self.gainExp = gift
        self.gainCoin = gift
        enter_select()
        self.health = 0
        heal_hp = self.healthMax / 2
        self.health += round(heal_hp)
        enemy.run()

    def win_attack(self, enemy, item):
        line()
        centerprint("== Win ==")
        enter_select()
        try:
            centerprint("Anda dapat item {} {}x".format(item.nama, item.amount))
            self.add_inv(item)
        except AttributeError:
            centerprint(item)
        gift = round(10 + self.level / 0.25)
        if self.type_hero == typeHero.Mage:
            self.mana = self.manaMax
        self.gainExp = gift
        self.gainCoin = gift
        enemy.run()
        enter_select()

    # TODO: ========= List inventory ==========
    def add_inv(self, item):
        if item.type == 'Weapons' or item.type == 'Armor':
            self.inventory.append(item)
        elif len(self.inventory) >= 0:
            for i in range(0, len(self.inventory)):
                items = self.inventory[i]
                if items.nama == item.nama:
                    items.amount += item.amount
                    break
                if i >= len(self.inventory):
                    self.inventory.append(item)
            else:
                self.inventory.append(item)
        else:
            self.inventory.append(item)
        self.delete_item()

    def print_inventory(self):
        try:
            self.delete_item()
        except IndexError:
            pass
        i = 1
        print("no\tNama")
        for item in self.inventory:
            if item.type == 'Weapons' or item.type == 'Armor':
                print("{}\t{} {}".format(i, item.type, item.nama))
            else:
                print("{}\t{}x {}".format(i, item.amount, item.nama))
            i += 1

    def delete_item(self):
        for i in range(0, len(self.inventory)):
            items = self.inventory[i]
            if items.amount <= 0:
                self.inventory.remove(items)
                break
        else:
            pass

    def use_item(self, item):
        item.equip = True
        if item.type == 'Weapons':
            self.use_weapons.append(item)
            if item.shape == "Wand":
                self.magic += item.power
            else:
                self.attpower += item.power
            self.crit += item.crit
        elif item.type == 'Armor':
            self.use_armor.append(item)
            if self.type_hero == typeHero.Mage:
                self.manaMax += round(0.3 * item.health)
                self.mana += round(0.3 * item.health)
            self.healthMax += item.health
            self.health += item.health
            self.armor += item.defn
        else:
            pass

    def discard_item(self, item):
        item.equip = False
        if item.type == 'Weapons':
            if item.shape == "Wand":
                self.magic -= item.power
            else:
                self.attpower -= item.power
            self.crit -= item.crit
            self.use_weapons.remove(item)
        elif item.type == 'Armor':
            if self.type_hero == typeHero.Mage:
                self.manaMax -= round(0.3 * item.health)
                self.mana -= round(0.3 * item.health)
            self.healthMax -= item.health
            self.armor -= item.defn
            self.use_armor.remove(item)
        else:
            pass

    def system_Weapone(self):
        items = self.use_weapons[0]
        self.discard_item(items)

    def system_Armor(self):
        items = self.use_armor[0]
        self.discard_item(items)

    def print_Weapone_Armor(self):
        if len(self.use_armor) == 0:
            centerprint("Anda tidak pakai Armor")
        else:
            print(" Armor \t Defn \t qualty")
            for armor in self.use_armor:
                print("{} \t {} \t {}".format(armor.nama, armor.armor, armor.qualty))
        line()
        if len(self.use_weapons) == 0:
            centerprint("Anda tidak pakai Weapons")
        else:
            if self.type_hero == typeHero.Mage:
                print(" weapons \t magic \t qualty ")
                for weapone in self.use_weapons:
                    print(" {} {} \t {} \t {}".format(weapone.shape, weapone.nama, weapone.power, weapone.qualty))
            else:
                print(" weapons \t Atk \t qualty")
                for weapone in self.use_weapons:
                    print(" {} {} \t {} \t {}".format(weapone.shape, weapone.nama, weapone.power, weapone.qualty))
