import textwrap
import time


class bcolors:
    OKGREEN = '\033[92m'
    OKYELLOW = '\033[93m'
    OKRED = '\033[91m'
    ENDC = '\033[0m'
    OKBLUE = '\033[94m'


class typeHero:
    Mage = 'Mage'
    Archer = 'Archer'
    Warrior = 'Warrior'


class level:
    easy = 'Easy'
    medium = 'Medium'
    hard = 'Hard'
    hardcore = 'HardCore'


def help():
    print("gunakan angka untung input")


def header_arena():
    print("==============================")
    print("|      Welcome to arena      |")
    print("==============================")


def enter_select():
    input('========== [Enter] ===========')


def header_camp():
    line()
    print("[1]Stats Player\n"
          "[2]Training\n"
          "[3]Perlengkapan\n"
          "[4]Inventory\n"
          "==============================\n"
          "[5]Save Game")
    print("[6]Main Page\n"
          "[7]Exit")


def line():
    print("==============================")


def loading():
    line()
    print("loading", end=' ')
    time.sleep(0.25)
    print(".", end='')
    time.sleep(0.25)
    print(".", end='')
    time.sleep(0.25)
    print(".", end='')
    time.sleep(0.25)
    print(".")
    time.sleep(0.25)


def centerprint(text):
    wrapstring = textwrap.wrap(text, width=30)
    for line in wrapstring:
        # print(line)
        print('{:^30}'.format(line))


def leftPrint_(text):
    # print('{:<30}'.format(text))
    wrapstring = textwrap.wrap(text, width=30)
    for line in wrapstring:
        # print(line)
        print('{:<30}'.format(line))


def header_lvl(player):
    print("==============================")
    player.show_exp()
    centerprint("Lvl {}".format(player.level))
    print("==============================")


def text_setting():
    print("==============================")
    print("|          Setting           |")
    print("==============================")
    print("[1]change name\n"
          "[2]load Game\n"
          "[3]Save Game\n"
          "[4]Refrest\n"
          "==============================\n"
          "[5]main page\n"
          "[6]Exit")

"""
simbol ASCII
╚ ╠ ╬ █ ©
"""


class description:
    doubleArrow = ""

    avoidAttack = ""

    fireBall = ""

    healing = ""

    BlackAnger = ""

    riseUp = ""
