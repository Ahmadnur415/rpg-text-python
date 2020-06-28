# TODO: STAR
from .hero import Hero
from source.battle import Enemy, playerAttack, enemyAttack
from .item import get_item
from .setup import *
import sys
import time

__author__ = "Ahmad Nur"
__version__ = "0.0.1"
__game__ = "Earl Last War"


def play():
    global player
    print("==============================\n"
          "|       == Mini RPG ==       |\n"
          "|    == Ahmad nur 2020 ==    |")
    line()
    print("[1]New game\n"
          "[2]Load game\n"
          "[3]Exit")
    line()
    game = input("==> ")
    if game == '1':
        loading()
        choise_hero()
    elif game == '2' or game == 2:
        try:
            line()
            player = loadgame()
            # player = relode_objeckt("Game.Sv")
            print('=' * 30)
            player.info()
            enter_select()
            gameLoop()
        except IndexError:
            line()
            centerprint("Sava game Tidak Ada")
            play()
        except ValueError:
            line()
            centerprint("Tidak Ada dalam list")
            play()
    elif game == '3' or game == 3:
        loading()
        print("==============================")
        centerprint("thanks for playing")
        print("==============================")
        sys.exit()
    else:
        play()


def choise_hero():
    global player
    line()
    centerprint("pilih role Hero")
    line()
    print("[1]warrior \n"
          "[2]mage \n"
          "[3]archer ")
    hero = input("==> ")
    if hero == '1':
        player = Hero(typeHero.Warrior)
        line()
        player.stats_warrior()
        line()
        nama = input("Nama Player : ")
        player.name = nama
        from .item.create_item import weapons_warrior
        player.add_inv(weapons_warrior(0))
        player.use_item(weapons_warrior(0))
        gameLoop()
    elif hero == '2':
        player = Hero(typeHero.Mage)
        line()
        player.stats_mage()
        line()
        nama = input("Nama Player : ")
        player.name = nama
        from .item.create_item import weapons_mage
        player.add_inv(weapons_mage(0))
        player.use_item(weapons_mage(0))
        gameLoop()
    elif hero == '3':
        player = Hero(typeHero.Archer)
        line()
        player.stats_archer()
        line()
        nama = input("Nama Player : ")
        player.name = nama
        from .item.create_item import weapons_archer
        player.add_inv(weapons_archer(0))
        player.use_item(weapons_archer(0))
        gameLoop()
    else:
        choise_hero()


# TODO : GAME LOOP
def gameLoop():
    loading()
    print("==============================\n"
          "|      == Earl last War ==   |\n"
          "|    == Versi beta 0.1.0 ==  |\n"
          "==============================")
    print("|Health {}            Coin {}|".format(player.health, player.coin))
    print("==============================\n"
          "[1]battle\n"
          "[2]Adventure\n"
          "[3]Shop\n"
          "[4]Refresh\n"
          "==============================\n"
          "[5]Camp\n"
          "[6]Setting\n"
          "[7].Exit")
    header_lvl(player=player)
    select_game()


def select_game():
    choose = input("==> ")
    if choose == '1':
        loading()
        line()
        arena(Enemy(player))
    elif choose == '2':
        line()
        Adventure()
        centerprint("Coming soon :(")
        enter_select()
        gameLoop()
    elif choose == '3':
        shop(player)
    elif choose == '4':
        gameLoop()
    elif choose == '5':
        camp()
    elif choose == '6':
        setting()
    elif choose == '7':
        loading()
        print("==============================")
        centerprint("thanks for playing")
        print("==============================")
        sys.exit()
    else:
        print("==============================")
        print("|     error input salah      |")
        gameLoop()


def Adventure():
    line()
    centerprint("Adventure")
    line()
    print('[1]Dungeons\n[2]Forest\n[3]Goa\n', '='*30, '\n[4]Main Page')
    input()
    gameLoop()

# TODO: Adventure
def Dungeons(hero, level, boss):
    """
        :param hero:
        :param level:
        :param boss:
        :return:
    """
    global reqAtk
    if level == 1:
        reqAtk = 15
    elif level == 2:
        reqAtk = 25

    if hero.attpower >= reqAtk or hero.magic >= reqAtk:
        print('=' * 30)
        centerprint("Selamat Di Dongeons")
        print('=' * 30)
        room = 1
        max_room = room + level
        while room <= max_room:
            centerprint("Level {} // Room {}".format(level, room))
            enemy = "Pass"

            """
            :argument
                Untuk musuh random dari enemyAdv    

            :keyword
                tidak Ada

            """

            hero.print_bar_fight()
            print("==============================")

            if room == max_room:
                centerprint("Melawan Bos Dungeons")
                print('=' * 30)
                print(boss.showinfo_boss)

            else:
                centerprint("")
                '''print(enemy.info_enemy)
                print(enemy.HpBar())'''

            room += 1

    else:
        print("=" * 30)
        centerprint("Anda belum bisa Ke Dungeons Minimal [Attack power / magic power] Anda harus {}".format(reqAtk))
        print("=" * 30)
        return camp()


# TODO : ARENA
def arena(enemy):
    global player
    player.print_bar_fight()
    print("==============================")
    print(enemy.info_enemy)
    print(enemy.HpBar())

    skill_1 = player.skill[0]
    skill_2 = player.skill[1]

    if player.health <= 0 and enemy.hpE <= 0:
        player.draw_attack(enemy)
        gameLoop()
    elif player.health <= 0:
        if player.type_hero == typeHero.Warrior and skill_2.Aktif:
            skill_2.immortal(player)
            arena(enemy)
        else:
            player.lose_attack(enemy)
            gameLoop()

    elif enemy.hpE <= 0:
        gift_items = get_item()
        player.win_attack(enemy, gift_items)
        gameLoop()

    line()
    if player.type_hero == 'mage':
        print("[1]Basic Magic {}\n"
              "\t|cost mana {}".format(
                player.magic, player.cost_mana))
    else:
        print("[1]Basic Attack")

    print("[2]", skill_1.printIndex(player))
    print("[3]", skill_2.printIndex(player))
    print("[4]Run")

    line()
    index = input(">>>> ")

    if index == '1':
        print('=' * 30)
        playerAttack(skill=False, attacker=player, defenders=enemy)
        enemyAttack(enemy, defenders=player)
        enter_select()
        arena(enemy)
    elif index == '2':
        skill_1.Active(player, enemy)
        enter_select()
        arena(enemy)
    elif index == '3':
        skill_2.Active(player, enemy)
        enter_select()
        arena(enemy)
    elif index == '4':
        enemy.run()
        line()
        print("| kamu lari dari pertempuran |")
        enter_select()
        gameLoop()
    else:
        arena(enemy)


# TODO: Camp
def camp():
    line()
    player.heal = player.hp_rgn
    if player.type_hero == 'mage':
        player.regenMana = round(0.5 * player.mana_rgn)
    centerprint("== Camp ==")
    line()
    print("|Health {}            Coin {}|".format(player.health, player.coin))
    header_camp()
    header_lvl(player=player)
    choose = input("==> ")
    """ stats player"""
    if choose == '1':
        line()
        print("      == STATS PLAYER ==      \n"
              "==============================")
        player.info()
        enter_select()
        camp()
    elif choose == '2':
        TrainingPlayer(player)
    elif choose == '3':
        perlengkapan(player)
    elif choose == '4':
        inventory(player=player)
        camp()
    elif choose == '5':
        savegame(player)
        # save_object(player, "Game.Sv")
        print("loading.....")
        time.sleep(2)
        print("Success.....")
        enter_select()
        camp()
    elif choose == '6':
        gameLoop()
    elif choose == '7':
        loading()
        print("==============================")
        centerprint("thanks for playing")
        print("==============================")
        sys.exit()
    else:
        camp()


# TODO : SETTING
def setting():
    global player
    text_setting()
    header_lvl(player)
    pilih = input("==> ")
    if pilih == '1':
        line()
        changeName = input("Nama baru: ")
        print("Loading.....")
        time.sleep(2)
        print("berhasil....")
        player.name = changeName
        enter_select()
        gameLoop()
    elif pilih == '2':
        try:
            player = loadgame()
            # player = relode_objeckt("Game.Sv")
            print("Loading.....")
            time.sleep(2)
            print("Success.....")
            print(player.info)
            enter_select()
            camp()
        except FileNotFoundError:
            line()
            centerprint("Sava game Tidak Ada coba untuk New Game")
            enter_select()
            setting()
    elif pilih == '4':
        setting()
    elif pilih == '3':
        savegame(player)
        # save_object(player, "Game.Sv")
        print("loading....")
        time.sleep(1)
        print("Success....")
        enter_select()
        camp()
    elif pilih == '5':
        gameLoop()
    elif pilih == '6':
        print("==============================")
        centerprint("thanks for playing")
        print("==============================")
        sys.exit()
    else:
        setting()

# TODO: END
