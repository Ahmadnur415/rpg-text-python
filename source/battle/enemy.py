from source.setup.text import bcolors
import random


class enemy:
    def __init__(self, name, lastName, hpMaxE, atkE, dfnE, crit, clss):
        # Nama
        self.name = name
        self.lastName = lastName
        # power
        self.crit = crit
        self.atkE = atkE
        # health dan dfn
        self.hpMaxE = hpMaxE
        self.hpE = self.hpMaxE
        self.dfnE = dfnE
        # class Enemy
        self.clss = clss

    @property
    def info_enemy(self):  # Menampilkan Info Musuh Ke dalam Pertarungan
        if self.hpE <= 0:
            self.hpE = 0
        return 'Enemy : {} {} |=| {} \n\tAtk  : {} \n\tCrit : {} \n\tHp   : {}/{} \n\tDefn : {}'.format(
            self.name, self.lastName, self.clss, self.atkE, self.crit, self.hpE, self.hpMaxE, self.dfnE)

    def HpBar(self):  # Menampilkan Bar Health Ke kedalam Pertaungan
        bar_health = ""
        bar = round((25 / self.hpMaxE) * self.hpE)
        while bar > 0:
            bar_health += "█"
            bar -= 1
        while len(bar_health) < 25:
            bar_health += " "
        return "Hp |" + bcolors.OKRED + bar_health + bcolors.ENDC + "|"

    def run(self):
        self.hpE = self.hpMaxE


class boss(enemy):
    def __init__(self, name, atkE, hpE, hpMaxE, dfnE, crit, clss):
        super().__init__(name, atkE, hpE, hpMaxE, dfnE, crit, clss)

    @property
    def showinfo_boss(self):
        return "Boss {} |=| {} \n\t" \
               "Atk  : {} \n\t" \
               "Crit : {} \n\t" \
               "Hp   : {}/{} \n\t" \
               "Defn : {}".format(
                self.name, self.clss, self.atkE, self.crit, self.hpE, self.hpMaxE, self.dfnE
                )


class monster(enemy):
    def __init__(self, name, atkE, hpE, hpMaxE, dfnE, crit, clss, lvl):
        super().__init__(name, atkE, hpE, hpMaxE, dfnE, crit, clss)
        self.level = lvl

    @property
    def showinfo(self):
        return "Monster {} |=| {} \n\t" \
               "Atk  : {} \n\t" \
               "Crit : {} \n\t" \
               "Hp   : {}/{} \n\t" \
               "Defn : {}".format(
                self.name, self.clss, self.atkE, self.crit, self.hpE, self.hpMaxE, self.dfnE
                )

    def no_Alive(self):
        if self.hpE <= 0:
            self.level += 1
            self.hpMaxE += round(2 * self.level / 0.6)
            self.atkE += round(1 * self.level / 0.8)

            self.hpE = self.hpMaxE


class monster_easy(monster):
    def __init__(self, name):
        super().__init__(name, atkE=random.randint(1, 10), hpE=20, hpMaxE=20, dfnE=random.randint(0, 5),
                         crit=random.randint(0, 15), clss="easy", lvl=random.randint(1, 10))


class monster_medium(monster):
    def __init__(self, name):
        super().__init__(name, atkE=random.randint(7, 15), hpE=25, hpMaxE=25, dfnE=random.randint(3, 10),
                         crit=random.randint(7, 20), clss="medium", lvl=random.randint(7, 15))


class monster_hard(monster):
    def __init__(self, name):
        super().__init__(name, atkE=random.randint(13, 20), hpE=30, hpMaxE=30, dfnE=random.randint(7, 12),
                         crit=random.randint(7, 20), clss="hard", lvl=random.randint(12, 20))


class monster_hardcore(monster):
    def __init__(self, name):
        super().__init__(name, atkE=random.randint(17, 25), hpE=40, hpMaxE=40, dfnE=random.randint(10, 15),
                         crit=random.randint(7, 20), clss="hardcore", lvl=random.randint(17, 25))
