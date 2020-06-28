from ..setup import typeHero


class item:
    def __init__(self, nama, coin, amount, type):
        self.nama = nama
        self.type = type
        self.coin = coin
        self.amount = amount

    def show_item(self):
        return "{} \n\t" \
               "Sell   : {} \n\t" \
               "Amount : {}".format(self.nama, self.coin, self.amount)


class potion(item):
    def __init__(self, nama, coin, amount, UpHealth, UpMana, use_hero):
        super().__init__(nama, coin, amount, type="Potion")
        self.Up_health = UpHealth
        self.UP_mana = UpMana
        self.use_hero = use_hero

    def show_potion(self):
        if self.use_hero == typeHero.Mage:
            return "{} \n\tRegen Mp : {} \n\tSell     :{} \n\tAmount   : {}".format(self.nama, self.UP_mana, self.coin,
                                                                                    self.amount)
        else:
            return "{} \n\tRegen Hp : {} \n\tSell     :{} \n\tAmount   : {}".format(self.nama, self.Up_health, self.coin,
                                                                          self.amount)


class food(item):
    def __init__(self, nama, coin, amount, Up_hp, Up_mana, Updmg):
        super().__init__(nama, coin, amount, type="Food")
        self.Up_hp = Up_hp
        self.Up_mana = Up_mana
        self.Up_Atk = Updmg

    def show_Food(self):
        return "{} \n\t" \
               "Type   : {}\n\t" \
               "Up Hp  : {}\n\t" \
               "Up Mp  : {}\n\t" \
               "Up Dmg : {}\n\t" \
               "Amount : {}".format(self.nama, self.type, self.Up_hp, self.Up_mana, self.Up_Atk, self.amount)


class Armor(item):
    def __init__(self, name, qualty, health, defn, coin, equip):
        super().__init__(name, coin, amount=1, type="Armor")
        self.defn = defn
        self.health = health
        self.coin = coin
        self.qualty = qualty
        self.equip = equip

    def show_armor(self):
        return "{} {} \n\tqualty : {}\n\thealth : {} \n\tArmor  : {}\n\tamount  : {} \n\tEquip  : {}".format(
            self.type, self.nama, self.qualty, self.health,self.defn, self.amount, self.equip)

    """
    def __repr__(self):
        return "{}\t {}".format(self.name, self.value)

    def showInfo_armor(self):
        return "{}: \n\tarmor up : {} \n\thealth up : {}".format(self.name, self.up_armor, self.up_healthMax)

    def __init__(self, name, Up_armor, Up_healthMax, maxArmor, coin, value):
        self.name = name
        self.up_armor = Up_armor
        self.up_healthMax = Up_healthMax
        self.max_armor = maxArmor
        self.coin = coin
        self.value = value
    """


# class weapons untuk warrior
class weapons(item):
    def __init__(self, nama, coin, power, crit, qualty, shape, equip):
        super().__init__(nama, coin, amount=1, type="Weapons")
        self.power = power
        self.crit = crit
        self.shape = shape
        self.qualty = qualty
        self.equip = equip
        self.type_hero = typeHero.Warrior

    def show_weapons(self):
        if self.type_hero == typeHero.Mage:
            return "{} {} \n\tqualty : {}\n\tmagic  : {} \n\tCrit   : {}% \n\tamount  : {} \n\tEquip  : {}".format(
                self.shape, self.nama, self.qualty, self.power, self.crit, self.amount, self.equip)
        else:
            return "{} {} \n\tqualty : {}\n\tpower  : {} \n\tCrit   : {}% \n\tAmount  : {} \n\tEquip  : {}".format(
                self.shape, self.nama, self.qualty, self.power, self.crit, self.amount, self.equip)


# class weapons untuk mage
class magic_wand(weapons):
    def __init__(self, nama, coin, power, crit, qualty, shape, equip):
        super().__init__(nama, coin, power, crit, qualty, shape, equip)
        self.type_hero = typeHero.Mage


# class weapons untuk archer
class bow(weapons):
    def __init__(self, nama, coin, power, crit, qualty, shape, equip):
        super().__init__(nama, coin, power, crit, qualty, shape, equip)
        self.type_hero = typeHero.Archer
