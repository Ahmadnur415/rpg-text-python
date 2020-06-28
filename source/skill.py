import time
from .battle import enemyAttack, playerAttack
from .setup import centerprint, leftPrint_


class CooldownException(Exception):
    pass


class cooldown(object):
    def __init__(self, second):
        self.second = second
        self.expire = None

    def __enter__(self):
        if not self.expire or time.time() > self.expire:
            self.expire = time.time() + self.second
        else:
            raise CooldownException("{:^30}".format(str(round(self.expire - time.time(), 1)) + " s"))

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


# TODO: Skill untuk Archer
class doubleArrow:
    def __init__(self):
        self.name = "Double Arrow"  # Double Arrow
        self.countdown = 60
        self.cooldown = cooldown(self.countdown)
        self.power = 0.2
        self.max_level = 10
        self.level = 1
        self.user = 'archer'
        self.description = None

    def Active(self, hero, enemy):
        try:
            with self.cooldown:
                powerUp = hero.attpower * self.power
                hero.attpower += round(powerUp)
                print("="*30)
                centerprint("Skill {} Digunakan".format(self.name))
                print("=" * 30)
                playerAttack(skill=True, defenders=enemy, attacker=hero)
                hero.attpower -= round(powerUp)
                playerAttack(skill=False, defenders=enemy, attacker=hero)
                enemyAttack(enemy, defenders=hero)

        except CooldownException as e:
            print('='*30)
            centerprint("Skill Masih Cooldown")
            print(e)

    def Skill_LevelUp(self):
        if self.level <= self.max_level:
            self.level += 1
            up_power = 0.05
            reduce_cooldown = 1.5

            self.power += up_power
            self.countdown -= reduce_cooldown

    def printIndex(self, hero=None):
        if hero is None:
            pass
        return "skill : {}\n\t|Power x{} dmg".format(self.name, self.power)

    def printInfo_(self, hero):
        print(
            "Skill: {}\n"
            "\tpower up : {}x({})\n"
            "\tLevel    : {}/{}\n"
            "\tcountdown: {}".format(
                self.name, self.power, hero.attpower * self.power, self.level, self.max_level, self.countdown
            )
        )
        print('='*30)
        leftPrint_(
            "Info : Skill {} Memberikan Serangan 2x ")


class avoidAttack:
    def __init__(self):
        self.name = "Avoid Attack"  # Double Arrow
        self.countdown = 70
        self.cooldown = cooldown(self.countdown)
        self.max_level = 10
        self.powerUp = 0.5
        self.level = 1
        self.user = 'archer'
        self.description = None

    def Active(self, hero, enemy):
        try:
            with self.cooldown:
                powerUp = hero.attpower * self.powerUp
                hero.attpower += powerUp
                print("="*30)
                centerprint("Skill {} Digunakan".format(self.name))
                print("=" * 30)
                playerAttack(skill=True, attacker=hero, defenders=enemy)
                hero.attpower -= powerUp
        except CooldownException as e:
            print('='*30)
            centerprint("Skill Masih Cooldown")
            print(e)

    def Skill_LevelUp(self):
        if self.level <= self.max_level:
            self.level += 1
            reduce_cooldown = 1.5
            self.countdown -= reduce_cooldown

    def printIndex(self, hero=None):
        if hero is None:
            pass
        return "skill : {}".format(self.name)

    def printInfo_(self, hero=None):
        if hero is None:
            pass
        print(
            'Skill : {}\n'
            '\tcountdown: {}'.format(self.name, self.countdown)
        )


# TODO: Skill untuk mage
class fireBall:
    def __init__(self):
        self.name = 'Fire Ball'
        self.countdown = 150
        self.cooldown = cooldown(self.countdown)
        self.magic = 10
        self.stack = 0
        self.mana = 50
        self.max_level = 10
        self.level = 1
        self.user = 'mage'
        self.description = None

    def attack(self, hero, enemy):
        hero.magic += round(self.magic)

        print("=" * 30)
        centerprint("Skill {} Digunakan".format(self.name))
        print("=" * 30)
        playerAttack(skill=True, defenders=enemy, attacker=hero)
        enemyAttack(enemy, defenders=hero)
        self.stack -= 1

        hero.magic -= round(self.magic)

    def Active(self, hero, enemy):
        """hero.cost_mana += round(self.mana)
        if self.stack == 0 and hero.mana >= hero.cost_mana:
            try:
                with self.cooldown:
                    self.stack += 2
                    self.attack(hero, enemy)

            except CooldownException as e:
                hero.cost_mana -= round(self.mana)
                print('='*30)
                print(e)
        elif self.stack >= 1 and hero.mana >= hero.cost_mana:
            self.attack(hero, enemy)
        else:
            print("Mana Anda Kurang")"""
        hero.cost_mana += round(self.mana)
        if hero.mana >= hero.cost_mana and self.stack <= 0:
            try:
                with self.cooldown:
                    hero.mana -= hero.cost_mana
                    hero.cost_mana -= round(self.mana)
                    print("=" * 30)
                    centerprint("Skill {} Digunakan".format(self.name))
                    self.stack += 4
            except CooldownException as e:
                hero.cost_mana -= round(self.mana)
                print('=' * 30)
                centerprint("Skill Masih Cooldown")
                print(e)
        elif self.stack >= 1:
            hero.cost_mana -= round(self.mana)
            costmana = hero.cost_mana
            hero.cost_mana = 0
            self.attack(hero=hero, enemy=enemy)
            hero.cost_mana = costmana
        else:
            hero.cost_mana -= round(self.mana)
            print("Mana Anda Kurang")

    def Skill_LevelUp(self):
        if self.level <= self.max_level:
            up_magic = 2
            reduce_cooldown = 5
            cost_mana = 1

            self.level += 1
            self.magic += up_magic
            self.countdown -= reduce_cooldown
            self.mana -= cost_mana

    def printIndex(self, hero=None):
        if self.stack == 0:
            return "Skill {} \n\t|cost mana : {} \n\t|Magic : {}".format(self.name, self.mana + hero.cost_mana,
                                                                         self.magic + hero.magic)
        else:
            return "Skill {} \n\t|Magic : {} \n\t|Stack : {}".format(self.name, self.magic + hero.magic, self.stack)


class healing:
    def __init__(self):
        self.name = 'Healing'
        self.countdown = 60
        self.cooldown = cooldown(self.countdown)
        self.healMp = 10
        self.healHp = 10
        self.max_level = 10
        self.level = 1
        self.user = 'mage'
        self.description = None

    def Active(self, hero, enemy):
        if enemy is None:
            pass
        try:
            with self.cooldown:
                healHp = round(hero.healthMax * self.healHp / 100)
                healMp = round(hero.manaMax * self.healMp / 100)
                hero.health += healHp
                hero.mana += healMp
                """if hero.health > hero.healthMax:
                    hero.health = hero.healthMax
                if hero.mana > hero.manaMax:
                    hero.mana = hero.healthMax"""
                print("="*30)
                centerprint("Skill {} Digunakan".format(self.name))

        except CooldownException as e:
            print('='*30)
            centerprint("Skill Masih Cooldown")
            print(e)

    def Skill_LevelUp(self):
        if self.level <= self.max_level:
            UpHealHp = 3
            UpHealMp = 2
            reduce_cooldown = 5

            self.level += 1
            self.healHp += UpHealHp
            self.countdown -= reduce_cooldown
            self.healMp += UpHealMp

    def printIndex(self, hero=None):
        if hero is None:
            pass
        return "Skill {} \n\t|regen Hp : {}% \n\t|regen Mp : {}%".format(self.name, self.healHp, self.healMp)


# TODO SKIll untuk Warrior
class blackAnger:
    def __init__(self):
        self.name = 'Black Anger'
        self.countdown = 60
        self.cooldown = cooldown(self.countdown)
        self.power = 60  # penambahan power memakai persen
        self.defense = 40
        self.max_level = 10
        self.level = 1
        self.user = 'warrior'
        self.description = None

    def Active(self, hero, enemy):
        try:
            with self.cooldown:
                powerUp = hero.attpower * self.power / 100
                dfnUp = hero.armor * self.defense / 100

                hero.attpower += round(powerUp)
                hero.armor += round(dfnUp)

                print("="*30)
                centerprint("Skill {} Digunakan".format(self.name))
                print("=" * 30)
                playerAttack(skill=True, defenders=enemy, attacker=hero)
                enemyAttack(enemy, defenders=hero)

                hero.attpower -= round(powerUp)
                hero.armor -= round(dfnUp)

        except CooldownException as e:
            print('='*30)
            centerprint("Skill Masih Cooldown")
            print(e)

    def Skill_LevelUp(self):
        if self.level <= self.max_level:
            powerUp = 3
            armorUp = 1.5
            reduce_cooldown = 3

            self.power += powerUp
            self.defense += armorUp
            self.countdown -= reduce_cooldown

    def printIndex(self, hero=None):
        if hero is None:
            pass
        return "Skill {} \n\tPower Up : {}% \n\tArmor Up : {}%".format(self.name, self.power, self.defense)


class riseUp:
    def __init__(self):
        self.name = 'Rise Up'
        self.countdown = 120
        self.cooldown = cooldown(self.countdown)
        self.heal = 20
        self.Aktif = False
        self.max_level = 10
        self.level = 1
        self.user = 'warrior'
        self.description = None

    def Active(self, hero, enemy):
        if hero is None and enemy is None:
            pass
        if not self.Aktif:
            try:
                with self.cooldown:
                    print("="*30)
                    centerprint("Skill '{}'Akan Digunakan secara otomatis".format(self.name))
                    time.sleep(1)
                    self.Aktif = True
            except CooldownException as e:
                print('='*30)
                centerprint("Skill Masih Cooldown")
                print(e)
        elif self.Aktif:
            print('='*30)
            centerprint("Skill ini Akan Aktif otomatis jika player mati")

    def immortal(self, hero):
        if self.Aktif:
            heal = hero.healthMax * self.heal / 100
            hero.health += round(heal)

            print("=" * 30)
            centerprint("Skill {} Telah Aktif".format(self.name))
            input('========== [Enter] ===========')
            self.Aktif = False

    def Skill_LevelUp(self):
        if self.level <= self.max_level:
            heal = 3
            reduce_cooldown = 4

            self.heal += heal
            self.countdown -= reduce_cooldown

    def printIndex(self, hero=None):
        if self.Aktif:
            return "Skill {} \n\tSkill akan aklif otomatis\n\tjika {} mati".format(self.name, hero.name)
        elif not self.Aktif:
            return "Skill {}".format(self.name)


def use_skill(Skill, attacker, defenders):
    Skill.Active(attacker, defenders)


"""
def skillWarrior():
    skill_1 = blackAnger()
    skill_2 = riseUp()
    return [skill_1] + [skill_2]


def skillMage():
    skill_1 = fireBoll()
    return skill_1


def skillArcher():
    skill_1 = Double_Arrow()
    return skill_1
    
    :argument
        skill untuk warrior
            - skill 1 = defn / pertahanan
    
                :argument
                    memberikan armor tambahan sebesar 5(player) dan mengurangi armor musuh sebesar 5
                    :cooldown 100 detik
                     
            - skill 2 = mengamuk
                :argument
                    memberikan tambahan regen hp sebesar 30 dan power 10 
                    :cooldown 15 detik
                
        skill untuk mage
        
            - skill 1 = brust damage
                :argument
                    memberikan tambahan magic power 10 selama 3 turn dan membutuhkan mana sebesar 15
                    :cooldown 20 detik
                    
            - skill 2 = regen Mp dan Hp
                :argument
                    dengan skill ini player dapat menambah hp +(30) dan Mp +(20)
                    :cooldown 15 detik 
                
        skill untuk archer
            - skill 1 = double arrow
                :argument
                    memberikan 1.5x damage dari dari biasanya
                    :cooldown 20 detik
 
            - skill 2 = Menghindar
                :argument
                    player dapat menghindar dari serangan musuh
                    :untuk cooldown 15 detik

"""